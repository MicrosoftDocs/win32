---
title: VersionedId element
description: The unique identity of a job or an assessment.
ms.assetid: '4D2D521F-AD6B-4CD0-9B1B-69B5614CAB32'
keywords: ["VersionedId element Access Execution Engine"]
topic_type:
- apiref
api_name:
- VersionedId
api_type:
- Schema
---

# VersionedId element

The unique identity of a job or an assessment. The identity uses a GUID and standard version number.

## Usage

``` syntax
<VersionedId>
  child elements
</VersionedId>
```

## Attributes

There are no attributes.

## Child elements



| Element                               | Description                                                                                                                                                                                                                                                                                                   |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Guid**](guid.md)<br/>       | A GUID representing the unique identity. The GUID must be in the registry format and the open and close braces are required.<br/> <br/>                                                                                                                                                           |
| [**Version**](version.md)<br/> | A standard four part version number. The version node contains four mandatory sub nodes making up a standard Microsoft four part version number. AXE makes no assumptions about the meaning of each field. Version numbers must all be simple integers equal to or greater than zero. <br/> <br/> |



### Child element sequence

``` syntax
(
  Guid, 
  Version
)
```

## Parent elements



| Element                                                           | Description                                                             |
|-------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288)<br/>       | The root node of the assessment.<br/> <br/>                 |
| [**AxeAssessmentManifest**](axeassessmentmanifest.md)<br/> | This is the root node of an assessment manifest.<br/> <br/> |
| [**AxeJobManifest**](axejobmanifest.md)<br/>               | Name of the root node of the assessment.<br/> <br/>         |



## Remarks

The **VersionedId** element should always be at the top of the file in the first node after the document node so that the Id can be determined by a streaming XML reader early in the reading process.

AXE compares versions as either the same, or different and does not use a greater (or later) than relationship between assessments.

## Examples

The following example demonstrates this element.


```XML
<VersionedId>
    <Guid>{73F635A4-0F2A-44e1-A7B7-927A17088561}</Guid>
    <Version>
        <Major>1</Major>
        <Minor>1</Minor>
        <Build>1</Build>
        <Revision>1</Revision>
    </Version>
</VersionedId>
```



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

 

 





