---
title: CheckForProcess element
description: Identifies a process that should not or cannot be running when an assessment begins.
ms.assetid: 0D1E23E6-4512-4504-B2CB-8004E404D969
keywords:
- CheckForProcess element Access Execution Engine
topic_type:
- apiref
api_name:
- CheckForProcess
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CheckForProcess element

Identifies a process that should not or cannot be running when an assessment begins.

## Usage

``` syntax
<CheckForProcess>
  child elements
</CheckForProcess>
```

## Attributes

There are no attributes.

## Child elements



| Element                           | Description                                                                                                         |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**Block**](block.md)<br/> | If this file is running as a process, AXE blocks the assessment from running.<br/> <br/>                |
| [**Warn**](warn.md)<br/>   | If this file is running as a process, AXE warns the users but the assessment can still run. <br/> <br/> |



### Child element sequence

``` syntax
BlockWarn
```

## Parent elements



| Element                                     | Description                                                          |
|---------------------------------------------|----------------------------------------------------------------------|
| [**Properties**](properties.md)<br/> | This element describes assessment properties.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





