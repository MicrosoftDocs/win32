---
title: EarliestStartTime element
description: Earliest start time and date for the job in Coordinated Universal Time (UTC).
ms.assetid: '8F0F4F02-C6D9-44F5-856F-FB448417A473'
keywords: ["EarliestStartTime element Access Execution Engine"]
topic_type:
- apiref
api_name:
- EarliestStartTime
api_type:
- Schema
---

# EarliestStartTime element

Earliest start time and date for the job in Coordinated Universal Time (UTC).

## Usage

``` syntax
<EarliestStartTime>
  text
</EarliestStartTime>
```

## Attributes

There are no attributes.

## Text value

Earliest start time and date for the job in Coordinated Universal Time (UTC). There is not guarantee that AXE will start the job exactly at this time. AXE will not start the job before this time and date.

## Child elements

There are no child elements.

## Parent elements



| Element                                           | Description                                                                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**JobParameters**](jobparameters.md)<br/> | Describes the parameters for a job. These parameters control how a job runs, and can be read by an assessment.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





