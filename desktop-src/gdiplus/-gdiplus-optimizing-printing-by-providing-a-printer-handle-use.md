---
description: One of the constructors for the Graphics class receives a device context handle and a printer handle.
ms.assetid: 9be67cb2-4bf9-4758-af03-7d92dd04feaf
title: Optimizing Printing by Providing a Printer Handle
ms.topic: article
ms.date: 05/31/2018
---

# Optimizing Printing by Providing a Printer Handle

One of the constructors for the [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) class receives a device context handle and a printer handle. When you send Windows GDI+ commands to certain PostScript printers, the performance will be better if you create your **Graphics** object with that particular constructor.

The following console application calls [GetDefaultPrinter](../printdocs/getdefaultprinter.md) to get the name of the default printer. The code passes the printer name to [CreateDC](/windows/win32/api/wingdi/nf-wingdi-createdcw) to obtain a device context handle for the printer. The code also passes the printer name to [OpenPrinter](../printdocs/openprinter.md) to obtain a printer handle. Both the device context handle and the printer handle are passed to the [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) constructor. Then two figures are drawn on the printer.

> [!Note]  
> The [GetDefaultPrinter](../printdocs/getdefaultprinter.md) function is supported only on Windows 2000 and later.

 


```
#include <windows.h>
#include <gdiplus.h>
#include <stdio.h>
using namespace Gdiplus;

INT main()
{
   // Initialize GDI+.
   GdiplusStartupInput gdiplusStartupInput;
   ULONG_PTR gdiplusToken;
   GdiplusStartup(&gdiplusToken, &gdiplusStartupInput, NULL);

   DWORD   size;
   HDC     hdcPrint;
   HANDLE  printerHandle;

   DOCINFO docInfo;
   ZeroMemory(&docInfo, sizeof(docInfo));
   docInfo.cbSize = sizeof(docInfo);
   docInfo.lpszDocName = "GdiplusPrint";

   // Get the length of the printer name.
   GetDefaultPrinter(NULL, &size);
   TCHAR* buffer = new TCHAR[size];

   // Get the printer name.
   if(!GetDefaultPrinter(buffer, &size))
   {
      printf("Failure");
   }
   else
   {
      // Get a device context for the printer.
      hdcPrint = CreateDC(NULL, buffer, NULL, NULL);

      // Get a printer handle.
      OpenPrinter(buffer, &printerHandle, NULL);

      StartDoc(hdcPrint, &docInfo);
      StartPage(hdcPrint);
         Graphics* graphics = new Graphics(hdcPrint, printerHandle);
         Pen* pen = new Pen(Color(255, 0, 0, 0));
         graphics->DrawRectangle(pen, 200, 500, 200, 150);
         graphics->DrawEllipse(pen, 200, 500, 200, 150);
         delete(pen);
         delete(graphics);
      EndPage(hdcPrint);
      EndDoc(hdcPrint);

      ClosePrinter(printerHandle);
      DeleteDC(hdcPrint);
   }

   delete buffer;
   
   GdiplusShutdown(gdiplusToken);
   return 0;
}
```



 

 
