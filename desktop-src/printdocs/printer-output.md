---
Description: Just as an application requires a display device context (DC) before it can begin drawing in the client area of a window, it needs a printer DC before it can begin sending output to a printer.
ms.assetid: 5bdcec28-e28d-402d-8d80-e8aa5ecb4e74
title: Printer Device Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Printer Device Contexts

Just as an application requires a display device context (DC) before it can begin drawing in the client area of a window, it needs a printer DC before it can begin sending output to a printer. A printer DC is similar to a display DC in that it is an internal data structure that defines a set of graphic objects and their associated attributes and specifies the graphic modes that affect output. The graphic objects include a pen for line drawing, a brush for painting and filling, and a font for text output.

Unlike a display DC, a printer DC is not owned by the window management component, and it cannot be obtained by calling the [**GetDC**](https://docs.microsoft.com/windows/desktop/api/winuser/nf-winuser-getdc) function. Instead, an application must call the [**CreateDC**](https://docs.microsoft.com/windows/desktop/api/wingdi/nf-wingdi-createdca) or [**PrintDlgEx**](https://msdn.microsoft.com/library/ms646942(v=VS.85).aspx) function.

If your application calls the [**CreateDC**](https://docs.microsoft.com/windows/desktop/api/wingdi/nf-wingdi-createdca) function, it must supply a driver and port name. To retrieve these names, call the [**GetPrinter**](getprinter.md) or [**EnumPrinters**](enumprinters.md) function.

If your application calls the [**PrintDlgEx**](https://msdn.microsoft.com/library/ms646942(v=VS.85).aspx) function and specifies the PD\_RETURNDC value in the **Flags** member of the [**PRINTDLGEX**](https://msdn.microsoft.com/library/ms646844(v=VS.85).aspx) structure, the system returns a handle to a device context for the printer selected by the user. For more information, see [Print Property Sheet](https://msdn.microsoft.com/library/ms646966(v=VS.85).aspx) and "Using the Print Property Sheet" in [Using Common Dialog Boxes](https://msdn.microsoft.com/library/ms646829(v=VS.85).aspx).

 

 



