---
title: ApplicationName element
description: This is the file path and name to the assessment s executable.
ms.assetid: CCB88FFA-15C2-4B46-9C92-49BE23CADD8B
keywords:
- ApplicationName element Access Execution Engine
topic_type:
- apiref
api_name:
- ApplicationName
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ApplicationName element

This is the file path and name to the assessment s executable.

## Usage

``` syntax
<ApplicationName>
  text
</ApplicationName>
```

## Attributes

There are no attributes.

## Text value

This may be any valid UNC path. AXE will call the Win32 API ExpandEnvironmentStringsW() until no more expansions occur.

## Child elements

There are no child elements.

## Parent elements



| Element                                           | Description                                                                                                                          |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateProcess**](createprocess.md)<br/> | AXE uses the fundamental create process API to specify an executable and a command line for that executable. <br/> <br/> |



## Examples

Note that AXE does not modify the Windows environment   an assessment inherits the same environment inherited by the process hosting AXE. This lets the assessment author using strings like these:

``` syntax
%WINDIR%\System32\WinSAT.EXE
    .\%PROCESSOR_ARCHITECTURE%\Assessment.exe
```

Calling ExpandEnvironmentStringsW() three times lets the assessment author nest expansions three levels deep. This is a relatively common thing to do. Note that AXE only calls the UNICODE (wide) version of this API.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





