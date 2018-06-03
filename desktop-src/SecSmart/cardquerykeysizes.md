---
title: CardQueryKeySizes function
description: Retrieves the public key lengths supported by a smart card.
ms.assetid: 912fdd13-2503-473d-88a9-9846ceca8863
keywords:
- CardQueryKeySizes function Security
topic_type:
- apiref
api_name:
- CardQueryKeySizes
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

# CardQueryKeySizes function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardQueryKeySizes** function, defined by a smart card module, retrieves the public [*key lengths*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-length-gly) supported by a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardQueryKeySizes(
  _In_  PCARD_DATA      pCardData,
  _In_  DWORD           dwKeySpec,
  _In_  DWORD           dwFlags,
  _Out_ PCARD_KEY_SIZES pKeySizes
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*dwKeySpec* \[in\]
</dt> <dd>

A **DWORD** value that specifies the type of the [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly) for which to find the length.

This parameter can be one of the following values.



| Value                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="AT_KEYEXCHANGE"></span><span id="at_keyexchange"></span><dl> <dt>**AT\_KEYEXCHANGE**</dt> <dt>1</dt> </dl> | This function gets the sizes of keys that are used to encrypt and decrypt [*session keys*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-session-key-gly).<br/>                  |
| <span id="AT_SIGNATURE"></span><span id="at_signature"></span><dl> <dt>**AT\_SIGNATURE**</dt> <dt>2</dt> </dl>       | This function gets the sizes of keys that are used to create and verify [*digital signatures*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-digital-signature-gly). <br/> |



 

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> <dt>

*pKeySizes* \[out\]
</dt> <dd>

A pointer to a [**CARD\_KEY\_SIZES**](card-key-sizes.md) structure that, on output, contains information about the sizes of private keys supported on the smart card.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero value.

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

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CARD\_KEY\_SIZES**](card-key-sizes.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[**CardCreateContainer**](cardcreatecontainer.md)
</dt> </dl>

 

 





