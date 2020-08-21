---
title: Styles Control Pattern
description: Describes guidelines and conventions for implementing IStylesProvider, including information about properties and methods. The Styles control pattern is used to describe a UI element that has a specific style, fill color, fill pattern, or shape.
ms.assetid: 65125E07-70D4-48E5-B18D-E9D66ABC6FC0
keywords:
- UI Automation,implementing Styles control pattern
- UI Automation,Styles control pattern
- UI Automation,IStylesProvider
- IStylesProvider
- implementing UI Automation Styles control pattern
- Styles control pattern
- control patterns,IStylesProvider
- control patterns,implementing UI Automation Styles
- control patterns,Styles
- interfaces,IStylesProvider
ms.topic: article
ms.date: 05/31/2018
---

# Styles Control Pattern

Describes guidelines and conventions for implementing [**IStylesProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-istylesprovider), including information about properties and methods. The **Styles** control pattern is used to describe a UI element that has a specific style, fill color, fill pattern, or shape.

The **Styles** control pattern is especially useful for describing elements in a document, which frequently have such styles. Styles typically carry information that is useful for customers with disabilities; for example, a style can describe a certain string as the title of a document, or a certain flowchart object as a diamond or a circle. For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IStylesProvider**](#required-members-for-istylesprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **Styles** control pattern, note the following guidelines and conventions:

-   The UIAutomationClient.h header file defines a set of named constant values used to identify several common styles. For more information, see [**Style Identifiers**](uiauto-style-identifiers.md).
-   If you use [**StyleId\_Custom**](uiauto-style-identifiers.md), you must implement the [**IStylesProvider::StyleName**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-istylesprovider-get_stylename) property to enable clients to discover the name of the style. You do not need to implement the **StyleName** property for a standard style because Microsoft UI Automation provides a default name, but you can implement it if you need to override the default name.
-   The other properties in the **Styles** pattern are optional; the provider can return [**UIA\_E\_NOTSUPPORTED**](uiauto-error-codes.md) for a property that is not supported.
-   Styles in a text range can be represented through the following text attributes:
    -   When responding to a request for the [**StyleId**](uiauto-textattribute-ids.md) text attribute, the text range should return one of the style identifiers described in [**Style Identifiers**](uiauto-style-identifiers.md).
    -   If [**StyleId\_Custom**](uiauto-style-identifiers.md) is used, the text range should return a string value for the [**StyleName**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-istylesprovider-get_stylename) text attribute to enable clients to discover the style name.
    -   A text range that has multiple styles, such as both heading and normal text, should return the special UI Automation [**ReservedMixedAttributeValue**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiagetreservedmixedattributevalue) property for both the [**StyleId**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-istylesprovider-get_styleid) and [**StyleName**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-istylesprovider-get_stylename) properties. A client receiving this response can subdivide the text range to find where the styles begin and end.
-   Applications can use a wide variety of styles to describe objects, but UI Automation represents only the most common ones. To represent additional style attributes, such as border color, a provider can return a list of additional attributes in the [**ExtendedProperties**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-istylesprovider-get_extendedproperties) property. This is basically a property bag with a set of extended properties, such as "BorderColor=0xFF0000;BorderStyle=dotted". The values of extended properties can be application-specific.

## Required Members for **IStylesProvider**

The following properties are required for implementing the [**IStylesProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-istylesprovider) interface.



| Required members                                                            | Member type | Notes |
|-----------------------------------------------------------------------------|-------------|-------|
| [**ExtendedProperties**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-istylesprovider-get_extendedproperties) | Property    | None  |
| [**FillColor**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-istylesprovider-get_fillcolor)                       | Property    | None  |
| [**FillPatternColor**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-istylesprovider-get_fillpatterncolor)         | Property    | None  |
| [**FillPatternStyle**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-istylesprovider-get_fillpatternstyle)         | Property    | None  |
| [**Shape**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-istylesprovider-get_shape)                               | Property    | None  |
| [**StyleId**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-istylesprovider-get_styleid)                           | Property    | None  |
| [**StyleName**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-istylesprovider-get_stylename)                       | Property    | None  |



 

This control pattern has no associated methods or events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 