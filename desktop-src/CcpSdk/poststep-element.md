---
Description: 'Defines the PostStep stage of a custom diagnostic test. The PostStep stage processes the output from all of the nodes on which the test ran and prepares the results for display.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '27c9c102-7997-4ea6-bcc8-62f22a7d5de0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: PostStep element
---

# PostStep element

Defines the PostStep stage of a custom diagnostic test. The PostStep stage processes the output from all of the nodes on which the test ran and prepares the results for display.

## Usage

``` syntax
<PostStep Element
  Command = "character_string"
  ResultXml = "boolean">
  child elements
</PostStep Element>
```

## Attributes



| Attribute                | Type                         | Required       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------|------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Command**<br/>   | character\_string<br/> | Yes<br/> | Specifies the command line for the command or application that you want to run for the PostStep stage of the test. <br/> You can specify any command or application that you can run from a command prompt, if it performs the tasks that are described in [Diagnostic Test Stages](diagnostic-test-phases.md). Possible commands include command-line commands, command files or batch files, instances of Windows PowerShell, and compiled console applications.<br/> If the command that you want to specify includes quotation marks (such as a command that includes a path with spaces) or other special characters in XML, use character entities to specify the characters, for example, `&quot;`. For more information about character entities, see [Character and Entity References](http://go.microsoft.com/fwlink/p/?linkid=165386) (http://go.microsoft.com/fwlink/p/?linkid=165386).<br/> The maximum length of the command line is 255 characters.<br/> <br/> |
| **ResultXml**<br/> | boolean<br/>           | No<br/>  | Indicates whether the diagnostic service reads the PostStepResult.xml file to get information about the results of the test. **True** indicates that the diagnostic service reads the PostStepResult.xml file to get information about the results of the test. **False** indicates that the diagnostic service does not read the PostStepResult.xml file to get information about the results of the test.<br/> <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |



## Child elements



| Element                                                                                  | Description                                                                                                                                      |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnvironmentVariables**](environmentvariables--diagnostictest--element.md)<br/> | Represents a set of one or more environment variables that you want to set for the PostStep stage of the diagnostic test.<br/> <br/> |
| [**Parameters**](parameters--diagnostictest--element.md)<br/>                     | Defines a set of one or more parameters for the PostStep stage in the diagnostic test.<br/> <br/>                                    |



### Child element sequence

``` syntax
Parameters?EnvironmentVariables?
```

## Parent elements



| Element                                                     | Description                                                                                                                                     |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiagnosticTest**](diagnostictest-element.md)<br/> | Defines a custom diagnostic test, including the metadata, parameters, environment variables, and commands for the test. <br/> <br/> |



## Remarks

The PostStep stage of a diagnostic test runs only on the head node.

If you include the [**AutoGenerateResult**](autogenerateresult.md) element in the definition of a custom diagnostic test, the test report is automatically generated and you do not need to implement a PostStep stage for the test. You can include the **AutoGenerateResult** element or the **PostStep** element in the XML file that defines a custom diagnostic test, but you cannot include both elements.

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

[**RunStep**](runstep-element.md)
</dt> </dl>

 

 




