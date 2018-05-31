---
Description: This topic lists the constructors of the Region class. For a complete class listing, see Region Class.
ms.assetid: 94f4971c-defa-43e0-a0c0-4000557b0a5c
title: Region.Region constructors
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Region.Region constructors

This topic lists the constructors of the [**Region**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-region) class. For a complete class listing, see **Region Class**.

### Overload list



| Constructor                                                                 | Description                                                                                                                                                                                      |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Region(HRGN)**](/windows/desktop/api/Gdiplusheaders/)                  | Creates a region that is identical to the region that is specified by a handle to a GDI region.<br/>                                                                                       |
| [**Region(Rect&)**](/windows/desktop/api/Gdiplusheaders/)            | Creates a region that is defined by a rectangle.<br/>                                                                                                                                      |
| [**Region(RectF&)**](/windows/desktop/api/Gdiplusheaders/)          | Creates a region that is defined by a rectangle.<br/>                                                                                                                                      |
| [**Region(BYTE\*,INT)**](/windows/desktop/api/Gdiplusheaders/) | Creates a region that is defined by data obtained from another region. <br/>                                                                                                               |
| [**Region(GraphicsPath\*)**](/windows/desktop/api/Gdiplusheaders/)        | Creates a region that is defined by a path (a [**GraphicsPath**](/windows/desktop/api/gdipluspath/nl-gdipluspath-graphicspath) object) and has a fill mode that is contained in the **GraphicsPath** object.<br/> |
| [**Region()**](/windows/desktop/api/Gdiplusheaders/nf-gdiplusheaders-region-region(const region &))                           | Creates a region that is infinite. This is the default constructor. <br/>                                                                                                                  |



 

 




