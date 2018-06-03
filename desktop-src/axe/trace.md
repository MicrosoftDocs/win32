---
title: Trace element
description: This is an optional trace file associated with this iteration.
ms.assetid: 89B4DF86-7B84-45F6-99E2-863BE70BFCC0
keywords:
- Trace element Access Execution Engine
topic_type:
- apiref
api_name:
- Trace
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Trace element

This is an optional trace file associated with this iteration.

## Usage

``` syntax
<Trace>
  child elements
</Trace>
```

## Attributes

There are no attributes.

## Child elements



| Element                                       | Description                                                            |
|-----------------------------------------------|------------------------------------------------------------------------|
| [**DisplayName**](displayname.md)<br/> | This is a human-readable name for the item.<br/> <br/>     |
| [**ToolTip**](tooltip.md)<br/>         | A short description that can be used in the UX.<br/> <br/> |



### Child element sequence

``` syntax
DisplayNameToolTip
```

## Parent elements



| Element                                   | Description                                                                      |
|-------------------------------------------|----------------------------------------------------------------------------------|
| [**Iteration**](iteration.md)<br/> | Receives metric values for a single assessment iteration.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





