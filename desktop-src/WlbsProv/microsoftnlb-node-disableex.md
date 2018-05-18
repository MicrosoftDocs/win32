---
title: DisableEx method of the MicrosoftNLB\_Node class
description: Disables a range of ports for a virtual IP address.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '13d377a5-8987-4453-b137-433a079c7a8c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DisableEx method", "DisableEx method, MicrosoftNLB_Node class", "MicrosoftNLB_Node class, DisableEx method"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_Node.DisableEx
api_location:
- WlbsProv.dll
api_type:
- COM
---

# DisableEx method of the MicrosoftNLB\_Node class

Disables a range of ports for a virtual [*IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly).

## Syntax


```mof
uint32 DisableEx(
  [in] string VirtualIpAddress,
  [in] uint32 Port
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

The range of ports to be disabled. To affect a range of ports, set *Port* to a port number (0 to 65,535). All ports in the [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) containing the specified port number will be affected. To affect all ports, set *Port* to 0xFFFFFFFF.

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

When enumerating instances of the [**MicrosoftNLB\_Node**](microsoftnlb-node.md) class, you will always receive an instance representing the provider node, regardless of the remote control setting on the provider node. If there are any nodes in the cluster with remote control enabled, you will get instances representing those nodes as well. However, the provider node will always be listed first in an enumeration. For more information, see [enumerating nodes](enumerating-nodes.md).

To block new connections while allowing existing connections to terminate normally, use the [**Drain**](microsoftnlb-node-drain.md) method of the [**MicrosoftNLB\_Node**](microsoftnlb-node.md) class.

To re-enable disabled ports, use the [**Enable**](microsoftnlb-node-enable.md) method of the [**MicrosoftNLB\_Node**](microsoftnlb-node.md) class.

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

[**MicrosoftNLB\_Node**](microsoftnlb-node.md)
</dt> <dt>

[**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)
</dt> <dt>

[**Disable Method of the MicrosoftNLB\_Node Class**](microsoftnlb-node-disable.md)
</dt> <dt>

[**Drain Method of the MicrosoftNLB\_Node Class**](microsoftnlb-node-drain.md)
</dt> <dt>

[**Enable Method of the MicrosoftNLB\_Node Class**](microsoftnlb-node-enable.md)
</dt> </dl>

 

 





