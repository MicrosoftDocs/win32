---
description: With a few minor adjustments to your code, you can send Windows GDI+ output to a printer rather than to a screen.
ms.assetid: be6286e9-d125-40ad-b33e-b4e734ac2709
title: Printing (GDI+)
ms.topic: article
ms.date: 05/31/2018
---

# Printing (GDI+)

With a few minor adjustments to your code, you can send Windows GDI+ output to a printer rather than to a screen. To draw on a printer, obtain a device context handle for the printer and pass that handle to a [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) constructor. Place your GDI+ drawing commands in between calls to [StartDoc](/windows/win32/api/wingdi/nf-wingdi-startdocw) and [EndDoc](/windows/win32/api/wingdi/nf-wingdi-enddoc).

The following topics cover sending GDI+ output to printers in more detail:

-   [Sending GDI+ Output to a Printer](-gdiplus-sending-gdi-output-to-a-printer-use.md)
-   [Displaying a Print Dialog Box](-gdiplus-displaying-a-print-dialog-box-use.md)
-   [Optimizing Printing by Providing a Printer Handle](-gdiplus-optimizing-printing-by-providing-a-printer-handle-use.md)

 

 



