import { inject, Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

import { environment } from "@Environments/environment";

@Injectable()
export class ImageService {
  private http: HttpClient = inject(HttpClient);

  private baseUrl: string = environment['ApiUrl'];


  public processImage(payload: any): any {
    return this.http.post(`${this.baseUrl}/process-image`, payload);
  }

  public grayScaleImage(payload: any): any {
    return this.http.post(`${this.baseUrl}/grayscale-image`, payload);
  }

  public invertImage(payload: any): any {
    return this.http.post(`${this.baseUrl}/invert-image`, payload);
  }
}
