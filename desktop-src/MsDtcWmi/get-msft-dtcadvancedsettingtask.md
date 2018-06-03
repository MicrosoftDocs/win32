---
title: Get method of the MSFT\_DtcAdvancedSettingTask class
description: Retrieves a DTC instance specific property from the registry.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6f7b29ba-f16e-4a70-bd58-256cf91d322c
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, MSFT_DtcAdvancedSettingTask class
- MSFT_DtcAdvancedSettingTask class, Get method
topic_type:
- apiref
api_name:
- MSFT_DtcAdvancedSettingTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the MSFT\_DtcAdvancedSettingTask class

Retrieves a DTC instance specific property from the registry.

## Syntax


```mof
uint32 Get(
  [in]  string DtcName,
  [in]  string Subkey,
  [in]  string Name,
  [out] string cmdletOutput
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

The name of the DTC instance.

</dd> <dt>

*Subkey* \[in\]
</dt> <dd>

The subkey name of the property to retrieve.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the property to retrieve.

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
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl>    |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcAdvancedSettingTask**](msft-dtcadvancedsettingtask.md)
</dt> </dl>

 

 





