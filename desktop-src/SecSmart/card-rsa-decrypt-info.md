---
title: CARD\_RSA\_DECRYPT\_INFO structure
description: Specifies the data to be decrypted by the CardRSADecrypt function as well as the private key used to perform the decryption.
ms.assetid: '728d7ba7-149c-43dd-9e62-7671ddffbb98'
keywords: ["CARD_RSA_DECRYPT_INFO structure Security", "PCARD_RSA_DECRYPT_INFO structure pointer Security"]
topic_type:
- apiref
api_name:
- CARD_RSA_DECRYPT_INFO
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CARD\_RSA\_DECRYPT\_INFO structure

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CARD\_RSA\_DECRYPT\_INFO** structure specifies the data to be decrypted by the [**CardRSADecrypt**](cardrsadecrypt.md) function as well as the private key used to perform the decryption.

## Syntax


```C++
typedef struct _CARD_RSA_DECRYPT_INFO {
  DWORD dwVersion;
  BYTE  bContainerIndex;
  DWORD dwKeySpec;
  PBYTE pbData;
  DWORD cbData;
} CARD_RSA_DECRYPT_INFO, *PCARD_RSA_DECRYPT_INFO;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version number of the structure.

</dd> <dt>

**bContainerIndex**
</dt> <dd>

The key container index number. The container holds the keys that perform the decryption.

</dd> <dt>

**dwKeySpec**
</dt> <dd>

The purpose of the keys in the new container. This member can be one of the following values.



| Value                                                                                                                                                                                                                   | Meaning                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <span id="AT_KEYEXCHANGE"></span><span id="at_keyexchange"></span><dl> <dt>**AT\_KEYEXCHANGE**</dt> <dt>1</dt> </dl> | The keys are used to encrypt and decrypt session keys.<br/>     |
| <span id="AT_SIGNATURE"></span><span id="at_signature"></span><dl> <dt>**AT\_SIGNATURE**</dt> <dt>2</dt> </dl>       | The keys are used to create and verify digital signatures.<br/> |



 

</dd> <dt>

**pbData**
</dt> <dd>

A pointer to an array of decrypted data values. On input, the array specifies the data to be decrypted. On output, the array specifies the decrypted data.

</dd> <dt>

**cbData**
</dt> <dd>

The length, in bytes, of the decrypted data pointed to by the **pbData** member. This value must always be the same as the key modulus.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> </dl>

 

 





