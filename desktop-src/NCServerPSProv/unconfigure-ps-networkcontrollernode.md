---
title: Unconfigure method of the PS\_NetworkControllerNode class
description: Unconfigures the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '66679db9-f816-405a-95b9-a9a8e8013df8'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Unconfigure method", "Unconfigure method, PS_NetworkControllerNode class", "PS_NetworkControllerNode class, Unconfigure method"]
topic_type:
- apiref
api_name:
- PS_NetworkControllerNode.Unconfigure
api_location:
- NCServerPSProvider.dll
api_type:
- COM
---

# Unconfigure method of the PS\_NetworkControllerNode class

Unconfigures the node.

## Syntax


```mof
uint32 Unconfigure(
  [in] boolean UnconfigureApplicationOnly,
  [in] boolean ForceCleanup
);
```



## Parameters

<dl> <dt>

*UnconfigureApplicationOnly* \[in\]
</dt> <dd>

Set **true** to unconfigure application settings only; **false** to unconfigure all settings.

</dd> <dt>

*ForceCleanup* \[in\]
</dt> <dd>

Flag to indicate force cleanup even if cluster is not reachable.

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

[**PS\_NetworkControllerNode**](ps-networkcontrollernode.md)
</dt> </dl>

 

 





