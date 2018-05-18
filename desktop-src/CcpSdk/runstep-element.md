---
Description: 'Defines the RunStep stage of a custom diagnostic test. The RunStep stage runs the actual diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '46fed3de-4273-43cd-84f6-f4bcaf5a3274'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: RunStep element
---

# RunStep element

Defines the RunStep stage of a custom diagnostic test. The RunStep stage runs the actual diagnostic test.

## Usage

``` syntax
<RunStep
  Command = "character_string"
  ResultXml = "boolean">
  child elements
</RunStep>
```

## Attributes



| Attribute                | Type                         | Required       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------|------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Command**<br/>   | character\_string<br/> | Yes<br/> | Specifies the command line for the command or application that you want to run for the RunStep stage of the test. <br/> You can specify any command or application that you can run from a command prompt. Possible commands include command-line commands, command files or batch files, instances of Windows PowerShell, and compiled console applications.<br/> If the command that you want to specify includes quotation marks (such as a command that includes a path with spaces) or other special characters in XML, use character entities to specify the characters, for example, `&quot;`. For more information about character entities, see [Character and Entity References](http://go.microsoft.com/fwlink/p/?linkid=165386) (http://go.microsoft.com/fwlink/p/?linkid=165386).<br/> The maximum length of the command line is 255 characters.<br/> <br/> |
| **ResultXml**<br/> | boolean<br/>           | No<br/>  | Indicates whether the result of the test for the node depends on StepResult XML content that the RunStep command sends to standard output, for tests that do not specify a [**PostStep**](poststep-element.md) or [**AutoGenerateResult**](autogenerateresult.md) element.<br/> **True** indicates that the RunStep command on each node sends StepResult XML to standard output and that the result of the test for each node depends on that output. **False** indicates that the result of the test for the node depends on the result of the task for the node in the **clusrun** job for the RunStep stage.<br/> <br/>                                                                                                                                                                                                                                                        |



## Child elements



| Element                                                                                  | Description                                                                                                                                     |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnvironmentVariables**](environmentvariables--diagnostictest--element.md)<br/> | Represents a set of one or more environment variables that you want to set for the RunStep stage of the diagnostic test.<br/> <br/> |
| [**Parameters**](parameters--diagnostictest--element.md)<br/>                     | Defines a set of one or more parameters for the RunStep stage in the diagnostic test.<br/> <br/>                                    |



### Child element sequence

``` syntax
Parameters?EnvironmentVariables?
```

## Parent elements



| Element                                                     | Description                                                                                                                                     |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiagnosticTest**](diagnostictest-element.md)<br/> | Defines a custom diagnostic test, including the metadata, parameters, environment variables, and commands for the test. <br/> <br/> |



## Remarks

The RunStep stage of a diagnostic test runs once on each of the nodes in the list of nodes in the output of the PreStep stage. A RunStep element is required in the test definition of a test that runs a command, and the RunStep element is not allowed in the test definition of a test that runs a job.

## Element information



|              |                     |
|--------------|---------------------|
| Schema file  | DiagnosticTests.xsd |
| Can be empty | Yes                 |



## See also

<dl> <dt>

[**DiagnosticTest**](diagnostictest-element.md)
</dt> <dt>

[**PreStep**](prestep-element.md)
</dt> <dt>

[**PostStep**](poststep-element.md)
</dt> </dl>

 

 




