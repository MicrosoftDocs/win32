---
title: CardGetContainerInfo function
description: Retrieves a CONTAINER\_INFO structure that contains information about a key container on a smart card.
ms.assetid: '5574a8c3-d6f3-4100-88d3-d518412f8f56'
keywords: ["CardGetContainerInfo function Security"]
topic_type:
- apiref
api_name:
- CardGetContainerInfo
api_location:
- Cardmod.h
api_type:
- HeaderDef
---

# CardGetContainerInfo function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardGetContainerInfo** function, defined by a smart card module, retrieves a [**CONTAINER\_INFO**](container-info.md) structure that contains information about a [*key container*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-container-gly) on a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardGetContainerInfo(
  _In_    PCARD_DATA      pCardData,
  _In_    BYTE            bContainerIndex,
  _In_    DWORD           dwFlags,
  _Inout_ PCONTAINER_INFO pContainerInfo
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*bContainerIndex* \[in\]
</dt> <dd>

A **BYTE** value that specifies the index number for the key container for which to get information. The [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) (CSP) and smart card [*key storage provider*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-storage-provider-gly) (KSP) use this index value to identify the key container.

The function fails if the specified key container does not exist.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> <dt>

*pContainerInfo* \[in, out\]
</dt> <dd>

A [**CONTAINER\_INFO**](container-info.md) structure that, on output, contains information about the key container specified by the *bContainerIndex* parameter.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                        | Description                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_NO\_KEY\_CONTAINER**</dt> <dt>2148532260 (0x80100024)</dt> </dl> | The value of the *bContainerIndex* parameter is not a valid index of an existing key container.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[**CardCreateContainer**](cardcreatecontainer.md)
</dt> <dt>

[**CONTAINER\_INFO**](container-info.md)
</dt> </dl>

 

 





