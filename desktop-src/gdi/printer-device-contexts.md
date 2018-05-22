---
Description: 'The printer DC can be used when printing on a dot-matrix printer, ink-jet printer, laser printer, or plotter.'
ms.assetid: 'c53f15d8-5a02-4095-8f05-ae309d4553ff'
title: Printer Device Contexts
---

# Printer Device Contexts

The printer DC can be used when printing on a dot-matrix printer, ink-jet printer, laser printer, or plotter. An application creates a printer DC by calling the [**CreateDC**](createdc.md) function and supplying the appropriate arguments (the name of the printer driver, the name of the printer, the file or device name for the physical output medium, and other initialization data). When an application has finished printing, it deletes the printer DC by calling the [**DeleteDC**](deletedc.md) function. An application must delete (rather than release) a printer DC; the [**ReleaseDC**](releasedc.md) function fails when an application attempts to use it to release a printer DC.

For more information, see [Printer Output](gdi.printer_output).

 

 



