---
title: DeployApplication method of the PS\_NetworkController class
description: Deploys the Network Controller application on the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '38a7116f-36d8-4f5f-8bd8-b28c930af98c'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DeployApplication method", "DeployApplication method, PS_NetworkController class", "PS_NetworkController class, DeployApplication method"]
topic_type:
- apiref
api_name:
- PS_NetworkController.DeployApplication
api_location:
- NCServerPSProvider.dll
api_type:
- COM
---

# DeployApplication method of the PS\_NetworkController class

Deploys the Network Controller application on the cluster

## Syntax


```mof
uint32 DeployApplication(
  [in] NetworkControllerApplicationConfiguration ApplicationConfiguration
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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_NetworkController**](ps-networkcontroller.md)
</dt> </dl>

 

 





