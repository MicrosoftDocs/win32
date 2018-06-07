---
Description: Drawing Text
ms.assetid: 8a06f659-4e08-4738-b7a9-956b599c1344
title: Drawing Text
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Drawing Text

After an application selects the appropriate font, sets the required text-formatting options, and computes the necessary character width and height values for a string of text, it can begin drawing characters and symbols by calling any of the text-output functions:

-   [DrawText](/windows/desktop/api/Winuser/nf-winuser-drawtext)
-   [DrawTextEx](/windows/desktop/api/Winuser/nf-winuser-drawtextexa)
-   [ExtTextOut](/windows/desktop/api/Wingdi/nf-wingdi-exttextouta)
-   [PolyTextOut](/windows/desktop/api/Wingdi/nf-wingdi-polytextouta)
-   [TabbedTextOut](/windows/desktop/api/Winuser/nf-winuser-tabbedtextouta)
-   [TextOut](/windows/desktop/api/Wingdi/nf-wingdi-textouta)

When an application calls one of these functions, the operating system passes the call to the graphics engine, which in turn passes the call to the appropriate device driver. At the device driver level, all of these calls are supported by one or more calls to the driver's own [ExtTextOut](/windows/desktop/api/Wingdi/nf-wingdi-exttextouta) or [TextOut](/windows/desktop/api/Wingdi/nf-wingdi-textouta) function. An application will achieve the fastest execution by calling [**ExtTextOut**](https://msdn.microsoft.com/74f8fcb8-8ad4-47f2-a330-fa56713bdb37), which is quickly converted into an **ExtTextOut** call for the device. However, there are instances when an application should call one of the other three functions; for example, to draw multiple lines of text within the borders of a specified rectangular region, it is more efficient to call [**DrawText**](https://msdn.microsoft.com/fe412280-d797-4abd-8a29-107a9cd96145). To create a multicolumn table with justified columns of text, it is more efficient to call [**TabbedTextOut**](https://msdn.microsoft.com/1cb78a75-752d-4e06-afdf-cd797f209114).

 

 



