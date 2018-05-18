---
title: WINBIO\_CREDENTIAL\_TYPE enumeration
description: Defines flags that can be used to filter on the credential type.
ms.assetid: '7ef2d4b3-e1f9-46a0-8fc2-0e8660805ac3'
keywords: ["WINBIO_CREDENTIAL_TYPE enumeration Windows Biometric Framework API"]
topic_type:
- apiref
api_name:
- WINBIO_CREDENTIAL_TYPE
api_location:
- Winbio_types.h
api_type:
- HeaderDef
---

# WINBIO\_CREDENTIAL\_TYPE enumeration

Defines flags that can be used to filter on the credential type. This enumeration is used by the [**WinBioSetCredential**](winbiosetcredential.md), [**WinBioRemoveCredential**](winbioremovecredential.md), and [**WinBioGetCredentialState**](winbiogetcredentialstate.md) functions.

## Syntax


```C++
typedef enum _WINBIO_CREDENTIAL_TYPE { 
  WINBIO_CREDENTIAL_PASSWORD  = 0x00000001,
  WINBIO_CREDENTIAL_ALL       = 0xffffffff
} WINBIO_CREDENTIAL_TYPE;
```



## Constants

<dl> <dt>

<span id="WINBIO_CREDENTIAL_PASSWORD"></span><span id="winbio_credential_password"></span>**WINBIO\_CREDENTIAL\_PASSWORD**
</dt> <dd>

Filters password credentials.

</dd> <dt>

<span id="WINBIO_CREDENTIAL_ALL"></span><span id="winbio_credential_all"></span>**WINBIO\_CREDENTIAL\_ALL**
</dt> <dd>

Filters all credentials.

</dd> </dl>

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winbio\_types.h (include Winbio.h)</dt> </dl> |



## See also

<dl> <dt>

[Client Application Enumerations](client-application-enumerations.md)
</dt> <dt>

[**WinBioGetCredentialState**](winbiogetcredentialstate.md)
</dt> <dt>

[**WinBioRemoveCredential**](winbioremovecredential.md)
</dt> <dt>

[**WinBioSetCredential**](winbiosetcredential.md)
</dt> </dl>

 

 





