---
description: Identifies whether the specified non-color style has underline.
ms.assetid: 72056bf7-0a18-4ad3-a8c4-d2335a7218ae
title: IdUlIMEStyle function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IdUlIMEStyle
api_type: 
- DllExport
api_location: 
- Imeshare.dll
---

# IdUlIMEStyle function

Identifies whether the specified non-color style has underline.

## Syntax


```C++
UINT __cdecl IdUlIMEStyle(
  _In_ const IMESTYLE *pimestyle
);
```



## Parameters

<dl> <dt>

*pimestyle* \[in\]
</dt> <dd>

An **IMESTYLE** structure returned from [**PIMEStyleFromAttr**](pimestylefromattr.md) function.

</dd> </dl>

## Return value

This function can returns one of the following values.

<dl> <dt>

**IMESTY\_UL\_MIN** (2002)
</dt> <dt>

**IMESTY\_UL\_NONE** (2002)
</dt> <dt>

**IMESTY\_UL\_SINGLE** (2003)
</dt> <dt>

**IMESTY\_UL\_DOTTED** (2005)
</dt> <dt>

**IMESTY\_UL\_THICK** (2006)
</dt> <dt>

**IMESTY\_UL\_LOWER** (2011)
</dt> <dt>

**IMESTY\_UL\_THICKLOWER** (2012)
</dt> <dt>

**IMESTY\_UL\_THICKDITHLOWER** (2013)
</dt> <dt>

**IMESTY\_UL\_DITHLOWER** (2014)
</dt> <dt>

**IMESTY\_UL\_MAX** (2014)
</dt> </dl>

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Imeshare.dll</dt> </dl> |



## See also

<dl> <dt>

[**PIMEStyleFromAttr**](pimestylefromattr.md)
</dt> </dl>

 

 
