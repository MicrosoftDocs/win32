---
title: SetByExeSet method of the MSFT\_DtcClusterTMMappingTask class
description: Updates a cluster DTC mapping for an application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dfdc244e-d9ac-4fa2-99a4-3a457412efca
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByExeSet method
- SetByExeSet method, MSFT_DtcClusterTMMappingTask class
- MSFT_DtcClusterTMMappingTask class, SetByExeSet method
topic_type:
- apiref
api_name:
- MSFT_DtcClusterTMMappingTask.SetByExeSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByExeSet method of the MSFT\_DtcClusterTMMappingTask class

Updates a cluster DTC mapping for an application.

## Syntax


```mof
uint32 SetByExeSet(
  [in] string  Name,
  [in] string  ExecutablePath,
  [in] string  ClusterResourceName,
  [in] boolean Local
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the DTC mapping to update.

</dd> <dt>

*ExecutablePath* \[in\]
</dt> <dd>

The path of the application to associate with this mapping.

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
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcClusterTMMappingTask**](msft-dtcclustertmmappingtask.md)
</dt> </dl>

 

 





