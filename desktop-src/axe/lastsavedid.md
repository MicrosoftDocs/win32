---
title: LastSavedId element
description: When AXE saves a job, it gives it a LastSavedId.
ms.assetid: 3DC635F1-BBE2-4A06-AC1E-69C97408471E
keywords:
- LastSavedId element Access Execution Engine
topic_type:
- apiref
api_name:
- LastSavedId
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LastSavedId element

When AXE saves a job, it gives it a **LastSavedId**.

## Usage

``` syntax
<LastSavedId>
  text
</LastSavedId>
```

## Attributes

There are no attributes.

## Text value

The new identity. This is a GUID in the registry format. If AXE saves the assessment, AXE ensures this tag exists and is populated with a non-empty GUID.

## Child elements

There are no child elements.

## Parent elements



| Element                                     | Description                                               |
|---------------------------------------------|-----------------------------------------------------------|
| [**Properties**](properties.md)<br/> | This element describes properties.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





