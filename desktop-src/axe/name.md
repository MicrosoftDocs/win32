---
title: Name element
description: A human-readable name for the item.
ms.assetid: '56b0a3ae-e226-4840-8f85-0d2ee6165fd0'
keywords: ["Name element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Name
api_type:
- Schema
---

# Name element

A human-readable name for the item.

## Usage

``` syntax
<Name>
  text
</Name>
```

## Attributes

There are no attributes.

## Text value

A valid NTFS name. A name suitable for a file or directory name. A human-readable name. File name of the assessment run.

## Child elements

There are no child elements.

## Parent elements



| Element                                           | Description                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------|
| [**AssessmentRun**](assessmentrun.md)<br/> | Defines the instance of an assessment for execution.<br/> <br/> |
| [**Description**](description.md)<br/>     | Provides a human-readable description.<br/> <br/>               |
| [**Flag**](flag.md)<br/>                   | Describes a flag.<br/> <br/>                                    |



## Remarks

The Name value of an assessment run is set by a user using a solution.

The Name cannot be used as the assessments identity because the value of Name can be localized.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





