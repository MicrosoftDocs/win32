---
title: ShellExecute element
description: AXE supports the ShellExecute method. Here we would use the shell (explorer.exe) to launch a process. The parameters are an operation (verb), file to operate on, command line parameters, and a directory.
ms.assetid: 0D98F410-C826-49AE-9FD3-D8A6C6A64829
keywords:
- ShellExecute element Access Execution Engine
topic_type:
- apiref
api_name:
- ShellExecute
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ShellExecute element

AXE supports the ShellExecute method. Here we would use the shell (explorer.exe) to launch a process. The parameters are an operation (verb), file to operate on, command line parameters, and a directory.

## Usage

``` syntax
<ShellExecute>
  child elements
</ShellExecute>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                                                                                                                    |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ShellExecuteFile**](shellexecutefile.md)<br/> | This tag must specifies the name of the file or object on which shell execute will perform the action specified by the verb parameter. <br/> <br/> |
| [**ShellExecuteVerb**](shellexecuteverb.md)<br/> | This tag must contain a verb as described by the documentation for the shell execute API.<br/> <br/>                                               |



### Child element sequence

``` syntax
(
  ShellExecuteVerb, 
  ShellExecuteFile
)
```

## Parent elements



| Element                                   | Description                                                                 |
|-------------------------------------------|-----------------------------------------------------------------------------|
| [**Execution**](execution.md)<br/> | This node describes how AXE executes an assessment. <br/> <br/> |



## Remarks

This node s presence is exclusive from &lt;CreateProcess&gt; and &lt;PowerShell&gt;.

This tag specifies that AXE uses the Win32 API ShellExecuteEx() to run the assessment. This node requires the following sub nodes. Note that AXE only calls the UNICODE (wide) version of this API.

Here, AXE determines the command line as documented in the AXE Assessment Assembly Design document.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





