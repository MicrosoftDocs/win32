---
title: Set method of the MSFT\_DtcAdvancedHostSettingTask class
description: Updates a DTC host level property in the registry.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6087a38f-ceca-4f5e-a3c6-f15388e11640
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, MSFT_DtcAdvancedHostSettingTask class
- MSFT_DtcAdvancedHostSettingTask class, Set method
topic_type:
- apiref
api_name:
- MSFT_DtcAdvancedHostSettingTask.Set
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the MSFT\_DtcAdvancedHostSettingTask class

Updates a DTC host level property in the registry.

## Syntax


```mof
uint32 Set(
  [in] string Name,
  [in] string Subkey,
  [in] string Value,
  [in] string Type
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the property to update.

</dd> <dt>

*Subkey* \[in\]
</dt> <dd>

The subkey name of the property to update.

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
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcAdvancedHostSettingTask**](msft-dtcadvancedhostsettingtask.md)
</dt> </dl>

 

 





