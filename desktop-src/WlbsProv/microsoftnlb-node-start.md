---
title: Start method of the MicrosoftNLB\_Node class
description: Starts cluster operations on the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e9e2d9c8-87a1-44d6-9e3f-205da497bc1a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Start method", "Start method, MicrosoftNLB_Node class", "MicrosoftNLB_Node class, Start method"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_Node.Start
api_location:
- WlbsProv.dll
api_type:
- COM
---

# Start method of the MicrosoftNLB\_Node class

Starts cluster operations on the [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly).

## Syntax


```mof
uint32 Start();
```



## Parameters

This method has no parameters.

## Return value

This method returns a **uint32** set to one of the [standard return values](standard-return-values.md).

<dl> <dt>

**WLBS\_OK** (1000)
</dt> <dt>

**WLBS\_SUSPENDED** (1013)
</dt> <dt>

**WLBS\_ALREADY** (1001)
</dt> <dt>

**WLBS\_DRAIN\_STOP** (1002)
</dt> <dt>

**WLBS\_BAD\_PARAMS** (1003)
</dt> </dl>

## Remarks

This method will fail if called on an instance of a [**MicrosoftNLB\_Node**](https://msdn.microsoft.com/library/aa371151) object that represents a remote node.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftNLB\_Node**](https://msdn.microsoft.com/library/aa371151)
</dt> <dt>

[**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)
</dt> <dt>

[**MicrosoftNLB\_Node**](microsoftnlb-node.md)
</dt> </dl>

 

 





