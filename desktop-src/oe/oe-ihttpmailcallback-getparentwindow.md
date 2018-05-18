---
title: IHTTPMailCallback GetParentWindow method
description: Gets the handle of the parent application's window.
ms.assetid: '129146ab-19e5-42c8-a882-9e9dc5fafe54'
keywords: ["GetParentWindow method Windows Mail (formerly Outlook Express)", "GetParentWindow method Windows Mail (formerly Outlook Express) , IHTTPMailCallback interface", "IHTTPMailCallback interface Windows Mail (formerly Outlook Express) , GetParentWindow method"]
topic_type:
- apiref
api_name:
- IHTTPMailCallback.GetParentWindow
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IHTTPMailCallback::GetParentWindow method

\[**IHTTPMailCallback::GetParentWindow** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets the handle of the parent application's window.

## Syntax


```C++
HRESULT GetParentWindow(
  [out] HWND *phwndParent
);
```



## Parameters

<dl> <dt>

*phwndParent* \[out\]
</dt> <dd>

Type: **HWND\***

Receives a pointer to the handle of the parent window.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                                               |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Indicates success. <br/>                            |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Indicates that an unknown error has occurred. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





