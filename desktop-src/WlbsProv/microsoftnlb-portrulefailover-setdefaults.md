---
title: SetDefaults method of the MicrosoftNLB\_PortRuleFailover class
description: Resets the nodes port rule configuration to the default.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7b935da6-ae84-40aa-8134-98a9e9a4506a
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetDefaults method
- SetDefaults method, MicrosoftNLB_PortRuleFailover class
- MicrosoftNLB_PortRuleFailover class, SetDefaults method
topic_type:
- apiref
api_name:
- MicrosoftNLB_PortRuleFailover.SetDefaults
api_location:
- WlbsProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetDefaults method of the MicrosoftNLB\_PortRuleFailover class

Resets the [*node's*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) configuration to the default.

## Syntax


```mof
void SetDefaults(
  [in] MicrosoftNLB_Node REF Node
);
```



## Parameters

<dl> <dt>

*Node* \[in\]
</dt> <dd>

A [**MicrosoftNLB\_Node**](microsoftnlb-node.md) object.

</dd> </dl>

## Return value

See [Standard Return Values](standard-return-values.md).

<dl> <dt>

**WLBS\_OK** (1000)
</dt> </dl>

## Remarks

Use the [**LoadAllSettings**](https://msdn.microsoft.com/library/aa371012) method to commit the setting changes to the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md)
</dt> <dt>

[**MicrosoftNLB\_PortRuleFailover**](microsoftnlb-portrulefailover.md)
</dt> </dl>

 

 





