---
Description: 'Represents a set of one or more environment variables that you want to set for a diagnostic test or set for a step in a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3cc0da84-93b7-47b1-ab2f-5e477e2a0e8f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: EnvironmentVariables element
---

# EnvironmentVariables element

Represents a set of one or more environment variables that you want to set for a diagnostic test or set for a step in a diagnostic test.

## Usage

``` syntax
<EnvironmentVariables>
  child elements
</EnvironmentVariables>
```

## Attributes

There are no attributes.

## Child elements



| Element                                         | Description                                                                                                                                  |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**Variable**](variable-element.md)<br/> | Represents an environment variable that you want to set for a diagnostic test or set for a step in a diagnostic test.<br/> <br/> |



### Child element sequence

``` syntax
Variable+
```

## Parent elements



| Element                                                     | Description                                                                                                                                                                                              |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiagnosticTest**](diagnostictest-element.md)<br/> | Defines a custom diagnostic test, including the metadata, parameters, environment variables, and commands for the test.<br/> <br/>                                                           |
| [**PostStep**](poststep-element.md)<br/>             | Defines the PostStep stage of a custom diagnostic test. The PostStep stage processes the output from all of the nodes on which the test ran and prepares the results for display.<br/> <br/> |
| [**PreStep**](prestep-element.md)<br/>               | Defines the PreStep stage of a custom diagnostic test The PreStep stage performs validation and prepares the environment for running the test.<br/> <br/>                                    |
| [**RunStep**](runstep-element.md)<br/>               | Defines the RunStep stage of a custom diagnostic test. The RunStep stage runs the actual diagnostic test.<br/> <br/>                                                                         |



## Remarks

This element can apply to an entire diagnostic test or to a specific stage in a diagnostic test.

When the **EnvironmentVariables** element is a child of the [**DiagnosticTest**](diagnostictest-element.md) element, the **EnvironmentVariables** element sets the environment variables for the entire test. When the **EnvironmentVariables** element is a child of the [**PreStep**](prestep-element.md), [**RunStep**](runstep-element.md), or [**PostStep**](poststep-element.md) element, the **EnvironmentVariables** element sets the environment variables only for the stage that corresponds to the parent element of the **EnvironmentVariables** element.

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

 

 




