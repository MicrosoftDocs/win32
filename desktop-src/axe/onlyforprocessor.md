---
title: OnlyForProcessor element
description: Indicates the platforms on which the assessment should run.
ms.assetid: 80E30B77-FB6B-460C-A8E8-2141CD5A9BDD
keywords:
- OnlyForProcessor element Access Execution Engine
topic_type:
- apiref
api_name:
- OnlyForProcessor
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OnlyForProcessor element

Indicates the platforms on which the assessment should run. If this node is present, then it must contain one or more of the following sub nodes. The Execution engine will not run an assessment on a platform not in this list. Omitting this node means the assessment can run on all platforms.

## Usage

``` syntax
<OnlyForProcessor>
  child elements
</OnlyForProcessor>
```

## Attributes

There are no attributes.

## Child elements



| Element                       | Description                                                                                |
|-------------------------------|--------------------------------------------------------------------------------------------|
| [**ARM**](arm.md)<br/> | This should be an empty leaf node containing no attributes or text.<br/> <br/> |
| [**X64**](x64.md)<br/> | This should be an empty leaf node containing no attributes or text.<br/> <br/> |
| [**X86**](x86.md)<br/> | This should be an empty leaf node containing no attributes or text.<br/> <br/> |



### Child element sequence

``` syntax
(
  X86, 
  X64, 
  ARM
)
```

## Parent elements



| Element                                     | Description                                            |
|---------------------------------------------|--------------------------------------------------------|
| [**Properties**](properties.md)<br/> | This node describes properties.<br/> <br/> |



## Remarks

AXE will issue a warning if a job contains assessments that don t run on the same platform.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



 

 





