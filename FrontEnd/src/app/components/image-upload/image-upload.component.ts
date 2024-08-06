import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormControl } from "@angular/forms";

import { DragDirective } from "@Shared/directives";
import { ButtonDirective } from "primeng/button";
import { Ripple } from "primeng/ripple";

@Component({
  selector: 'app-image-upload',
  standalone: true,
  imports: [
    DragDirective,
    ButtonDirective,
    Ripple,
  ],
  templateUrl: './image-upload.component.html',
  styleUrl: './image-upload.component.scss'
})
export class ImageUploadComponent {
  @Input({required: true}) imgControl: FormControl<string | null> = new FormControl<string | null>(null);

  @Output() imgBase64: EventEmitter<string> = new EventEmitter<string>();

  public onFileChange(event: any): void {
    const reader: FileReader = new FileReader();

    if (event.target.files && event.target.files.length) {
      const [file] = event.target.files;
      reader.readAsDataURL(file);

      reader.onload = (): void => {
        this.imgControl.setValue(reader.result as string);

        const base64Str: string = (reader.result as string).split(',')[1];
        this.imgBase64.emit(base64Str);
      };
    }
  }

  public imageDropped(imgData: { Image: string, Img64: string }): void {
    this.imgControl.setValue(imgData.Image);
    this.imgBase64.emit(imgData.Img64);
  }

  public imageClear(): void {
    this.imgControl.setValue(null);
    this.imgControl.markAsTouched();
    this.imgBase64.emit('');
  }
}
