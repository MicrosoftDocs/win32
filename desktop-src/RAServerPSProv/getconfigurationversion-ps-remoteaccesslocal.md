---
title: GetConfigurationVersion method of the PS\_RemoteAccessLocal class
description: This method gets the server Gpo version information.
audience: developer
ms.assetid: 35877fa6-2e43-4868-88c5-0c69abed7ccf
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetConfigurationVersion method
- GetConfigurationVersion method, PS_RemoteAccessLocal class
- PS_RemoteAccessLocal class, GetConfigurationVersion method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.GetConfigurationVersion
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetConfigurationVersion method of the PS\_RemoteAccessLocal class

This method gets the server Gpo version information.

## Syntax


```mof
uint32 GetConfigurationVersion(
  [out] RemoteAccessConfigurationVersion ConfigVersion
);
```



## Parameters

<dl> <dt>

*ConfigVersion* \[out\]
</dt> <dd>

On success, returns a [**RemoteAccessConfigurationVersion**](remoteaccessconfigurationversion.md) that describes. the Server Gpo version.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





