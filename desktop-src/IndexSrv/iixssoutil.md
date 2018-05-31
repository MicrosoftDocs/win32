---
title: IixssoUtil interface
description: An ActiveX server-side control that is an automation object with a dual interface supporting IDispatch. The methods supported by this object give script writers utility routines for use with the Query object.
ms.assetid: 7eb3b238-fda3-429b-9b21-db8345f17f02
keywords:
- IixssoUtil interface Indexing Service
- IixssoUtil interface Indexing Service , described
topic_type:
- apiref
api_name:
- IixssoUtil
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
api_location:
- Ixsso.dll
api_type:
- COM
---

# IixssoUtil interface

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

An ActiveX server-side control that is an automation object with a dual interface supporting **IDispatch**. The methods supported by this object give script writers utility routines for use with the Query object.

The programmatic identifier (ProgID) for the object is IXSSO.Util.2. The version-independent ProgID is IXSSO.Util.

## Members

The **IixssoUtil** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IixssoUtil** also has these types of members:

-   [Methods](#methods)

### Methods

The **IixssoUtil** interface has these methods.



| Method                                                          | Description                                                                    |
|:----------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**AddScopeToQuery**](iixssoutil-addscopetoquery.md)           | Adds a new scope restriction to a query.<br/>                            |
| [**GetArrayElement**](iixssoutil-getarrayelement.md)           | Accesses a safe-array vector element. <br/>                              |
| [**HTMLEncode**](iixssoutil-htmlencode.md)                     | Encodes a string using HTML encoding using the specified code page.<br/> |
| [**ISOToLocaleID**](iixssoutil-isotolocaleid.md)               | Converts a language code to a locale identifier (LCID).<br/>             |
| [**LocaleIDToISO**](iixssoutil-localeidtoiso.md)               | Converts a locale identifier (LCID) to a language code.<br/>             |
| [**TruncateToWhitespace**](iixssoutil-truncatetowhitespace.md) | Truncates a string at a white-space character.<br/>                      |
| [**URLEncode**](iixssoutil-urlencode.md)                       | Encodes a string using URL encoding using the specified code page.<br/>  |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



 

 





