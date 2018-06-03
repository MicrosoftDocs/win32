---
title: PostExecutionAction element
description: After a job has completed, AXE may optionally run a program.
ms.assetid: 70A42E94-0401-4081-BC70-A62B3D4B3E48
keywords:
- PostExecutionAction element Access Execution Engine
topic_type:
- apiref
api_name:
- PostExecutionAction
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PostExecutionAction element

After a job has completed, AXE may optionally run a program.

## Usage

``` syntax
<PostExecutionAction>
  text
</PostExecutionAction>
```

## Attributes

There are no attributes.

## Text value

Defines the operation using the same XML sub-schema as the [**Execution**](execution.md) element in the [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288). AXE processes the command text using **ExpandEnvironmentStringsW** until no more expansions occur.

## Child elements

There are no child elements.

## Parent elements



| Element                                           | Description                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------|
| [**JobParameters**](jobparameters.md)<br/> | This node describes the parameters for a job. <br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





