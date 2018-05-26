---
Description: User-Mode Rendering DLL Functions
ms.assetid: efda56a0-eaec-4b6f-b55c-14a77e90994f
title: User-Mode Rendering DLL Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# User-Mode Rendering DLL Functions

## 

This section describes the functions defined by user-mode rendering DLLs. The functions are defined in header file Winddiui.h.

These functions are obsolete, and are supported only so that user-mode rendering DLLs, optionally supplied with Windows NT 4.0 drivers, will execute under Windows 2000 and later. To supply user-mode image-rendering code for printers, see [Choosing User Mode or Kernel Mode](print.choosing_user_mode_or_kernel_mode).

<dl>

[**DrvSplAbort**](drvsplabort.md)  
[**DrvSplClose**](drvsplclose.md)  
[**DrvSplEndDoc**](drvsplenddoc.md)  
[**DrvSplEndPage**](drvsplendpage.md)  
[**DrvSplStartDoc**](drvsplstartdoc.md)  
[**DrvSplStartPage**](drvsplstartpage.md)  
[**DrvSplWritePrinter**](drvsplwriteprinter.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20User-Mode%20Rendering%20DLL%20Functions%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



