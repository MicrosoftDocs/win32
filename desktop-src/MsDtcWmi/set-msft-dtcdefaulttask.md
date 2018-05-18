---
title: Set method of the MSFT\_DtcDefaultTask class
description: Sets the default DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b21464d4-b82c-419a-a3c3-322452ad27d7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, MSFT_DtcDefaultTask class", "MSFT_DtcDefaultTask class, Set method"]
topic_type:
- apiref
api_name:
- MSFT_DtcDefaultTask.Set
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Set method of the MSFT\_DtcDefaultTask class

Sets the default DTC instance.

## Syntax


```mof
uint32 Set(
  [in] string ServerName
);
```



## Parameters

<dl> <dt>

*ServerName* \[in\]
</dt> <dd>

The host name or virtual server name of the DTC to set as the default coordinator. If you do not specify this parameter, this method specifies the local DTC as the default coordinator.

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

[**MSFT\_DtcDefaultTask**](msft-dtcdefaulttask.md)
</dt> </dl>

 

 





