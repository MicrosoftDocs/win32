---
title: ConvertToByRawBytes method of the MSFT\_HgsKeyProtector class
description: Converts a byte array of an existing key protector to a HGS key protector object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7fdbc891-1c1e-4dde-a452-5ffb11d2bc2f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'host-guardian-service'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ConvertToByRawBytes method", "ConvertToByRawBytes method, MSFT_HgsKeyProtector class", "MSFT_HgsKeyProtector class, ConvertToByRawBytes method"]
topic_type:
- apiref
api_name:
- MSFT_HgsKeyProtector.ConvertToByRawBytes
api_location:
- HgsClientWmi.dll
api_type:
- COM
---

# ConvertToByRawBytes method of the MSFT\_HgsKeyProtector class

Converts a byte array of an existing key protector to a HGS key protector object.

## Syntax


```mof
uint32 ConvertToByRawBytes(
  [in]  uint8                Bytes[],
  [out] MSFT_HgsKeyProtector cmdletOutput
);
```



## Parameters

<dl> <dt>

*Bytes* \[in\]
</dt> <dd>

A byte array of an existing key protector from which to generate a HGS key protector object.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, returns a [**MSFT\_HgsKeyProtector**](msft-hgskeyprotector.md) object containing the new key protector.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Hgs<br/>                                                    |
| MOF<br/>                      | <dl> <dt>HgsClientWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>HgsClientWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_HgsKeyProtector**](msft-hgskeyprotector.md)
</dt> </dl>

 

 





