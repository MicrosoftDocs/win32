---
title: Customizing Ribbon Colors
description: The Windows Ribbon framework exposes a set of color properties that allow an application to customize the appearance of various Ribbon UI elements at run time.
ms.assetid: e070aaca-d350-4336-8e5d-d5d9c8167287
keywords:
- Windows Ribbon,customizing colors
- Ribbon,customizing colors
- customizing Windows Ribbon colors
ms.topic: article
ms.date: 05/31/2018
---

# Customizing Ribbon Colors

The Windows Ribbon framework exposes a set of color properties that allow an application to customize the appearance of various Ribbon UI elements at run time.

-   [Introduction](#introduction)
-   [Specify Ribbon Colors](#specify-ribbon-colors)
-   [Convert RGB to HSB](#convert-rgb-to-hsb)
-   [Related topics](#related-topics)

## Introduction

The [framework property keys](windowsribbon-reference-properties-framework.md) listed in the following table are used to set the color of various UI elements in a Ribbon application. These properties allow the Ribbon framework to support personalization, identity requirements, and branding specifications across applications.

| Ribbon Color                     | Framework Property Key                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Background color                 | [UI\_PKEY\_GlobalBackgroundColor](windowsribbon-reference-properties-uipkey-globalbackgroundcolor.md)                                                                                                                                                                                                                                                                                                                                                                 |
| Highlight color (Windows 7 only) | [UI\_PKEY\_GlobalHighlightColor](windowsribbon-reference-properties-uipkey-globalhighlightcolor.md)****Introduced in Windows 8**:  ** [UI\_PKEY\_GlobalHighlightColor](windowsribbon-reference-properties-uipkey-globalhighlightcolor.md) cannot be set independently of [UI\_PKEY\_GlobalBackgroundColor](windowsribbon-reference-properties-uipkey-globalbackgroundcolor.md).<br/> <br/>                                                              |
| Text color                       | [UI\_PKEY\_GlobalTextColor](windowsribbon-reference-properties-uipkey-globaltextcolor.md)****Introduced in Windows 8**:** Changes to the default value of [UI\_PKEY\_GlobalBackgroundColor](windowsribbon-reference-properties-uipkey-globalbackgroundcolor.md) in Windows 8 might require an adjustment to [UI\_PKEY\_GlobalTextColor](windowsribbon-reference-properties-uipkey-globaltextcolor.md) in Ribbon apps designed for Windows 7.<br/> <br/> |



 

## Specify Ribbon Colors

The Ribbon framework uses a Hue, Saturation, Brightness (HSB) color model, which differs from the more common hue, saturation, luminosity (HSL) or hue, saturation, value (HSV) color spaces. In particular, B represents an overall brightness or luminosity level rather than the lightness of a particular color.

To specify the color of UI elements in the Ribbon framework, an application assigns HSB values to each of the global color properties. These values are then applied universally across all Ribbon elements as required by the Ribbon application (the framework does not support assigning HSB values to individual elements and controls).

****Introduced in Windows 8**:  **[UI\_PKEY\_GlobalHighlightColor](windowsribbon-reference-properties-uipkey-globalhighlightcolor.md) is assigned the same value as [UI\_PKEY\_GlobalBackgroundColor](windowsribbon-reference-properties-uipkey-globalbackgroundcolor.md).

The following table describes the Ribbon framework HSB parameters.



Component

Description

Adjusted Values\*

Hue (H)

The pigment, or actual, color is typically identified as a value from a circlular range of 0 to 359 degrees.

0 (red) to 255 (red)

Saturation (S)

The purity, or saturation, of the color measured as a percentage from 0 to 100%.

0 (grey) to 255 (fully saturated)

Brightness (B)

The overall brightness or darkness of the color measured as a percentage from 0 to 100%.

0 (dark) to 255 (light)

\* The original range for each parameter value is translated into a range of 0 to 255 for the framework.



 

HSB values do not identify specific colors. Instead, the combination of HSB property values influences how color gradients throughout the UI are adjusted relative to each other.

When assigning custom HSB values to [UI\_PKEY\_GlobalTextColor](windowsribbon-reference-properties-uipkey-globaltextcolor.md) and [UI\_PKEY\_GlobalBackgroundColor](windowsribbon-reference-properties-uipkey-globalbackgroundcolor.md), it is recommended that these values be of high enough contrast to ensure readability. Specifically, the text color should be darker than the lightest shade of the ribbon UI. Where necessary, the framework automatically adjusts the UI\_PKEY\_GlobalTextColor HSB value to provide sufficient contrast against any background shade or gradient derived from UI\_PKEY\_GlobalBackgroundColor.

> [!Note]  
> In Windows 7, [UI\_PKEY\_GlobalHighlightColor](windowsribbon-reference-properties-uipkey-globalhighlightcolor.md) can be set independently of [UI\_PKEY\_GlobalBackgroundColor](windowsribbon-reference-properties-uipkey-globalbackgroundcolor.md).

 

The following example demonstrates how to specify a custom color for the [UI\_PKEY\_GlobalTextColor](windowsribbon-reference-properties-uipkey-globaltextcolor.md), [UI\_PKEY\_GlobalBackgroundColor](windowsribbon-reference-properties-uipkey-globalbackgroundcolor.md), and [UI\_PKEY\_GlobalHighlightColor](windowsribbon-reference-properties-uipkey-globalhighlightcolor.md) properties.


```C++
CComPtr<IPropertyStore> spPropertyStore;

// _spFramework is a pointer to the IUIFramework interface that is assigned 
// when the Ribbon is initialized.
if (SUCCEEDED(_spFramework->QueryInterface(&spPropertyStore)))
{
  PROPVARIANT propvarBackground;
  PROPVARIANT propvarHighlight;
  PROPVARIANT propvarText;
 
  // UI_HSBCOLOR is a type defined in UIRibbon.h that is composed of 
  // three component values: hue, saturation and brightness, respectively.
  UI_HSBCOLOR BackgroundColor = UI_HSB(0x14, 0x38, 0x54);
  UI_HSBCOLOR HighlightColor = UI_HSB(0x00, 0x36, 0x87);
  UI_HSBCOLOR TextColor = UI_HSB(0x2B, 0xD6, 0x00);

  InitPropVariantFromUInt32(BackgroundColor, &propvarBackground);
  InitPropVariantFromUInt32(HighlightColor, &propvarHighlight);
  InitPropVariantFromUInt32(TextColor, &propvarText);
 
  spPropertyStore->SetValue(UI_PKEY_GlobalBackgroundColor, propvarBackground);
  spPropertyStore->SetValue(UI_PKEY_GlobalTextColor, propvarText);
 
  spPropertyStore->Commit();
}
```



## Convert RGB to HSB

This section describes the formula that is required for dynamically matching a Ribbon framework HSB value, the [UI\_PKEY\_GlobalBackgroundColor](windowsribbon-reference-properties-uipkey-globalbackgroundcolor.md) in this example, to a specific RGB color at run time.

The tab row background is used as a reference point because it is rendered as a flat color surface compared to the brightness gradient of the ribbon background.

A preliminary conversion is necessary to obtain an intermediate HSL value. This HSL value can then be converted to an HSB value.

> [!Note]  
> The conversion from RGB to HSL is easily accomplished with most photo editing software.

 

Conversion of HSL (with each component in the range of 0.0 to 1.0) to a Ribbon HSB setting is accomplished through the following formulas:

-   H<sub>background</sub> = Round(255.0 H)
-   S<sub>background</sub> = Round(255.0 S)
-   B<sub>background</sub> = Round(257.7 + 149.9 ln(L)) if 0.1793 <= L <= 0.9821

## Related topics

<dl> <dt>

[Color Guidelines](https://msdn.microsoft.com/library/aa511283.aspx)
</dt> <dt>

[Framework Properties](windowsribbon-reference-properties-framework.md)
</dt> </dl>

 

 





