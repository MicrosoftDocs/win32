---
title: ResultsLocation element
description: This is the relative path from the directory containing the job results file to the directory containing the assessment results file that contains the results in this AssessmentResult.
ms.assetid: '532EE61B-C794-43D8-96ED-C577C7F3BED0'
keywords: ["ResultsLocation element Access Execution Engine"]
topic_type:
- apiref
api_name:
- ResultsLocation
api_type:
- Schema
---

# ResultsLocation element

This is the relative path from the directory containing the job results file to the directory containing the assessment results file that contains the results in this [**AssessmentResult**](assessmentresult.md). AXE guarantees this node is present in results files that it writes. Assessments are not to write this node.

## Usage

``` syntax
<ResultsLocation/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                                 | Description                                                                |
|---------------------------------------------------------|----------------------------------------------------------------------------|
| [**AssessmentResult**](assessmentresult.md)<br/> | Describes the results for an individual assessment.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





