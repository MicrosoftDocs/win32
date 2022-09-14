---
description: Defines the prefix to which the namespace should be mapped to make the XML more readable.
ms.assetid: 955f4785-5657-4a89-9728-bce99a0a4234
title: preferredPrefix element
ms.topic: reference
ms.date: 05/31/2018
---

# preferredPrefix element

Defines the prefix to which the namespace should be mapped to make the XML more readable.

## Usage

``` syntax
<preferredPrefix/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                   | Description                                                        |
|-------------------------------------------|--------------------------------------------------------------------|
| [**nameSpace**](namespace.md)<br/> | A namespace to be used for code generation.<br/> <br/> |



## Remarks

This element overrides the default URI prefix used for generated code. For example, a media-related namespace might have the preferred prefix "av" (for audio/visual).

By default, the code generated creates a preferred prefix from the URI.

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




