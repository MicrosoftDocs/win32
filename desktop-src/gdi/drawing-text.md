---
Description: Drawing Text
ms.assetid: 8a06f659-4e08-4738-b7a9-956b599c1344
title: Drawing Text
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Drawing Text

After an application selects the appropriate font, sets the required text-formatting options, and computes the necessary character width and height values for a string of text, it can begin drawing characters and symbols by calling any of the text-output functions:

-   [DrawText](/windows/win32/Winuser/nf-winuser-drawtext?branch=master)
-   [DrawTextEx](/windows/win32/Winuser/nf-winuser-drawtextexa?branch=master)
-   [ExtTextOut](/windows/win32/Wingdi/nf-wingdi-exttextouta?branch=master)
-   [PolyTextOut](/windows/win32/Wingdi/nf-wingdi-polytextouta?branch=master)
-   [TabbedTextOut](/windows/win32/Winuser/nf-winuser-tabbedtextouta?branch=master)
-   [TextOut](/windows/win32/Wingdi/nf-wingdi-textouta?branch=master)

When an application calls one of these functions, the operating system passes the call to the graphics engine, which in turn passes the call to the appropriate device driver. At the device driver level, all of these calls are supported by one or more calls to the driver's own [ExtTextOut](/windows/win32/Wingdi/nf-wingdi-exttextouta?branch=master) or [TextOut](/windows/win32/Wingdi/nf-wingdi-textouta?branch=master) function. An application will achieve the fastest execution by calling [**ExtTextOut**](gdi.ExtTextOut), which is quickly converted into an **ExtTextOut** call for the device. However, there are instances when an application should call one of the other three functions; for example, to draw multiple lines of text within the borders of a specified rectangular region, it is more efficient to call [**DrawText**](gdi.DrawText). To create a multicolumn table with justified columns of text, it is more efficient to call [**TabbedTextOut**](gdi.TabbedTextOut).

 

 



