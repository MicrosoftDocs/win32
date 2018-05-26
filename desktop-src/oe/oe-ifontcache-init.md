---
title: IFontCache Init method
description: Creates a new font cache entry and initializes its resources.
ms.assetid: e81d415f-c9ba-4f57-af56-3637e6d378d7
keywords:
- Init method Windows Mail (formerly Outlook Express)
- Init method Windows Mail (formerly Outlook Express) , IFontCache interface
- IFontCache interface Windows Mail (formerly Outlook Express) , Init method
topic_type:
- apiref
api_name:
- IFontCache.Init
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IFontCache::Init method

\[**IFontCache::Init** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a new font cache entry and initializes its resources.

## Syntax


```C++
HRESULT Init(
  [in] HKEY   hkey,
  [in] LPCSTR pszIntlKey,
  [in] DWORD  dwFlags
);
```



## Parameters

<dl> <dt>

*hkey* \[in\]
</dt> <dd>

Type: **HKEY**

Specifies the handle to the current key.

</dd> <dt>

*pszIntlKey* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the key path as a string.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies bitmask flags.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Entry is created and initialized. <br/>    |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Initialization failed.<br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | An attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





