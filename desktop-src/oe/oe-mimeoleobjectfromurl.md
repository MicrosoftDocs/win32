---
title: MimeOleObjectFromUrl function
description: Do not use. Creates a new message object and loads its state from the supplied URL (on success).
ms.assetid: 4adfb652-e8b4-45a4-8a3f-5b7a6d1bb5c8
keywords:
- MimeOleObjectFromUrl function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleObjectFromUrl
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleObjectFromUrl function

Do not use. Creates a new message object and loads its state from the supplied URL (on success).

## Syntax


```C++
HRESULT MimeOleObjectFromUrl(
  _In_  LPCSTR   pszUrl,
  _In_  BOOL     fCreate,
  _In_  REFIID   riid,
  _Out_ LPVOID   *ppvObject,
  _Out_ IUnknown **ppUnkKeepAlive
);
```



## Parameters

<dl> <dt>

*pszUrl* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the base URL.

</dd> <dt>

*fCreate* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies whether a new message object should be created if *pszUrl* cannot be resolved.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

Specifies IID of the interface client used to communicate with object that URL identifies.

</dd> <dt>

*ppvObject* \[out\]
</dt> <dd>

Type: **LPVOID\***

Receives address of a pointer to interface specified by *riid*.

</dd> <dt>

*ppUnkKeepAlive* \[out\]
</dt> <dd>

Type: **[IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp)\*\***

Receives address of interface pointer that allows *ppvObject* to control lifetime, not *pszUrl*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that allocation failed. <br/> |



 

## Remarks

> [!Note]  
> Not applicable to Macintosh.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





