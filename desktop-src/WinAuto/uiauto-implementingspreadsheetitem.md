---
title: SpreadsheetItem Control Pattern
description: Describes guidelines and conventions for implementing ISpreadsheetItemProvider, including information about properties and methods.
ms.assetid: AADD06C5-CF51-4A1A-9ACB-3E896050D7DD
keywords:
- UI Automation,implementing SpreadsheetItem control pattern
- UI Automation,SpreadsheetItem control pattern
- UI Automation,ISpreadsheetItemProvider
- ISpreadsheetItemProvider
- implementing UI Automation SpreadsheetItem control pattern
- SpreadsheetItem control pattern
- control patterns,ISpreadsheetItemProvider
- control patterns,implementing UI Automation SpreadsheetItem
- control patterns,SpreadsheetItem
- interfaces,ISpreadsheetItemProvider
ms.topic: article
ms.date: 05/31/2018
---

# SpreadsheetItem Control Pattern

Describes guidelines and conventions for implementing [**ISpreadsheetItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ispreadsheetitemprovider), including information about properties and methods. The **SpreadsheetItem** control pattern is used to expose the properties of a cell in a spreadsheet or other grid-based document.

The **SpreadsheetItem** control pattern is closely related to the [GridItem](uiauto-implementinggriditem.md) control pattern; controls that implement the **SpreadsheetItem** control pattern should also implement the GridItem control pattern. Controls can also implement the [TableItem](uiauto-implementingtableitem.md) control pattern, if appropriate. For examples of controls that implement these control patterns, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **ISpreadsheetItemProvider**](#required-members-for-ispreadsheetitemprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **SpreadsheetItem** control pattern, note the following guidelines and conventions:

-   When implementing the [**ISpreadsheetItemProvider::GetAnnotationObjects**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetitemprovider-getannotationobjects) and [**ISpreadsheetItemProvider::GetAnnotationTypes**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetitemprovider-getannotationtypes) methods, please refer to the [**IAnnotationProvider**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-iannotationprovider) documentation. These methods both return arrays to enable providers to support multiple annotations on a single cell.
-   Some kinds of annotations do not require a full implementation of the [**IAnnotationProvider**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-iannotationprovider) interface. For example, a simple spelling-error indicator could be represented by having [**GetAnnotationTypes**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetitemprovider-getannotationtypes) return a text attribute identifier of [**AnnotationType\_SpellingError**](uiauto-annotation-type-identifiers.md), and having [**GetAnnotationObjects**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetitemprovider-getannotationobjects) return a null value.

## Required Members for **ISpreadsheetItemProvider**

The following properties and methods are required for implementing the [**ISpreadsheetItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ispreadsheetitemprovider) interface.



| Required members                                                                         | Member type | Notes                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Formula**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetitemprovider-get_formula)                           | Property    | Implementing a separate [**Formula**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetitemprovider-get_formula) property is necessary because a cell’s [Value](value-property.md) property typically returns the computed value of the cell. The **Formula** property should be **NULL** if no formula is set. |
| [**GetAnnotationObjects**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetitemprovider-getannotationobjects) | Method      | Returns an array of element providers that refer to the annotations linked to this cell. Pointers within the array can be null if an annotation does not have a linked provider.                                                                                                       |
| [**GetAnnotationTypes**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetitemprovider-getannotationtypes)     | Method      | Returns an array of annotation type identifiers that describe the annotations on this cell. The array must be the same size as the array returned by [**GetAnnotationObjects**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetitemprovider-getannotationobjects).                                         |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[Spreadsheet Control Pattern](uiauto-implementingspreadsheet.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 