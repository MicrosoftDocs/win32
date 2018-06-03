---
title: UpdateApplicationConfiguration method of the PS\_NetworkController class
description: Updates the Network Controller application configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7d5f9445-c2a1-4230-99c6-4ba5749f7ddc
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- UpdateApplicationConfiguration method
- UpdateApplicationConfiguration method, PS_NetworkController class
- PS_NetworkController class, UpdateApplicationConfiguration method
topic_type:
- apiref
api_name:
- PS_NetworkController.UpdateApplicationConfiguration
api_location:
- NCServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UpdateApplicationConfiguration method of the PS\_NetworkController class

Updates the Network Controller application configuration.

## Syntax


```mof
uint32 UpdateApplicationConfiguration(
  [in] NetworkControllerApplicationConfiguration ApplicationConfiguration
);
```



## Parameters

<dl> <dt>

*ApplicationConfiguration* \[in\]
</dt> <dd>

A [**NetworkControllerApplicationConfiguration**](networkcontrollerapplicationconfiguration.md) embedded instance containing the application configuration.

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

 

 





