---
title: Grid Control Pattern
description: Describes guidelines and conventions for implementing IGridProvider, including information about properties and methods. The Grid control pattern is used to support controls that act as containers for a collection of child elements.
ms.assetid: 'c50fb6f7-884a-4147-a6b2-c59d787fc04b'
keywords: ["UI Automation,implementing Grid control pattern", "UI Automation,Grid control pattern", "UI Automation,IGridProvider", "IGridProvider", "implementing UI Automation Grid control patterns", "Grid control patterns", "control patterns,IGridProvider", "control patterns,implementing UI Automation Grid", "control patterns,Grid", "interfaces,IGridProvider"]
---

# Grid Control Pattern

Describes guidelines and conventions for implementing [**IGridProvider**](uiauto-igridprovider.md), including information about properties and methods. The **Grid** control pattern is used to support controls that act as containers for a collection of child elements.

The children of this element must implement [**IGridItemProvider**](uiauto-igriditemprovider.md) and be organized in a two-dimensional logical coordinate system that can be traversed by row and column. For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IGridProvider**](#required-members-for-igridprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **Grid** control pattern, note the following guidelines and conventions:

-   Grid coordinates are zero-based with the upper left (or upper right cell depending on locale) having coordinates (0,0).
-   If a cell is empty, a Microsoft UI Automation element must still be returned in order to support the [**IGridItemProvider::ContainingGrid**](uiauto-igriditemprovider-containinggrid.md) property for that cell. This is possible when the layout of child elements in the grid is similar to a ragged array (see example below).

    ![example of a grid control with empty coordinates](images/grid.png)

-   A grid with a single item is still required to implement [**IGridProvider**](uiauto-igridprovider.md) if it is logically considered to be a grid. The number of child items in the grid is immaterial.
-   Hidden rows and columns, depending on the provider implementation, may be loaded in the UI Automation tree and will therefore be reflected in the [**IGridProvider::RowCount**](uiauto-igridprovider-rowcount.md) and [**ColumnCount**](uiauto-igridprovider-columncount.md) properties. If the hidden rows and columns have not yet been loaded, they should not be counted.
-   [**IGridProvider**](uiauto-igridprovider.md) does not enable active manipulation of a grid; [**ITransformProvider**](uiauto-itransformprovider.md) must be implemented to enable this functionality.
-   Use a [**IUIAutomationStructureChangedEventHandler**](uiauto-iuiautomationstructurechangedeventhandler.md) to listen for structural or layout changes to the grid such as cells that have been added, removed, or merged.
-   Use a [**IUIAutomationFocusChangedEventHandler**](uiauto-iuiautomationfocuschangedeventhandler.md) to track traversal through the items or cells of a grid.

## Required Members for **IGridProvider**

The following properties and methods are required for implementing the [**IGridProvider**](uiauto-igridprovider.md) interface.



| Required members                                        | Member type | Notes |
|---------------------------------------------------------|-------------|-------|
| [**RowCount**](uiauto-igridprovider-rowcount.md)       | Property    | None  |
| [**ColumnCount**](uiauto-igridprovider-columncount.md) | Property    | None  |
| [**GetItem**](uiauto-igridprovider-getitem.md)         | Method      | None  |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[GridItem Control Pattern](uiauto-implementinggriditem.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




