---
Description: The Win32\_DiskDriveToDiskPartition association WMI class relates a disk drive and a partition existing on it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 82953097-ebfb-42b8-84b4-fb4ed19f3525
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_DiskDriveToDiskPartition class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_DiskDriveToDiskPartition class

The **Win32\_DiskDriveToDiskPartition** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a disk drive and a partition existing on it.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4F9-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_DiskDriveToDiskPartition : CIM_MediaPresent
{
  Win32_DiskDrive     REF Antecedent;
  Win32_DiskPartition REF Dependent;
};
```

## Members

The **Win32\_DiskDriveToDiskPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DiskDriveToDiskPartition** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_DiskDrive**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_DiskDrive")
</dt> </dl>

Reference to the instance representing the properties of the disk drive where the partition exists.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_DiskPartition**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_DiskPartition")
</dt> </dl>

Reference to the instance representing the disk partition residing on the disk drive.

</dd> </dl>

## Remarks

The **Win32\_DiskDriveToDiskPartition** class is derived from [**CIM\_MediaPresent**](cim-mediapresent.md).

For a discussion on how to use this class, see the [Use PowerShell to Map Disk Drives and Partitions](http://blogs.technet.com/b/heyscriptingguy/archive/2012/12/17/use-powershell-to-map-disk-drives-and-partitions.aspx) and the [How Can I Correlate Logical Drives and Physical Disks?](http://blogs.technet.com/b/heyscriptingguy/archive/2005/05/23/how-can-i-correlate-logical-drives-and-physical-disks.aspx) blog articles.

## Examples

The [Use Powershell to Gather Disk/Partition/Mount Point Information](https://Gallery.TechNet.Microsoft.Com/Use-Powershell-to-Gather-b5c746d0) PowerShell sample uses **Win32\_DiskDriveToDiskPartition** to return information about local disks/partitions and mount points.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_MediaPresent**](cim-mediapresent.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[WMI Tasks: Disks and File Systems](https://msdn.microsoft.com/library/aa394592)
</dt> </dl>

 

 




