---
Description: 'Defines the PreStep stage of a custom diagnostic test, The PreStep stage performs validation and prepares the environment for running the test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '97f6fe7e-9471-46d4-8d35-d0d89a89c180'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: PreStep element
---

# PreStep element

Defines the PreStep stage of a custom diagnostic test, The PreStep stage performs validation and prepares the environment for running the test.

## Usage

``` syntax
<PreStep
  Command = "character_string"
  ResultXml = "boolean">
  child elements
</PreStep>
```

## Attributes



| Attribute                | Type                         | Required       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------|------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Command**<br/>   | character\_string<br/> | Yes<br/> | Specifies the command line for the command or application that you want to run for the PreStep stage of the test. <br/> You can specify any command or application that you can run from a command prompt, if performs the tasks described in [Diagnostic Test Stages](diagnostic-test-phases.md). Possible commands include command-line commands, command files or batch files, instances of Windows PowerShell, and compiled console applications.<br/> If the command that you want to specify includes quotation marks (such as a command that includes a path with spaces) or other special characters in XML, use character entities to specify the characters, for example, `&quot;`. For more information about character entities, see [Character and Entity References](http://go.microsoft.com/fwlink/p/?linkid=165386) (http://go.microsoft.com/fwlink/p/?linkid=165386).<br/> The maximum length of the command line is 255 characters.<br/> <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **ResultXml**<br/> | boolean<br/>           | No<br/>  | Indicates whether the test generates a PreStepResult.xml file in the working directory on the head node.<br/> **True** indicates that test generates a PreStepResult.xml file that the diagnostic service should use to obtain the results of the stage. This file can specify a node list that overrides the list of nodes the user specified when the user started the test. This file also specifies custom parameters for the RunStep stage of the test. If the PreStepResult.xml file contains an empty [**Nodes**](nodes-element.md) element, the test fails. If the PreStepResult.xml file does not contains a **Nodes** element, the RunStep stage runs on the nodes that the user specified when the user started the test.<br/> **False** indicates that the diagnostic service should not use the information in the PreStepResult.xml file, and that the diagnostic service should check the last line of standard output of the PreStep command for a node list, rather than check the PreStep.xml file. If the last line of standard output has a format of Nodes: *Node1*, *Node2*,..., the diagnostic service runs the RunStep stage on the nodes in that list. If the last line does not start with **Nodes**, the RunStep stage runs on the nodes that the user specified when the user started the test. If the last line starts with **Nodes** but does not specify any nodes, the test fails. <br/> <br/> |



## Child elements



| Element                                                                                  | Description                                                                                                                                     |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnvironmentVariables**](environmentvariables--diagnostictest--element.md)<br/> | Represents a set of one or more environment variables that you want to set for the PreStep stage of the diagnostic test.<br/> <br/> |
| [**Parameter**](parameter-element.md)<br/>                                        | Defines a set of one or more parameters for the PreStep stage in the diagnostic test.<br/> <br/>                                    |



### Child element sequence

``` syntax
Parameter?EnvironmentVariables?
```

## Parent elements



| Element                                                     | Description                                                                                                                                     |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiagnosticTest**](diagnostictest-element.md)<br/> | Defines a custom diagnostic test, including the metadata, parameters, environment variables, and commands for the test. <br/> <br/> |



## Remarks

The PreStep stage of a diagnostic test runs only on the head node. A **PreStep** element is required in the test definition for a diagnostic test that runs a job.

## Element information



|              |                     |
|--------------|---------------------|
| Schema file  | DiagnosticTests.xsd |
| Can be empty | Yes                 |



## See also

<dl> <dt>

[**DiagnosticTest**](diagnostictest-element.md)
</dt> <dt>

[**RunStep**](runstep-element.md)
</dt> <dt>

[**PostStep**](poststep-element.md)
</dt> </dl>

 

 




