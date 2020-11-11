---
title: Property Condition Interfaces for Clients
description: This section describes property condition interfaces for UI Automation clients for Microsoft Win32 applications.
ms.assetid: cea34e47-03a9-4ff9-9019-427a2a3e13d6
ms.topic: article
ms.date: 05/31/2018
---

# Property Condition Interfaces for Clients

This section describes property condition interfaces for UI Automation clients for Microsoft Win32 applications.

## In this section



| Interface                                                                                  | Description                                                                                                                                                        |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUIAutomationAndCondition**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationandcondition)<br/>           | Exposes properties and methods that Microsoft UI Automation client applications can use to retrieve information about an AND-based property condition. <br/> |
| [**IUIAutomationBoolCondition**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationboolcondition)<br/>         | Represents a condition that can be either **TRUE** (selects all elements) or **FALSE** (selects no elements).<br/>                                           |
| [**IUIAutomationCondition**](/windows/win32/api/uiautomationclient/nn-uiautomationclient-iuiautomationcondition)<br/>                 | This is the primary interface for conditions used in filtering when searching for elements in the UI Automation tree.<br/>                                   |
| [**IUIAutomationNotCondition**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationnotcondition)<br/>           | Represents a condition that is the negative of another condition.<br/>                                                                                       |
| [**IUIAutomationOrCondition**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationorcondition)<br/>             | Represents a condition made up of multiple conditions, at least one of which must be true.<br/>                                                              |
| [**IUIAutomationPropertyCondition**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationpropertycondition)<br/> | Represents a condition based on a property value that is used to find UI Automation elements.<br/>                                                           |



 

## Related topics

<dl> <dt>

[UI Automation Clients](uiauto-entry-uiautoclientsforwin32apps.md)
</dt> </dl>

 

