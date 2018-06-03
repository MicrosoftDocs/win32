---
title: MSFT\_SMFileServerToFileShare class
description: Represents a relationship between a file server and a file share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 18deff1f-80d3-460c-8ddd-7a02f93a1ad0
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMFileServerToFileShare class
- MSFT_SMFileServerToFileShare class, described
topic_type:
- apiref
api_name:
- MSFT_SMFileServerToFileShare
- MSFT_SMFileServerToFileShare.Parent
- MSFT_SMFileServerToFileShare.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMFileServerToFileShare class

Represents a relationship between a file server and a file share.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMFileServerToFileShare
{
  MSFT_SMFileServer REF Parent;
  MSFT_SMFileShare  REF Child;
};
```

## Members

The **MSFT\_SMFileServerToFileShare** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMFileServerToFileShare** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMFileShare**](msft-smfileshare.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMFileShare**](msft-smfileshare.md) object that represents the file share in the relationship.

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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





