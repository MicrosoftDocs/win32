---
title: Set method of the MSFT\_DtcAdvancedSettingTask class
description: Updates a DTC instance specific property in the registry.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5e384897-10db-4a00-af61-977184dabeb8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, MSFT_DtcAdvancedSettingTask class", "MSFT_DtcAdvancedSettingTask class, Set method"]
topic_type:
- apiref
api_name:
- MSFT_DtcAdvancedSettingTask.Set
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Set method of the MSFT\_DtcAdvancedSettingTask class

Updates a DTC instance specific property in the registry.

## Syntax


```mof
uint32 Set(
  [in] string DtcName,
  [in] string Subkey,
  [in] string Name,
  [in] string Value,
  [in] string Type
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

The subkey name of the property to update.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the property to update.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

The new property value to use for the update.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of new property value.

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

[**MSFT\_DtcAdvancedSettingTask**](msft-dtcadvancedsettingtask.md)
</dt> </dl>

 

 





