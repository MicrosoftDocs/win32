---
title: Image element
description: A UNC path to an offline image.
ms.assetid: 993A6E73-F76F-4848-B72A-C7DB3E72A979
keywords:
- Image element Access Execution Engine
topic_type:
- apiref
api_name:
- Image
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Image element

A UNC path to an offline image.

## Usage

``` syntax
<Image>
  text
</Image>
```

## Attributes

There are no attributes.

## Text value

A relative or absolute UNC path to an offline image. If the path is relative, the solution should ensure that the path is relative to the current directory at the time the job is run. AXE processes this path using **ExpandEnvironmentStringsW**.

## Child elements

There are no child elements.

## Parent elements



| Element                                           | Description                                               |
|---------------------------------------------------|-----------------------------------------------------------|
| [**JobParameters**](jobparameters.md)<br/> | Describes the parameters of a job.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





