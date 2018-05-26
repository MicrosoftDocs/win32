---
title: About the BCD WMI Provider
description: The BCD Windows Management Instrumentation (WMI) provider consists of classes exposed as COM objects that support programmatic access to BCD stores. The BcdElement class is the base for all elements. Each BCD element represents a specific boot option.
ms.assetid: f0c9f54b-b178-44cf-aa70-607a167972be
keywords:
- Boot Configuration Data WMI Provider Boot Config , about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About the BCD WMI Provider

When you start your computer, the first code that executes is the BIOS. The BIOS reads the master boot record (MBR) from the boot device and transfers control to the boot code stored in the MBR. (The Windows setup program writes the MBR to the first sector on the hard disk during installation.) The boot manager reads the boot entries from the Boot Configuration Data (BCD) store so they are available to the loader and displays a boot menu to the user. The *boot environment* provides a native application programming interface for primitive graphics and other system support. *Boot applications* are pieces of code that are located on a boot device and run in the boot environment.

The BCD Windows Management Instrumentation (WMI) provider consists of a set of classes exposed as COM objects that support programmatic access to BCD stores. The [**BcdElement**](bcdelement.md) class is the base for all elements. Each *BCD element* represents a specific boot option. All elements share a common header that describes the element type and data format. The remainder of the element is determined by the element's data format. An application can define its own elements or use one of the predefined element types.

The [**BcdObject**](bcdobject.md) class represents a *BCD object*, which is a collection of elements that describes the settings for the object that are used during the boot process. There are three main types of objects: application, device, and inherited.

The following are examples of application objects:

-   The Windows boot manager
-   The Windows operating system loader
-   The Windows memory tester

A device object describes the device-specific properties that are not stored in an application object. Inheritable objects contain elements that contain settings that can apply to more than one object. An object can add the GUID for an inheritable object to its inherited object list.

The [**BcdStore**](bcdstore.md) class represents a *BCD store*. Each object in a BCD store is identified by a GUID. The *system store* is the store that will be read at the next system boot.

The BCDEdit tool can be used to manage BCD stores at the command line. For more information, see [BCDEdit Commands for Boot Environment](http://go.microsoft.com/fwlink/p/?linkid=113151).

## Related topics

<dl> <dt>

[Mapping Boot Options to Elements](mapping-boot-options-to-elements.md)
</dt> <dt>

[Boot Configuration Data in Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=79084)
</dt> <dt>

[BCDEdit Commands for Boot Environment](http://go.microsoft.com/fwlink/p/?linkid=113151)
</dt> <dt>

[BCDEdit on TechNet](http://go.microsoft.com/fwlink/p/?linkid=128459)
</dt> <dt>

[BCD Boot Options Reference in the Windows Driver Kit](http://go.microsoft.com/fwlink/p/?linkid=93291)
</dt> </dl>

 

 




