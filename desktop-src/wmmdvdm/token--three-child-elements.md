---
title: Token (Three Child Elements) element
description: Creates a media node in the pipeline graph.
ms.assetid: c10c22ec-46e0-48ff-84b0-9bb77a5770ba
keywords:
- Token (Three Child Elements) element Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- Token
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Token (Three Child Elements) element

Creates a media node in the pipeline graph.

## Usage

``` syntax
<Token/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                              |
|--------------------------------------|
| [**Graph**](GraphElement)<br/> |



## Remarks

The VideoToFill media node (the example cited here) takes two input sources and provides a single output. It composites a rectangular mesh (consisting of two planar triangles), textured with the second input source, onto the first input source. The media node's property bag contains properties to transform the rectangular mesh in space. The rectangular mesh has vertices at (-1, -1, 0), (-1, 1, 0), (1, -1, 0), and (1, 1, 0). The default camera position and aspect ratio are such that this output exactly fills the camera's view.

## Element information



|                                     |               |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



## See also

<dl> <dt>

[**Elements**](elements.md)
</dt> <dt>

[**Token Element (One Child Element)**](token--one-child-element.md)
</dt> <dt>

[**Token Element (Four Child Elements)**](token--four-child-elements.md)
</dt> </dl>

 

 





