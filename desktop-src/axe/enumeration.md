---
title: Enumeration element
description: Describes an enumeration.
ms.assetid: 29235302-74F9-47D9-A465-090921948BB1
keywords:
- Enumeration element Access Execution Engine
topic_type:
- apiref
api_name:
- Enumeration
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumeration element

Describes an enumeration.

## Usage

``` syntax
<Enumeration>
  child elements
</Enumeration>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                                                                                                                                                                                                  |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Name**](name.md)<br/>                         | A human-readable name for the item.<br/> <br/>                                                                                                                                                                                   |
| [**ProgrammaticName**](programmaticname.md)<br/> | This is the programmatic name of the parameter or metric.<br/> <br/>                                                                                                                                                             |
| [**Value**](value.md)<br/>                       | Must contain an integer value (positive, zero or negative) that corresponds to the enumerated value. These values do not need to be contiguous. Each enumeration value must be unique in for a particular parameter. <br/> <br/> |



### Child element sequence

``` syntax
(
  ProgrammaticName, 
  Name, 
  Value
)
```

## Parent elements



| Element                                         | Description                                                       |
|-------------------------------------------------|-------------------------------------------------------------------|
| [**Enumerations**](enumerations.md)<br/> | Contains one or more **Enumeration** tags.<br/> <br/> |



## Examples

This node describes an enumeration as follows.

``` syntax
<Enumeration>
<ProgrammaticName></ProgrammaticName>
<Name></Name>
<Value></Value>
</Enumeration> 
```

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





