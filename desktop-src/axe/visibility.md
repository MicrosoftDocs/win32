---
title: Visibility element
description: Defines the visibility of the parameter.
ms.assetid: 703F32EA-B390-4109-8EC4-51D6C446D9D8
keywords:
- Visibility element Access Execution Engine
topic_type:
- apiref
api_name:
- Visibility
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Visibility element

Defines the visibility of the parameter.

## Usage

``` syntax
<Visibility>
  child elements
</Visibility>
```

## Attributes

There are no attributes.

## Child elements



| Element                                          | Description                                                                                                |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**Collapsed**](collapsed.md)<br/>        | Indicates that the parameter definition is collapsed when first presented.<br/> <br/>          |
| [**Hidden**](hidden--visibility-.md)<br/> | Indicates that the parameter definition is not shown.<br/> <br/>                               |
| [**Visible**](visible.md)<br/>            | Indicates that the parameter definition is visible (expanded) when first presented.<br/> <br/> |



### Child element sequence

``` syntax
(
  Collapsed
, 
  Hidden, 
  Visible
)
```

## Parent elements

There are no parent elements.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



 

 





