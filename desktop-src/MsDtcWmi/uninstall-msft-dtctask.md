---
title: Uninstall method of the MSFT\_DtcTask class
description: Uninstalls the local transactions coordinator.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '27fae008-c81e-44c6-a2b9-54d33307ad8b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Uninstall method", "Uninstall method, MSFT_DtcTask class", "MSFT_DtcTask class, Uninstall method"]
topic_type:
- apiref
api_name:
- MSFT_DtcTask.Uninstall
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Uninstall method of the MSFT\_DtcTask class

Uninstalls the local transactions coordinator.

## Syntax


```mof
uint32 Uninstall();
```



## Parameters

This method has no parameters.

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

[**MSFT\_DtcTask**](msft-dtctask.md)
</dt> </dl>

 

 





