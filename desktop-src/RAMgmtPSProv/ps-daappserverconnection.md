---
title: PS\_DAAppServerConnection class
description: Refers to the properties of the connection made to the application servers and other servers in corpnet.
audience: developer
ms.assetid: 84b07b8a-c3d9-4c53-8b5f-dafb6d99fadb
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DAAppServerConnection class
- PS_DAAppServerConnection class, described
topic_type:
- apiref
api_name:
- PS_DAAppServerConnection
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DAAppServerConnection class

Refers to the properties of the connection made to the application servers and other servers in corpnet.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DAAppServerConnection
{
};
```

## Members

The **PS\_DAAppServerConnection** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DAAppServerConnection** class has these methods.



| Method                                      | Description                                                                                                                                                                                                                                                                                                                 |
|:--------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Set**](set-ps-daappserverconnection.md) | This cmdlet configures the properties of the connection to application servers and the IPsec security traffic protection policies for the connection. This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients and when no application servers have been configured<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





