---
Description: 'Uniscribe saves Unicode-to-glyph (cmap) mappings, glyph widths, and OpenType script shaping tables.'
ms.assetid: 'c06c0eaf-41cb-4fd1-9750-a78355217f12'
title: Caching
---

# Caching

Uniscribe saves Unicode-to-glyph (cmap) mappings, glyph widths, and OpenType script shaping tables. A handle to the tables for a particular font of a particular size is called a "script cache". Many Uniscribe functions call for both a device context handle parameter and a pointer to a [**SCRIPT\_CACHE**](script-cache.md) structure. These functions look first for information through the script cache, using the device context only when required tables are not already cached. When calling the [**ScriptShape**](scriptshape.md), [**ScriptPlace**](scriptplace.md), or [**ScriptTextOut**](scripttextout.md) function, the application must pass a pointer to a **SCRIPT\_CACHE** structure. The handle should be initialized to **NULL** before the first time the application passes it to a Uniscribe function. The application should never pass the same handle for different fonts or different sizes.

An application can free a script cache at any time. Uniscribe maintains reference counts in its font and shaper caches, frees font data only when all sizes of the font are freed, and frees shaper data only when all fonts that the shaper supports are freed. When the application is done with a style, it should call the [**ScriptFreeCache**](scriptfreecache.md) function to free the script cache for the style.

For [**ScriptShape**](scriptshape.md) and [**ScriptPlace**](scriptplace.md), it is valid for the application to pass a null device context. Most often the call will succeed, as required tables are already cached. If the shaping or placement requires access to a device context, **ScriptShape** or **ScriptPlace** returns immediately with the E\_PENDING error code. Then the application must select the font in the device context. For most applications, this helps performance by avoiding repeated preparation of a device context handle with calls to [**SelectObject**](gdi.selectobject).

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 



