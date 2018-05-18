---
title: VerifyOSVersion element
description: This node describes the minimum Windows version required for this assessment.
ms.assetid: '104B7A46-0D5D-4466-B2E6-0183BD5D851E'
keywords: ["VerifyOSVersion element Access Execution Engine"]
topic_type:
- apiref
api_name:
- VerifyOSVersion
api_type:
- Schema
---

# VerifyOSVersion element

This node describes the minimum Windows version required for this assessment.

## Usage

``` syntax
<VerifyOSVersion>
  child elements
</VerifyOSVersion>
```

## Attributes

There are no attributes.

## Child elements



| Element                                 | Description              |
|-----------------------------------------|--------------------------|
| [**Build**](build.md)<br/>       | 0<br/> <br/> |
| [**Major**](major.md)<br/>       | 6<br/> <br/> |
| [**Minor**](minor.md)<br/>       | 1<br/> <br/> |
| [**Revision**](revision.md)<br/> | 0<br/> <br/> |



### Child element sequence

``` syntax
(
  Major, 
  Minor, 
  Build, 
  Revision
)
```

## Parent elements



| Element                                     | Description                                            |
|---------------------------------------------|--------------------------------------------------------|
| [**Properties**](properties.md)<br/> | This node describes properties.<br/> <br/> |



## Remarks

AXE will issue a warning if a job is configured with assessments that do not all support the same minimum OS version.

## Examples

**VerifyOSVersion** describes the minimum Windows version required for this assessment and has the following mandatory sub-nodes:

``` syntax
<Version> 
  <Major>6</Major>
  <Minor>1</Minor>
  <Build>0</Build>
  <Revision>0</Revision>
</Version> 
```

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





