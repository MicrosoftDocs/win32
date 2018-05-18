---
title: RangeValue Control Pattern
description: Describes guidelines and conventions for implementing IRangeValueProvider, including information about properties and methods. The RangeValue control pattern is used to support controls that can be set to a value within a range.
ms.assetid: 'e5c1104c-4b20-4fdd-bd12-dfc27cb73ac5'
keywords: ["UI Automation,implementing RangeValue control pattern", "UI Automation,RangeValue control pattern", "UI Automation,IRangeValueProvider", "IRangeValueProvider", "implementing UI Automation RangeValue control patterns", "RangeValue control patterns", "control patterns,IRangeValueProvider", "control patterns,implementing UI Automation RangeValue", "control patterns,RangeValue", "interfaces,IRangeValueProvider"]
---

# RangeValue Control Pattern

Describes guidelines and conventions for implementing [**IRangeValueProvider**](uiauto-irangevalueprovider.md), including information about properties and methods. The **RangeValue** control pattern is used to support controls that can be set to a value within a range.

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IRangeValueProvider**](#required-members-for-irangevalueprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **RangeValue** control pattern, note the following guidelines and conventions:

-   Controls allow recalibration of their supported properties based upon locale or user preference. An example of this is a thermometer control that can be set to display the temperature in Fahrenheit or Celsius.
-   Controls that have ambiguous range values, such as progress bars or sliders, should have those values normalized.

## Required Members for **IRangeValueProvider**

The following properties and methods are required for implementing the [**IRangeValueProvider**](uiauto-irangevalueprovider.md) interface.



| Required members                                              | Member type | Notes |
|---------------------------------------------------------------|-------------|-------|
| [**IsReadOnly**](uiauto-irangevalueprovider-isreadonly.md)   | Property    | None  |
| [**Value**](uiauto-irangevalueprovider-value.md)             | Property    | None  |
| [**LargeChange**](uiauto-irangevalueprovider-largechange.md) | Property    | None  |
| [**SmallChange**](uiauto-irangevalueprovider-smallchange.md) | Property    | None  |
| [**Maximum**](uiauto-irangevalueprovider-maximum.md)         | Property    | None  |
| [**Minimum**](uiauto-irangevalueprovider-minimum.md)         | Property    | None  |
| [**SetValue**](uiauto-irangevalueprovider-setvalue.md)       | Method      | None  |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




