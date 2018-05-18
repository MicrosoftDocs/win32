---
title: ID2D1Factory CreateWicBitmapRenderTarget methods
description: Creates a render target that renders to a Microsoft Windows Imaging Component (WIC) bitmap.
ms.assetid: '93141743-c11d-40b4-83c5-07c9066836c7'
keywords: ["CreateWicBitmapRenderTarget methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1Factory::CreateWicBitmapRenderTarget methods

Creates a render target that renders to a Microsoft Windows Imaging Component (WIC) bitmap.

### Overload list



| Method                                                                                                                                                                                                                            | Description                                                                                            |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| [**CreateWicBitmapRenderTarget(IWICBitmap\*,D2D1\_RENDER\_TARGET\_PROPERTIES\*,ID2D1RenderTarget\*\*)**](id2d1factory-createwicbitmaprendertarget-ptr-iwicbitmap-ptr-d2d1-render-target-properties-ptr-ptr-id2d1rendertarget.md) | Creates a render target that renders to a Microsoft Windows Imaging Component (WIC) bitmap.<br/> |
| [**CreateWicBitmapRenderTarget(IWICBitmap\*,D2D1\_RENDER\_TARGET\_PROPERTIES&,ID2D1RenderTarget\*\*)**](id2d1factory-createwicbitmaprendertarget-ptr-iwicbitmap-ref-d2d1-render-target-properties-ptr-ptr-id2d1rendertarget.md)  | Creates a render target that renders to a Microsoft Windows Imaging Component (WIC) bitmap.<br/> |



## Remarks

Your application should create render targets once and hold onto them for the life of the application or until the [**D2DERR\_RECREATE\_TARGET**](direct2d-error-codes.md) error is received. When you receive this error, you need to recreate the render target (and any resources it created).

-   ![applies to windows phone](../common/phone.png)

**Note**   This method isn't supported on Windows Phone and will fail when called on a device with error code 0x8899000b (“There is no hardware rendering device available for this operation”). Because the Windows Phone Emulator supports WARP rendering, this method will fail when called on the emulator with a different error code, 0x88982f80 (wincodec\_err\_unsupportedpixelformat).

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Factory**](id2d1factory.md)
</dt> </dl>

 

 





