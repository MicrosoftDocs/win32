---
title: GridItem Control Pattern
description: Describes guidelines and conventions for implementing IGridItemProvider, including information about properties. The GridItem control pattern is used to support individual child controls of containers that implement IGridProvider.
ms.assetid: ae4b9021-1800-485b-99a2-54ddf9c21f93
keywords:
- UI Automation,implementing GridItem control pattern
- UI Automation,GridItem control pattern
- UI Automation,IGridItemProvider
- IGridItemProvider
- implementing UI Automation GridItem control patterns
- GridItem control patterns
- control patterns,IGridItemProvider
- control patterns,implementing UI Automation GridItem
- control patterns,GridItem
- interfaces,IGridItemProvider
ms.topic: article
ms.date: 05/31/2018
---

# GridItem Control Pattern

Describes guidelines and conventions for implementing [**IGridItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igriditemprovider), including information about properties. The **GridItem** control pattern is used to support individual child controls of containers that implement [**IGridProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igridprovider).

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IGridItemProvider**](#required-members-for-igriditemprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **GridItem** control pattern, note the following guidelines and conventions:

-   Grid coordinates are zero-based with the upper left cell having coordinates (0, 0).
-   Merged cells will report their [**Row**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_row) and [**Column**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_column) properties based on their underlying anchor cell as defined by the Microsoft UI Automation provider. Typically, it will be the topmost and leftmost row or column.
-   [**IGridProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igridprovider) does not provide for active manipulation of the grid such as merging or splitting cells.
-   Controls that implement [**IGridProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igridprovider) can typically be traversed (that is, a UI Automation client can move to adjacent controls) by using the keyboard.

## Required Members for **IGridItemProvider**

The following properties are required for implementing the [**IGridItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igriditemprovider) interface.



| Required members                                                  | Member type | Notes |
|-------------------------------------------------------------------|-------------|-------|
| [**Row**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_row)                       | Property    | None  |
| [**Column**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_column)                 | Property    | None  |
| [**RowSpan**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_rowspan)               | Property    | None  |
| [**ColumnSpan**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_columnspan)         | Property    | None  |
| [**ContainingGrid**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_containinggrid) | Property    | None  |



 

This control pattern has no associated methods or events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[Grid Control Pattern](uiauto-implementinggrid.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




