---
title: Get method of the MSFT\_DtcNetworkSettingTask class
description: Retrieves DTC network and security configuration settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f47403f8-c7e2-45ad-974a-7babbe08cf74'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, MSFT_DtcNetworkSettingTask class", "MSFT_DtcNetworkSettingTask class, Get method"]
topic_type:
- apiref
api_name:
- MSFT_DtcNetworkSettingTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Get method of the MSFT\_DtcNetworkSettingTask class

Retrieves DTC network and security configuration settings.

## Syntax


```mof
uint32 Get(
  [in]  string             DtcName,
  [out] DtcNetworkSettings cmdletOutput
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

The name of the DTC instance that is associated with the settings. If you do not specify this parameter, or if you specify a value of "Local", this method modifies the local DTC instance.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DtcNetworkSettings**](dtcnetworksettings.md) embedded instance containing the retrieved settings.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl>    |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcNetworkSettingTask**](msft-dtcnetworksettingtask.md)
</dt> </dl>

 

 





