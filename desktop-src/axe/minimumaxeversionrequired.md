---
title: MinimumAxeVersionRequired element
description: Describes the minimum AXE version required.
ms.assetid: '29F199F9-6FF2-46E5-8B2F-BA101073BA43'
keywords: ["MinimumAxeVersionRequired element Access Execution Engine"]
topic_type:
- apiref
api_name:
- MinimumAxeVersionRequired
api_type:
- Schema
---

# MinimumAxeVersionRequired element

Describes the minimum AXE version required. Created and maintained by the AXE assessment management object model.

## Usage

``` syntax
<MinimumAxeVersionRequired>
  child elements
</MinimumAxeVersionRequired>
```

## Attributes

There are no attributes.

## Child elements



| Element                               | Description                                                                                               |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**Version**](version.md)<br/> | Four mandatory sub nodes making up a standard Microsoft four part version number. <br/> <br/> |



### Child element sequence

``` syntax
Version
```

## Parent elements



| Element                                                     | Description                                                     |
|-------------------------------------------------------------|-----------------------------------------------------------------|
| [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288)<br/> | The root node of the assessment.<br/> <br/>         |
| [**AxeJobManifest**](axejobmanifest.md)<br/>         | Name of the root node of the assessment.<br/> <br/> |



## Remarks

A newly created job has a version number of 1.0.0.0.

Note that this element implicitly versions the assessment manifest schema. The value for this element is determined by the code that writes the XML manifest. This information cannot be set by the user or author of the assessment.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





