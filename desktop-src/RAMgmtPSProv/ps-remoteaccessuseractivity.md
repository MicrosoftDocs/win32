---
title: PS\_RemoteAccessUserActivity class
description: Refers to the resources in corpnet accessed by a user over a remote access connection.
audience: developer
ms.assetid: 80711289-4b13-4acd-b2c1-e3de92650c08
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RemoteAccessUserActivity class
- PS_RemoteAccessUserActivity class, described
topic_type:
- apiref
api_name:
- PS_RemoteAccessUserActivity
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_RemoteAccessUserActivity class

Refers to the resources in corpnet accessed by a user over a remote access connection

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessUserActivity
{
};
```

## Members

The **PS\_RemoteAccessUserActivity** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessUserActivity** class has these methods.



| Method                                                               | Description                                                                                                                                                                                   |
|:---------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetByHostIP**](getbyhostip-ps-remoteaccessuseractivity.md)       | This cmdlet displays the following1. Resources accessed over the active DA and VPN connections2. Resources accessed over historical DA and VPN connections<br/>                         |
| [**GetBySessionId**](ps-remoteaccessuseractivity-getbysessionid.md) | This cmdlet displays the following<br/> 1. Resources accessed over the active DA and VPN connections<br/> 2. Resources accessed over historical DA and VPN connections<br/> |
| [**GetByUserName**](getbyusername-ps-remoteaccessuseractivity.md)   | This cmdlet displays the following1. Resources accessed over the active DA and VPN connections2. Resources accessed over historical DA and VPN connections<br/>                         |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





