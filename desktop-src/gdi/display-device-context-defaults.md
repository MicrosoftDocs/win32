---
description: Upon first creating a display device context, the system assigns default values for the attributes (that is, drawing objects, colors, and modes) that comprise the device context.
ms.assetid: 1a9244e6-2773-435a-8569-806df3a0cd39
title: Display Device Context Defaults
ms.topic: article
ms.date: 05/31/2018
---

# Display Device Context Defaults

Upon first creating a display device context, the system assigns default values for the attributes (that is, drawing objects, colors, and modes) that comprise the device context. The following table shows the default values for the attributes of a display device context.



| Attribute                             | Default value                                                                                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Background color                      | Background color setting from Control Panel (typically, white).                                                                               |
| Background mode                       | OPAQUE                                                                                                                                        |
| Bitmap                                | None                                                                                                                                          |
| Brush                                 | WHITE\_BRUSH                                                                                                                                  |
| Brush origin                          | (0,0)                                                                                                                                         |
| Clipping region                       | Entire window or client area with the update region clipped, as appropriate. Child and pop-up windows in the client area may also be clipped. |
| Palette                               | DEFAULT\_PALETTE                                                                                                                              |
| Current pen position                  | (0,0)                                                                                                                                         |
| Device origin                         | Upper left corner of the window or the client area.                                                                                           |
| Drawing mode                          | R2\_COPYPEN                                                                                                                                   |
| Font                                  | SYSTEM\_FONT                                                                                                                                  |
| Intercharacter spacing                | 0                                                                                                                                             |
| Mapping mode                          | MM\_TEXT                                                                                                                                      |
| Pen                                   | BLACK\_PEN                                                                                                                                    |
| [**Polygon**](/windows/desktop/api/Wingdi/nf-wingdi-polygon) -fill mode | ALTERNATE                                                                                                                                     |
| Stretch mode                          | BLACKONWHITE                                                                                                                                  |
| Text color                            | Text color setting from Control Panel (typically, black).                                                                                     |
| Viewport extent                       | (1,1)                                                                                                                                         |
| Viewport origin                       | (0,0)                                                                                                                                         |
| Window extent                         | (1,1)                                                                                                                                         |
| Window origin                         | (0,0)                                                                                                                                         |



 

An application can modify the values of the display device context attributes by using selection and attribute functions, such as [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject), [**SetMapMode**](/windows/desktop/api/Wingdi/nf-wingdi-setmapmode), and [**SetTextColor**](/windows/desktop/api/Wingdi/nf-wingdi-settextcolor). For example, an application can modify the default units of measure in the coordinate system by using **SetMapMode** to change the mapping mode.

Changes to the attribute values of a common, parent, or window device context are not permanent. When an application releases these device contexts, the current selections, such as mapping mode and clipping region, are lost as the context is returned to the cache. Changes to a class or private device context persist indefinitely. To restore them to their original defaults, an application must explicitly set each attribute.

 

 



