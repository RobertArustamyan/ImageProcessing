import { Component, inject, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {
  AbstractControl,
  FormArray,
  FormBuilder,
  FormControl,
  FormGroup,
  ReactiveFormsModule,
  Validators
} from "@angular/forms";
import { finalize, take } from "rxjs";

import { PrimeNGConfig } from "primeng/api";
import { Button, ButtonDirective } from "primeng/button";
import { Ripple } from "primeng/ripple";

import { ImageUploadComponent } from "@Components/image-upload/image-upload.component";
import { ImagePreviewComponent } from "@Components/image-preview/image-preview.component";
import { ImageService } from "@Shared/services/image.service";
import { ICustomConfigs, ICustomConfigsForm } from "@Shared/interfaces/custom-config.interface";
import { ColorPickerModule } from "primeng/colorpicker";


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    ImageUploadComponent,
    ImagePreviewComponent,
    Button,
    Ripple,
    ButtonDirective,
    ReactiveFormsModule,
    ColorPickerModule,
  ],
  providers: [
    ImageService,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit {
  private primengConfig: PrimeNGConfig = inject(PrimeNGConfig);
  private imgService: ImageService = inject(ImageService);

  public imgControl: FormControl<string | null> = new FormControl<string | null>(null);
  public imgSrc: string = '';
  public img64: string = '';

  private fb: FormBuilder = inject(FormBuilder);

  public customConfigsForm: FormGroup<ICustomConfigsForm>;

  constructor() {
    this.customConfigsForm = this.fb.group<ICustomConfigsForm>({
      Image: new FormControl<string | null>(null),
      ColorConfigs: this.fb.array<FormGroup>([])
    });
  }


  public pending: boolean = false;

  ngOnInit(): void {
    this.primengConfig.ripple = true;
  }

  public onGrayScaleOrInvertImage(type: string): void {
    if (!this.img64) return;

    this.pending = true;

    const payload: { Image: string } = {
      Image: this.img64,
    };

    this.imgService[type === 'invert' ? 'invertImage' : 'grayScaleImage'](payload)
      .pipe(
        finalize((): boolean => this.pending = false),
        take(1)
      )
      .subscribe({
        next: (res: { ProcessedImage: string }): void => {
          this.imgSrc = `data:image/jpeg;base64,${ res.ProcessedImage }`;
        },
        error: (err: any): void => {
          alert(err);
        }
      });
  }

  public set64Str(base64Img: string): void {
    if (!base64Img) {
      this.imgSrc = '';
    }

    this.img64 = base64Img;
  }

  public addRow(): void {
    this.colorConfigs.push(this.createFormGroup());
  }

  public createFormGroup(): FormGroup {
    return this.fb.group({
      ColorRange: this.fb.group({
        FromColor: [null],
        ToColor: [null]
      }),
      ReplaceColor: [null]
    });
  }

  public get colorConfigs(): FormArray {
    return this.customConfigsForm.get('ColorConfigs') as FormArray;
  }

  public onCustom(): void {
    if (!this.img64) return;

    this.pending = true;

    const payload: ICustomConfigs = {
      Image: this.img64,
      ColorConfigs: this.colorConfigs.value,
    };

    this.imgService.processImage(payload)
      .pipe(
        finalize((): boolean => this.pending = false),
        take(1)
      )
      .subscribe({
        next: (res: { ProcessedImage: string }): void => {
          this.imgSrc = `data:image/jpeg;base64,${ res.ProcessedImage }`;
        },
        error: (err: any): void => {
          alert(err);
        }
      });
  }

  public removeRow(idx: number): void {
    this.colorConfigs.removeAt(idx);
  }
}
