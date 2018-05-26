---
title: NavigationButtonTFXToken element
description: Specifies the globally unique identifier (GUID) of the navigation button style to be used by this menu style.
ms.assetid: 82ce59e2-db73-4209-95c2-d76a2592e957
keywords:
- NavigationButtonTFXToken element Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- NavigationButtonTFXToken
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NavigationButtonTFXToken element

Specifies the globally unique identifier (GUID) of the navigation button style to be used by this menu style.

## Usage

``` syntax
<NavigationButtonTFXToken/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                         |
|-------------------------------------------------|
| [**DVDMenuStyle**](dvdmenustyle.md)<br/> |



## Remarks

Built-in button styles are referenced as follows:

"TFX\\&lt; *DVDButton guid* &gt;".

Third-party button styles are referenced as follows:

"COM\\&lt; *DVDButtonDLL guid* &gt;\\&lt; *DVDButton guid* &gt;".

In addition, some media nodes are referenced as follows:

"Pipeline\\&lt; *DVDButton guid* &gt;".

## Element information



|                                     |               |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



## See also

<dl> <dt>

[**Elements**](elements.md)
</dt> </dl>

 

 





