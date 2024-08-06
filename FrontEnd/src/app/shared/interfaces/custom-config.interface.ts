import { FormControl, FormGroup, FormArray } from "@angular/forms";

export interface IColorRange {
  FromColor: string;
  ToColor: string;
}

export interface ICustomConfig {
  ColorRange: IColorRange;
  ReplaceColor: string;
}

export interface ICustomConfigs {
  Image: string;
  ColorConfigs: ICustomConfig[];
}

export interface ICustomConfigsForm {
  Image: FormControl<string | null>;
  ColorConfigs: FormArray<FormGroup<{
    ColorRange: FormGroup<{
      FromColor: FormControl<string | null>;
      ToColor: FormControl<string | null>;
    }>;
    ReplaceColor: FormControl<string | null>;
  }>>;
}

export interface ICustomConfigs {
  Image: string;
  ColorConfigs: ICustomConfig[];
}
