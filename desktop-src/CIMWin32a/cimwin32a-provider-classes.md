---
title: CIMWin32a Provider
description: The CIMWin32a provider extends the classes available in the CIMWin32 provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 72292141-14A1-48D1-9C8C-BEADC627143E
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIMWin32a Provider

The CIMWin32a provider extends the classes available in the [CIMWin32 provider](https://msdn.microsoft.com/library/dn792179). The classes supported by the CIMWin32a provider are declared in Wmipcima.mof and implemented in Wmipcima.dll.

## In this section

<dl> <dt>

[**CIM\_CollectedCollections**](cim-collectedcollections.md)
</dt> <dd>

[**CIM\_CollectedCollections**](cim-collectedcollections.md) is an aggregation association representing that a [**CollectionOfMSEs**](cim-collectionofmses.md) may itself be contained in a collection of SMEs.

</dd> <dt>

[**CIM\_CollectedMSEs**](cim-collectedmses.md)
</dt> <dd>

[**CIM\_CollectedMSEs**](cim-collectedmses.md) is a generic association used to establish the members of the grouping object, [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md).

</dd> <dt>

[**CIM\_CollectionOfMSEs**](cim-collectionofmses.md)
</dt> <dd>

[**CollectionOfMSEs**](cim-collectionofmses.md) allows the grouping of [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) objects for the purposes of associating settings and configurations.

</dd> <dt>

[**CIM\_CollectionSetting**](cim-collectionsetting.md)
</dt> <dd>

[**CollectionSetting**](cim-collectionsetting.md) represents the association between a [**CollectionOfMSEs**](cim-collectionofmses.md) class and the Setting class(es) defined for them.

</dd> <dt>

[**CIM\_LogicalIdentity**](cim-logicalidentity.md)
</dt> <dd>

[**CIM\_LogicalIdentity**](cim-logicalidentity.md) is an abstract and generic association, indicating that two [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892) objects represent different aspects of the same underlying entity.

</dd> <dt>

[**Win32\_CollectionStatistics**](win32-collectionstatistics.md)
</dt> <dd>

The [**Win32\_CollectionStatistics**](win32-collectionstatistics.md) abstract association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a managed system element collection and the class that represents statistical information about the collection.

</dd> <dt>

[**Win32\_ComputerShutdownEvent**](win32-computershutdownevent.md)
</dt> <dd>

The [**Win32\_ComputerShutdownEvent**](win32-computershutdownevent.md) is a Windows Management Instrumentation (WMI) event class that represents events when a computer begins the process of shutting down. It identifies the type of shutdown, which can be a user log off, complete shutdown, or restart.

</dd> <dt>

[**Win32\_ComputerSystemEvent**](win32-computersystemevent.md)
</dt> <dd>

The [**Win32\_ComputerSystemEvent**](win32-computersystemevent.md) [WMI class](https://msdn.microsoft.com/library/aa393244) represents events related to a computer system.

</dd> <dt>

[**Win32\_ControllerHasHub**](win32-controllerhashub.md)
</dt> <dd>

The [**Win32\_ControllerHasHub**](win32-controllerhashub.md) association [WMI class](https://msdn.microsoft.com/library/aa393244) represents the hubs downstream from the universal serial bus (USB) controller.

</dd> <dt>

[**Win32\_DiskDrivePhysicalMedia**](win32-diskdrivephysicalmedia.md)
</dt> <dd>

The [**Win32\_DiskDrivePhysicalMedia**](win32-diskdrivephysicalmedia.md) association [WMI class](https://msdn.microsoft.com/library/aa393244) defines the mapping between a disk drive and the physical components that implement it.

</dd> <dt>

[**Win32\_GroupInDomain**](win32-groupindomain.md)
</dt> <dd>

The [**Win32\_GroupInDomain**](win32-groupindomain.md) association [WMI class](https://msdn.microsoft.com/library/aa393244) identifies the group accounts associated with a Windows domain.

</dd> <dt>

[**Win32\_NTDomain**](win32-ntdomain.md)
</dt> <dd>

The [**Win32\_NTDomain**](win32-ntdomain.md) [WMI class](https://msdn.microsoft.com/library/aa393244) represents a Windows domain.

</dd> <dt>

[**Win32\_PhysicalMedia**](win32-physicalmedia.md)
</dt> <dd>

The [**Win32\_PhysicalMedia**](win32-physicalmedia.md) class represents any type of documentation or storage medium, such as tapes, CD ROMs, and so on. To obtain the characteristics of the media in a CD drive, such as whether it is writeable, use [**Win32\_CDROMDrive**](https://msdn.microsoft.com/library/aa394081) and the **Capabilities** property.

</dd> <dt>

[**Win32\_USBHub**](win32-usbhub.md)
</dt> <dd>

The [**Win32\_USBHub**](win32-usbhub.md) [WMI class](https://msdn.microsoft.com/library/aa393244) represents the management characteristics of a universal serial bus (USB) hub.

</dd> <dt>

[**Win32\_UserInDomain**](win32-userindomain.md)
</dt> <dd>

The [**Win32\_UserInDomain**](win32-userindomain.md) association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a user account and a Windows domain.

</dd> </dl>

 

 




