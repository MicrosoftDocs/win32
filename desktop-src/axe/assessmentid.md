---
title: AssessmentId element
description: This is the identity of the assessment.
ms.assetid: '5774CBFD-221B-4FFA-890D-E169A7841B69'
keywords: ["AssessmentId element Access Execution Engine"]
topic_type:
- apiref
api_name:
- AssessmentId
api_type:
- Schema
---

# AssessmentId element

This is the identity of the assessment. This data is used to lookup the assessment manifest data in the [**AssessmentManifests**](assessmentmanifests.md)collection in a job manifest.

## Usage

``` syntax
<AssessmentId>
  child elements
</AssessmentId>
```

## Attributes

There are no attributes.

## Child elements



| Element                               | Description                                                                                                                                              |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Guid**](guid.md)<br/>       | A GUID representing an unique assessment identity.<br/> <br/>                                                                                |
| [**Version**](version.md)<br/> | A standard version number. The version node has four mandatory sub nodes making up a standard Microsoft four part version number.<br/> <br/> |



### Child element sequence

``` syntax
(
  Guid, 
  Version
)
```

## Parent elements



| Element                                           | Description                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------|
| [**AssessmentRun**](assessmentrun.md)<br/> | Defines the instance of an assessment for execution.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





