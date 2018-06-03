---
title: GetPortRule method of the MicrosoftNLB\_NodeSetting class
description: Retrieves the port rule associated with a port number.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dfe74ec3-1e0d-49c9-85df-de70c2477e53
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetPortRule method
- GetPortRule method, MicrosoftNLB_NodeSetting class
- MicrosoftNLB_NodeSetting class, GetPortRule method
topic_type:
- apiref
api_name:
- MicrosoftNLB_NodeSetting.GetPortRule
api_location:
- WlbsProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetPortRule method of the MicrosoftNLB\_NodeSetting class

Retrieves the [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) associated with a port number.

## Syntax


```mof
void GetPortRule(
  [in]  uint32                Port,
  [out] MicrosoftNLB_PortRule PortRule
);
```



## Parameters

<dl> <dt>

*Port* \[in\]
</dt> <dd>

A port number within the [*range of ports*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-6-gly) covered by the port rule.

</dd> <dt>

*PortRule* \[out\]
</dt> <dd>

A [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md) object.

</dd> </dl>

## Return value

This method returns a **uint32** set to one of the [standard return values](standard-return-values.md).

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

[**GetPortRuleEx Method of the MicrosoftNLB\_NodeSetting Class**](microsoftnlb-nodesetting-getportruleex.md)
</dt> <dt>

[**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md)
</dt> <dt>

[**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md)
</dt> </dl>

 

 





