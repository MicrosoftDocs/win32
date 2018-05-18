---
title: SceneButtonTFXToken element
description: Specifies the globally unique identifier (GUID) of the scene button style to be used by this menu style.
ms.assetid: '42585a4a-e45a-49dd-ac0c-6c4bbc1076dd'
keywords: ["SceneButtonTFXToken element Windows Movie Maker and DVD Maker"]
topic_type:
- apiref
api_name:
- SceneButtonTFXToken
api_type:
- Schema
---

# SceneButtonTFXToken element

Specifies the globally unique identifier (GUID) of the scene button style to be used by this menu style.

## Usage

``` syntax
<SceneButtonTFXToken/>
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
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



## See also

<dl> <dt>

[**Elements**](elements.md)
</dt> </dl>

 

 





