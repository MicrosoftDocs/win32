---
title: AddByComPlusSet method of the MSFT\_DtcClusterTMMappingTask class
description: Creates a DTC mapping for a COM+ application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dfedf63f-5a9b-4a9a-bf54-fd829ce9ba2d
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByComPlusSet method
- AddByComPlusSet method, MSFT_DtcClusterTMMappingTask class
- MSFT_DtcClusterTMMappingTask class, AddByComPlusSet method
topic_type:
- apiref
api_name:
- MSFT_DtcClusterTMMappingTask.AddByComPlusSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByComPlusSet method of the MSFT\_DtcClusterTMMappingTask class

Creates a DTC mapping for a COM+ application.

## Syntax


```mof
uint32 AddByComPlusSet(
  [in] string  Name,
  [in] string  ClusterResourceName,
  [in] boolean Local,
  [in] string  ComPlusAppId
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the DTC mapping to add.

</dd> <dt>

*ClusterResourceName* \[in\]
</dt> <dd>

The name of the cluster resource to assign to the mapping.

</dd> <dt>

*Local* \[in\]
</dt> <dd>

**true** if the application type is local. **false** if the application is a clustered resource. If the application type is local, the application maps to the local DTC instance and this method ignores the value of the *ClusterResourceName* parameter.

</dd> <dt>

*ComPlusAppId* \[in\]
</dt> <dd>

The COM+ application identifier to associate with the mapping.

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

 

 





