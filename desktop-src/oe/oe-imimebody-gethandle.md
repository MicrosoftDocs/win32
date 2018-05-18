---
title: IMimeBody GetHandle method
description: Gets the handle of the body.
ms.assetid: 'cf061273-4871-4ec5-b364-86a54abfc52e'
keywords: ["GetHandle method Windows Mail (formerly Outlook Express)", "GetHandle method Windows Mail (formerly Outlook Express) , IMimeBody interface", "IMimeBody interface Windows Mail (formerly Outlook Express) , GetHandle method"]
topic_type:
- apiref
api_name:
- IMimeBody.GetHandle
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeBody::GetHandle method

Gets the handle of the body.

## Syntax


```C++
HRESULT GetHandle(
  [out] LPHBODY phBody
);
```



## Parameters

<dl> <dt>

*phBody* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the body.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                      | Description                                                   |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | Indicates success.<br/>                                 |
| <dl> <dt>**E\_FAIL**</dt> </dl>           | Indicates that an unknown error has occurred.<br/>      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>     | Indicates that *phBody* is **NULL**.<br/>               |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl> | Indicates that the handle of the body is **NULL**.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





