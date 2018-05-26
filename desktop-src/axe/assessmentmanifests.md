---
title: AssessmentManifests element
description: Contains one or more AssessmentManifest elements.
ms.assetid: DBC8686F-7C81-4C27-942C-9C4523094A38
keywords:
- AssessmentManifests element Access Execution Engine
topic_type:
- apiref
api_name:
- AssessmentManifests
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AssessmentManifests element

Contains one or more [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288) elements.

## Usage

``` syntax
<AssessmentManifests>
  child elements
</AssessmentManifests>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                     | Description                                                                                                                                          |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288)<br/> | Each assessment manifest will be marshaled under this &lt;AssessmentManfiests&gt; node in an &lt;AssessmentManfiest&gt; node.<br/> <br/> |



### Child element sequence

``` syntax
AssessmentManifest
```

## Parent elements



| Element                                            | Description                                                     |
|----------------------------------------------------|-----------------------------------------------------------------|
| [**AxeJobManfest**](axejobmanifest.md)<br/> | Name of the root node of the assessment.<br/> <br/> |



## Remarks

The ordering of assessment manifests is not important and no dependencies should be taken by tools on the ordering.

This data can be indexed using the [**AssessmentId**](assessmentid.md) from the assessment.

When a Job manifest is fixed the assessment management object model will marshal the entire assessment manifest into the job manifest. Each [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288) will be marshaled under this **AssessmentManifests**.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





