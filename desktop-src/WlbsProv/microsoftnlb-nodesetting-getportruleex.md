---
title: GetPortRuleEx method of the MicrosoftNLB\_NodeSetting class
description: Provides an optimized means for obtaining the port rule which encapsulates the input virtual IP address and Port number.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a1cbe8c5-d7e5-4bb8-8e39-734bb613c7a0
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetPortRuleEx method
- GetPortRuleEx method, MicrosoftNLB_NodeSetting class
- MicrosoftNLB_NodeSetting class, GetPortRuleEx method
topic_type:
- apiref
api_name:
- MicrosoftNLB_NodeSetting.GetPortRuleEx
api_location:
- WlbsProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetPortRuleEx method of the MicrosoftNLB\_NodeSetting class

Provides an optimized means for obtaining the [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) which encapsulates the input virtual [*IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly) and Port number. The value of virtual IP address to specify 'All Vip'(AKA 'Rest of the VIPs') is 255.255.255.255 : Amended

## Syntax


```mof
void GetPortRuleEx(
  [in]  string                  VirtualIpAddress,
  [in]  UINT32                  Port,
  [out] MicrosoftNLB_PortRuleEx PortRule
);
```



## Parameters

<dl> <dt>

*VirtualIpAddress* \[in\]
</dt> <dd>

One or more virtual IP addresses to be affected by the operation.

</dd> <dt>

*Port* \[in\]
</dt> <dd>

A port number within the [*range of ports*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-6-gly) covered by the port rule.

</dd> <dt>

*PortRule* \[out\]
</dt> <dd>

A [**MicrosoftNLB\_PortRuleEx**](microsoftnlb-portruleex.md) object.

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

[**GetPortRule Method of the MicrosoftNLB\_NodeSetting Class**](microsoftnlb-nodesetting-getportrule.md)
</dt> <dt>

[**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md)
</dt> <dt>

[**MicrosoftNLB\_PortRuleEx**](microsoftnlb-portruleex.md)
</dt> </dl>

 

 





