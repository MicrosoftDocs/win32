---
Description: 'The following table describes the XML elements that you can use to define a custom diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '51130a89-bf11-44de-b0ac-144752675270'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Diagnostic Test Definition Elements
---

# Diagnostic Test Definition Elements

The following table describes the XML elements that you can use to define a custom diagnostic test.



| Element                                                                       | Description                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AutoGenerateResult**](autogenerateresult.md)<br/>                   | Designates the custom diagnostic test as a test that validates whether the result of the test matches an expected value or if it is consistent for all nodes in the HPC cluster. It also indicates that the diagnostic service should automatically generate a report for the test that is appropriate for these types of tests.<br/> |
| [**DiagnosticTest**](diagnostictest-element.md)<br/>                   | Defines a custom diagnostic test, including the metadata, parameters, environment variables, and commands for the test.<br/>                                                                                                                                                                                                          |
| [**DiagnosticTests**](diagnostictests-element.md)<br/>                 | Includes the definition of one or more custom diagnostic tests, and it serves as the root element for the diagnostic test definition XML file.<br/>                                                                                                                                                                                   |
| [**EnvironmentVariables**](environmentvariables--diagnostictest--element.md) | Represents a set of one or more environment variables that you want to set for a diagnostic test or set for a step in a diagnostic test.<br/>                                                                                                                                                                                         |
| [**Parameter**](parameter-element.md)<br/>                             | Defines a parameter for a stage in the diagnostic test or for the entire diagnostic test. <br/>                                                                                                                                                                                                                                       |
| [**Parameters**](parameters--diagnostictest--element.md)<br/>          | Defines a set of one or more parameters for a stage in the diagnostic test or for the entire diagnostic test. <br/>                                                                                                                                                                                                                   |
| [**PostStep**](poststep-element.md)<br/>                               | Defines the PostStep stage of a custom diagnostic test. The PostStep stage processes the output from all of the nodes on which the test ran and prepares the results for display.<br/>                                                                                                                                                |
| [**PreStep**](prestep-element.md)<br/>                                 | Defines the PreStep stage of a custom diagnostic test. The PreStep stage performs validation and prepares the environment for running the test.<br/>                                                                                                                                                                                  |
| [**RunStep**](runstep-element.md)<br/>                                 | Defines the RunStep stage of a custom diagnostic test. The RunStep stage runs the actual diagnostic test.<br/>                                                                                                                                                                                                                        |
| [**Variable**](variable-element.md)<br/>                               | Represents an environment variable that you want to set for a diagnostic test or set for a step in a diagnostic test. <br/>                                                                                                                                                                                                           |



 

## Related topics

<dl> <dt>

[Diagnostic Test Definition Schema](diagnostic-test-definition-schema.md)
</dt> </dl>

 

 




