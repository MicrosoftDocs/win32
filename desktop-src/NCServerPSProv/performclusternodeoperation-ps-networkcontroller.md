---
title: PerformClusterNodeOperation method of the PS\_NetworkController class
description: Performs cluster node-specific operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1c2b3563-e024-40d5-99a6-9e295e294baa
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PerformClusterNodeOperation method
- PerformClusterNodeOperation method, PS_NetworkController class
- PS_NetworkController class, PerformClusterNodeOperation method
topic_type:
- apiref
api_name:
- PS_NetworkController.PerformClusterNodeOperation
api_location:
- NCServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PerformClusterNodeOperation method of the PS\_NetworkController class

Performs cluster node-specific operations.

## Syntax


```mof
uint32 PerformClusterNodeOperation(
  [in] sint8  Operation,
  [in] string NodeName
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

The operation ID.

<dt>

<span id="EnableNode"></span><span id="enablenode"></span><span id="ENABLENODE"></span>

**EnableNode** (0)


</dt> <dd></dd> <dt>

<span id="DisableNode"></span><span id="disablenode"></span><span id="DISABLENODE"></span>

**DisableNode** (1)


</dt> <dd></dd> <dt>

<span id="DisableNodeWithRemoveData"></span><span id="disablenodewithremovedata"></span><span id="DISABLENODEWITHREMOVEDATA"></span>

**DisableNodeWithRemoveData** (2)


</dt> <dd></dd> <dt>

<span id="RemoveNodeState"></span><span id="removenodestate"></span><span id="REMOVENODESTATE"></span>

**RemoveNodeState** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*NodeName* \[in\]
</dt> <dd>

The name of the node.

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

 

 





