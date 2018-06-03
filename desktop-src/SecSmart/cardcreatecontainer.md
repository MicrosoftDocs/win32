---
title: CardCreateContainer function
description: Creates a new key container on a smart card.
ms.assetid: e9718b0d-1ee1-4f9f-8ef3-1c1966db6c80
keywords:
- CardCreateContainer function Security
topic_type:
- apiref
api_name:
- CardCreateContainer
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CardCreateContainer function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardCreateContainer** function, defined by a smart card module, creates a new [*key container*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-container-gly) on a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardCreateContainer(
  _In_ PCARD_DATA pCardData,
  _In_ BYTE       bContainerIndex,
  _In_ DWORD      dwFlags,
  _In_ DWORD      dwKeySpec,
  _In_ DWORD      dwKeySize,
  _In_ PBYTE      pbKeyData
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to the [**CARD\_DATA**](card-data.md) structure received from the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*bContainerIndex* \[in\]
</dt> <dd>

The index number for the new key container. The [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) (CSP) and smart card [*key storage provider*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-storage-provider-gly) (KSP) use this index value to identify the key container.

If a key container with the specified index exists on the smart card, it is overwritten by this function.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

A **DWORD** value that specifies the source of the keys in the new container. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                            | Meaning                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <span id="CARD_CREATE_CONTAINER_KEY_GEN"></span><span id="card_create_container_key_gen"></span><dl> <dt>**CARD\_CREATE\_CONTAINER\_KEY\_GEN**</dt> <dt>1</dt> </dl>          | The keys are generated on the smart card.<br/>              |
| <span id="CARD_CREATE_CONTAINER_KEY_IMPORT"></span><span id="card_create_container_key_import"></span><dl> <dt>**CARD\_CREATE\_CONTAINER\_KEY\_IMPORT**</dt> <dt>2</dt> </dl> | The *pbKeyData* parameter points to the imported keys.<br/> |



 

</dd> <dt>

*dwKeySpec* \[in\]
</dt> <dd>

The purpose or type of the keys in the new container. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                   | Meaning                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <span id="AT_KEYEXCHANGE"></span><span id="at_keyexchange"></span><dl> <dt>**AT\_KEYEXCHANGE**</dt> <dt>1</dt> </dl> | The keys are used to encrypt and decrypt session keys.<br/>                                                     |
| <span id="AT_SIGNATURE"></span><span id="at_signature"></span><dl> <dt>**AT\_SIGNATURE**</dt> <dt>2</dt> </dl>       | The keys in the new container are used to create and verify digital signatures.<br/>                            |
| <span id="AT_ECDSA_P256"></span><span id="at_ecdsa_p256"></span><dl> <dt>**AT\_ECDSA\_P256**</dt> <dt>3</dt> </dl>   | The keys in the new container use the 256-bit Elliptic Curve Digital Signature Algorithm (ECDSA) protocol.<br/> |
| <span id="AT_ECDSA_P384"></span><span id="at_ecdsa_p384"></span><dl> <dt>**AT\_ECDSA\_P384**</dt> <dt>4</dt> </dl>   | The keys in the new container use the 384-bit ECDSA protocol.<br/>                                              |
| <span id="AT_ECDSA_P521"></span><span id="at_ecdsa_p521"></span><dl> <dt>**AT\_ECDSA\_P521**</dt> <dt>5</dt> </dl>   | The keys in the new container use the 521-bit ECDSA protocol.<br/>                                              |
| <span id="AT_ECDHE_P256"></span><span id="at_ecdhe_p256"></span><dl> <dt>**AT\_ECDHE\_P256**</dt> <dt>6</dt> </dl>   | The keys in the new container use the 256-bit Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) protocol.<br/>    |
| <span id="AT_ECDHE_P384"></span><span id="at_ecdhe_p384"></span><dl> <dt>**AT\_ECDHE\_P384**</dt> <dt>7</dt> </dl>   | The keys in the new container use the 384-bit ECDHE protocol.<br/>                                              |
| <span id="AT_ECDHE_P521"></span><span id="at_ecdhe_p521"></span><dl> <dt>**AT\_ECDHE\_P521**</dt> <dt>8</dt> </dl>   | The keys in the new container use the 521-bit ECDHE protocol.<br/>                                              |



 

</dd> <dt>

*dwKeySize* \[in\]
</dt> <dd>

The size, in bits, of the key in the *pbKeyData* buffer.

This parameter is used only if the **CARD\_CREATE\_CONTAINER\_KEY\_IMPORT** flag is set in the *dwFlags* parameter. Otherwise, this parameter is ignored.

For Elliptic Curve Cryptography (ECC) keys, the value of this parameter must be zero.

</dd> <dt>

*pbKeyData* \[in\]
</dt> <dd>

A pointer to a buffer that contains the key to import to the new container. The key data is in the form of a [*private key BLOB*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-blob-gly) returned from a call to the [**CryptExportKey**](https://msdn.microsoft.com/library/windows/desktop/aa379931) function.

This parameter is used only if the **CARD\_CREATE\_CONTAINER\_KEY\_IMPORT** flag is set in the *dwFlags* parameter. Otherwise, this parameter is ignored.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                        | Description                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>2148532228 (0x80100004)</dt> </dl> | The smart card does not support importing the key type specified by the *dwKeySpec* parameter.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Base Provider Key BLOBs](https://msdn.microsoft.com/library/windows/desktop/aa375601)
</dt> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[**CryptExportKey**](https://msdn.microsoft.com/library/windows/desktop/aa379931)
</dt> </dl>

 

 





