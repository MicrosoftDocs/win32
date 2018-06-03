---
title: CardDeleteContainer function
description: Deletes a key container from a smart card.
ms.assetid: 78a4d830-802f-4150-a9c8-230fc3681ed4
keywords:
- CardDeleteContainer function Security
topic_type:
- apiref
api_name:
- CardDeleteContainer
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

# CardDeleteContainer function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardDeleteContainer** function, defined by a smart card module, deletes a [*key container*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-container-gly) from a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardDeleteContainer(
  _In_ PCARD_DATA pCardData,
  _In_ BYTE       bContainerIndex,
  _In_ DWORD      dwReserved
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to the [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*bContainerIndex* \[in\]
</dt> <dd>

The index number for the key container to delete. The [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) (CSP) and smart card [*key storage provider*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-storage-provider-gly) (KSP) use this index value to identify the key container.

The function fails if the specified key container does not exist.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, it returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                        | Description                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_NO\_KEY\_CONTAINER**</dt> <dt>2148532260 (0x80100024)</dt> </dl> | The value of the *bContainerIndex* parameter is not a valid index of an existing key container.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[**CardCreateContainer**](cardcreatecontainer.md)
</dt> </dl>

 

 





