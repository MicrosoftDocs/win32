---
title: Storport Driver Virtual Miniport Routines
description: Storport Driver Virtual Miniport Routines
ms.assetid: 6df07d9d-a5c2-4dc4-a219-38400fb200a7
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Storport Driver Virtual Miniport Routines

Storport virtual miniport (VMiniport) drivers and Storport physical miniport drivers (that is, one that uses a physical host bus adapter) are equivalent in many respects. The main difference between the two is that the VMiniport driver controls no hardware. Consequently, the Storport miniport driver does not obtain a DMA object (therefore no interrupt object, no interrupt lock, and no non-cached storage). Additionally, a virtual miniport driver can employ all APIs that are documented in the WDK to complete its work. Conversely, a physical miniport driver uses only Storport APIs. A virtual miniport driver can use other APIs such as those that the kernel provides, as long as the virtual miniport driver observes restrictions applying to WDM drivers.

For more information about Storport support routines, see [Storport Driver Support Routines](storport-driver-support-routines.md). For more information about the Storport driver itself, see [Storage Port Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566994).

A Storport virtual miniport driver must implement most if not all of the routines described in this section:

<dl>

[**HwStorCleanupTracing**](hwstorcleanuptracing.md)  
[**HwStorCompleteServiceIrp**](hwstorcompleteserviceirp.md)  
[**HwStorFreeAdapterResources**](hwstorfreeadapterresources.md)  
[**HwStorInitializeTracing**](hwstorinitializetracing.md)  
[**HwStorProcessServiceRequest**](hwstorprocessservicerequest.md)  
[**VirtualHwStorFindAdapter**](virtualhwstorfindadapter.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Storport%20Driver%20Virtual%20Miniport%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




