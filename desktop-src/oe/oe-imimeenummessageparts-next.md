---
title: IMimeEnumMessageParts Next method
description: Retrieves the next specified number of elements in the enumeration sequence.
ms.assetid: ed3a3047-ebe6-4d62-b1fd-502fbba63f23
keywords:
- Next method Windows Mail (formerly Outlook Express)
- Next method Windows Mail (formerly Outlook Express) , IMimeEnumMessageParts interface
- IMimeEnumMessageParts interface Windows Mail (formerly Outlook Express) , Next method
topic_type:
- apiref
api_name:
- IMimeEnumMessageParts.Next
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeEnumMessageParts::Next method

Retrieves the next specified number of elements in the enumeration sequence.

## Syntax


```C++
HRESULT Next(
  [in]      ULONG        cFetch,
  [in, out] IMimeMessage **prgpMessage,
  [out]     ULONG        *pcFetched
);
```



## Parameters

<dl> <dt>

*cFetch* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that indicates the number of requested elements.

</dd> <dt>

*prgpMessage* \[in, out\]
</dt> <dd>

Type: **[**IMimeMessage**](oe-imimemessage.md)\*\***

Receives an array of [**IMimeMessage**](oe-imimemessage.md) objects in which to store the retrieved elements. The array can be freed by calling [**ReleaseObjects**](oe-imimeallocator-releaseobjects.md).

</dd> <dt>

*pcFetched* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of elements that were retrieved.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates that the method retrieved the number of elements specified by *cFetch*. <br/>            |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Indicates that the method retrieved fewer than the number of elements specified by *cFetch*. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>                                          |



 

## Remarks

If there are fewer than the requested number of elements remaining in the sequence, this method retrieves the remaining elements. The number of elements actually retrieved is returned through *pcFetched* (unless the caller passed in **NULL** for this parameter).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





