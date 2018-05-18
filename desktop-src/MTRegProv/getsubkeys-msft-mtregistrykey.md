---
title: GetSubKeys method of the MSFT\_MTRegistryKey class
description: Get child registry keys.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '738bb719-99a5-4855-a1c2-fe7f2f3eb904'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSubKeys method", "GetSubKeys method, MSFT_MTRegistryKey class", "MSFT_MTRegistryKey class, GetSubKeys method"]
topic_type:
- apiref
api_name:
- MSFT_MTRegistryKey.GetSubKeys
api_location:
- RegProv.dll
api_type:
- COM
---

# GetSubKeys method of the MSFT\_MTRegistryKey class

Get child registry keys.

## Syntax


```mof
uint32 GetSubKeys(
  [out] MSFT_MTRegistryKey Results[]
);
```



## Parameters

<dl> <dt>

*Results* \[out\]
</dt> <dd>

On success, returns an array containing embedded instances of the child [**MSFT\_MTRegistryKey**](msft-mtregistrykey.md) objects.

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

 

 





