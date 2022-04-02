---
title: Application element
description: Represents the top-level element in the Windows Ribbon framework markup specification.
ms.assetid: 05396d8b-fbd1-40bb-8d0f-8ac11506e7db
keywords:
- Application element Windows Ribbon
topic_type:
- apiref
api_name:
- Application
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Application element

Represents the top-level element in the Windows Ribbon framework markup specification.

## Usage

``` syntax
<Application
  xmlns = "xs:string">
  child elements
</Application>
```

## Attributes



| Attribute            | Type                 | Required       | Description                                                                                                                                                                                                       |
|----------------------|----------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **xmlns**<br/> | xs:string<br/> | Yes<br/> | <dt>`http://schemas.microsoft.com/windows/2009/Ribbon`<br/> </dt> <dd> The URI for the Ribbon markup namespace binding. <br/> </dd> </dl> |



## Child elements



| Element                                                                               | Description                                    |
|---------------------------------------------------------------------------------------|------------------------------------------------|
| [**Application.Commands**](windowsribbon-element-application-commands.md)<br/> | May occur at most once<br/> <br/>  |
| [**Application.Views**](windowsribbon-element-application-views.md)<br/>       | Must occur exactly once<br/> <br/> |



## Parent elements

There are no parent elements.

## Remarks

Required.

Must occur exactly once as the container for all of the Ribbon markup.

The child elements of the **Application** element must occur in the specified order:

1.  [**Application.Commands**](windowsribbon-element-application-commands.md)
2.  [**Application.Views**](windowsribbon-element-application-views.md)

## Examples

The following example shows an **Application** element declaration.


```XML
<Application xmlns="http://schemas.microsoft.com/windows/2009/Ribbon">
...
</Application>
```



## Element information



|     Requirement                                |   Details        |
|-------------------------------------|-----------|
| Minimum supported system<br/> | Windows 7 |
| Can be empty                        | No        |



## See also

<dl> <dt>

[Declaring Commands and Controls with Ribbon Markup](windowsribbon-schema.md)
</dt> </dl>

 

 





