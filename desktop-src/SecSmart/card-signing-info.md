---
title: CARD\_SIGNING\_INFO structure
description: Specifies data to be signed by the CardSignData function.
ms.assetid: 120e7980-63ea-40cb-9e66-622e9ff7e194
keywords:
- CARD_SIGNING_INFO structure Security
- PCARD_SIGNING_INFO structure pointer Security
topic_type:
- apiref
api_name:
- CARD_SIGNING_INFO
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# CARD\_SIGNING\_INFO structure

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CARD\_SIGNING\_INFO** structure specifies data to be signed by the [**CardSignData**](cardsigndata.md) function.

## Syntax


```C++
typedef struct _CARD_SIGNING_INFO {
  DWORD  dwVersion;
  BYTE   bContainerIndex;
  DWORD  dwKeySpec;
  DWORD  dwSigningFlags;
  ALG_ID aiHashAlg;
  PBYTE  pbData;
  DWORD  cbData;
  PBYTE  pbSignedData;
  DWORD  cbSignedData;
  LPVOID pPaddingInfo;
  DWORD  dwPaddingType;
} CARD_SIGNING_INFO, *PCARD_SIGNING_INFO;
```



## Members

<dl> <dt>

**dwVersion**
</dt> <dd>

The version number of the structure. You must set this member to 1.

</dd> <dt>

**bContainerIndex**
</dt> <dd>

The key container index number. The container holds the keys used to sign the data.

</dd> <dt>

**dwKeySpec**
</dt> <dd>

The purpose of the keys in the key container. This member can be one of the following values.



| Value                                                                                                                                                                                                                   | Meaning                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="AT_KEYEXCHANGE"></span><span id="at_keyexchange"></span><dl> <dt>**AT\_KEYEXCHANGE**</dt> <dt>1</dt> </dl> | The keys in the container are used to encrypt and decrypt session keys.<br/>     |
| <span id="AT_SIGNATURE"></span><span id="at_signature"></span><dl> <dt>**AT\_SIGNATURE**</dt> <dt>2</dt> </dl>       | The keys in the container are used to create and verify digital signatures.<br/> |



 

</dd> <dt>

**dwSigningFlags**
</dt> <dd>

Specifies certain behavior of this structure. The following flags are defined.



| Value                                                                                                                                                                                                                                                                            | Meaning                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CARD_BUFFER_SIZE_ONLY"></span><span id="card_buffer_size_only"></span><dl> <dt>**CARD\_BUFFER\_SIZE\_ONLY**</dt> <dt>0x20000000</dt> </dl>                          | The card module returns only the size of the signed data in the **cbSignedData** member, and is not required to return the signed data in the **pbSignedData** member.<br/> |
| <span id="CARD_PADDING_INFO_PRESENT"></span><span id="card_padding_info_present"></span><dl> <dt>**CARD\_PADDING\_INFO\_PRESENT**</dt> <dt>0x40000000 (0x40000000)</dt> </dl> | The **pPaddingInfo** member points to a structure specified by the **dwPaddingType** member. Otherwise, the **pPaddingInfo** member is ignored.<br/>                        |



 

</dd> <dt>

**aiHashAlg**
</dt> <dd>

A value of the [**ALG\_ID**](https://msdn.microsoft.com/library/windows/desktop/aa375549) enumeration that specifies the algorithm used to sign the data.

</dd> <dt>

**pbData**
</dt> <dd>

A pointer to an array that contains the data to be signed.

</dd> <dt>

**cbData**
</dt> <dd>

The size, in bytes, of the **pbData** array.

</dd> <dt>

**pbSignedData**
</dt> <dd>

A pointer to an array that, on output, contains the signed data.

</dd> <dt>

**cbSignedData**
</dt> <dd>

The size, in bytes, of the **pbSignedData** buffer.

</dd> <dt>

**pPaddingInfo**
</dt> <dd>

A pointer to a structure that specifies padding scheme options. The value of the **dwPaddingType** member determines which padding structure is used.

**Windows Server 2003, Windows 2000 Server with SP4 and later, Windows XP and Windows 2000 Professional with SP4 and later:** This member is not supported.

</dd> <dt>

**dwPaddingType**
</dt> <dd>

The type of padding structure that the **pPaddingInfo** member points to. The following values are defined.

**Windows Server 2003, Windows 2000 Server with SP4 and later, Windows XP and Windows 2000 Professional with SP4 and later:** This member is not supported.



| Value                                                                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CARD_PADDING_NONE"></span><span id="card_padding_none"></span><dl> <dt>**CARD\_PADDING\_NONE**</dt> <dt>1 (0x1)</dt> </dl>    | No card padding structure is used.<br/>                                                                                                                                                                                                                                                                                                                       |
| <span id="CARD_PADDING_PKCS1"></span><span id="card_padding_pkcs1"></span><dl> <dt>**CARD\_PADDING\_PKCS1**</dt> <dt>2 (0x2)</dt> </dl> | The **pPaddingInfo** member points to a [**BCRYPT\_PKCS1\_PADDING\_INFO**](https://msdn.microsoft.com/library/windows/desktop/aa375527) structure. PKCS1 version 1.5 padding is used, and the [*object identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721599#-security-object-identifier-gly) (OID) of the hash algorithm is embedded in the signature.<br/>                     |
| <span id="CARD_PADDING_PSS"></span><span id="card_padding_pss"></span><dl> <dt>**CARD\_PADDING\_PSS**</dt> <dt>4 (0x4)</dt> </dl>       | The **pPaddingInfo** member points to a [**BCRYPT\_PSS\_PADDING\_INFO**](https://msdn.microsoft.com/library/windows/desktop/aa375529) structure. PKCS1 version 2.0 PSS padding is used. This value is supported only by card modules called by the smart card [*key storage provider*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-storage-provider-gly) (KSP).<br/> |



 

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> <dt>

[**CardSignData**](cardsigndata.md)
</dt> </dl>

 

 





