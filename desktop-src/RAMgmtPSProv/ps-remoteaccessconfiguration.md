---
title: PS\_RemoteAccessConfiguration class
description: Represents the remote access configuration.
audience: developer
ms.assetid: 4bca8d34-12af-4f7c-8888-b0466a745704
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RemoteAccessConfiguration class
- PS_RemoteAccessConfiguration class, described
topic_type:
- apiref
api_name:
- PS_RemoteAccessConfiguration
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_RemoteAccessConfiguration class

Represents the remote access configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessConfiguration
{
};
```

## Members

The **PS\_RemoteAccessConfiguration** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessConfiguration** class has these methods.



| Method                                          | Description                                         |
|:------------------------------------------------|:----------------------------------------------------|
| [**Get**](get-ps-remoteaccessconfiguration.md) | Retrieves a remote access configuration.<br/> |
| [**Set**](set-ps-remoteaccessconfiguration.md) | Updates a remote access configuration.<br/>   |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





