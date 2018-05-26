---
title: Start method of the MSFT\_DtcTask class
description: Starts the DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 39dcd0cf-6072-48de-a71f-1fdfa75cdbf4
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Start method
- Start method, MSFT_DtcTask class
- MSFT_DtcTask class, Start method
topic_type:
- apiref
api_name:
- MSFT_DtcTask.Start
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Start method of the MSFT\_DtcTask class

Starts the DTC instance.

## Syntax


```mof
uint32 Start(
  [in] string DtcName
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

Specifies the DTC instance to start. If you do not specify this parameter, or if you specify a value of Local, this method starts the local DTC instance.

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

 

 





