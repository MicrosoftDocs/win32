---
title: RemoveByAllParameterSet method of the MSFT\_DtcClusterTMMappingTask class
description: Deletes all cluster DTC mappings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2c8e565f-0074-4144-9039-0a9de9f9dba5
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByAllParameterSet method
- RemoveByAllParameterSet method, MSFT_DtcClusterTMMappingTask class
- MSFT_DtcClusterTMMappingTask class, RemoveByAllParameterSet method
topic_type:
- apiref
api_name:
- MSFT_DtcClusterTMMappingTask.RemoveByAllParameterSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveByAllParameterSet method of the MSFT\_DtcClusterTMMappingTask class

Deletes all cluster DTC mappings.

## Syntax


```mof
uint32 RemoveByAllParameterSet(
  [in] boolean All
);
```



## Parameters

<dl> <dt>

*All* \[in\]
</dt> <dd>

**true** to remove all mappings; otherwise, **false**.

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

 

 





