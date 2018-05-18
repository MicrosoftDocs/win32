---
Description: 'Designates the custom diagnostic test as a test that validates whether the result of the test matches an expected value or if it is consistent for all nodes in the HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '11a8046e-ed23-4a42-8edb-795428f1876c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: AutoGenerateResult element
---

# AutoGenerateResult element

Designates the custom diagnostic test as a test that validates whether the result of the test matches an expected value or if it is consistent for all nodes in the HPC cluster. It also indicates that the diagnostic service should automatically generate a report for the test that is appropriate for these types of tests.

## Usage

``` syntax
<AutoGenerateResult
  TestType = "enumeration"
  ExpectedValue = "character_string"/>
```

## Attributes



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ExpectedValue</strong><br/></td>
<td>character_string<br/></td>
<td>No<br/></td>
<td>Specifies the name of the global parameter that contains the value that the results of the test should match, when the value of the <strong>TestType</strong> attribute is Comparison.<br/> This attribute is required if the value of the <strong>TestType</strong> attribute is Comparison. If the value of the <strong>TestType</strong> attribute is Consistency, the <strong>ExpectedValue</strong> attribute is ignored.<br/> The definition for the parameter that the <strong>ExpectedValue</strong> attribute names cannot contain a value for the <strong>Format</strong> attribute of the [<strong>Parameter</strong>](parameter-element.md) element unless that value is the default value of -{0}:{1}.<br/> <br/></td>
</tr>
<tr class="even">
<td><strong>TestType</strong><br/></td>
<td>enumeration<br/></td>
<td>Yes<br/></td>
<td>Specifies the type of the diagnostic test and the kind of report that the test should generate. This attribute can have one of the following values:<br/> <br/>
<dt>Consistency</dt> <dd> The diagnostic test checks that the results of the RunStep stage of the test are identical for all of the nodes that the user runs the test on. The test succeeds if all of the results are identical, and the test fails if any of the results differ from one another.<br/> The diagnostic service automatically generates a report for the test that indicates whether the results were identical, and the report lists the output of test for each node.<br/> </dd> <dt>Comparison</dt> <dd> The diagnostic test checks that the results of the RunStep stage for each node in the test match the value that the user supplied for the global parameter that is named by the <strong>ExpectedValue</strong> attribute. The test succeeds if the results for all of the nodes match the expected value, and the test fails if the result for any of the nodes differs from the expected value.<br/> The diagnostic service automatically generates a report for the test that indicates whether the results for all of the nodes matched the expected value, and the report lists the output of test for each node.<br/> </dd> </dl></td>
</tr>
</tbody>
</table>



## Child elements

There are no child elements.

## Parent elements



| Element                                                     | Description                                                                                                                                    |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiagnosticTest**](diagnostictest-element.md)<br/> | Defines a custom diagnostic test, including the metadata, parameters, environment variables, and commands for the test.<br/> <br/> |



## Remarks

You can include the **AutoGenerateResult** element or the [**PostStep**](poststep-element.md) element in the XML file that define a custom diagnostic test, but do not include both elements. If the definition of the test includes a **PostStep** element, the **AutoGenerateResult** element is ignored.

## Element information



|              |                     |
|--------------|---------------------|
| Schema file  | DiagnosticTests.xsd |
| Can be empty | Yes                 |



## See also

<dl> <dt>

[**DiagnosticTest**](diagnostictest-element.md)
</dt> </dl>

 

 




