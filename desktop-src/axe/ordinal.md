---
title: Ordinal element
description: This is an optional unsigned integer that specifies the order in which Iteration nodes should appear in the Job Results file.
ms.assetid: 7F9071CD-E451-4A6C-8DDA-0AE9E38D0D05
keywords:
- Ordinal element Access Execution Engine
topic_type:
- apiref
api_name:
- Ordinal
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ordinal element

This is an optional unsigned integer that specifies the order in which [**Iteration**](iteration.md) nodes should appear in the Job Results file. It identifies [**Iteration**](iteration.md) nodes that should be combined by AXE into a single **Iteration** node when AXE creates the Job Results file. This enables an assessment to write different parts of an **Iteration** node into different XML files and have AXE combine them. **Iteration** nodes will only be combined with other **Iteration** nodes for the same assessment.

## Usage

``` syntax
<Ordinal>
  text
</Ordinal>
```

## Attributes

There are no attributes.

## Text value

An optional unsigned integer that specifies the order in which [**Iteration**](iteration.md) nodes should appear in the Job Results file

## Child elements

There are no child elements.

## Parent elements



| Element                                   | Description                                                                      |
|-------------------------------------------|----------------------------------------------------------------------------------|
| [**Iteration**](iteration.md)<br/> | Receives metric values for a single assessment iteration.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





