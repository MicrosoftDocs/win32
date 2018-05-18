---
title: IMimeEditTagCollection Next method
description: On success, obtains some number of IMimeEditTag objects.
ms.assetid: 'f1cb2a7c-b763-4738-aed5-880dfd6722e8'
keywords: ["Next method Windows Mail (formerly Outlook Express)", "Next method Windows Mail (formerly Outlook Express) , IMimeEditTagCollection interface", "IMimeEditTagCollection interface Windows Mail (formerly Outlook Express) , Next method"]
topic_type:
- apiref
api_name:
- IMimeEditTagCollection.Next
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeEditTagCollection::Next method

\[**IMimeEditTagCollection::Next** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

On success, obtains some number of [**IMimeEditTag**](oe-imimeedittag.md) objects.

## Syntax


```C++
HRESULT Next(
  [in]  ULONG        cFetch,
  [out] IMimeEditTag **ppTag,
  [out] ULONG        *pcFetched
);
```



## Parameters

<dl> <dt>

*cFetch* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the desired number of tags to fetch.

</dd> <dt>

*ppTag* \[out\]
</dt> <dd>

Type: **[**IMimeEditTag**](oe-imimeedittag.md)\*\***

On success, returns [**IMimeEditTag**](oe-imimeedittag.md) objects.

</dd> <dt>

*pcFetched* \[out\]
</dt> <dd>

Type: **ULONG\***

Specifies the number of tags fetched.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





