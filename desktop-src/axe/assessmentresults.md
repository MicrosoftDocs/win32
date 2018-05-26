---
title: AssessmentResults element
description: This element is a container for one or more AssessmentResult elements.
ms.assetid: 1C6B9DD8-7389-4D82-969F-908885A4FA15
keywords:
- AssessmentResults element Access Execution Engine
topic_type:
- apiref
api_name:
- AssessmentResults
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AssessmentResults element

This element is a container for one or more [**AssessmentResult**](assessmentresult.md) elements.

## Usage

``` syntax
<AssessmentResults>
  child elements
</AssessmentResults>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                                |
|---------------------------------------------------------|----------------------------------------------------------------------------|
| [**AssessmentResult**](assessmentresult.md)<br/> | Describes the results for an individual assessment.<br/> <br/> |



### Child element sequence

``` syntax
AssessmentResult
```

## Parent elements



| Element                             | Description                                             |
|-------------------------------------|---------------------------------------------------------|
| [**AxeJob**](https://msdn.microsoft.com/library/windows/desktop/hh707420)<br/> | The root node of the assessment.<br/> <br/> |



## Remarks

Assessments produce one or more XML files that contain individual results. AXE aggregates all of the assessment result files into the final job results file. During that process, Axe adds this node around all of the aggregated results from individual assessments. Assessments do not write this node into their own results files.

## Examples

``` syntax
<AxeJobResults>
    <AssessmentResults>
        <AssessmentResult> ... </AssessmentResult>
        <AssessmentResult> ... </AssessmentResult>
        ... more ...
        <AssessmentResult> ... </AssessmentResult>
    </AssessmentResults>
</AxeJobResults>
```

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





