---
description: Defines a Uniscribe font metric cache.
ms.assetid: 56a98529-6ae9-4b71-bd7d-cf056a1e3683
title: SCRIPT_CACHE (Usp10.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SCRIPT\_CACHE

Defines a Uniscribe font metric cache.


```C++
typedef void* SCRIPT_CACHE;
```



## Remarks

This is an opaque structure. The application must allocate and retain one SCRIPT\_CACHE variable for each character style used. The variable must be initialized to **NULL**.

Many script functions take a combination of a hardware device context handle and a SCRIPT\_CACHE variable. Uniscribe first attempts to access font data by using the SCRIPT\_CACHE variable. It only inspects the hardware device context if the required data is not already cached.

The hardware device context handle can be passed to Uniscribe as **NULL**. If data required by Uniscribe is already cached, the device context is not accessed, and the operation continues normally.

If the device context is passed as **NULL** and Uniscribe needs to access it for any reason, Uniscribe returns the error code E\_PENDING. This code is returned quickly, allowing the application to avoid time-consuming [**SelectObject**](/windows/win32/api/wingdi/nf-wingdi-selectobject) calls.

## Examples

The following example applies to all functions that take a SCRIPT\_CACHE variable and an optional handle to a hardware device context.


```C++
hr = ScriptShape(NULL, &sc,
                 pwcChars, cChars, cMaxGlyphs, psa, pwOutGlyphs, pwLogClust, psva, pcGlyphs);
if (hr == E_PENDING)
{
    // ... select font into hdc ...
    hr = ScriptShape(hdc, &sc,
                 pwcChars, cChars, cMaxGlyphs, psa, pwOutGlyphs, pwLogClust, psva, pcGlyphs);
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Usp10.h</dt> </dl> |



## See also

<dl> <dt>

[Uniscribe](uniscribe.md)
</dt> <dt>

[Uniscribe Structures](uniscribe-structures.md)
</dt> <dt>

[Caching](caching.md)
</dt> </dl>

 

 
