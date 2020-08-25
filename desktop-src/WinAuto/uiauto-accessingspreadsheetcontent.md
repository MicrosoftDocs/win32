---
title: Accessing Spreadsheet Content
description: This topic describes how Microsoft UI Automation client applications can access the content of a spreadsheet.
ms.assetid: F32EFA46-222B-4A4E-9938-10DE0F6A2CA7
keywords:
- clients,accessing spreadsheet content
- clients,text-based controls
- clients,Spreadsheet control pattern
- clients,SpreadsheetItem control pattern
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Spreadsheet Content

A text-based control that contains spreadsheet content can enable clients to access the content by supporting the [Spreadsheet](uiauto-implementingspreadsheet.md) and [SpreadsheetItem](uiauto-implementingspreadsheetitem.md) control patterns. This topic describes how Microsoft UI Automation client applications can access the content of a spreadsheet.

To determine whether a text-based control supports the [Spreadsheet](uiauto-implementingspreadsheet.md) and [SpreadsheetItem](uiauto-implementingspreadsheetitem.md) control patterns, first retrieve the [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface for the control (see [Obtaining UI Automation Elements](uiauto-obtainingelements.md).) Next, call the [**IUIAutomationElement::GetCurrentPattern**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpattern) method, specifying a control pattern identifier of [**UIA\_SpreadsheetPatternId**](uiauto-controlpattern-ids.md) or [**UIA\_SpreadsheetItemPatternId**](uiauto-controlpattern-ids.md), and a variant that receives TRUE if the control supports the particular control pattern.

To access the spreadsheet content, retrieve the [**IUIAutomationSpreadsheetPattern**](/windows/desktop/api/uiautomationclient/nn-uiautomationclient-iuiautomationspreadsheetpattern) interface by calling [**IUIAutomationElement::GetCurrentPattern**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpattern) method and specifying [**UIA\_SpreadsheetPatternId**](uiauto-controlpattern-ids.md) as the control pattern identifier. Next, use the [**IUIAutomationSpreadsheetPattern::GetItemByName**](/windows/desktop/api/uiautomationclient/nf-uiautomationclient-iuiautomationspreadsheetpattern-getitembyname) method to get the [**IUIAutomationSpreadsheetItem**](/windows/desktop/api/uiautomationclient/nn-uiautomationclient-iuiautomationspreadsheetitempattern) interface for a particular spreadsheet item (typically a cell). Use the properties and methods of the **IUIAutomationSpreadsheetItem** interface to retrieve the formula for the cell, and any annotations associated with the cell. For more information about annotations, see [Retrieving Annotations.](uiauto-usingtextrangeobjects.md)

## Related topics

<dl> <dt>

[UI Automation Support for Textual Content](uiauto-ui-automation-textpattern-overview.md)
</dt> <dt>

[Working with Text-based Controls](uiauto-workingwithtextbasedcontrols.md)
</dt> </dl>

 

 