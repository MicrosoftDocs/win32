---
title: Specifying Ribbon Image Resources
description: As a rich command presentation system, the Windows Ribbon framework is designed to support image resources extensively throughout the Ribbon user interface (UI). All image resources are declared in Ribbon markup or queried from a Ribbon host application.
ms.assetid: 37b57992-8da8-4e6b-869d-72a136f6ad77
keywords:
- Windows Ribbon,image resources
- Ribbon,image resources
- Windows Ribbon,transparency
- Ribbon,transparency
- Windows Ribbon,color depth
- Ribbon,color depth
- Windows Ribbon,contrast
- Ribbon,contrast
- image resources in Windows Ribbon
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Ribbon Image Resources

As a rich command presentation system, the Windows Ribbon framework is designed to support image resources extensively throughout the Ribbon user interface (UI). All image resources are declared in [Ribbon markup](windowsribbon-schema.md) or queried from a Ribbon host application.

For Windows 8 and later, the Ribbon framework supports the following graphics formats: 32-bit ARGB bitmap (BMP) files and Portable Network Graphics (PNG) files with transparency.

For Windows 7 and earlier, image resources must conform to the standard BMP graphics format used in Windows.

> [!Note]  
> A compilation error may occur if an unsupported image format is supplied to the framework.

 

## Image Sizes

To provide greater flexibility for Ribbon control layouts when resizing an application window, the Ribbon framework accepts and renders images in one of two sizes: large or small.

The following images illustrate a Ribbon application that supports multiple Ribbon sizes through flexible control layouts and the replacement of large images with small images where available.

The following screen shot shows the Ribbon with large images for the Zoom controls.

![screen shot showing a ribbon that uses large images for the zoom controls.](images/overviews/imageresources-largeimage.png)

The following screen shot shows the same Ribbon resized with small images for the Zoom controls

![screen shot showing a ribbon that uses small images for the zoom controls.](images/overviews/imageresources-smallimage.png)

The following screen shot shows the ribbon in hidden state. The ribbon is hidden when all potential control layouts have been exhausted and the ribbon cannot be rendered with a usable application workspace.

![screen shot showing a collapsed ribbon.](images/overviews/imageresources-noimage.png)

For any image, the exact pixel size is dependent on the display resolution, or dots per inch (dpi), of the monitor being used. At 96 dpi, large images are 32x32 pixels in size and small images are 16x16 pixels in size. The image sizes increase in a linear fashion relative to dpi as illustrated in the following table.



| DPI     | Small Image  | Large Image  |
|---------|--------------|--------------|
| 96 dpi  | 16x16 pixels | 32x32 pixels |
| 120 dpi | 20x20 pixels | 40x40 pixels |
| 144 dpi | 24x24 pixels | 48x48 pixels |
| 192 dpi | 32x32 pixels | 64x64 pixels |



 

The Ribbon framework scales image resources as required. However, because resizing may yield undesirable artifacts and image degradation, it is highly recommended that the application provide a small set of image resources that span various commonly used dpi settings. If an exact match is not found, the nearest image will be scaled up or down.

To facilitate this, image resources can be declared in Ribbon markup by using a set of [**Image**](windowsribbon-element-image.md) elements for each [**Command**](windowsribbon-element-command.md) element. At run time, the framework selects the image to display based on the *MinDPI* attribute of each **Image** element.

> [!IMPORTANT]
>
> When a collection of image resources that are designed to support specific screen dpi settings is supplied to the Ribbon framework through a set of [**Image**](windowsribbon-element-image.md) elements, the framework uses the **Image** with a *MinDPI* attribute value that matches the current screen dpi setting.
>
> If no [**Image**](windowsribbon-element-image.md) element is declared with a *MinDPI* value that matches the current screen dpi setting, the framework picks the **Image** that has the nearest *MinDPI* value less than the current screen dpi setting and scales the image resource up. Otherwise, if no **Image** element is declared with a *MinDPI* attribute value less than the current screen dpi setting, the framework picks the nearest *MinDPI* value greater than the current screen dpi setting and scales the image resource down.

 

The following example illustrates how to declare a set of images to accommodate various Ribbon sizes and system settings.


```C++
<Command.LargeImages>
  <Image Source="res/CutLargeImage32.bmp" Id="116" Symbol="ID_CUT_LARGEIMAGE1" MinDPI="96" />
  <Image Source="res/CutLargeImage40.bmp" Id="117" Symbol="ID_CUT_LARGEIMAGE2" MinDPI="120" />
  <Image Source="res/CutLargeImage48.bmp" Id="118" Symbol="ID_CUT_LARGEIMAGE3" MinDPI="144" />
  <Image Source="res/CutLargeImage64.bmp" Id="119" Symbol="ID_CUT_LARGEIMAGE4" MinDPI="192" />
</Command.LargeImages>
<Command.SmallImages>
  <Image Source="res/CutSmallImage16.bmp" Id="122" Symbol="ID_CUT_SMALLIMAGE1" MinDPI="96" />
  <Image Source="res/CutSmallImage20.bmp" Id="123" Symbol="ID_CUT_SMALLIMAGE2" MinDPI="120" />
  <Image Source="res/CutSmallImage24.bmp" Id="124" Symbol="ID_CUT_SMALLIMAGE3" MinDPI="144" />
  <Image Source="res/CutSmallImage32.bmp" Id="125" Symbol="ID_CUT_SMALLIMAGE4" MinDPI="192" />
</Command.SmallImages>
<Command.LargeHighContrastImages>
  <Image Source="res/CutLargeImage32HC.bmp" Id="130" Symbol="ID_CUT_LARGEIMAGE1HC" MinDPI="96" />
  <Image Source="res/CutLargeImage40HC.bmp" Id="131" Symbol="ID_CUT_LARGEIMAGE2HC" MinDPI="120" />
  <Image Source="res/CutLargeImage48HC.bmp" Id="132" Symbol="ID_CUT_LARGEIMAGE3HC" MinDPI="144" />
  <Image Source="res/CutLargeImage64HC.bmp" Id="133" Symbol="ID_CUT_LARGEIMAGE4HC" MinDPI="192" />
</Command.LargeHighContrastImages>
<Command.SmallHighContrastImages>
  <Image Source="res/CutSmallImage16HC.bmp" Id="135" Symbol="ID_CUT_SMALLIMAGE1HC" MinDPI="96" />
  <Image Source="res/CutSmallImage20HC.bmp" Id="136" Symbol="ID_CUT_SMALLIMAGE2HC" MinDPI="120" />
  <Image Source="res/CutSmallImage24HC.bmp" Id="137" Symbol="ID_CUT_SMALLIMAGE3HC" MinDPI="144" />
  <Image Source="res/CutSmallImage32HC.bmp" Id="138" Symbol="ID_CUT_SMALLIMAGE4HC" MinDPI="192" />
</Command.SmallHighContrastImages>
```



If images declared in markup are invalidated at run time for any reason, the host application is queried for new images. When these images are generated and loaded programmatically, the application should attempt to return images that are sized according to the default system icon sizes determined by the [SM\_CXICON system metric](/windows/win32/api/winuser/nf-winuser-getsystemmetrics).

> [!Note]  
> Large images have a size of SM\_CXICON by SM\_CXICON and small images have a size of SM\_CXICON/2 by SM\_CXICON/2.

 

## Color Depth, Transparency, and Contrast

Regular images are expected to be in 32 bits per pixel (BPP) ARGB pixel format and scaled to the default system icon size. This format supports both transparency and antialiasing (using 8 bits per channel).

> [!WARNING]
> Many image editing tools do not preserve the highest order 8-bit alpha channel when loading or saving 32 BPP images.

 

For an image to display correctly in high-contrast mode, it must be in a 4 BPP palletized pixel format. When the image is rendered, the Ribbon framework remaps specific colors based on the high-contrast context of the image.

The following table lists the high-contrast color rendering behavior of the framework.



Pixel color

RGB value

Behavior

White background

Dark Background

MAGENTA

800080

Transparent

Transparent

BLACK

000000

COLOR\_WINDOWTEXT

WHITE

WHITE

FFFFFF

COLOR\_WINDOW

BLACK

DARK GRAY

808080

COLOR\_3DSHADOW

COLOR\_3DSHADOW

GRAY

C0C0C0

COLOR\_3DFACE

COLOR\_3DFACE

LIGHT GRAY

DFDFDF

COLOR\_3DLIGHT

COLOR\_3DLIGHT

DARK BLUE

000080

n/a

WHITE



 

For more information on the image formats supported by the Ribbon framework, see the following:

-   [BITMAPINFOHEADER structure](/previous-versions//dd183376(v=vs.85)) - describes the 32 BPP ARGB pixel format.
-   [CreateDIBSection function](/windows/win32/api/wingdi/nf-wingdi-createdibsection) - describes how to create a 32 BPP ARGB pixel format image.
-   [LoadImage function](/windows/win32/api/winuser/nf-winuser-loadimagea) - describes how to load a 32 BPP ARGB pixel format image.

## Accessibility

Relying on image resources to provide information, convey control functionality, and expose application state, increases the need for accessibility requirements during application design and development.

For basic high contrast support, the Ribbon allows for a separate set of image files to be displayed when a high-contrast theme is active. These images can be 32 BPP or 4 BPP, with colors mapped to a special palette where dark and light colors are inverted depending on the foreground and background colors of the active high-contrast theme.

The following example demonstrates how high-contrast image resources are declared in Ribbon markup:


```C++
<Command Name="cmdNew" Id="0xE100" Symbol="ID_CMD_NEW" LabelTitle="New document" Keytip="N" >
      <Command.TooltipTitle>New (Ctrl+N)</Command.TooltipTitle>
      <Command.TooltipDescription>Create a new document.</Command.TooltipDescription>
      <Command.LargeImages>
        <Image Source="cmdNew-32px.bmp" MinDPI="96" />
        <Image Source="cmdNew-40px.bmp" MinDPI="120" />
        <Image Source="cmdNew-48px.bmp" MinDPI="144" />
        <Image Source="cmdNew-64px.bmp" MinDPI="192" />
      </Command.LargeImages>
      <Command.LargeHighContrastImages>
        <Image Source="cmdNew-32px-HC.bmp" MinDPI="96" />
        <Image Source="cmdNew-40px-HC.bmp" MinDPI="120" />
        <Image Source="cmdNew-48px-HC.bmp" MinDPI="144" />
        <Image Source="cmdNew-64px-HC.bmp" MinDPI="192" />
      </Command.LargeHighContrastImages>
      <Command.SmallImages>
        <Image Source="cmdNew-16px.bmp" MinDPI="96" />
        <Image Source="cmdNew-20px.bmp" MinDPI="120" />
        <Image Source="cmdNew-24px.bmp" MinDPI="144" />
        <Image Source="cmdNew-32px.bmp" MinDPI="192" />
      </Command.SmallImages>
      <Command.SmallHighContrastImages>
        <Image Source="cmdNew-16px-HC.bmp" MinDPI="96" />
        <Image Source="cmdNew-20px-HC.bmp" MinDPI="120" />
        <Image Source="cmdNew-24px-HC.bmp" MinDPI="144" />
        <Image Source="cmdNew-32px-HC.bmp" MinDPI="192" />
      </Command.SmallHighContrastImages>
    </Command>
```



## Related topics

<dl> <dt>

[**Command.SmallImages**](windowsribbon-element-command-smallimages.md)
</dt> <dt>

[UI\_PKEY\_SmallImage](windowsribbon-reference-properties-uipkey-smallimage.md)
</dt> <dt>

[**Command.LargeImages**](windowsribbon-element-command-largeimages.md)
</dt> <dt>

[UI\_PKEY\_LargeImage](windowsribbon-reference-properties-uipkey-largeimage.md)
</dt> <dt>

[**Command.SmallHighContrastImages**](windowsribbon-element-command-smallhighcontrastimages.md)
</dt> <dt>

[UI\_PKEY\_SmallHighContrastImage](windowsribbon-reference-properties-uipkey-smallhighcontrastimage.md)
</dt> <dt>

[**Command.LargeHighContrastImages**](windowsribbon-element-command-largehighcontrastimages.md)
</dt> <dt>

[UI\_PKEY\_LargeHighContrastImage](windowsribbon-reference-properties-uipkey-largehighcontrastimage.md)
</dt> </dl>

 

 