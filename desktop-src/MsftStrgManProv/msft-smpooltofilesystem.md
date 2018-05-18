---
title: MSFT\_SMPoolToFileSystem class
description: Represents a relationship between a storage pool and a file system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8bbf6327-6041-452f-bd92-7b18c562e937'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMPoolToFileSystem class", "MSFT_SMPoolToFileSystem class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMPoolToFileSystem
- MSFT_SMPoolToFileSystem.Parent
- MSFT_SMPoolToFileSystem.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMPoolToFileSystem class

Represents a relationship between a storage pool and a file system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMPoolToFileSystem
{
  MSFT_SMPool       REF Parent;
  MSFT_SMFileSystem REF Child;
};
```

## Members

The **MSFT\_SMPoolToFileSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMPoolToFileSystem** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMFileSystem**](msft-smfilesystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the file system.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMPool**](msft-smpool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the storage pool.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





