---
Description: 'Includes the definition of one or more custom diagnostic tests, and it serves as the root element for the diagnostic test definition XML file.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '81211a17-01d6-4717-9071-2709edfb7126'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: DiagnosticTests element
---

# DiagnosticTests element

Includes the definition of one or more custom diagnostic tests, and it serves as the root element for the diagnostic test definition XML file.

## Usage

``` syntax
<DiagnosticTests>
  child elements
</DiagnosticTests>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                     | Description                                                                                                                                    |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiagnosticTest**](diagnostictest-element.md)<br/> | Defines a custom diagnostic test, including the metadata, parameters, environment variables, and commands for the test.<br/> <br/> |



### Child element sequence

``` syntax
DiagnosticTest+
```

## Parent elements

There are no parent elements.

## Element information



|              |                     |
|--------------|---------------------|
| Schema file  | DiagnosticTests.xsd |
| Can be empty | No                  |



## See also

<dl> <dt>

[Diagnostic Test Definition Elements](diagnostic-test-definition-elements.md)
</dt> </dl>

 

 




