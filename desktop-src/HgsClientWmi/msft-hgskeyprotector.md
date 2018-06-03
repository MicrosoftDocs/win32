---
title: MSFT\_HgsKeyProtector class
description: A secure wrapping of a key that delegates rights to unwrap and use that key to one or more guardians.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 181d258e-f978-42a7-8d70-5ea566e2d546
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_HgsKeyProtector class
- MSFT_HgsKeyProtector class, described
topic_type:
- apiref
api_name:
- MSFT_HgsKeyProtector
- MSFT_HgsKeyProtector.Owner
- MSFT_HgsKeyProtector.Guardians
- MSFT_HgsKeyProtector.RawData
api_location:
- HgsClientWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_HgsKeyProtector class

A secure wrapping of a key that delegates rights to unwrap and use that key to one or more guardians.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("HgsClientWmi"), ClassVersion("1.0"), AMENDMENT]
class MSFT_HgsKeyProtector
{
  MSFT_HgsGuardian Owner;
  MSFT_HgsGuardian Guardians[];
  uint8            RawData[];
};
```

## Members

The **MSFT\_HgsKeyProtector** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_HgsKeyProtector** class has these methods.



| Method                                                                  | Description                                                                                                                                                              |
|:------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ConvertToByRawBytes**](msft-hgskeyprotector-converttobyrawbytes.md) | Converts a byte array of an existing key protector to a HGS Key Protector object.<br/>                                                                             |
| [**Grant**](grant-msft-hgskeyprotector.md)                             | Grants access to a key protected by a key protector to a given guardian. This operation requires access to the owner signing private key, to prove ownership.<br/> |
| [**NewByGuardians**](msft-hgskeyprotector-newbyguardians.md)           | Creates a new key protector.<br/>                                                                                                                                  |
| [**Revoke**](revoke-msft-hgskeyprotector.md)                           | Revokes key access for a given guardian. This operation requires access to the owner signing private key.<br/>                                                     |



 

### Properties

The **MSFT\_HgsKeyProtector** class has these properties.

<dl> <dt>

**Guardians**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_HgsGuardian** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_HgsGuardian**](msft-hgsguardian.md)")
</dt> </dl>

Gets an array of embedded instances of [**MSFT\_HgsGuardian**](msft-hgsguardian.md) classes that represents the guardians granted access to the key contained in the key protector.

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_HgsGuardian**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_HgsGuardian**](msft-hgsguardian.md)")
</dt> </dl>

Gets an embedded instance of a [**MSFT\_HgsGuardian**](msft-hgsguardian.md) class that represents the owner who created the key protector.

</dd> <dt>

**RawData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Octetstring**
</dt> </dl>

Gets the raw bytes of the Key Protector.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Hgs<br/>                                                    |
| MOF<br/>                      | <dl> <dt>HgsClientWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>HgsClientWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Host Guardian Service WMI Provider](hoster-guardian-service-wmi-provider-portal.md)
</dt> <dt>

[**MSFT\_HgsGuardian**](msft-hgsguardian.md)
</dt> </dl>

 

 





