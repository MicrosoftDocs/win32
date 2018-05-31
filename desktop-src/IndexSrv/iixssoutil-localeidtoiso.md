---
title: IixssoUtil LocaleIDToISO method
description: Converts a locale identifier (LCID) to a language code.
ms.assetid: e9ce07a2-e5a3-4920-a493-203c65741933
keywords:
- LocaleIDToISO method Indexing Service
- LocaleIDToISO method Indexing Service , IixssoUtil interface
- IixssoUtil interface Indexing Service , LocaleIDToISO method
topic_type:
- apiref
api_name:
- IixssoUtil.LocaleIDToISO
api_location:
- Ixsso.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoUtil::LocaleIDToISO method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Converts a locale identifier (LCID) to a language code.

## Syntax


```C++
HRESULT LocaleIDToISO(
  [in]          LONG lcid,
  [out, retval] BSTR *ppwszLocale
);
```



## Parameters

<dl> <dt>

*lcid* \[in\]
</dt> <dd>

The LCID to be translated.

</dd> <dt>

*ppwszLocale* \[out, retval\]
</dt> <dd>

The language code. In addition to the ISO language codes, the name neutral can be used.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoUtil**](iixssoutil.md)
</dt> </dl>

 

 





