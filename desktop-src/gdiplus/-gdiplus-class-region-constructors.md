---
Description: This topic lists the constructors of the Region class. For a complete class listing, see Region Class.
ms.assetid: 94f4971c-defa-43e0-a0c0-4000557b0a5c
title: Region.Region constructors
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
api_type: 
- NA
api_location: 
---

# Region.Region constructors

This topic lists the constructors of the [**Region**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-region) class. For a complete class listing, see **Region Class**.

### Overload list



| Constructor                                                                 | Description                                                                                                                                                                                      |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Region(HRGN)**](https://msdn.microsoft.com/en-us/library/ms534924(v=VS.85).aspx)                  | Creates a region that is identical to the region that is specified by a handle to a GDI region.<br/>                                                                                       |
| [**Region(Rect&)**](https://msdn.microsoft.com/en-us/library/ms534920(v=VS.85).aspx)            | Creates a region that is defined by a rectangle.<br/>                                                                                                                                      |
| [**Region(RectF&)**](https://msdn.microsoft.com/en-us/library/ms534925(v=VS.85).aspx)          | Creates a region that is defined by a rectangle.<br/>                                                                                                                                      |
| [**Region(BYTE\*,INT)**](https://msdn.microsoft.com/en-us/library/ms534922(v=VS.85).aspx) | Creates a region that is defined by data obtained from another region. <br/>                                                                                                               |
| [**Region(GraphicsPath\*)**](https://msdn.microsoft.com/en-us/library/ms534923(v=VS.85).aspx)        | Creates a region that is defined by a path (a [**GraphicsPath**](/windows/desktop/api/gdipluspath/nl-gdipluspath-graphicspath) object) and has a fill mode that is contained in the **GraphicsPath** object.<br/> |
| [**Region()**](https://msdn.microsoft.com/en-us/library/ms534921(v=VS.85).aspx)                           | Creates a region that is infinite. This is the default constructor. <br/>                                                                                                                  |



 

 




