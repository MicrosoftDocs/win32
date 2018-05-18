---
title: Changer Miniclass Driver Routines
description: Changer Miniclass Driver Routines
ms.assetid: '28a91bf2-f01a-4fb7-b881-8ae30af4e24d'
keywords: ["changer drivers WDK storage , miniclass drivers"]
---

# Changer Miniclass Driver Routines

## 

This section describes the required and optional routines in a changer miniclass driver. The routines are listed in alphabetical order.

The changer class driver calls changer miniclass driver routines to complete device-specific processing for requests from library-management applications such as the removable storage manager (RSM). For details about RSM, see the Microsoft Windows SDK documentation.

File I/O on a changer's data transfer elements (tape, disk, or CD-ROM drives, for example) is handled by the appropriate mass storage driver for those drives. The mass storage driver is responsible for all transfers of user data to and from media in a changer's drives. The changer driver is responsible only for controlling the movement of media between drives and other elements in the changer.

The routines required for a changer miniclass driver are declared in *mcd.h*. The structures and constants required by a changer miniclass driver are declared in *ntddchgr.h*.

For information about the changer class/miniclass architecture, see [Changer Drivers](https://msdn.microsoft.com/library/windows/hardware/ff551455).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Changer%20Miniclass%20Driver%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




