---
title: Issues element
description: A container element for one or more issues.
ms.assetid: F161E185-EDC9-42CE-9097-E925E5E87B85
keywords:
- Issues element Access Execution Engine
topic_type:
- apiref
api_name:
- Issues
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Issues element

A container element for one or more issues.

## Usage

``` syntax
<Issues>
  child elements
</Issues>
```

## Attributes

There are no attributes.

## Child elements



| Element                                             | Description                                                                                         |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**AnalysisLinks**](https://msdn.microsoft.com/library/windows/desktop/hh449264)<br/> | A container for [**Link**](link.md) elements used to launch analysis tools.<br/> <br/> |
| [**Issue**](issue.md)<br/>                   | This element holds information about a single issue.<br/> <br/>                         |



### Child element sequence

``` syntax
(
  Issue, 
  AnalysisLinks
)
```

## Parent elements



| Element                                   | Description                                                                      |
|-------------------------------------------|----------------------------------------------------------------------------------|
| [**Iteration**](iteration.md)<br/> | Receives metric values for a single assessment iteration.<br/> <br/> |
| [**TestCase**](testcase.md)<br/>   | An individual case.<br/> <br/>                                       |



## Examples

Each [**Issue**](issue.md) element is a child of a single **Issues** node under an [**Iteration**](iteration.md) or [**TestCase**](testcase.md) element.

``` syntax
<Iteration>
    <MetricValues>
    </MetricValues>
    <Issues>
    <Issue>  ...  </Issue>
    <Issue>  ...  </Issue>
    <Issue>  ...  </Issue>
    </Issues>
</Metric>
```

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





