---
title: GetKey method of the MSFT\_MTRegistryKey class
description: Gets the registry key object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '985AEE76-0D2C-420A-A402-3A75DF89BEDF'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetKey method", "GetKey method, MSFT_MTRegistryKey interface", "MSFT_MTRegistryKey interface, GetKey method"]
topic_type:
- apiref
api_name:
- MSFT_MTRegistryKey.GetKey
api_location:
- RegProv.dll
api_type:
- COM
---

# GetKey method of the MSFT\_MTRegistryKey class

Gets the registry key object.

## Syntax


```mof
uint32 GetKey(
  [in]  string             Name,
  [out] MSFT_MTRegistryKey Result
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The unique name of the registry key object.

</dd> <dt>

*Result* \[out\]
</dt> <dd>

On success, returns the [**MSFT\_MTRegistryKey**](msft-mtregistrykey.md) as an embedded instance.

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

[**MSFT\_MTRegistryKey**](msft-mtregistrykey.md)
</dt> </dl>

 

 





