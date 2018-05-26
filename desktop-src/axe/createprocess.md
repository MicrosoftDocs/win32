---
title: CreateProcess element
description: AXE supports the CreateProcess method. AXE uses the fundamental create process API to specify an executable and a command line for that executable. This would also include an optional current directory.
ms.assetid: 13986B46-651C-4E53-9052-FEC5E2ABF904
keywords:
- CreateProcess element Access Execution Engine
topic_type:
- apiref
api_name:
- CreateProcess
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CreateProcess element

AXE supports the CreateProcess method. AXE uses the fundamental create process API to specify an executable and a command line for that executable. This would also include an optional current directory.

## Usage

``` syntax
<CreateProcess>
  child elements
</CreateProcess>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                                                                                          |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**ApplicationName**](applicationname.md)<br/>   | This is the file path and name to the assessment s executable.<br/> <br/>                                                |
| [**CreateNewConsole**](createnewconsole.md)<br/> | The present of this tag causes AXE to set the CREATE\_NEW\_CONSOLE flag in the call to CreateProcess.<br/> <br/>         |
| [**CreateNoWindow**](createnowindow.md)<br/>     | The presence of this tag causes AXE to set the CREATE\_NO\_WINDOW flag in the call to CreateProcess.<br/> <br/>          |
| [**DetachedProcess**](detachedprocess.md)<br/>   | The presence of this tag causes AXE to set the DETACHED\_PROCESS flag in the call to CreateProcess.<br/> <br/>           |
| [**RequiresUIAccess**](requiresuiaccess.md)<br/> | The presence of this tag indicates that the assessment requires UI access in order to manipulate UI elements.<br/> <br/> |



### Child element sequence

``` syntax
(
  ApplicationName, 
  CreateNewConsole, 
  CreateNoWindow, 
  DetachedProcess, 
  RequiresUIAccess
)
```

## Parent elements



| Element                                   | Description                                                                 |
|-------------------------------------------|-----------------------------------------------------------------------------|
| [**Execution**](execution.md)<br/> | This node describes how AXE executes an assessment. <br/> <br/> |



## Remarks

This tag specifies that AXE uses the Win32 API CreateProcessW() to run the assessment. This node requires the following sub nodes. Note that AXE only calls the UNICODE (wide) version of this API.

Here, AXE determines the command line as documented in the AXE Assessment Assembly Design document.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





