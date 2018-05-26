---
title: GetValues method of the MSFT\_MTRegistryKey class
description: Gets child registry values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 93c5365e-0e72-4df0-8458-5a765470a6a1
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetValues method
- GetValues method, MSFT_MTRegistryKey class
- MSFT_MTRegistryKey class, GetValues method
topic_type:
- apiref
api_name:
- MSFT_MTRegistryKey.GetValues
api_location:
- RegProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetValues method of the MSFT\_MTRegistryKey class

Gets child registry values.

## Syntax


```mof
uint32 GetValues(
  [out] MSFT_MTRegistryValue Results[]
);
```



## Parameters

<dl> <dt>

*Results* \[out\]
</dt> <dd>

On success, returns an array containing embedded instances of the child [**MSFT\_MTRegistryValue**](msft-mtregistryvalue.md) objects.

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

[**MSFT\_MTRegistryKey**](msft-mtregistrykey.md)
</dt> </dl>

 

 





