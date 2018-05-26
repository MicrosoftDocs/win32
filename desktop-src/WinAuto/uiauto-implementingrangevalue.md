---
title: RangeValue Control Pattern
description: Describes guidelines and conventions for implementing IRangeValueProvider, including information about properties and methods. The RangeValue control pattern is used to support controls that can be set to a value within a range.
ms.assetid: e5c1104c-4b20-4fdd-bd12-dfc27cb73ac5
keywords:
- UI Automation,implementing RangeValue control pattern
- UI Automation,RangeValue control pattern
- UI Automation,IRangeValueProvider
- IRangeValueProvider
- implementing UI Automation RangeValue control patterns
- RangeValue control patterns
- control patterns,IRangeValueProvider
- control patterns,implementing UI Automation RangeValue
- control patterns,RangeValue
- interfaces,IRangeValueProvider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RangeValue Control Pattern

Describes guidelines and conventions for implementing [**IRangeValueProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irangevalueprovider?branch=master), including information about properties and methods. The **RangeValue** control pattern is used to support controls that can be set to a value within a range.

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

The following properties and methods are required for implementing the [**IRangeValueProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irangevalueprovider?branch=master) interface.



| Required members                                              | Member type | Notes |
|---------------------------------------------------------------|-------------|-------|
| [**IsReadOnly**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_isreadonly?branch=master)   | Property    | None  |
| [**Value**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_value?branch=master)             | Property    | None  |
| [**LargeChange**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_largechange?branch=master) | Property    | None  |
| [**SmallChange**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_smallchange?branch=master) | Property    | None  |
| [**Maximum**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_maximum?branch=master)         | Property    | None  |
| [**Minimum**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_minimum?branch=master)         | Property    | None  |
| [**SetValue**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-setvalue?branch=master)       | Method      | None  |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




