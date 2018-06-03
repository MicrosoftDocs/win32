---
title: Execution element
description: This node describes how AXE executes an assessment.
ms.assetid: 2B29D5E4-B61F-4F4B-85C4-6630B9AFD19E
keywords:
- Execution element Access Execution Engine
topic_type:
- apiref
api_name:
- Execution
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Execution element

This node describes how AXE executes an assessment.

## Usage

``` syntax
<Execution>
  child elements
</Execution>
```

## Attributes

There are no attributes.

## Child elements



| Element                                           | Description                                                                                                                                                                                                                                                 |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateProcess**](createprocess.md)<br/> | AXE supports the [**CreateProcess**](createprocess.md) method. AXE uses the fundamental create process API to specify an executable and a command line for that executable. This would also include an optional current directory. <br/> <br/> |
| [**ShellExecute**](shellexecute.md)<br/>   | AXE supports the ShellExecute method. Here we would use the shell (explorer.exe) to launch a process. The parameters are an operation (verb), file to operate on, command line parameters, and a directory. <br/> <br/>                         |



### Child element sequence

``` syntax
(
  CreateProcess, 
  ShellExecute
)
```

## Parent elements



| Element                                                           | Description                                                             |
|-------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288)<br/>       | The root node of the assessment.<br/> <br/>                 |
| [**AxeAssessmentManifest**](axeassessmentmanifest.md)<br/> | This is the root node of an assessment manifest.<br/> <br/> |



## Remarks

Note that this node is marked as optional, but it is somewhat of a special case. When an assessment authoring tool saves an assessment manifest, the user may not have completed the manifest. This means that this node must be optional. However, this node is required so that the AXE engine knows how to execute the assessment. So, the AXE object model enforces this by not letting an assessment be added to a job that is missing this information.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





