---
title: RemoveByMappingNameParameterSet method of the MSFT\_DtcClusterTMMappingTask class
description: Deletes a cluster DTC mapping object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ef032454-24ff-45d8-8e55-97e58fd2b483
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByMappingNameParameterSet method
- RemoveByMappingNameParameterSet method, MSFT_DtcClusterTMMappingTask class
- MSFT_DtcClusterTMMappingTask class, RemoveByMappingNameParameterSet method
topic_type:
- apiref
api_name:
- MSFT_DtcClusterTMMappingTask.RemoveByMappingNameParameterSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveByMappingNameParameterSet method of the MSFT\_DtcClusterTMMappingTask class

Deletes a cluster DTC mapping object.

## Syntax


```mof
uint32 RemoveByMappingNameParameterSet(
  [in] string Name
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the DTC mapping object to delete.

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

 

 





