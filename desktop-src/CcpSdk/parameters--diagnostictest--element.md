---
Description: 'Defines a set of one or more parameters for a stage in the diagnostic test or for the entire diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b7fa93bb-9c63-442b-b36d-8dac4ee6a169'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Parameters element
---

# Parameters element

Defines a set of one or more parameters for a stage in the diagnostic test or for the entire diagnostic test.

## Usage

``` syntax
<Parameters>
  child elements
</Parameters>
```

## Attributes

There are no attributes.

## Child elements



| Element                                           | Description                                                                                                       |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [**Parameter**](parameter-element.md)<br/> | Defines a parameter for a stage in the diagnostic test or for the entire diagnostic test. <br/> <br/> |



### Child element sequence

``` syntax
Parameter+
```

## Parent elements



| Element                                                     | Description                                                                                                                                                                                              |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiagnosticTest**](diagnostictest-element.md)<br/> | Defines a custom diagnostic test, including the metadata, parameters, environment variables, and commands for the test.<br/> <br/>                                                           |
| [**PostStep**](poststep-element.md)<br/>             | Defines the PostStep stage of a custom diagnostic test. The PostStep stage processes the output from all of the nodes on which the test ran and prepares the results for display.<br/> <br/> |
| [**PreStep**](prestep-element.md)<br/>               | Defines the PreStep stage of a custom diagnostic test. The PreStep stage performs validation and prepares the environment for running the test.<br/> <br/>                                   |
| [**RunStep**](runstep-element.md)<br/>               | Defines the RunStep stage of a custom diagnostic test. The RunStep stage runs the actual diagnostic test.<br/> <br/>                                                                         |



## Remarks

This element can apply to an entire diagnostic test or to a specific stage in a diagnostic test.

When the **Parameters** element is a child of the [**DiagnosticTest**](diagnostictest-element.md) element, the set of parameters that the **Parameters** element defines applies to the entire test. When the **Parameters** element is a child of the [**PreStep**](prestep-element.md), [**RunStep**](runstep-element.md), or [**PostStep**](poststep-element.md) element, the set of parameters that the **Parameters** element defines applies only to the stage that corresponds to the element that is the parent of the **Parameters** element.

## Element information



|              |                     |
|--------------|---------------------|
| Schema file  | DiagnosticTests.xsd |
| Can be empty | No                  |



## See also

<dl> <dt>

[**DiagnosticTest**](diagnostictest-element.md)
</dt> <dt>

[**PreStep**](prestep-element.md)
</dt> <dt>

[**RunStep**](runstep-element.md)
</dt> <dt>

[**PostStep**](poststep-element.md)
</dt> </dl>

 

 




