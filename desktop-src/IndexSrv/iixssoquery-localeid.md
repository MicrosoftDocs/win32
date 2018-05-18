---
title: IixssoQuery LocaleID property
description: Retrieves or sets the language locale ID (LCID) to be used when executing the query. Otherwise, the system default LCID is used.
ms.assetid: '6c8bb16d-01a5-4dfc-a1a4-2c67c3ae1110'
keywords: ["LocaleID property Indexing Service", "LocaleID property Indexing Service , IixssoQuery interface", "IixssoQuery interface Indexing Service , LocaleID property"]
topic_type:
- apiref
api_name:
- IixssoQuery.LocaleID
- IixssoQuery.get_LocaleID
- IixssoQuery.put_LocaleID
api_location:
- Ixsso.dll
api_type:
- COM
---

# IixssoQuery::LocaleID property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves or sets the language locale ID (LCID) to be used when executing the query. Otherwise, the system default LCID is used.

This property is read/write.

## Syntax


```C++
HRESULT put_LocaleID(
  [in]          LONG val
);

HRESULT get_LocaleID(
  [out, retval] LONG *val
);
```



## Property value

Specifies the LCID.

## Remarks

This locale identifies the language to use to perform a query on existing indexes. Convert between language identifiers (strings) and LCIDs (constants) by using the [**ISOToLocaleID**](iixssoutil-isotolocaleid.md) and [**LocaleIDToISO**](iixssoutil-localeidtoiso.md) methods.

For Web clients requesting an Active Server Pages (ASP), browsers send an HTTP header ? HTTP\_ACCEPT\_LANGUAGE ? that specifies the locale to use in a query. This can be overridden with this **LocaleID** property. The U.S. English locale is 1033 (equivalent to the language code "en-us").

For Web clients using the ISAPI .idq files to define queries, assign the locale identifier string to CiLocale in the \[Query\] section of the query.idq file to override browser settings. See [Valid Locale Identifiers](valid-locale-identifiers.md) for a list of language identifiers recognized by Indexing Services.

## Examples


```VB
objQuery.LocaleID = 1033 ' EN-US locale code
```



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

[**IixssoQuery**](iixssoquery.md)
</dt> </dl>

 

 





