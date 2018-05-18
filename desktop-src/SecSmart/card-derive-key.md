---
title: CARD\_DERIVE\_KEY structure
description: Contains the key derivation function (KDF) that the CardDeriveKey function uses to derive a session key and receives the derived key on output.
ms.assetid: '38311c70-65e6-4e08-9d7b-a378a1b71d1d'
keywords: ["CARD_DERIVE_KEY structure Security", "PCARD_DERIVE_KEY structure pointer Security"]
topic_type:
- apiref
api_name:
- CARD_DERIVE_KEY
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CARD\_DERIVE\_KEY structure

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CARD\_DERIVE\_KEY** structure contains the *key derivation function* (KDF) that the [**CardDeriveKey**](cardderivekey.md) function uses to derive a session key and receives the derived key on output.

## Syntax


```C++
typedef struct _CARD_DERIVE_KEY {
  DWORD   dwVersion;
  DWORD   dwFlags;
  LPCWSTR pwszKDF;
  BYTE    bSecretAgreementIndex;
  PVOID   pParameterList;
  PUCHAR  pbDerivedKey;
  DWORD   cbDerivedKey;
} CARD_DERIVE_KEY, *PCARD_DERIVE_KEY;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version number of this structure, defined in Cardmod.h by the **CARD\_DERIVE\_KEY\_VERSION** constant. The current version number is 1.

</dd> <dt>

**dwFlags**
</dt> <dd>

If **CARD\_BUFFER\_SIZE\_ONLY** is specified, the smart card module returns only the size of the resulting key in the **cbDerivedKey** member and is not required to return the key in the **pbDerivedKey** member.

</dd> <dt>

**pwszKDF**
</dt> <dd>

A pointer to a null-terminated Unicode string that contains an [*object identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721599#-security-object-identifier-gly) (OID). The OID identifies the KDF that derives the key. The **pwszKDF** member can be one of the following strings.



| Value                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BCRYPT_KDF_HASH"></span><span id="bcrypt_kdf_hash"></span><dl> <dt>**BCRYPT\_KDF\_HASH**</dt> <dt>L"HASH"</dt> </dl>               | Use the hash key derivation function. The parameters identified by the **pParameterList** parameter can contain the following parameters.<br/> <dl> <dd>**KDF\_HASH\_ALGORITHM**</dd> <dd>**KDF\_SECRET\_PREPEND**</dd> <dd>**KDF\_SECRET\_APPEND**</dd> </dl>                                                                                                                                                                                                                                                    |
| <span id="BCRYPT_KDF_HMAC"></span><span id="bcrypt_kdf_hmac"></span><dl> <dt>**BCRYPT\_KDF\_HMAC**</dt> <dt>L"HMAC"</dt> </dl>               | Use the [*Hash-Based Message Authentication Code*](https://msdn.microsoft.com/library/windows/desktop/ms721586#-security-hash-based-message-authentication-code-gly) (HMAC) key derivation function. The parameters identified by the *pParameterList* parameter can or must contain the following parameters.<br/> <dl> <dd>**KDF\_HASH\_ALGORITHM**—The default algorithm is SHA1.</dd> <dd>**KDF\_HMAC\_KEY**</dd> <dd>**KDF\_SECRET\_PREPEND**</dd> <dd>**KDF\_SECRET\_APPEND**</dd> </dl> |
| <span id="BCRYPT_KDF_TLS_PRF"></span><span id="bcrypt_kdf_tls_prf"></span><dl> <dt>**BCRYPT\_KDF\_TLS\_PRF**</dt> <dt>L"TLS\_PRF"</dt> </dl> | Use the [*transport layer security*](https://msdn.microsoft.com/library/windows/desktop/ms721627#-security-transport-layer-security-protocol-gly) (TLS) [*pseudo-random function*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-pseudo-random-function-gly) (PRF) key derivation function. The parameters identified by the *pParameterList* parameter can or must contain the following parameters.<br/> <dl> <dd>**KDF\_TLS\_PRF\_LABEL**</dd> <dd>**KDF\_TLS\_PRF\_SEED**</dd> </dl>                  |



 

</dd> <dt>

**bSecretAgreementIndex**
</dt> <dd>

The index of the key container that holds the secret agreement. The [**CardDeriveKey**](cardderivekey.md) function creates the session key from this agreement.

</dd> <dt>

**pParameterList**
</dt> <dd>

A pointer to a [**BCryptBufferDesc**](https://msdn.microsoft.com/library/windows/desktop/aa375370) structure that contains the KDF parameters. This member is optional and can be **NULL** if it is not needed.

</dd> <dt>

**pbDerivedKey**
</dt> <dd>

The address of a buffer that receives the key. The **cbDerivedKey** member contains the size of this buffer. The buffer should be allocated by the [**CardDeriveKey**](cardderivekey.md) function by calling the [**PFN\_CSP\_ALLOC**](pfn-csp-alloc.md) function, and is freed by the smart card key storage provider (KSP).

</dd> <dt>

**cbDerivedKey**
</dt> <dd>

The size, in bytes, of the **pbDerivedKey** buffer.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



 

 





