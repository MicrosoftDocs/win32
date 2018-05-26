---
title: ParameterDefinition element
description: Information that fully describes an assessment parameter.
ms.assetid: BD6F2A7B-0A32-4D71-9655-F88F3FCBB78F
keywords:
- ParameterDefinition element Access Execution Engine
topic_type:
- apiref
api_name:
- ParameterDefinition
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ParameterDefinition element

Information that fully describes an assessment parameter.

## Usage

``` syntax
<ParameterDefinition>
  child elements
</ParameterDefinition>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                   | Description                                                                                             |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**BenchmarkValue**](benchmarkvalue.md)<br/>       | Contains a benchmark value.<br/> <br/>                                                      |
| [**CommandLineFormat**](commandlineformat.md)<br/> | Describes how a parameter is formatted for the assessment command line.<br/> <br/>          |
| [**Constraints**](constraints.md)<br/>             | Constraints specified for a parameter's value.<br/> <br/>                                   |
| [**DefaultValue**](defaultvalue.md)<br/>           | Contains a default value for the parameter. <br/> <br/>                                     |
| [**Description**](description.md)<br/>             | Provides a human-readable description about a manifest or metric.<br/> <br/>                |
| [**Enumerations**](enumerations.md)<br/>           | Contains one or more [**Enumeration**](enumeration.md) elements.<br/> <br/>                |
| [**Flags**](flags.md)<br/>                         | Contains one or more [**Flag**](flag.md) elements.<br/> <br/>                              |
| [**Inclusion**](https://msdn.microsoft.com/library/windows/desktop/hh437683)<br/>                 | Describes a value.<br/> <br/>                                                               |
| [**PresentWith**](presentwith.md)<br/>             | Describes other parameters that must be present for this parameter to be valid. <br/> <br/> |
| [**StandardType**](https://msdn.microsoft.com/library/windows/desktop/hh449610)<br/>                   | Describes the data type of an item.<br/> <br/>                                              |



### Child element sequence

``` syntax
(
  Description, 
  StandardType, 
  Inclusion, 
  DefaultValue, 
  BenchmarkValue, 
  Enumerations, 
  Flags, 
  PresentWith, 
  Constraints, 
  CommandLineFormat
)
```

## Parent elements



| Element                                                         | Description                                                                                 |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**ParameterDefinitions**](parameterdefinitions.md)<br/> | This element holds a collection of **ParameterDefinition** elements.<br/> <br/> |



## Remarks

A parameter definition is the meta information that fully describes an assessment parameter. This information is used by AXE solutions (UX or scripts) to add, validate and otherwise manipulate parameter values.

Note that parameter definitions are separate from parameter values. Definitions are static and defined by an assessment author when an assessment is authored. Values are defined by a user (or script) using an AXE solution. Solutions can be any program that uses the AXE API s to create and run jobs. This includes UX based tools and PowerShell scripts.

The order of **ParameterDefinition** elements in the [**ParameterDefinitions**](parameterdefinitions.md) elements is significant. AXE assessment authoring tools should maintain the order. The order determines how a assessment s command line is formatted (if there is one). Parameters should be put on the assessment command line in the same order as in **ParameterDefinitions**. This means each parameter has an implicit zero based index based on its position in the **ParameterDefinitions** collection.

Each of the **ParameterDefinition** nodes in the [**ParameterDefinitions**](parameterdefinitions.md) collection must each have a unique programmatic name.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





