---
title: MSFT\_SMStorageGroupToStorageHardwareID class
description: Represents a relationship between a storage group and a hardware ID.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7dae35c7-4432-4b93-aeae-0cfaef47ab58
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMStorageGroupToStorageHardwareID class
- MSFT_SMStorageGroupToStorageHardwareID class, described
topic_type:
- apiref
api_name:
- MSFT_SMStorageGroupToStorageHardwareID
- MSFT_SMStorageGroupToStorageHardwareID.Parent
- MSFT_SMStorageGroupToStorageHardwareID.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMStorageGroupToStorageHardwareID class

Represents a relationship between a storage group and a hardware ID.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMStorageGroupToStorageHardwareID
{
  MSFT_SMStorageGroup      REF Parent;
  MSFT_SMStorageHardwareID REF Child;
};
```

## Members

The **MSFT\_SMStorageGroupToStorageHardwareID** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMStorageGroupToStorageHardwareID** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageHardwareID**](msft-smstoragehardwareid.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the hardware ID in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageGroup**](msft-smstoragegroup.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the storage group in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





