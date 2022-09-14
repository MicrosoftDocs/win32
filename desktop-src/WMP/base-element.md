---
title: BASE Element
description: The BASE element defines a URL string appended to the front of URLs sent to Windows Media Player.
ms.assetid: 887cf860-d06e-44a1-b729-28a285f6c7d3
keywords:
- BASE Element Windows Media Player
topic_type:
- apiref
api_name:
- BASE Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# BASE Element

The **BASE** element defines a URL string appended to the front of URLs sent to Windows Media Player.

``` syntax
<BASE
   HREF = "URL"
/>
```

## Attributes

**HREF** (required)

The string appended to the front to URLs sent to Windows Media Player. The default value is the null string ("").

## Parent/Child Elements



| Hierarchy       | Elements           |
|-----------------|--------------------|
| Parent elements | **ASX**, **ENTRY** |
| Child elements  | None               |



 

## Remarks

This element defines a URL string appended to the front of URL-flip URLs sent to Windows Media Player. URL-flipping is a scripting mechanism that causes Windows Media Player to open a new URL in a browser or browser frame when it receives a script command.

The **BASE** element is similar to a home directory for relative links. It only affects URLs sent using script commands as part of the content stream that is playing in Windows Media Player.

A **BASE** element defined as the child of an **ASX** element becomes the default for the entire metafile. A **BASE** element defined in an **ENTRY** element overrides any **BASE** element in the parent **ASX** element (for that **ENTRY** element only).

> [!Note]  
> If the **HREF** attribute does not end with a / character, Windows Media Player appends one to the end of the string.

 

## Examples


```XML
<BASE HREF="https://msdn.microsoft.com/" />

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> </dl>

 

 





