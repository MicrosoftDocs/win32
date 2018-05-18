---
title: SetByServiceSet method of the MSFT\_DtcClusterTMMappingTask class
description: Updates a cluster DTC mapping for a service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '29fa80dc-d82f-4984-bfa4-c583465054dd'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByServiceSet method", "SetByServiceSet method, MSFT_DtcClusterTMMappingTask class", "MSFT_DtcClusterTMMappingTask class, SetByServiceSet method"]
topic_type:
- apiref
api_name:
- MSFT_DtcClusterTMMappingTask.SetByServiceSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# SetByServiceSet method of the MSFT\_DtcClusterTMMappingTask class

Updates a cluster DTC mapping for a service.

## Syntax


```mof
uint32 SetByServiceSet(
  [in] string  Name,
  [in] string  Service,
  [in] string  ClusterResourceName,
  [in] boolean Local
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the DTC mapping to update.

</dd> <dt>

*Service* \[in\]
</dt> <dd>

The name of the service to assign to the mapping.

</dd> <dt>

*ClusterResourceName* \[in\]
</dt> <dd>

The name of the cluster resource to assign to the mapping.

</dd> <dt>

*Local* \[in\]
</dt> <dd>

**true** if the application type is local. **false** if the application is a clustered resource. If the application type is local, the application maps to the local DTC instance and this method ignores the value of the *ClusterResourceName* parameter.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcClusterTMMappingTask**](msft-dtcclustertmmappingtask.md)
</dt> </dl>

 

 





