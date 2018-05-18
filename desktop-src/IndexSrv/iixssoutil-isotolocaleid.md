---
title: IixssoUtil ISOToLocaleID method
description: Converts a language code to a locale identifier (LCID).
ms.assetid: '79f4bc71-86a2-49c2-a7a4-8dbb847805b2'
keywords: ["ISOToLocaleID method Indexing Service", "ISOToLocaleID method Indexing Service , IixssoUtil interface", "IixssoUtil interface Indexing Service , ISOToLocaleID method"]
topic_type:
- apiref
api_name:
- IixssoUtil.ISOToLocaleID
api_location:
- Ixsso.dll
api_type:
- COM
---

# IixssoUtil::ISOToLocaleID method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Converts a language code to a locale identifier (LCID).

## Syntax


```C++
HRESULT ISOToLocaleID(
  [in]          BSTR pwszLocale,
  [out, retval] LONG *plcid
);
```



## Parameters

<dl> <dt>

*pwszLocale* \[in\]
</dt> <dd>

The language code. In addition to the ISO language codes, the name "neutral" can be used.

</dd> <dt>

*plcid* \[out, retval\]
</dt> <dd>

The LCID. If there is no matching language code, 1 is returned.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The first recognized language code found in *pwszLocale* is converted to an LCID. The recognized language codes include all those from the ISO 639 standard that map to language IDs and some country codes that have sublanguage codes. If a language code is recognized, but the country code is not, the language code alone is used, unless there is a better match later in the string.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoUtil**](iixssoutil.md)
</dt> </dl>

 

 





