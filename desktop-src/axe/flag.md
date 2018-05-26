---
title: Flag element
description: Describes a flag.
ms.assetid: C80BC963-8F45-4BEE-9724-A826C941A7AE
keywords:
- Flag element Access Execution Engine
topic_type:
- apiref
api_name:
- Flag
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Flag element

Describes a flag.

## Usage

``` syntax
<Flag>
  child elements
</Flag>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                                                                                                                                                                                                                      |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Name**](name.md)<br/>                         | Has the same semantics as that for the overall parameter s name. This name can be localized.<br/> <br/>                                                                                                                                              |
| [**ProgrammaticName**](programmaticname.md)<br/> | This is the non-localized name of the parameter. This is to be used only programmatically and never shown to a user.<br/> <br/>                                                                                                                      |
| [**Value**](value.md)<br/>                       | The flag's value. The value must be an integer from 1 to 32 and corresponds to the bit positions in of **Int32** value. The values do not need to be contiguous. Each enumeration value must be unique in for this particular parameter. <br/> <br/> |



### Child element sequence

``` syntax
(
  ProgrammaticName, 
  Name, 
  Value
)
```

## Parent elements



| Element                           | Description                                                    |
|-----------------------------------|----------------------------------------------------------------|
| [**Flags**](flags.md)<br/> | Contains one or more **Flag** elements.<br/> <br/> |



## Examples

This node describes a flag as follows.

``` syntax
<Flag>
    <ProgrammaticName></ProgrammaticName>
<Name></Name>
<Value></Value>
</Flag> 
```

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





