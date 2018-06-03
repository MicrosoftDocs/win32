---
title: Win32\_DiskDrivePhysicalMedia class
description: The Win32\_DiskDrivePhysicalMedia association WMI class defines the mapping between a disk drive and the physical components that implement it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6191ced1-48bd-4199-b1d0-c50ce19240de
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_DiskDrivePhysicalMedia class
- Win32_DiskDrivePhysicalMedia class, described
topic_type:
- apiref
api_name:
- Win32_DiskDrivePhysicalMedia
- Win32_DiskDrivePhysicalMedia.Antecedent
- Win32_DiskDrivePhysicalMedia.Dependent
api_location:
- Wmipcima.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_DiskDrivePhysicalMedia class

The **Win32\_DiskDrivePhysicalMedia** association [WMI class](https://msdn.microsoft.com/library/aa393244) defines the mapping between a disk drive and the physical components that implement it.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32a"), UUID("{}"), AMENDMENT]
class Win32_DiskDrivePhysicalMedia : CIM_Realizes
{
  Win32_PhysicalMedia REF Antecedent;
  Win32_DiskDrive     REF Dependent;
};
```

## Members

The **Win32\_DiskDrivePhysicalMedia** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DiskDrivePhysicalMedia** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PhysicalMedia**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("")
</dt> </dl>

The Antecedent reference represents the physical component that implements the DiskDrive device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_DiskDrive**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("")
</dt> </dl>

The Dependent reference represents the disk drive.

</dd> </dl>

## Remarks

The **Win32\_DiskDrivePhysicalMedia** class is derived from [**CIM\_Realizes**](https://msdn.microsoft.com/library/aa387991).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipcima.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipcima.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Realizes**](https://msdn.microsoft.com/library/aa387991)
</dt> <dt>

[Computer System Hardware Classes](https://msdn.microsoft.com/library/aa389273)
</dt> </dl>

 

 





