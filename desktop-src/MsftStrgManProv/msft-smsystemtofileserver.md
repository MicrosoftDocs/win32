---
title: MSFT\_SMSystemToFileServer class
description: Represents a relationship between a system and a file server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a073f854-4f92-45cc-947f-2c718e5944cc
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMSystemToFileServer class
- MSFT_SMSystemToFileServer class, described
topic_type:
- apiref
api_name:
- MSFT_SMSystemToFileServer
- MSFT_SMSystemToFileServer.Parent
- MSFT_SMSystemToFileServer.Child
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMSystemToFileServer class

Represents a relationship between a system and a file server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMSystemToFileServer
{
  MSFT_SMSystem     REF Parent;
  MSFT_SMFileServer REF Child;
};
```

## Members

The **MSFT\_SMSystemToFileServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMSystemToFileServer** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMFileServer**](msft-smfileserver.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the file server in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMSystem**](msft-smsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the system in the relationship.

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

 

 





