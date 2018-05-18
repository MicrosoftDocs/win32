---
title: IPropFindMultiResponse GetResponse method
description: IPropFindMultiResponse GetResponse method
ms.assetid: '1c5ee8f2-a3f9-438c-8258-7a6cf4f16f1c'
keywords: ["GetResponse method Windows Mail (formerly Outlook Express)", "GetResponse method Windows Mail (formerly Outlook Express) , IPropFindMultiResponse interface", "IPropFindMultiResponse interface Windows Mail (formerly Outlook Express) , GetResponse method"]
topic_type:
- apiref
api_name:
- IPropFindMultiResponse.GetResponse
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IPropFindMultiResponse::GetResponse method

\[**IPropFindMultiResponse::GetResponse** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

## Syntax


```C++
HRESULT GetResponse(
  [in]  ULONG             ulIndex,
  [out] IPropFindResponse **ppResponse
);
```



## Parameters

<dl> <dt>

*ulIndex* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies index.

</dd> <dt>

*ppResponse* \[out\]
</dt> <dd>

Type: **[**IPropFindResponse**](oe-ipropfindresponse.md)\*\***

Returns address of [**IPropFindResponse**](oe-ipropfindresponse.md) object.

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
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





