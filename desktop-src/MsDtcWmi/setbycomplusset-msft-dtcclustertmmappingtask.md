---
title: SetByComPlusSet method of the MSFT\_DtcClusterTMMappingTask class
description: Updates a DTC mapping for a COM+ application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f33ff0b5-3014-41b3-b02d-9b3c8a520c78'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByComPlusSet method", "SetByComPlusSet method, MSFT_DtcClusterTMMappingTask class", "MSFT_DtcClusterTMMappingTask class, SetByComPlusSet method"]
topic_type:
- apiref
api_name:
- MSFT_DtcClusterTMMappingTask.SetByComPlusSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# SetByComPlusSet method of the MSFT\_DtcClusterTMMappingTask class

Updates a DTC mapping for a COM+ application.

## Syntax


```mof
uint32 SetByComPlusSet(
  [in] string  Name,
  [in] string  ComPlusAppId,
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

*ComPlusAppId* \[in\]
</dt> <dd>

The COM+ application identifier to associate with the mapping.

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

 

 





