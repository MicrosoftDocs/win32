---
title: ParameterValue element
description: Describes a single assessment parameter.
ms.assetid: 646A8269-0C4A-4211-B20D-1FCBC6EBD9CD
keywords:
- ParameterValue element Access Execution Engine
topic_type:
- apiref
api_name:
- ParameterValue
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ParameterValue element

Describes a single assessment parameter.

## Usage

``` syntax
<ParameterValue>
  child elements
</ParameterValue>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                            |
|---------------------------------------------------------|------------------------------------------------------------------------|
| [**ProgrammaticName**](programmaticname.md)<br/> | This is the programmatic name of the parameter.<br/> <br/> |
| [**Value**](value.md)<br/>                       | Contains the value for the parameter.<br/> <br/>           |



### Child element sequence

``` syntax
(
  ProgrammaticName, 
  Value
)
```

## Parent elements



| Element                                               | Description                                                               |
|-------------------------------------------------------|---------------------------------------------------------------------------|
| [**ParameterValues**](parametervalues.md)<br/> | Contains zero or more **ParameterValue** elements.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





