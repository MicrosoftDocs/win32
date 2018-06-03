---
title: Enable method of the MicrosoftNLB\_Node class
description: Enables ports that have been disabled on the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dc01e2fa-ad68-46be-bc1f-e52552c5d45e
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Enable method
- Enable method, MicrosoftNLB_Node class
- MicrosoftNLB_Node class, Enable method
topic_type:
- apiref
api_name:
- MicrosoftNLB_Node.Enable
api_location:
- WlbsProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enable method of the MicrosoftNLB\_Node class

Enables ports that have been disabled on the [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly).

## Syntax


```mof
uint32 Enable(
  [in] uint32 Port
);
```



## Parameters

<dl> <dt>

*Port* \[in\]
</dt> <dd>

The range of the ports to be enabled. To affect a [*range of ports*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-6-gly), set *Port* to a port number (0 to 65,535). All ports in the [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) containing the specified port number will be affected. To affect all ports, set *Port* to 0xFFFFFFFF.

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

[**EnableEx Method of the MicrosoftNLB\_Node Class**](microsoftnlb-node-enableex.md)
</dt> </dl>

 

 





