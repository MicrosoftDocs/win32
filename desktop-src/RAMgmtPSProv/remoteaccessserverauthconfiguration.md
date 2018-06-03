---
title: RemoteAccessServerAuthConfiguration class
description: The server authentication configuration for the Remote Access service.
audience: developer
ms.assetid: 7a7cc884-cc90-414d-8212-60e9fe849cdf
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessServerAuthConfiguration class
- RemoteAccessServerAuthConfiguration class, described
topic_type:
- apiref
api_name:
- RemoteAccessServerAuthConfiguration
- RemoteAccessServerAuthConfiguration.AuthConfig
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessServerAuthConfiguration class

The server authentication configuration for the Remote Access service

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessServerAuthConfiguration
{
  object AuthConfig;
};
```

## Members

The **RemoteAccessServerAuthConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessServerAuthConfiguration** class has these properties.

<dl> <dt>

**AuthConfig**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **EmbeddedObject**
</dt> </dl>

The authentication configuration of the server as an embedded object

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





