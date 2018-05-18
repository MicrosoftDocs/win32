---
title: GridItem Control Pattern
description: Describes guidelines and conventions for implementing IGridItemProvider, including information about properties. The GridItem control pattern is used to support individual child controls of containers that implement IGridProvider.
ms.assetid: 'ae4b9021-1800-485b-99a2-54ddf9c21f93'
keywords: ["UI Automation,implementing GridItem control pattern", "UI Automation,GridItem control pattern", "UI Automation,IGridItemProvider", "IGridItemProvider", "implementing UI Automation GridItem control patterns", "GridItem control patterns", "control patterns,IGridItemProvider", "control patterns,implementing UI Automation GridItem", "control patterns,GridItem", "interfaces,IGridItemProvider"]
---

# GridItem Control Pattern

Describes guidelines and conventions for implementing [**IGridItemProvider**](uiauto-igriditemprovider.md), including information about properties. The **GridItem** control pattern is used to support individual child controls of containers that implement [**IGridProvider**](uiauto-igridprovider.md).

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IGridItemProvider**](#required-members-for-igriditemprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **GridItem** control pattern, note the following guidelines and conventions:

-   Grid coordinates are zero-based with the upper left cell having coordinates (0, 0).
-   Merged cells will report their [**Row**](uiauto-igriditemprovider-row.md) and [**Column**](uiauto-igriditemprovider-column.md) properties based on their underlying anchor cell as defined by the Microsoft UI Automation provider. Typically, it will be the topmost and leftmost row or column.
-   [**IGridProvider**](uiauto-igridprovider.md) does not provide for active manipulation of the grid such as merging or splitting cells.
-   Controls that implement [**IGridProvider**](uiauto-igridprovider.md) can typically be traversed (that is, a UI Automation client can move to adjacent controls) by using the keyboard.

## Required Members for **IGridItemProvider**

The following properties are required for implementing the [**IGridItemProvider**](uiauto-igriditemprovider.md) interface.



| Required members                                                  | Member type | Notes |
|-------------------------------------------------------------------|-------------|-------|
| [**Row**](uiauto-igriditemprovider-row.md)                       | Property    | None  |
| [**Column**](uiauto-igriditemprovider-column.md)                 | Property    | None  |
| [**RowSpan**](uiauto-igriditemprovider-rowspan.md)               | Property    | None  |
| [**ColumnSpan**](uiauto-igriditemprovider-columnspan.md)         | Property    | None  |
| [**ContainingGrid**](uiauto-igriditemprovider-containinggrid.md) | Property    | None  |



 

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

 

 




