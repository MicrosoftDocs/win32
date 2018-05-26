---
title: CardDestroyDHAgreement function
description: Removes a Diffie-Hellman secret agreement from the specified key container on the smart card.
ms.assetid: 48fea080-8f8e-45bf-9dba-b886a5445878
keywords:
- CardDestroyDHAgreement function Security
topic_type:
- apiref
api_name:
- CardDestroyDHAgreement
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CardDestroyDHAgreement function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardDestroyDHAgreement** function, defined by a smart card module, removes a Diffie-Hellman secret agreement from the specified [*key container*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-container-gly) on the [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardDestroyDHAgreement(
  _In_ PCARD_DATA pCardData,
  _In_ BYTE       bSecretAgreementIndex,
  _In_ DWORD      dwFlags
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*bSecretAgreementIndex* \[in\]
</dt> <dd>

The index of the key container that contains the secret agreement to be removed.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero value.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



 

 





