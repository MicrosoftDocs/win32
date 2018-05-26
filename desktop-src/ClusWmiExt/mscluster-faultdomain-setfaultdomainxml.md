---
title: SetFaultDomainXML method of the MSCluster\_FaultDomain class
description: Sets a fault domain using XML.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cba11023-053e-477a-a7d8-368f80c15492
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetFaultDomainXML method
- SetFaultDomainXML method, MSCluster_FaultDomain class
- MSCluster_FaultDomain class, SetFaultDomainXML method
topic_type:
- apiref
api_name:
- MSCluster_FaultDomain.SetFaultDomainXML
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetFaultDomainXML method of the MSCluster\_FaultDomain class

Sets a fault domain using XML.

## Syntax


```mof
uint32 SetFaultDomainXML(
  [in] string XML,
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*XML* \[in\]
</dt> <dd>

The xml representation of the fault domain.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MSCluster\_FaultDomain**](mscluster-faultdomain.md)
</dt> </dl>

 

 





