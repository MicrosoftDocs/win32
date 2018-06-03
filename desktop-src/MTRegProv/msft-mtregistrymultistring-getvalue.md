---
title: GetValue method of the MSFT\_MTRegistryMultiString class
description: Gets the registry value object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 35B76ADE-D2BF-4E74-8B3A-2DC787935280
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetValue method
- GetValue method, MSFT_MTRegistryMultiString interface
- MSFT_MTRegistryMultiString interface, GetValue method
topic_type:
- apiref
api_name:
- MSFT_MTRegistryMultiString.GetValue
api_location:
- RegProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetValue method of the MSFT\_MTRegistryMultiString class

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

[**MSFT\_MTRegistryMultiString**](msft-mtregistrymultistring.md)
</dt> </dl>

 

 





