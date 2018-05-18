---
title: GetApplicationConfiguration method of the PS\_NetworkController class
description: Retrieves the Network Controller application configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6e7e4b5f-78b2-43fb-a2c8-1737b3c876fd'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetApplicationConfiguration method", "GetApplicationConfiguration method, PS_NetworkController class", "PS_NetworkController class, GetApplicationConfiguration method"]
topic_type:
- apiref
api_name:
- PS_NetworkController.GetApplicationConfiguration
api_location:
- NCServerPSProvider.dll
api_type:
- COM
---

# GetApplicationConfiguration method of the PS\_NetworkController class

Retrieves the Network Controller application configuration.

## Syntax


```mof
uint32 GetApplicationConfiguration(
  [out] NetworkControllerApplicationConfiguration ApplicationConfiguration
);
```



## Parameters

<dl> <dt>

*ApplicationConfiguration* \[out\]
</dt> <dd>

On success, returns a [**NetworkControllerApplicationConfiguration**](networkcontrollerapplicationconfiguration.md) containing the application configuration.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_NetworkController**](ps-networkcontroller.md)
</dt> </dl>

 

 





