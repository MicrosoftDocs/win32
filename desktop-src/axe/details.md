---
title: Details element
description: Information about the analysis job, including start time, duration, and location of the log files.
ms.assetid: '9ACCAAB4-6100-4BC4-B8E9-04BC200FB37A'
keywords: ["Details element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Details
api_type:
- Schema
---

# Details element

Information about the analysis job, including start time, duration, and location of the log files.

## Usage

``` syntax
<Details>
  child elements
</Details>
```

## Attributes

There are no attributes.

## Child elements



| Element                    | Description                                                          |
|----------------------------|----------------------------------------------------------------------|
| Duration<br/>        | The length of time that the analysis job ran.<br/> <br/> |
| SessionLogFiles<br/> | Location of the log files for the analysis.<br/> <br/>   |
| Start<br/>           | The date and time when analysis began.<br/> <br/>        |



### Child element sequence

``` syntax
StartDurationSessionLogFiles
```

## Parent elements

There are no parent elements.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





