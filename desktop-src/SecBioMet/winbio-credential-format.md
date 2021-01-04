---
title: WINBIO_CREDENTIAL_FORMAT enumeration (Winbio\_types.h)
description: Defines flags that can be used to specify the end-user credential format.
ms.assetid: f107e000-98a2-44f0-aa5e-d13b5d9c8d43
keywords:
- WINBIO_CREDENTIAL_FORMAT enumeration Windows Biometric Framework API
topic_type:
- apiref
api_name:
- WINBIO_CREDENTIAL_FORMAT
api_location:
- Winbio_types.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WINBIO\_CREDENTIAL\_FORMAT enumeration

Defines flags that can be used to specify the end-user credential format. This enumeration is used by the [**WinBioSetCredential**](/windows/desktop/api/Winbio/nf-winbio-winbiosetcredential) function.

## Syntax


```C++
typedef enum _WINBIO_CREDENTIAL_FORMAT { 
  WINBIO_PASSWORD_GENERIC    = 0x00000001,
  WINBIO_PASSWORD_PACKED     = 0x00000002,
  WINBIO_PASSWORD_PROTECTED  = 0x00000003
} WINBIO_CREDENTIAL_FORMAT;
```



## Constants

<dl> <dt>

<span id="WINBIO_PASSWORD_GENERIC"></span><span id="winbio_password_generic"></span>**WINBIO\_PASSWORD\_GENERIC**
</dt> <dd>

The password is in a generic format.

</dd> <dt>

<span id="WINBIO_PASSWORD_PACKED"></span><span id="winbio_password_packed"></span>**WINBIO\_PASSWORD\_PACKED**
</dt> <dd>

The password is in a compressed format.

</dd> <dt>

<span id="WINBIO_PASSWORD_PROTECTED"></span><span id="winbio_password_protected"></span>**WINBIO\_PASSWORD\_PROTECTED**
</dt> <dd>

The password credential was wrapped with [**CredProtect**](/windows/desktop/api/wincred/nf-wincred-credprotecta).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Enumerations](client-application-enumerations.md)
</dt> <dt>

[**WinBioSetCredential**](/windows/desktop/api/Winbio/nf-winbio-winbiosetcredential)
</dt> </dl>

 

