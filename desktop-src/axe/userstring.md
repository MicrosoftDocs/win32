---
title: UserString element
description: A string provided by a solution.
ms.assetid: 71311648-6BD1-40EF-9941-E7C0901F4C07
keywords:
- UserString element Access Execution Engine
topic_type:
- apiref
api_name:
- UserString
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UserString element

A string provided by a solution.

## Usage

``` syntax
<UserString>
  text
</UserString>
```

## Attributes

There are no attributes.

## Text value

A string provided by the solution. AXE ignores this value and merely persists and restores it from a job manifest. Its length is determined by the solution.

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

 

 





