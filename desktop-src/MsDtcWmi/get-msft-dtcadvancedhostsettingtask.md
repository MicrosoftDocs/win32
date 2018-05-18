---
title: Get method of the MSFT\_DtcAdvancedHostSettingTask class
description: Retrieves a DTC host level property from the registry.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '600449de-6860-49f2-a4e5-e219deed43a6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, MSFT_DtcAdvancedHostSettingTask class", "MSFT_DtcAdvancedHostSettingTask class, Get method"]
topic_type:
- apiref
api_name:
- MSFT_DtcAdvancedHostSettingTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Get method of the MSFT\_DtcAdvancedHostSettingTask class

Retrieves a DTC host level property from the registry.

## Syntax


```mof
uint32 Get(
  [in]  string Name,
  [in]  string Subkey,
  [out] string cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the property to retrieve.

</dd> <dt>

*Subkey* \[in\]
</dt> <dd>

The subkey name of the property to retrieve.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The string representation of the retrieved property.

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

[**MSFT\_DtcAdvancedHostSettingTask**](msft-dtcadvancedhostsettingtask.md)
</dt> </dl>

 

 





