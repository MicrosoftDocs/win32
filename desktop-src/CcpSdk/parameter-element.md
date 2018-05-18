---
Description: 'Defines a parameter for a stage in the diagnostic test or for the entire diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a8f0cd58-e560-4d18-8c9f-192f04208f48'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Parameter element
---

# Parameter element

Defines a parameter for a stage in the diagnostic test or for the entire diagnostic test.

## Usage

``` syntax
<Parameter
  Name = "character_string"
  SwitchName = "character_string"
  Description = "character_string"
  Type = "enumeration"
  DefaultValue = "character_string"
  MinimumValue = "int"
  MaximumValue = "int"
  Visibility = "boolean"
  Value = "character_string"
  AllowedValues = "character_string"
  Format = "character_string"
  UseOnlyInStep = "character_string"/>
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
<td><strong>AllowedValues</strong><br/></td>
<td>character_string<br/></td>
<td>No<br/></td>
<td>Specifies a list of values that are allowed for the parameter, which are separated by commas (,). The user can choose a value from this list in the <strong>Run Diagnostic Tests</strong> dialog box when the user runs the test in <strong>HPC Cluster Manager</strong>.<br/> You can only specify this attribute when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>DiagnosticTest</strong>](diagnostictest-element.md) element. You cannot specify a value for this attribute when the <strong>Parameters</strong> element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element.<br/> The maximum length for the complete list of allowed values is 2000 characters.<br/> <br/></td>
</tr>
<tr class="even">
<td><strong>DefaultValue</strong><br/></td>
<td>character_string<br/></td>
<td>No<br/></td>
<td>Specifies a default value to use for the parameter if the user does not specify a value when the user runs the test.<br/> This attribute is required when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>DiagnosticTest</strong>](diagnostictest-element.md) element. You cannot specify a value for this attribute when the <strong>Parameters</strong> element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element.<br/> The maximum length of the default value is 255 characters.<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>Description</strong><br/></td>
<td>character_string<br/></td>
<td>No<br/></td>
<td>Specifies a description for the parameter. The <strong>Run Diagnostic Tests</strong> dialog box displays the description for the parameter when the user runs the test in <strong>HPC Cluster Manager</strong>.<br/> You can only specify this attribute when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>DiagnosticTest</strong>](diagnostictest-element.md) element. You cannot specify a value for this attribute when the <strong>Parameters</strong> element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element.<br/> The maximum length of the description is 255 characters.<br/> <br/></td>
</tr>
<tr class="even">
<td><strong>Format</strong><br/></td>
<td>character_string<br/></td>
<td>No<br/></td>
<td>Specifies the format that the <strong>Command</strong> attribute for the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element should use for the parameter and its value. For this format string, {0} represents the switch name and {1} represents the value that the user specified for the parameter.<br/> The default value for this attribute is -{0}:{1}. The maximum length for the format string is 64 characters.<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>MaximumValue</strong><br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>Specifies the maximum value that is allowed for the parameter. You can only specify this attribute if the <strong>Type</strong> attribute has a value of Integer.<br/> You can only specify this attribute when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>DiagnosticTest</strong>](diagnostictest-element.md) element. You cannot specify a value for this attribute when the <strong>Parameters</strong> element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element.<br/> <br/></td>
</tr>
<tr class="even">
<td><strong>MinimumValue</strong><br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>Specifies the minimum value that is allowed for the parameter. You can only specify this attribute if the <strong>Type</strong> attribute has a value of Integer.<br/> You can only specify this attribute when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>DiagnosticTest</strong>](diagnostictest-element.md) element. You cannot specify a value for this attribute when the <strong>Parameters</strong> element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element.<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>Name</strong><br/></td>
<td>character_string<br/></td>
<td>Yes<br/></td>
<td>Specifies the name that the <strong>Run Diagnostic Tests</strong> dialog box displays for the parameter when the user runs the test in <strong>HPC Cluster Manager</strong>.<br/> The maximum length of the parameter name is 64 characters.<br/> <br/></td>
</tr>
<tr class="even">
<td><strong>SwitchName</strong><br/></td>
<td>character_string<br/></td>
<td>No<br/></td>
<td>Specifies the name to use for the parameter when the parameter is used in a command for the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), and [<strong>PostStep</strong>](poststep-element.md) elements.<br/> You can specify this attribute only for global parameters (that is, you can only specify this attribute when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>DiagnosticTest</strong>](diagnostictest-element.md) element). If you do not specify this attribute for a global parameter, the value of the <strong>Name</strong> attribute is used for the <strong>SwitchName</strong> attribute.<br/> If you define a parameter for a specific stage of the diagnostic test by including the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element as a child of the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element, the value of the <strong>Name</strong> attribute is automatically used for the switch name. You cannot specify a value for the <strong>SwitchName</strong> attribute when the <strong>Parameters</strong> element that is the parent of this <strong>Parameter</strong> element is a child of the <strong>PreStep</strong>, <strong>RunStep</strong>, or <strong>PostStep</strong> element.<br/> The maximum length of the switch name is 64 characters.<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>Type</strong><br/></td>
<td>enumeration<br/></td>
<td>Yes<br/></td>
<td>Specifies the data type for the parameter.<br/> This attribute is required when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>DiagnosticTest</strong>](diagnostictest-element.md) element. You cannot specify a value for this attribute when the <strong>Parameters</strong> element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element.<br/> The <strong>Type</strong> attribute can have one of the following values:<br/> <br/>
<dt><span id="String"></span><span id="string"></span><span id="STRING"></span><span id="String"></span><span id="string"></span><span id="STRING"></span><strong><strong>String</strong></strong><br/> </dt> <dd> The value for the parameter is a string of characters.<br/> </dd> <dt><span id="Boolean"></span><span id="boolean"></span><span id="BOOLEAN"></span><span id="Boolean"></span><span id="boolean"></span><span id="BOOLEAN"></span><strong><strong>Boolean</strong></strong><br/> </dt> <dd> The value for the parameter is a Boolean value. It can be <strong>True</strong> or <strong>False</strong>.<br/> </dd> <dt><span id="Integer"></span><span id="integer"></span><span id="INTEGER"></span><span id="Integer"></span><span id="integer"></span><span id="INTEGER"></span><strong><strong>Integer</strong></strong><br/> </dt> <dd> The value for the parameter is an integer.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>UseOnlyInStep</strong><br/></td>
<td>character_string<br/></td>
<td>No<br/></td>
<td>Specifies the stages for which the diagnostic service should include the parameter in the command.<br/> The possible values are PreStep, RunStep, PostStep, or any comma-separated list of two or three of these values. The default value of PreStep,RunStep,PostStep specifies all three stages.<br/> The <strong>Parameter</strong> element for the parameter that specifies the expected value for a comparison test often uses this attribute to prevent the diagnostic service from including the parameter in the commands for the PreStep and RunStep stages. In these circumstances, use a value of PostStep for the <strong>UseOnlyInStep</strong> attribute.<br/> You can only specify this attribute when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>DiagnosticTest</strong>](diagnostictest-element.md) element. You cannot specify a value for this attribute when the <strong>Parameters</strong> element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element.<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>Value</strong><br/></td>
<td>character_string<br/></td>
<td>No<br/></td>
<td>Specifies the value to use for the parameter.<br/> This attribute only applies and is required when the parameter is specific to a test stage. In other words, this attribute only applies and is required when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element.<br/> You cannot set a value for this attribute for a global, visible parameter. In other words, you cannot set this attribute when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>DiagnosticTest</strong>](diagnostictest-element.md) element.<br/> The maximum length of the value is 255 characters.<br/> <br/></td>
</tr>
<tr class="even">
<td><strong>Visibility</strong><br/></td>
<td>boolean<br/></td>
<td>No<br/></td>
<td>Indicates whether the user can see and set the parameter.<br/> A <strong>True</strong> value indicates that the user can see and set the parameter. A <strong>false</strong> value indicates that the user cannot see or set the parameter, and that the parameter can only be used by the test developer.<br/> This attribute only applies when the parameter is a global parameter (that is, when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>DiagnosticTest</strong>](diagnostictest-element.md) element).<br/> For a parameter that you define for a specific stage of the diagnostic test, the visibility is automatically <strong>false</strong> and cannot be set. In other words, the visibility is automatically <strong>false</strong> when the [<strong>Parameters</strong>](parameters--diagnostictest--element.md) element that is the parent of this <strong>Parameter</strong> element is a child of the [<strong>PreStep</strong>](prestep-element.md), [<strong>RunStep</strong>](runstep-element.md), or [<strong>PostStep</strong>](poststep-element.md) element.<br/> <br/></td>
</tr>
</tbody>
</table>



## Child elements

There are no child elements.

## Parent elements



| Element                                                              | Description                                                                                                                          |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**Parameters**](parameters--diagnostictest--element.md)<br/> | Defines a set of one or more parameters for a stage in the diagnostic test or for the entire diagnostic test.<br/> <br/> |



## Remarks

This element can apply to an entire diagnostic test or to a specific stage in a diagnostic test.

When the [**Parameters**](parameters--diagnostictest--element.md) element that is the parent of this **Parameter** element is a child of the [**DiagnosticTest**](diagnostictest-element.md) element, the parameter applies to the entire test. When the **Parameters** element that is the parent of this **Parameter** element is a child of the [**PreStep**](prestep-element.md), [**RunStep**](runstep-element.md), or [**PostStep**](poststep-element.md) element, the parameter applies only to the stage that corresponds to the element that is the parent of the **Parameters** element.

When the [**Parameters**](parameters--diagnostictest--element.md) element that is the parent of this **Parameter** element is a child of the [**PreStep**](prestep-element.md), [**RunStep**](runstep-element.md), or [**PostStep**](poststep-element.md) element, the diagnostic service applies only the values of the **Name**, **Value**, and **Format** attributes, and it ignores the remaining attributes.

A parameter that applies to a specific stage of a diagnostic test cannot be set by the user, and that parameter can only be used by the developer of the test.

If the value of a parameter includes spaces, the diagnostic service automatically encloses the value in quotation marks (") when adding it to the commands for the stages of the diagnostic test.

## Element information



|              |                     |
|--------------|---------------------|
| Schema file  | DiagnosticTests.xsd |
| Can be empty | Yes                 |



## See also

<dl> <dt>

[**Parameters**](parameters--diagnostictest--element.md)
</dt> </dl>

 

 




