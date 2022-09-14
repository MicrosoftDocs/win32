---
title: TableItem Control Pattern
description: Describes guidelines and conventions for implementing ITableItemProvider, including information about methods. The TableItem control pattern is used to support child controls of containers that implement ITableProvider.
ms.assetid: e00c7a58-410c-4818-8f61-57ee98527d6e
keywords:
- UI Automation,implementing TableItem control pattern
- UI Automation,TableItem control pattern
- UI Automation,ITableItemProvider
- ITableItemProvider
- implementing UI Automation TableItem control patterns
- TableItem control patterns
- control patterns,ITableItemProvider
- control patterns,implementing UI Automation TableItem
- control patterns,TableItem
- interfaces,ITableItemProvider
ms.topic: article
ms.date: 05/31/2018
---

# TableItem Control Pattern

Describes guidelines and conventions for implementing [**ITableItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itableitemprovider), including information about methods. The **TableItem** control pattern is used to support child controls of containers that implement [**ITableProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itableprovider).

Access to individual cell functionality is provided by the required, concurrent implementation of [**IGridItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igriditemprovider). This control pattern is analogous to **IGridItemProvider** with the distinction that any control implementing [**ITableItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itableitemprovider) must programmatically expose the relationship between the individual cell and its row and column information. For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **ITableItemProvider**](#required-members-for-itableitemprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **TableItem** control pattern, note the following guidelines and conventions:

-   For related grid item functionality, see [GridItem Control Pattern](uiauto-implementinggriditem.md).

## Required Members for **ITableItemProvider**

The following methods are required for implementing the [**ITableItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itableitemprovider) interface.



| Required members                                                               | Member type | Notes |
|--------------------------------------------------------------------------------|-------------|-------|
| [**GetColumnHeaderItems**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itableitemprovider-getcolumnheaderitems) | Method      | None  |
| [**GetRowHeaderItems**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-itableitemprovider-getrowheaderitems)       | Method      | None  |



 

This control pattern has no associated properties or events.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[Table Control Pattern](uiauto-implementingtable.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




