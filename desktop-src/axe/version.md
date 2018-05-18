---
title: Version element
description: The version node has four mandatory sub nodes making up a standard Microsoft four part version number.
ms.assetid: '1d07d13e-cc49-40d3-a323-803d56ab2fb7'
keywords: ["Version element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Version
api_type:
- Schema
---

# Version element

The version node has four mandatory sub nodes making up a standard Microsoft four part version number.

## Usage

``` syntax
<Version>
  child elements
</Version>
```

## Attributes

There are no attributes.

## Child elements



| Element                                 | Description                                                           |
|-----------------------------------------|-----------------------------------------------------------------------|
| [**Build**](build.md)<br/>       | Build part of standard version number.<br/> <br/>         |
| [**Major**](major.md)<br/>       | Major version part of standard version number.<br/> <br/> |
| [**Minor**](minor.md)<br/>       | Minor version part of standard version number.<br/> <br/> |
| [**Revision**](revision.md)<br/> | Revision part of standard version number.<br/> <br/>      |



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



| Element                                       | Description                                                           |
|-----------------------------------------------|-----------------------------------------------------------------------|
| [**AppVersion**](appversion.md)<br/>   | Contains the application name and version.<br/> <br/>     |
| [**VersionedId**](versionedid.md)<br/> | The unique identity of a job or an assessment.<br/> <br/> |



## Remarks

AXE never changes a job's version number. The AXE assessment management object model provides a read/write version property to the solution. This lets the solution mange the version numbers for jobs.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





