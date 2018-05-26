---
title: GetClusterConfiguration method of the PS\_NetworkController class
description: Retrieves the Network Controller cluster configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6f860eb3-c107-43a1-a225-ae88d7f9f71e
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetClusterConfiguration method
- GetClusterConfiguration method, PS_NetworkController class
- PS_NetworkController class, GetClusterConfiguration method
topic_type:
- apiref
api_name:
- PS_NetworkController.GetClusterConfiguration
api_location:
- NCServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetClusterConfiguration method of the PS\_NetworkController class

Retrieves the Network Controller cluster configuration.

## Syntax


```mof
uint32 GetClusterConfiguration(
  [out] NetworkControllerClusterConfiguration ClusterConfiguration
);
```



## Parameters

<dl> <dt>

*ClusterConfiguration* \[out\]
</dt> <dd>

On success, returns a [**NetworkControllerClusterConfiguration**](networkcontrollerclusterconfiguration.md) object containing the cluster configuration.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_NetworkController**](ps-networkcontroller.md)
</dt> </dl>

 

 





