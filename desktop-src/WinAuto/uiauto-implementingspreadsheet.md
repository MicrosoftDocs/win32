---
title: Spreadsheet Control Pattern
description: Describes guidelines and conventions for implementing ISpreadsheetProvider, including information about methods.
ms.assetid: 4004D867-8367-486A-96ED-DE5B41D24935
keywords:
- UI Automation,implementing spreadsheet control pattern
- UI Automation,spreadsheet control pattern
- UI Automation,ISpreadsheetProvider
- ISpreadsheetProvider
- implementing UI Automation spreadsheet control pattern
- spreadsheet control pattern
- control patterns,ISpreadsheetProvider
- control patterns,implementing UI Automation spreadsheet
- control patterns,spreadsheet
- interfaces,ISpreadsheetProvider
ms.topic: article
ms.date: 05/31/2018
---

# Spreadsheet Control Pattern

Describes guidelines and conventions for implementing [**ISpreadsheetProvider**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-ispreadsheetprovider), including information about methods. Links to additional references are listed at the end of the topic. The **Spreadsheet** control pattern is used to expose the contents of a spreadsheet or other grid-based document.

The **Spreadsheet** control pattern is closely related to the [Grid](uiauto-implementinggrid.md) control pattern; controls that implement the **Spreadsheet** control pattern should also implement the Grid control pattern. Controls can also implement the [Table](uiauto-implementingtable.md) control pattern, if appropriate. For examples of controls that implement these control patterns, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

## Implementation Guidelines and Conventions

When implementing the **Spreadsheet** control pattern, note the following guidelines and conventions:

-   If a spreadsheet implements the [**ISpreadsheetProvider**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-ispreadsheetprovider) interface, its cells must implement the [**ISpreadsheetItemProvider**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-ispreadsheetitemprovider) interface.
-   The [**ISpreadsheetProvider::GetItemByName**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetprovider-getitembyname) method is intended to provide the same kind of navigation that an application might supply with a **Jump to Label** feature. Many spreadsheet programs let specific cells be given a friendly name or label. **GetItemByName** enables the client to look up a cell based on its friendly name. This method should not retrieve any cells that contain the name text because the results can be highly ambiguous. If the spreadsheet program allows multiple cells in the same a spreadsheet to have the same friendly name or label, the Microsoft UI Automation behavior is undefined.

## Required Members for **ISpreadsheetProvider**

The following method is required for implementing the [**ISpreadsheetProvider**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-ispreadsheetprovider) interface.



| Required members                                                       | Member type | Notes |
|------------------------------------------------------------------------|-------------|-------|
| [**GetItemByName**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-ispreadsheetprovider-getitembyname) | Method      | None  |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 