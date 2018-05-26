---
title: ShellExecuteFile element
description: The name of the file or object on which shell execute will perform the action specified by the verb parameter.
ms.assetid: 1719E056-5163-47D7-AA17-9CE42AC8643B
keywords:
- ShellExecuteFile element Access Execution Engine
topic_type:
- apiref
api_name:
- ShellExecuteFile
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ShellExecuteFile element

The name of the file or object on which shell execute will perform the action specified by the verb parameter.

## Usage

``` syntax
<ShellExecuteFile>
  text
</ShellExecuteFile>
```

## Attributes

There are no attributes.

## Text value

Name of the file or object on which shell execute will perform the action specified by the verb parameter.

## Child elements

There are no child elements.

## Parent elements



| Element                                         |
|-------------------------------------------------|
| [**ShellExecute**](shellexecute.md)<br/> |



## Remarks

This tag must specifies the name of the file or object on which shell execute will perform the action specified by the verb parameter. As with CreateProcess() AXE will call the Win32 API ExpandEnvironmentStringsW() on this value until no more expansions occur.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





