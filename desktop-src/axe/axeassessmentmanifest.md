---
title: AxeAssessmentManifest element
description: This is the root node of an assessment manifest.
ms.assetid: '4BEDABF7-5D79-4BB3-8E2F-8B37545D305F'
keywords: ["AxeAssessmentManifest element Access Execution Engine"]
topic_type:
- apiref
api_name:
- AxeAssessmentManifest
api_type:
- Schema
---

# AxeAssessmentManifest element

This is the root node of an assessment manifest.

## Usage

``` syntax
<AxeAssessmentManifest>
  child elements
</AxeAssessmentManifest>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                                   | Description                                                                                                         |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**Description**](description.md)<br/>                             | Describes an assessment manifest.<br/> <br/>                                                            |
| [**Execution**](execution.md)<br/>                                 | This node describes how AXE executes an assessment.<br/> <br/>                                          |
| [**LocalizedStringDictionary**](localizedstringdictionary.md)<br/> | The localized strings that should be displayed in a UI for localized nodes in the manifest. <br/> <br/> |
| [**MetricDefinitions**](metricdefinitions.md)<br/>                 | This element contains a collection of [**MetricDefinition**](metricdefinition.md) elements.<br/> <br/> |
| [**MetricThresholds**](metricthresholds.md)<br/>                   | Contains one or more metric thresholds.<br/> <br/>                                                      |
| [**MinimumAxeVersionRequired**](minimumaxeversionrequired.md)<br/> | Describes the minimum AXE version required.<br/> <br/>                                                  |
| [**ParameterDefinitions**](parameterdefinitions.md)<br/>           | A collection of [**ParameterDefinition**](parameterdefinition.md) elements.<br/> <br/>                 |
| [**PresentationHints**](presentationhints.md)<br/>                 | The root node of the presentation hints section.<br/> <br/>                                             |
| [**Properties**](properties.md)<br/>                               | This element describes assessment properties.<br/> <br/>                                                |
| [**VersionedId**](versionedid.md)<br/>                             | The unique identity of a job or an assessment.<br/> <br/>                                               |



### Child element sequence

``` syntax
(
  VersionedId, 
  MinimumAxeVersionRequired, 
  Description, 
  Properties, 
  ParameterDefinitions, 
  MetricDefinitions, 
  PresentationHints, 
  MetricThresholds, 
  Execution, 
  LocalizedStringDictionary
)
```

## Parent elements

There are no parent elements.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





