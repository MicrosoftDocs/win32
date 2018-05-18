---
title: GetValue method of the MSFT\_MTRegistryValue class
description: Gets the registry value object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'DDF40AFF-8DE4-4008-9FBC-F4755F5CDDB2'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetValue method", "GetValue method, MSFT_MTRegistryValue interface", "MSFT_MTRegistryValue interface, GetValue method"]
topic_type:
- apiref
api_name:
- MSFT_MTRegistryValue.GetValue
api_location:
- RegProv.dll
api_type:
- COM
---

# GetValue method of the MSFT\_MTRegistryValue class

Gets the registry value object.

## Syntax


```mof
uint32 GetValue(
  [in]  string               Name,
  [out] MSFT_MTRegistryValue Result
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The unique name of the registry value object.

</dd> <dt>

*Result* \[out\]
</dt> <dd>

On success, returns the requested [**MSFT\_MTRegistryValue**](msft-mtregistryvalue.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                   |
| MOF<br/>                      | <dl> <dt>RegProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RegProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MTRegistryValue**](msft-mtregistryvalue.md)
</dt> </dl>

 

 





