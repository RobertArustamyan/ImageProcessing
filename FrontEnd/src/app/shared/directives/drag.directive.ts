import { Directive, EventEmitter, HostBinding, HostListener, Output } from '@angular/core';

@Directive( {
  selector: '[imgDrag]',
  standalone: true,
} )

export class DragDirective {

  @Output() file: EventEmitter<any> = new EventEmitter();

  @HostBinding( "style.border" ) private border: string = "1px solid darkgray";
  @HostBinding( "style.transition" ) private transition: string = "0.2s";

  constructor() {}

  @HostListener( "dragover", [ "$event" ] )
  public onDragOver( event: DragEvent ): void {
    event.preventDefault();
    event.stopPropagation();
    this.border = "4px dotted #1f1d1d";
  }

  @HostListener( "dragleave", [ "$event" ] )
  public onDragLeave( event: DragEvent ): void {
    event.preventDefault();
    event.stopPropagation();
    this.border = "4px dotted darkgray";
  }

  @HostListener( "drop", [ "$event" ] )
  public onDrop( event: DragEvent ): void {
    event.preventDefault();
    event.stopPropagation();
    this.border = "4px dotted darkgray";

    const reader: FileReader = new FileReader();

    if ( event.dataTransfer?.files && event.dataTransfer?.files.length ) {
      const file: File = event.dataTransfer?.files[0];
      reader.readAsDataURL( file );

      if (
        file.type === "image/jpeg" ||
        file.type === "image/png" ||
        file.type === "image/jpg"
      ) {
        reader.onload = (): void => {
          if (file.size > 600_00_00) {
            alert('File Size Is Too Large, Please Choose Another One')
            return;
          }
          const base64String = (reader.result as string).split(',')[1];
          this.file.emit( { Image: reader.result, Img64: base64String } );
        }
      } else {
        return;
      }
    }
  }
}
