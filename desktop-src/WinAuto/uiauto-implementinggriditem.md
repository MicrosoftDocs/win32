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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GridItem Control Pattern

Describes guidelines and conventions for implementing [**IGridItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-igriditemprovider?branch=master), including information about properties. The **GridItem** control pattern is used to support individual child controls of containers that implement [**IGridProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-igridprovider?branch=master).

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IGridItemProvider**](#required-members-for-igriditemprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **GridItem** control pattern, note the following guidelines and conventions:

-   Grid coordinates are zero-based with the upper left cell having coordinates (0, 0).
-   Merged cells will report their [**Row**](/windows/win32/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_row?branch=master) and [**Column**](/windows/win32/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_column?branch=master) properties based on their underlying anchor cell as defined by the Microsoft UI Automation provider. Typically, it will be the topmost and leftmost row or column.
-   [**IGridProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-igridprovider?branch=master) does not provide for active manipulation of the grid such as merging or splitting cells.
-   Controls that implement [**IGridProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-igridprovider?branch=master) can typically be traversed (that is, a UI Automation client can move to adjacent controls) by using the keyboard.

## Required Members for **IGridItemProvider**

The following properties are required for implementing the [**IGridItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-igriditemprovider?branch=master) interface.



| Required members                                                  | Member type | Notes |
|-------------------------------------------------------------------|-------------|-------|
| [**Row**](/windows/win32/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_row?branch=master)                       | Property    | None  |
| [**Column**](/windows/win32/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_column?branch=master)                 | Property    | None  |
| [**RowSpan**](/windows/win32/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_rowspan?branch=master)               | Property    | None  |
| [**ColumnSpan**](/windows/win32/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_columnspan?branch=master)         | Property    | None  |
| [**ContainingGrid**](/windows/win32/UIAutomationCore/nf-uiautomationcore-igriditemprovider-get_containinggrid?branch=master) | Property    | None  |



 

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

 

 




