---
title: ReleaseAddress method of the MSCluster\_Resource class
description: Releases the IPv4 address DHCP lease.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: afd14889-c532-4285-b59b-3daef5e24724
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ReleaseAddress method
- ReleaseAddress method, MSCluster_Resource class
- MSCluster_Resource class, ReleaseAddress method
topic_type:
- apiref
api_name:
- MSCluster_Resource.ReleaseAddress
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ReleaseAddress method of the MSCluster\_Resource class

Releases the IPv4 address DHCP lease. Valid only for IP address resources.

## Syntax


```mof
void ReleaseAddress();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| Header<br/>                   | <dl> <dt>Mdhcp.h</dt> </dl>     |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





