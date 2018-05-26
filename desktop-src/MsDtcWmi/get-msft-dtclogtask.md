---
title: Get method of the MSFT\_DtcLogTask class
description: Retrieves DTC log file settings for a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7d774dcb-2c90-4011-a137-6163baea4ace
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, MSFT_DtcLogTask class
- MSFT_DtcLogTask class, Get method
topic_type:
- apiref
api_name:
- MSFT_DtcLogTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the MSFT\_DtcLogTask class

Retrieves DTC log file settings for a DTC instance.

## Syntax


```mof
uint32 Get(
  [in]  string             DtcName,
  [out] DtcLogFileSettings cmdletOutput
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

The name of the DTC instance.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DtcLogFileSettings**](dtclogfilesettings.md) embedded instance containing the settings.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl>    |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcLogTask**](msft-dtclogtask.md)
</dt> </dl>

 

 





