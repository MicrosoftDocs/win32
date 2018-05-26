---
title: GetFaultDomainXML method of the MSCluster\_FaultDomain class
description: Gets an XML representation of the cluster fault domains.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eab9470b-7429-4e4c-93a4-ab44d3723d59
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetFaultDomainXML method
- GetFaultDomainXML method, MSCluster_FaultDomain class
- MSCluster_FaultDomain class, GetFaultDomainXML method
topic_type:
- apiref
api_name:
- MSCluster_FaultDomain.GetFaultDomainXML
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetFaultDomainXML method of the MSCluster\_FaultDomain class

Gets an XML representation of the cluster fault domains.

## Syntax


```mof
uint32 GetFaultDomainXML(
  [out] string XML,
  [in]  uint32 Flags
);
```



## Parameters

<dl> <dt>

*XML* \[out\]
</dt> <dd>

The XML representation of the fault domain.

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

 

 





