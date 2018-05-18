---
title: MetricDefinition element
description: Describes the metrics produced by an assessment.
ms.assetid: '1C466422-63EE-49D4-B927-D612C74661A6'
keywords: ["MetricDefinition element Access Execution Engine"]
topic_type:
- apiref
api_name:
- MetricDefinition
api_type:
- Schema
---

# MetricDefinition element

Describes the metrics produced by an assessment.

## Usage

``` syntax
<MetricDefinition>
  child elements
</MetricDefinition>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                     | Description                                                                                                                                 |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**BetterDirection**](betterdirection.md)<br/>       | This node describes the direction that is “better”. For some metrics this is “higher” for others it is lower.<br/> <br/>        |
| [**DecimalPlaces**](decimalplaces.md)<br/>           | The number of decimal places to retain for the metric.<br/> <br/>                                                               |
| [**Description**](description.md)<br/>               | This node contains the description of the assessment. <br/> <br/>                                                               |
| [**Importance**](importance.md)<br/>                 | The importance of the activity. <br/> <br/>                                                                                     |
| [**Ordinal**](ordinal--metricdefinition-.md)<br/>    | Ordinal of this **MetricDefinition** within [**MetricDefinitions**](metricdefinitions.md).<br/> <br/>                          |
| [**PrimaryStatistic**](primarystatistic.md)<br/>     | This node describes the primary descriptive statistic the assessment author recommends for describing the metrics.<br/> <br/>   |
| [**SecondaryStatistic**](secondarystatistic.md)<br/> | This node describes the secondary descriptive statistic the assessment author recommends for describing the metrics.<br/> <br/> |
| [**StandardType**](standardtype.md)<br/>             | This node describes the metric's data type.<br/> <br/>                                                                          |
| [**Units**](units.md)<br/>                           | This node describes the units of the metric's value.<br/> <br/>                                                                 |



### Child element sequence

``` syntax
(
  Description, 
  StandardType, 
  Units, 
  DecimalPlaces, 
  Ordinal, 
  BetterDirection, 
  PrimaryStatistic, 
  SecondaryStatistic, 
  Importance
)
```

## Parent elements



| Element                                                   | Description                                                                             |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**MetricDefinitions**](metricdefinitions.md)<br/> | This element contains a collection of MetricDefinition elements.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





