---
title: EnableEx method of the MicrosoftNLB\_Node class
description: Enables all traffic handling for a rule that contains the specified virtual IP address and port.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7987d90b-c430-43e7-9f3f-244494d450d5
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableEx method
- EnableEx method, MicrosoftNLB_Node class
- MicrosoftNLB_Node class, EnableEx method
topic_type:
- apiref
api_name:
- MicrosoftNLB_Node.EnableEx
api_location:
- WlbsProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableEx method of the MicrosoftNLB\_Node class

Enables all traffic handling for a rule that contains the specified virtual [*IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly) and port. The values of virtual IP address to specify 'All Vip' (AKA 'Rest of the VIPs') and 'Every Vip' are '255.255.255.255' and '0.0.0.0' respectively. Port may take any value from 0 to 65,535 or 0xFFFFFFFF to specify all ports. This method fails when called on instances of objects that represent remote nodes.

## Syntax


```mof
uint32 EnableEx(
  [in] string VirtualIpAddress,
  [in] uint32 Port
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

The range of the ports to be enabled. To affect a [*range of ports*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-6-gly), set *Port* to a port number (0 to 65,535). All ports in the [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) that contain the specified port number are affected. To affect all ports, set *Port* to 0xFFFFFFFF.

</dd> </dl>

## Return value

This method returns a **uint32** set to one of the [standard return values](standard-return-values.md).

<dl> <dt>

**WLBS\_OK** (1000)
</dt> <dt>

**WLBS\_NOT\_FOUND** (1004)
</dt> <dt>

**WLBS\_SUSPENDED** (1013)
</dt> <dt>

**WLBS\_ALREADY** (1001)
</dt> <dt>

**WLBS\_STOPPED** (1005)
</dt> <dt>

**WLBS\_DRAINING** (1009)
</dt> </dl>

## Remarks

This method will fail if called on an instance of a [**MicrosoftNLB\_Node**](https://msdn.microsoft.com/library/aa371151) object that represents a remote node.

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

[**MicrosoftNLB\_Node**](microsoftnlb-node.md)
</dt> <dt>

[**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)
</dt> <dt>

[**Enable Method of the MicrosoftNLB\_Node Class**](microsoftnlb-node-enable.md)
</dt> </dl>

 

 





