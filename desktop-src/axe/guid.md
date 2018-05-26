---
title: Guid element
description: Each job requires a unique identity represented by a GUID .
ms.assetid: 2D4A44B6-9EC4-4320-8A47-95345362C4FC
keywords:
- Guid element Access Execution Engine
topic_type:
- apiref
api_name:
- Guid
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Guid element

Each job requires a unique identity represented by a **GUID** . This Id is created by the AXE assessment management API's when it creates a job object. Once created this **GUID** it is never changed.

## Usage

``` syntax
<Guid>
  text
</Guid>
```

## Attributes

There are no attributes.

## Text value

A **GUID** in registry format. The open and close braces are required.

## Child elements

There are no child elements.

## Parent elements



| Element                                                 | Description                                                                          |
|---------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**AssessmentResult**](assessmentresult.md)<br/> | This element describes the results for individual assessment.<br/> <br/> |



## Remarks

### Assessment Result

AXE uniquely identifies each assessments run by a GUID. AXE guarantees this node is present in results files . Assessments are not to write this node because they do not have access to the **GUID** of the corresponding assessment manifest.

Solutions should look up the value of this **Guid** in the **AssessmentRun** element to index the collection of assessment manifests the reports in the **AssessmentManifests** element.

Note that the GUID property will always be read only as it is initialized on when a job is newly created.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





