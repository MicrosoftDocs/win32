---
title: MSFT\_SMPoolToVolume class
description: Represents a relationsip between a storage pool and a volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d6d8bf10-8052-4cfa-b9b4-3cb1e8f5bb49
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMPoolToVolume class
- MSFT_SMPoolToVolume class, described
topic_type:
- apiref
api_name:
- MSFT_SMPoolToVolume
- MSFT_SMPoolToVolume.Parent
- MSFT_SMPoolToVolume.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMPoolToVolume class

Represents a relationsip between a storage pool and a volume.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMPoolToVolume
{
  MSFT_SMPool          REF Parent;
  MSFT_SMStorageVolume REF Child;
};
```

## Members

The **MSFT\_SMPoolToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMPoolToVolume** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageVolume**](msft-smstoragevolume.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The object that represents the storage volume.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMPool**](msft-smpool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The object that represents the storage pool.

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

 

 





