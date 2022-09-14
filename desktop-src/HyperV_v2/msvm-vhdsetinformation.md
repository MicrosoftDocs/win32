---
description: Provides information about a VHD Set file.
ms.assetid: a975c131-d3f3-4be3-bc69-e277e3ce4d28
title: Msvm_VHDSetInformation class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VHDSetInformation
- Msvm_VHDSetInformation.Path
- Msvm_VHDSetInformation.SnapshotIdList
- Msvm_VHDSetInformation.AllPaths
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VHDSetInformation class

Provides information about a VHD Set file.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_VHDSetInformation
{
  string Path;
  string SnapshotIdList[];
  string AllPaths[];
};
```

## Members

The **Msvm\_VHDSetInformation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VHDSetInformation** class has these properties.

<dl> <dt>

**AllPaths**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of all files encompassed by the VHD Set file, including any unreferenced files and any parents of the root virtual hard disk. All files listed after the root virtual hard disk are unmanaged by this VHD Set file. This field may be empty if this information was not specifically requested.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of the VHD Set file.

</dd> <dt>

**SnapshotIdList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of GUIDs representing all of the snapshots contained by this VHD Set file.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

 




