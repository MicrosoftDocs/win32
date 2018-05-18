---
title: Tape Miniclass Driver Routines
description: Tape Miniclass Driver Routines
ms.assetid: 'f44692dc-010c-430b-a633-c92f143d3a11'
keywords: ["Tape Miniclass Driver Routines", "tape"]
---

# Tape Miniclass Driver Routines

## 

References for the required and optional routines in a tape miniclass driver are listed in alphabetical order.

**DriverEntry** is a required name. A tape miniclass driver's other routines can have any name chosen by the driver writer. In this reference, such routines are prefixed with "*TapeMini*" to identify the routines as belonging to a tape miniclass driver. All tape miniclass routines with the exception of **DriverEntry** are called only by the tape class driver.

The routines, structures, and constants required by a tape miniclass driver are declared in *minitape.h*.

For information about the tape class/miniclass architecture and designing a tape miniclass driver, see [Tape Drivers](https://msdn.microsoft.com/library/windows/hardware/ff567961). For a description of Microsoft Win32 tape functions provided for user-mode applications to control a tape device, see the Microsoft Windows SDK documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Tape%20Miniclass%20Driver%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




