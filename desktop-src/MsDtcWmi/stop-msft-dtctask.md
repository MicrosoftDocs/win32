---
title: Stop method of the MSFT\_DtcTask class
description: Stops a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0ccf4c4c-0e54-489f-9532-f49ff64eaabe
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Stop method
- Stop method, MSFT_DtcTask class
- MSFT_DtcTask class, Stop method
topic_type:
- apiref
api_name:
- MSFT_DtcTask.Stop
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Stop method of the MSFT\_DtcTask class

Stops a DTC instance.

## Syntax


```mof
uint32 Stop(
  [in] string  DtcName,
  [in] boolean Recursive
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

Specifies the DTC instance to stop. If you do not specify this parameter, or if you specify a value of Local, this method stops the local DTC instance.

</dd> <dt>

*Recursive* \[in\]
</dt> <dd>

**true** to stop any services that rely on the specified DTC instance; otherwise, **false**.

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

[**MSFT\_DtcTask**](msft-dtctask.md)
</dt> </dl>

 

 





