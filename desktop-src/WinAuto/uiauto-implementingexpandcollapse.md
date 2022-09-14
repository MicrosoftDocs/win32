---
title: ExpandCollapse Control Pattern
description: Describes guidelines and conventions for implementing IExpandCollapseProvider, including information about properties, methods, and events.
ms.assetid: 0ffc26c3-8696-44f9-b463-902a69e06d21
keywords:
- UI Automation,implementing ExpandCollapse control pattern
- UI Automation,ExpandCollapse control pattern
- UI Automation,IExpandCollapseProvider
- IExpandCollapseProvider
- implementing UI Automation ExpandCollapse control patterns
- ExpandCollapse control patterns
- control patterns,IExpandCollapseProvider
- control patterns,implementing UI Automation ExpandCollapse
- control patterns,ExpandCollapse
- interfaces,IExpandCollapseProvider
ms.topic: article
ms.date: 05/31/2018
---

# ExpandCollapse Control Pattern

Describes guidelines and conventions for implementing [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider), including information about properties, methods, and events. The **ExpandCollapse** control pattern is used to support controls that visually expand to display more content and collapse to hide content.

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IExpandCollapseProvider**](#required-members-for-iexpandcollapseprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **ExpandCollapse** control pattern, note the following guidelines and conventions:

-   Aggregate controls, built with child objects that provide the UI with expand/collapse functionality, must support the **ExpandCollapse** control pattern whereas their child elements do not. For example, a combo box control is built with a combination of list box, button, and edit controls, but it is only the parent combo box that must support the **ExpandCollapse** control pattern.
    > [!Note]  
    > An exception is the menu control, which is an aggregate of individual menu item objects. The menu item objects can support the **ExpandCollapse** control pattern, but the parent menu control cannot. A similar exception applies to the tree and tree item controls.

     

-   When the [**IExpandCollapseProvider::ExpandCollapseState**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-get_expandcollapsestate) of a control is set to **ExpandCollapseState\_LeafNode**, any **ExpandCollapse** functionality is currently inactive for the control and the only information that can be obtained using this control pattern is the **ExpandCollapseState**. If any child objects are subsequently added, the **ExpandCollapseState** changes and **ExpandCollapse** functionality is activated.
-   [**ExpandCollapseState**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-get_expandcollapsestate) refers to the visibility of immediate child objects only; it does not refer to the visibility of all descendant objects.
-   [**IExpandCollapseProvider::Expand**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-expand) and [**Collapse**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-collapse) functionality is control-specific. The following are examples of this behavior.
    -   The Office Personal Menu can be a three-state menu item ("Expanded", "Collapsed" and "PartiallyExpanded") where the control specifies the state to adopt when [**Expand**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-expand) or [**Collapse**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-collapse) is called.
    -   Calling [**Expand**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-expand) on a tree item may display all descendants or only immediate children.
    -   If calling [**Expand**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-expand) or [**Collapse**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-collapse) on a control maintains the state of its descendants, a visibility change event should be sent, not a state change event. If the parent control does not maintain the state of its descendants when collapsed, the control may destroy all the descendants that are no longer visible and raise a destroyed event; or it may change the [**ExpandCollapseState**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-get_expandcollapsestate) for each descendant and raise a visibility change event.
-   To guarantee navigation, it is desirable for an object to be in the Microsoft UI Automation tree (with appropriate visibility state) regardless of its parents [**ExpandCollapseState**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-get_expandcollapsestate). If descendants are generated on demand, they may only appear in the UI Automation tree after being displayed for the first time or only while they are visible.

## Required Members for **IExpandCollapseProvider**

The following properties, methods, and events are required for implementing the [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider) interface.



| Required members                                                                                    | Member type | Notes                                                                  |
|-----------------------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------|
| [**ExpandCollapseState**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-get_expandcollapsestate)                   | Property    | None                                                                   |
| [**Expand**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-expand)                                             | Method      | None                                                                   |
| [**Collapse**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-collapse)                                         | Method      | None                                                                   |
| [**IUIAutomationPropertyChangedEventHandler**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationpropertychangedeventhandler) | Event       | This control has no associated events; use this generic event handler. |



 

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




