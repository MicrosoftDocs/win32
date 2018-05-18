---
Description: 'Defines a custom diagnostic test, including the metadata, parameters, environment variables, and commands for the test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a3866cab-f6bd-461f-a57e-0211dc7d2f2d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: DiagnosticTest element
---

# DiagnosticTest element

Defines a custom diagnostic test, including the metadata, parameters, environment variables, and commands for the test.

## Usage

``` syntax
<DiagnosticTest
  Name = "character_string"
  Description = "character_string"
  Suite = "character_string"
  Company = "character_string"
  Alias = "character_string"
  Version = "character_string">
  child elements
</DiagnosticTest>
```

## Attributes



| Attribute                  | Type                         | Required       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------|------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Alias**<br/>       | character\_string<br/> | Yes<br/> | Specifies a short name for the diagnostic test that users can use as an alias in **HPC PowerShell** cmdlets. The alias also appears in the list of diagnostic tests in **HPC Cluster Manager** in **Diagnostics**.<br/> The maximum length of the alias is 64 characters.<br/> <br/>                                                                                                                                                                                                                                                                                      |
| **Company**<br/>     | character\_string<br/> | Yes<br/> | Specifies the name of the company that developed the diagnostic test. The **Tests** hierarchy in **Navigation Pane** in **Diagnostics** in **HPC Cluster Manager** groups tests by company, then by suite. <br/> The combination of the **Company** and **Name** attributes uniquely identifies a custom diagnostic test. <br/> This attribute cannot have a value equal to System, because that value is reserved for the built-in tests that Windows HPC Server 2008 R2 provides.<br/> The maximum length of the company name is 128 characters.<br/> <br/> |
| **Description**<br/> | character\_string<br/> | No<br/>  | Specifies a description for the diagnostic test. The description appears in the list of diagnostic tests in **HPC Cluster Manager** in **Diagnostics**.<br/> The maximum length of the description is 255 characters.<br/> <br/>                                                                                                                                                                                                                                                                                                                                          |
| **Name**<br/>        | character\_string<br/> | Yes<br/> | Specifies the full name of the diagnostic test. The maximum length of the name is 255 characters.<br/> The combination of the **Company** and **Name** attributes uniquely identifies a custom diagnostic test. <br/> <br/>                                                                                                                                                                                                                                                                                                                                               |
| **Suite**<br/>       | character\_string<br/> | Yes<br/> | Specifies the suite of diagnostic tests in which this test should be included. The **Tests** hierarchy in **Navigation Pane** in **Diagnostics** in **HPC Cluster Manager** groups tests by company, then by suite. <br/> The maximum length of the suite name is 128 characters.<br/> <br/>                                                                                                                                                                                                                                                                              |
| **Version**<br/>     | character\_string<br/> | No<br/>  | Specifies the version of the test. The maximum length of the version string is 64 characters.<br/> <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |



## Child elements



| Element                                                                                  | Description                                                                                                                                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AutoGenerateResult**](autogenerateresult.md)<br/>                              | Designates the custom diagnostic test as a test that validates whether the result of the test matches an expected value or if it is consistent for all nodes in the HPC cluster. It also indicates that the diagnostic service should automatically generate a report for the test that is appropriate for these types of tests.<br/> <br/> |
| [**EnvironmentVariables**](environmentvariables--diagnostictest--element.md)<br/> | Represents a set of one or more environment variables that you want to set for the entire diagnostic test.<br/> <br/>                                                                                                                                                                                                                       |
| [**Parameters**](parameters--diagnostictest--element.md)<br/>                     | Defines a set of one or more parameters for the entire diagnostic test. <br/> <br/>                                                                                                                                                                                                                                                         |
| [**PostStep**](poststep-element.md)<br/>                                          | Defines the PostStep stage of a custom diagnostic test. The PostStep stage processes the output from all of the nodes on which the test ran and prepares the results for display.<br/> <br/>                                                                                                                                                |
| [**PreStep**](prestep-element.md)<br/>                                            | Defines the PreStep stage of a custom diagnostic test. The PreStep stage performs validation and prepares the environment for running the test.<br/> <br/>                                                                                                                                                                                  |
| [**RunStep**](runstep-element.md)<br/>                                            | Defines the RunStep stage of a custom diagnostic test. The RunStep stage runs the actual diagnostic test.<br/> <br/>                                                                                                                                                                                                                        |



### Child element sequence

``` syntax
Parameters*EnvironmentVariables*PreStep?RunStep?(
  AutoGenerateResult? | PostStep?
)
```

## Parent elements



| Element                                                       | Description                                                                                                                                                           |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiagnosticTests**](diagnostictests-element.md)<br/> | Includes the definition of one or more custom diagnostic tests, and it serves as the root element for the diagnostic test definition XML file.<br/> <br/> |



## Remarks

The **DiagnosticTest** element must contain a [**PreStep**](prestep-element.md) element, [**RunStep**](runstep-element.md) element, or both.

All of the values of the attributes for the **DiagnosticTest** element are case-insensitive.

## Element information



|              |                     |
|--------------|---------------------|
| Schema file  | DiagnosticTests.xsd |
| Can be empty | Yes                 |



## See also

<dl> <dt>

[**DiagnosticTests**](diagnostictests-element.md)
</dt> </dl>

 

 




