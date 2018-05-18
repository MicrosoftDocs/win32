---
Description: 'Represents an environment variable that you want to set for a diagnostic test or set for a step in a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9a849c55-7ee9-42bd-a7ee-a7e111ffdcc9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Variable element
---

# Variable element

Represents an environment variable that you want to set for a diagnostic test or set for a step in a diagnostic test.

## Usage

``` syntax
<Variable
  Name = "character_string"
  Value = "character_string"/>
```

## Attributes



| Attribute            | Type                         | Required       | Description                                                                                                                                                                                                                                  |
|----------------------|------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Name**<br/>  | character\_string<br/> | Yes<br/> | Specifies the name of an environment variable that you want to set for a diagnostic test or set for a step in a diagnostic test.<br/> The maximum length of the environment variable name is 255 characters.<br/> <br/>    |
| **Value**<br/> | character\_string<br/> | No<br/>  | Specifies the value that you want to set for an environment variable for a diagnostic test or set for a step in a diagnostic test.<br/> The maximum length of the environment variable value is 255 characters.<br/> <br/> |



## Child elements

There are no child elements.

## Parent elements



| Element                                                                                  | Description                                                                                                                                                     |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnvironmentVariables**](environmentvariables--diagnostictest--element.md)<br/> | Represents a set of one or more environment variables that you want to set for a diagnostic test or set for a step in a diagnostic test.<br/> <br/> |



## Remarks

If the parent [**EnvironmentVariables**](environmentvariables--diagnostictest--element.md) element for the **Variable** element is the child of the [**PreStep**](prestep-element.md), [**RunStep**](runstep-element.md), or [**PostStep**](poststep-element.md) element, the environment variable is set only for the corresponding phase of the diagnostic test.

If the parent [**EnvironmentVariables**](environmentvariables--diagnostictest--element.md) element for the **Variable** element is the child of the [**DiagnosticTest**](diagnostictest-element.md) element, the environment variable is set globally for the entire diagnostic test.

To unset an environment variable, specify the **Name** attribute without a **Value** attribute, or specify an empty string for the **Value** attribute, for example:


```XML
<Variable Name="Variable1"/>
<Variable Name="Variable2" Value=""/>
```



You cannot specify multiple **Variable** elements that have the same value for the **Name** attribute in the definition of a single diagnostic test.

## Element information



|              |                     |
|--------------|---------------------|
| Schema file  | DiagnosticTests.xsd |
| Can be empty | Yes                 |



## See also

<dl> <dt>

[**EnvironmentVariables**](environmentvariables--diagnostictest--element.md)
</dt> </dl>

 

 




