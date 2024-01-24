---
title: Win32_TSVmMetadataAssociation class
description: Represents an association between a Remote Desktop virtual machine and its metadata properties.
ms.assetid: 374b1a29-78de-45fd-97b3-c5a5b724e66b
ms.tgt_platform: multiple
keywords:
- Win32_TSVmMetadataAssociation class Remote Desktop Services
- Win32_TSVmMetadataAssociation class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSVmMetadataAssociation
- Win32_TSVmMetadataAssociation.TSVm
- Win32_TSVmMetadataAssociation.MetadataItem
api_location:
- TSVmHostWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSVmMetadataAssociation class

Represents an association between a Remote Desktop virtual machine and its metadata properties.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, Association, provider("Win32_TSVmHost_Prov"), AMENDMENT]
class Win32_TSVmMetadataAssociation
{
  Win32_TSVm             REF TSVm;
  Win32_TSVmMetadataItem REF MetadataItem;
};
```

## Members

The **Win32\_TSVmMetadataAssociation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_TSVmMetadataAssociation** class has these properties.

<dl> <dt>

**MetadataItem**
</dt> <dd> <dl> <dt>

Data type: **[**Win32\_TSVmMetadataItem**](win32-tsvmmetadataitem.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An instance of the [**Win32\_TSVmMetadataItem**](win32-tsvmmetadataitem.md) class that represents the metadata for the virtual machine.

</dd> <dt>

**TSVm**
</dt> <dd> <dl> <dt>

Data type: **[**Win32\_TSVm**](win32-tsvm.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

An instance of the [**Win32\_TSVm**](win32-tsvm.md) class that represents the virtual machine.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\CIMV2\\TerminalServices<br/>                                                   |
| MOF<br/>                      | <dl> <dt>TSVmHost.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>TSVmHostWmi.dll</dt> </dl> |



 

