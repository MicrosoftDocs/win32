---
title: GetValue method of the MSFT\_MTRegistryDword class
description: Gets the registry value object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 991E3193-DCF0-4AF5-B975-7088B5F14683
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetValue method
- GetValue method, MSFT_MTRegistryDword interface
- MSFT_MTRegistryDword interface, GetValue method
topic_type:
- apiref
api_name:
- MSFT_MTRegistryDword.GetValue
api_location:
- RegProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetValue method of the MSFT\_MTRegistryDword class

Gets the registry value object.

## Syntax


```mof
uint32 GetValue(
  [in]  string               Name,
  [out] MSFT_MTRegistryValue Result
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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                   |
| MOF<br/>                      | <dl> <dt>RegProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RegProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MTRegistryDword**](msft-mtregistrydword.md)
</dt> </dl>

 

 





