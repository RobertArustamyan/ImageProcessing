import { Component, Input } from '@angular/core';
import { NgClass } from "@angular/common";
import { ButtonDirective } from "primeng/button";
import { Ripple } from "primeng/ripple";

@Component({
  selector: 'app-image-preview',
  standalone: true,
  templateUrl: './image-preview.component.html',
    imports: [
        NgClass,
        ButtonDirective,
        Ripple,
    ],
  styleUrl: './image-preview.component.scss'
})
export class ImagePreviewComponent {
  @Input() imgSrc: string = '';
  @Input() placeholderText: string = 'You will see the result here';

  public onDownloadImage(): void {
    const a: HTMLAnchorElement = document.createElement("a");
    a.href = this.imgSrc;
    a.download = 'processed Image';
    a.click();
    a.remove();
  }
}
