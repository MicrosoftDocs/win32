---
Description: 'Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h.'
ms.assetid: '06718603-e001-49d4-ac5e-decdd98df42b'
title: CachedBitmap Functions
---

# CachedBitmap Functions

Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h. The functions in the GDI+ flat API are wrapped by a collection of about 40 C++ classes. It is recommended that you do not directly call the functions in the flat API. Whenever you make calls to GDI+, you should do so by calling the methods and functions provided by the C++ wrappers. Microsoft Product Support Services will not provide support for code that calls the flat API directly. For more information on using these wrapper methods, see [GDI+ Flat API](-gdiplus-flatapi-flat.md).

The following flat API functions are wrapped by the [**CachedBitmap**](-gdiplus-class-cachedbitmap-class.md) C++ class.

## CachedBitmap Functions and Corresponding Wrapper Methods



| Flat function                                                                                                             | Wrapper method                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GpStatus WINGDIPAPI GdipCreateCachedBitmap( GpBitmap \*bitmap, GpGraphics \*graphics, GpCachedBitmap \*\*cachedBitmap )   | [**CachedBitmap::CachedBitmap**](-gdiplus-class-cachedbitmap-cachedbitmap-bitmap-graphics-.md) | Creates a [**CachedBitmap::CachedBitmap**](-gdiplus-class-cachedbitmap-cachedbitmap-bitmap-graphics-.md) object based on a [**Bitmap**](-gdiplus-class-bitmap-class.md) object and a [**Graphics**](-gdiplus-class-graphics-class.md) object. The cached bitmap takes the pixel data from the **Bitmap** object and stores it in a format that is optimized for the display device associated with the **Graphics** object. |
| GpStatus WINGDIPAPI GdipDeleteCachedBitmap(GpCachedBitmap \*cachedBitmap)<br/>                                      | ~CachedBitmap()                                                                                 | Cleans up resources used by a [**CachedBitmap**](-gdiplus-class-cachedbitmap-class.md) object.                                                                                                                                                                                                                                                                                                                                |
| GpStatus WINGDIPAPI GdipDrawCachedBitmap( GpGraphics \*graphics, GpCachedBitmap \*cachedBitmap, INT x, INT y )            | [**Graphics::DrawCachedBitmap**](-gdiplus-class-graphics-drawcachedbitmap-cb-x-y-.md)          | The [**Graphics::DrawCachedBitmap**](-gdiplus-class-graphics-drawcachedbitmap-cb-x-y-.md) method draws the image stored in a [**CachedBitmap**](-gdiplus-class-cachedbitmap-class.md) object.                                                                                                                                                                                                                                |
| UINT WINGDIPAPI GdipEmfToWmfBits( HENHMETAFILE hemf, UINT cbData16, LPBYTE pData16, INT iMapMode, INT eFlags )<br/> | [**Metafile::EmfToWmfBits**](-gdiplus-class-metafile-emftowmfbits-.md)                         | Converts an enhanced-format metafile to a Windows Metafile Format (WMF) metafile and stores the converted records in a specified buffer.                                                                                                                                                                                                                                                                                       |



 

 

 




