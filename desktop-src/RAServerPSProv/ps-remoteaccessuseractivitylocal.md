---
title: PS\_RemoteAccessUserActivityLocal class
description: Refers to the resources in corpnet accessed by a user over a remote access connection.
audience: developer
ms.assetid: 5b7a94f3-21df-4df1-b794-902a885bc015
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_RemoteAccessUserActivityLocal class
- PS_RemoteAccessUserActivityLocal class, described
topic_type:
- apiref
api_name:
- PS_RemoteAccessUserActivityLocal
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_RemoteAccessUserActivityLocal class

Refers to the resources in corpnet accessed by a user over a remote access connection.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class PS_RemoteAccessUserActivityLocal
{
};
```

## Members

The **PS\_RemoteAccessUserActivityLocal** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessUserActivityLocal** class has these methods.



| Method                                                                                              | Description                                                                                                                                    |
|:----------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetByAccountingUserActivity**](getbyaccountinguseractivity-ps-remoteaccessuseractivitylocal.md) | This cmdlet displays the following1. Remote user activity over an active connection2. Remote user activity based on accounting data<br/> |
| [**GetByActiveUserActivity**](getbyactiveuseractivity-ps-remoteaccessuseractivitylocal.md)         | This cmdlet displays the following1. Remote user activity over an active connection2. Remote user activity based on accounting data<br/> |
| [**GetBySessionId**](ps-remoteaccessuseractivitylocal-getbysessionid.md)                           | This cmdlet displays the user activity for a particular session as identified by the SessionId parameter.<br/>                           |



 

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





