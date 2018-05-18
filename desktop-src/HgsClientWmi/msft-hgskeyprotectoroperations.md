---
title: MSFT\_HgsKeyProtectorOperations class
description: The principal to whom key rights can be assigned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd2ad77fc-0211-4b2b-a421-5250ba6d19e8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'host-guardian-service'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_HgsKeyProtectorOperations class", "MSFT_HgsKeyProtectorOperations class, described"]
topic_type:
- apiref
api_name:
- MSFT_HgsKeyProtectorOperations
api_location:
- HgsClientWmi.dll
api_type:
- DllExport
---

# MSFT\_HgsKeyProtectorOperations class

The principal to whom key rights can be assigned.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("HgsClientWmi"), ClassVersion("1.0"), AMENDMENT]
class MSFT_HgsKeyProtectorOperations
{
};
```

## Members

The **MSFT\_HgsKeyProtectorOperations** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_HgsKeyProtectorOperations** class has these methods.



| Method                                                                                            | Description                                                                                                                   |
|:--------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**CreateKeyProtector**](createkeyprotector-msft-hgskeyprotectoroperations.md)                   | Creates a new key protector.<br/>                                                                                       |
| [**DecryptDataWithKeyProtector**](msft-hgskeyprotectoroperations-decryptdatawithkeyprotector.md) | Decrypts data by using a supplied key protector.<br/>                                                                   |
| [**EncryptDataWithKeyProtector**](msft-hgskeyprotectoroperations-encryptdatawithkeyprotector.md) | Encrypts data returning the encrypted data along with an egress key protector based on the provided key protector.<br/> |
| [**UnwrapKeyProtector**](unwrapkeyprotector-msft-hgskeyprotectoroperations.md)                   | Unwraps an existing key protector returning the ingress key along with a new egress key and egress key protector.<br/>  |



 

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

[Host Guardian Service WMI Provider](hoster-guardian-service-wmi-provider-portal.md)
</dt> </dl>

 

 





