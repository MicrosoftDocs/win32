---
Description: Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h.
ms.assetid: 06718603-e001-49d4-ac5e-decdd98df42b
title: CachedBitmap Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CachedBitmap Functions

Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h. The functions in the GDI+ flat API are wrapped by a collection of about 40 C++ classes. It is recommended that you do not directly call the functions in the flat API. Whenever you make calls to GDI+, you should do so by calling the methods and functions provided by the C++ wrappers. Microsoft Product Support Services will not provide support for code that calls the flat API directly. For more information on using these wrapper methods, see [GDI+ Flat API](-gdiplus-flatapi-flat.md).

The following flat API functions are wrapped by the [**CachedBitmap**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-cachedbitmap?branch=master) C++ class.

## CachedBitmap Functions and Corresponding Wrapper Methods



| Flat function                                                                                                             | Wrapper method                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GpStatus WINGDIPAPI GdipCreateCachedBitmap( GpBitmap \*bitmap, GpGraphics \*graphics, GpCachedBitmap \*\*cachedBitmap )   | [**CachedBitmap::CachedBitmap**](/windows/win32/Gdiplusheaders/nf-gdiplusheaders-cachedbitmap-cachedbitmap(const cachedbitmap &)?branch=master) | Creates a [**CachedBitmap::CachedBitmap**](/windows/win32/Gdiplusheaders/nf-gdiplusheaders-cachedbitmap-cachedbitmap(const cachedbitmap &)?branch=master) object based on a [**Bitmap**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-bitmap?branch=master) object and a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object. The cached bitmap takes the pixel data from the **Bitmap** object and stores it in a format that is optimized for the display device associated with the **Graphics** object. |
| GpStatus WINGDIPAPI GdipDeleteCachedBitmap(GpCachedBitmap \*cachedBitmap)<br/>                                      | ~CachedBitmap()                                                                                 | Cleans up resources used by a [**CachedBitmap**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-cachedbitmap?branch=master) object.                                                                                                                                                                                                                                                                                                                                |
| GpStatus WINGDIPAPI GdipDrawCachedBitmap( GpGraphics \*graphics, GpCachedBitmap \*cachedBitmap, INT x, INT y )            | [**Graphics::DrawCachedBitmap**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-drawcachedbitmap?branch=master)          | The [**Graphics::DrawCachedBitmap**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-drawcachedbitmap?branch=master) method draws the image stored in a [**CachedBitmap**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-cachedbitmap?branch=master) object.                                                                                                                                                                                                                                |
| UINT WINGDIPAPI GdipEmfToWmfBits( HENHMETAFILE hemf, UINT cbData16, LPBYTE pData16, INT iMapMode, INT eFlags )<br/> | [**Metafile::EmfToWmfBits**](/windows/win32/gdiplusheaders/nf-gdiplusheaders-metafile-emftowmfbits?branch=master)                         | Converts an enhanced-format metafile to a Windows Metafile Format (WMF) metafile and stores the converted records in a specified buffer.                                                                                                                                                                                                                                                                                       |



 

 

 




