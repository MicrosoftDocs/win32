---
Description: This topic lists the constructors of the Region class. For a complete class listing, see Region Class.
ms.assetid: 94f4971c-defa-43e0-a0c0-4000557b0a5c
title: Region.Region constructors
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Region.Region constructors

This topic lists the constructors of the [**Region**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-region?branch=master) class. For a complete class listing, see **Region Class**.

### Overload list



| Constructor                                                                 | Description                                                                                                                                                                                      |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Region(HRGN)**](/windows/win32/Gdiplusheaders/?branch=master)                  | Creates a region that is identical to the region that is specified by a handle to a GDI region.<br/>                                                                                       |
| [**Region(Rect&)**](/windows/win32/Gdiplusheaders/?branch=master)            | Creates a region that is defined by a rectangle.<br/>                                                                                                                                      |
| [**Region(RectF&)**](/windows/win32/Gdiplusheaders/?branch=master)          | Creates a region that is defined by a rectangle.<br/>                                                                                                                                      |
| [**Region(BYTE\*,INT)**](/windows/win32/Gdiplusheaders/?branch=master) | Creates a region that is defined by data obtained from another region. <br/>                                                                                                               |
| [**Region(GraphicsPath\*)**](/windows/win32/Gdiplusheaders/?branch=master)        | Creates a region that is defined by a path (a [**GraphicsPath**](/windows/win32/gdipluspath/nl-gdipluspath-graphicspath?branch=master) object) and has a fill mode that is contained in the **GraphicsPath** object.<br/> |
| [**Region()**](/windows/win32/Gdiplusheaders/nf-gdiplusheaders-region-region(const region &)?branch=master)                           | Creates a region that is infinite. This is the default constructor. <br/>                                                                                                                  |



 

 




