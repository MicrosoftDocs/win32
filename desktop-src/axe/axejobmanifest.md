---
title: AxeJobManifest element
description: Name of the root node of the assessment.
ms.assetid: 640D2692-5E6B-48A2-9C93-CA2D8112CB79
keywords:
- AxeJobManifest element Access Execution Engine
topic_type:
- apiref
api_name:
- AxeJobManifest
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AxeJobManifest element

Name of the root node of the assessment.

## Usage

``` syntax
<AxeJobManifest>
  child elements
</AxeJobManifest>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                                   | Description                                                             |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**Guid**](guid.md)<br/>                                           | Unique identity represented by a GUID.<br/> <br/>           |
| [**MinimumAxeVersionRequired**](minimumaxeversionrequired.md)<br/> | Describes the minimum AXE version required.<br/> <br/>      |
| [**VersionedId**](versionedid.md)<br/>                             | Unique identity of a job represented by a GUID. <br/> <br/> |



### Child element sequence

``` syntax
(
  VersionedId, 
  Guid, 
  MinimumAxeVersionRequired
)
```

## Parent elements

There are no parent elements.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





