---
title: Reset method of the MSFT\_DtcLogTask class
description: Resets the log file of a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '36fec13a-31ba-41ee-9b7f-383fa448de5b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Reset method", "Reset method, MSFT_DtcLogTask class", "MSFT_DtcLogTask class, Reset method"]
topic_type:
- apiref
api_name:
- MSFT_DtcLogTask.Reset
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Reset method of the MSFT\_DtcLogTask class

Resets the log file of a DTC instance.

## Syntax


```mof
uint32 Reset(
  [in] string DtcName
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

The name of the DTC instance.

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

[**MSFT\_DtcLogTask**](msft-dtclogtask.md)
</dt> </dl>

 

 





