---
title: MSFT\_SMStorageGroupToStorageVolume class
description: Represents a relationship between a storage group and a storage volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'de004ecb-8aa4-49a2-b7f8-e92b8a5eb6d4'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMStorageGroupToStorageVolume class", "MSFT_SMStorageGroupToStorageVolume class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMStorageGroupToStorageVolume
- MSFT_SMStorageGroupToStorageVolume.Parent
- MSFT_SMStorageGroupToStorageVolume.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMStorageGroupToStorageVolume class

Represents a relationship between a storage group and a storage volume.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMStorageGroupToStorageVolume
{
  MSFT_SMStorageGroup  REF Parent;
  MSFT_SMStorageVolume REF Child;
};
```

## Members

The **MSFT\_SMStorageGroupToStorageVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMStorageGroupToStorageVolume** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageVolume**](msft-smstoragevolume.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The object that represents the storage volume in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageGroup**](msft-smstoragegroup.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The object that represents the storage group in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





