---
title: MSFT\_SMFileServerToFileSystem class
description: Represents a relationship between a file server and a file system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '95504ec1-8274-4d06-acfd-48d56911910e'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMFileServerToFileSystem class", "MSFT_SMFileServerToFileSystem class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMFileServerToFileSystem
- MSFT_SMFileServerToFileSystem.Parent
- MSFT_SMFileServerToFileSystem.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMFileServerToFileSystem class

Represents a relationship between a file server and a file system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[association, dynamic, provider("WMIStorage")]
class MSFT_SMFileServerToFileSystem
{
  MSFT_SMFileServer REF Parent;
  MSFT_SMFileSystem REF Child;
};
```

## Members

The **MSFT\_SMFileServerToFileSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMFileServerToFileSystem** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMFileSystem**](msft-smfilesystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMFileSystem**](msft-smfilesystem.md) object that represents the file system in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMFileServer**](msft-smfileserver.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMFileServer**](msft-smfileserver.md) object that represents the file server in the relationship.

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

 

 





