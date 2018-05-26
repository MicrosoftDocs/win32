---
Description: The printer DC can be used when printing on a dot-matrix printer, ink-jet printer, laser printer, or plotter.
ms.assetid: c53f15d8-5a02-4095-8f05-ae309d4553ff
title: Printer Device Contexts
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Printer Device Contexts

The printer DC can be used when printing on a dot-matrix printer, ink-jet printer, laser printer, or plotter. An application creates a printer DC by calling the [**CreateDC**](/windows/win32/Wingdi/nf-wingdi-createdca?branch=master) function and supplying the appropriate arguments (the name of the printer driver, the name of the printer, the file or device name for the physical output medium, and other initialization data). When an application has finished printing, it deletes the printer DC by calling the [**DeleteDC**](/windows/win32/Wingdi/nf-wingdi-deletedc?branch=master) function. An application must delete (rather than release) a printer DC; the [**ReleaseDC**](/windows/win32/Winuser/nf-winuser-releasedc?branch=master) function fails when an application attempts to use it to release a printer DC.

For more information, see [Printer Output](gdi.printer_output).

 

 



