---
title: LogFailureEvent method of the PS\_NetworkControllerNode class
description: This method logs failure event on the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 808c485b-eb36-4f4e-bd79-86007daf8609
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- LogFailureEvent method
- LogFailureEvent method, PS_NetworkControllerNode class
- PS_NetworkControllerNode class, LogFailureEvent method
topic_type:
- apiref
api_name:
- PS_NetworkControllerNode.LogFailureEvent
api_location:
- NCServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LogFailureEvent method of the PS\_NetworkControllerNode class

This method logs failure event on the node

## Syntax


```mof
uint32 LogFailureEvent(
  [in] uint32 EventId,
  [in] string ErrorCode
);
```



## Parameters

<dl> <dt>

*EventId* \[in\]
</dt> <dd>

Event identifier

</dd> <dt>

*ErrorCode* \[in\]
</dt> <dd>

Error code

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

[**PS\_NetworkControllerNode**](ps-networkcontrollernode.md)
</dt> </dl>

 

 





