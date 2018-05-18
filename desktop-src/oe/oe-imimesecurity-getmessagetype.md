---
title: IMimeSecurity GetMessageType method
description: Gets the security type ID for the specified message body.
ms.assetid: '5bbf47cd-1bfc-4c1d-aa70-ebaa0b0c95b3'
keywords: ["GetMessageType method Windows Mail (formerly Outlook Express)", "GetMessageType method Windows Mail (formerly Outlook Express) , IMimeSecurity interface", "IMimeSecurity interface Windows Mail (formerly Outlook Express) , GetMessageType method"]
topic_type:
- apiref
api_name:
- IMimeSecurity.GetMessageType
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeSecurity::GetMessageType method

Gets the security type ID for the specified message body.

## Syntax


```C++
HRESULT GetMessageType(
  [in]  const HWND      hwndParent,
  [in]        IMimeBody pBody,
  [out]       DWORD     pdwSecType
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **const HWND**

Specifies the handle of the window to use as a parent for interacting with the user.

</dd> <dt>

*pBody* \[in\]
</dt> <dd>

Type: **[**IMimeBody**](oe-imimebody.md)**

Specifies a pointer to the [**IMimeBody**](oe-imimebody.md) object.

</dd> <dt>

*pdwSecType* \[out\]
</dt> <dd>

Type: **DWORD**

Receives a pointer to a **DWORD** that contains the security type ID.

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



 

 





