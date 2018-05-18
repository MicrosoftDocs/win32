---
title: IDE Controller Library and Minidriver Routines
description: IDE Controller Library and Minidriver Routines
ms.assetid: 'bc80c124-bc9b-46f6-8ac6-69ef510bdbd6'
keywords: ["IDE controllers WDK storage", "IDE controller minidrivers WDK storage , routines"]
---

# IDE Controller Library and Minidriver Routines

## 

All integrated drive electronics (IDE) controller drivers must implement a series of standard routines that implement hardware-specific functionality. Microsoft supplies the PciIdeX library (*pciidex.lib*) to facilitate the development of these routines in a platform-independent manner. The following two sections describe the PciIdeX library API and list the routines that a controller minidriver requires:

<dl>

[PciIdeX Library Routines](pciidex-library-routines.md)  
[IDE Controller Minidriver Routines](ide-controller-minidriver-routines.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE%20Controller%20Library%20and%20Minidriver%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




