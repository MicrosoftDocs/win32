---
title: IMimeEnumHeaderRows Next method
description: On success, retrieves a specified number of elements in the enumeration sequence.
ms.assetid: '31e41d58-9dc0-48f4-85bd-f309979400c6'
keywords: ["Next method Windows Mail (formerly Outlook Express)", "Next method Windows Mail (formerly Outlook Express) , IMimeEnumHeaderRows interface", "IMimeEnumHeaderRows interface Windows Mail (formerly Outlook Express) , Next method"]
topic_type:
- apiref
api_name:
- IMimeEnumHeaderRows.Next
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeEnumHeaderRows::Next method

\[**IMimeEnumHeaderRows::Next** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

On success, retrieves a specified number of elements in the enumeration sequence. If there are fewer than the requested number of elements remaining in the sequence, this method retrieves the remaining elements.

## Syntax


```C++
HRESULT Next(
  [in]      ULONG           cFetch,
  [in, out] LPENUMHEADERROW prgRow,
  [out]     ULONG           *pcFetched
);
```



## Parameters

<dl> <dt>

*cFetch* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the number of elements being requested.

</dd> <dt>

*prgRow* \[in, out\]
</dt> <dd>

Type: **LPENUMHEADERROW**

Array in which to store the fetched elements. Note: array can be freed by calling [**FreeEnumHeaderRowArray**](oe-imimeallocator-freeenumheaderrowarray.md).

</dd> <dt>

*pcFetched* \[out\]
</dt> <dd>

Type: **ULONG\***

If **NULL** is not specified, contains the actual number of fetched elements.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates that the method retrieved the number of elements specified by *cFetch*. <br/>            |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Indicates that the method retrieved fewer than the number of elements specified by *cFetch*. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/>                                          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





