---
title: LogFile element
description: This is the file name of a log or trace file produced by the assessment. It is an absolute path to the file.
ms.assetid: e2146b74-9914-436b-a339-8778e162bedc
keywords:
- LogFile element Access Execution Engine
topic_type:
- apiref
api_name:
- LogFile
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LogFile element

This is the file name of a log or trace file produced by the assessment. It is an absolute path to the file.

## Usage

``` syntax
<LogFile>
  text
</LogFile>
```

## Attributes

There are no attributes.

## Text value

An absolute path to a directory containing any log files associated with this assessment.

## Child elements

There are no child elements.

## Parent elements



| Element                                 | Description                                                           |
|-----------------------------------------|-----------------------------------------------------------------------|
| [**LogFiles**](logfiles.md)<br/> | A container node to hold **LogFile** elements.<br/> <br/> |



## Remarks

The path comes from the job. This is a temporary location where the assessment places it s files. The AXE execution engine will package these up and place them in a cabinet file in a location defined by the job.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





