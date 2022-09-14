---
description: Describes a namespace.
ms.assetid: 8e31526a-639f-481b-91f1-fcd376818cbf
title: nameSpace element
ms.topic: reference
ms.date: 05/31/2018
---

# nameSpace element

Describes a namespace. This namespace may be used for code generation or for handling \<wsdl:import> directives.

## Usage

``` syntax
<nameSpace
  uri = "character_string">
  child elements
</nameSpace>
```

## Attributes



| Attribute          | Type                         | Required       | Description                                             |
|--------------------|------------------------------|----------------|---------------------------------------------------------|
| **uri**<br/> | character\_string<br/> | Yes<br/> | The unique URI of the namespace.<br/> <br/> |



## Child elements



| Element                                               | Description                                                                                              |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**codeName**](codename.md)<br/>               | The name to be used to identify the namespace in generated code.<br/> <br/>                  |
| [**macroPrefix**](macroprefix.md)<br/>         | The prefix to be used in the generated code for names of macros in the namespace.<br/> <br/> |
| [**name**](name.md)<br/>                       | A qualified name in the namespace.<br/> <br/>                                                |
| [**preferredPrefix**](preferredprefix.md)<br/> | The prefix to which the namespace should be mapped to make the XML more readable.<br/> <br/> |



### Child element sequence

``` syntax
(
  preferredPrefix?, 
  macroPrefix?, 
  codeName?, 
  name*
)
```

## Parent elements



| Element                                     | Description                                                                          |
|---------------------------------------------|--------------------------------------------------------------------------------------|
| [**wsdCodeGen**](wsdcodegen.md)<br/> | The root element of an WSDAPI code generator XML script file.<br/> <br/> |



## Remarks

This element may be used to provide the code generator with additional information about namespaces that it encounters in WSDL and XSD files or to introduce new namespaces.

Namespaces implied by type reflection or specified in WSDL and XSD files are parsed automatically by the code generator and do not have to be explicitly defined in the script. In some cases, this element can be used to add additional properties or names to a namespace that is referenced by type reflection or WSDL/XSD. The code generator does not regard this as a conflict.

The following XML shows a nameSpace element (with children omitted for brevity).

``` syntax
<nameSpace uri="https://www.example.com/namespace">
  ...
</nameSpace>
```

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




