---
title: Invoke Control Pattern
description: Describes guidelines and conventions for implementing IInvokeProvider, including information about methods.
ms.assetid: 6557a03c-fd1f-4e44-8393-fe367d7a17af
keywords:
- UI Automation,implementing Invoke control pattern
- UI Automation,Invoke control pattern
- UI Automation,IInvokeProvider
- IInvokeProvider
- implementing UI Automation Invoke control patterns
- Invoke control patterns
- control patterns,IInvokeProvider
- control patterns,implementing UI Automation Invoke
- control patterns,Invoke
- interfaces,IInvokeProvider
ms.topic: article
ms.date: 05/31/2018
---

# Invoke Control Pattern

Describes guidelines and conventions for implementing [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider), including information about methods. The **Invoke** control pattern is used to support controls that do not maintain state when activated but rather initiate or perform a single, unambiguous action.

Controls that do maintain state, such as check boxes and radio buttons, must instead implement [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider) and [**ISelectionProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionprovider) respectively. For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IInvokeProvider**](#required-members-for-iinvokeprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **Invoke** control pattern, note the following guidelines and conventions:

-   Controls implement [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider) if the same behavior is not exposed through another control pattern provider. For example, if the [**IUIAutomationInvokePattern::Invoke**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationinvokepattern-invoke) method on a control performs the same action as the [**IUIAutomationExpandCollapsePattern::Expand**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationexpandcollapsepattern-expand) or [**Collapse**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationexpandcollapsepattern-collapse) method, the control should not implement **IInvokeProvider**.
-   Invoking a control is generally performed by clicking or double-clicking or pressing ENTER, a predefined keyboard shortcut, or some alternate combination of keystrokes.
-   The **Invoked** event ([**UIA\_Invoke\_InvokedEventId**](uiauto-event-ids.md)) event is raised on a control that has been activated (as a response to a control carrying out its associated action). If possible, the event should be raised after the control has completed the action and returned without blocking. The **Invoked** event (**UIA\_Invoke\_InvokedEventId**) should be raised before servicing the **Invoke** request in the following scenarios:
    -   It is not possible or practical to wait until the action is complete.
    -   The action requires user interaction.
    -   The action is time-consuming and will cause the calling client to block for a significant amount of time.
-   If invoking the control has significant side-effects, those side-effects should be exposed through the **HelpText** property. For example, even though [**IUIAutomationInvokePattern::Invoke**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationinvokepattern-invoke) is not associated with selection, **Invoke** may cause another control to become selected.
-   Hover (or mouse-over) effects generally do not constitute an **Invoked** event. However, controls that perform an action (as opposed to cause a visual effect) based on the hover state should support the **Invoke** control pattern.
    > [!Note]  
    > This implementation is considered an accessibility issue if the control can be invoked only as a result of a mouse-related side effect.

     

-   Invoking a control is different from selecting an item. However, depending on the control, invoking it may cause the item to become selected as a side-effect. For example, invoking a Microsoft Word document list item in the My Documents folder both selects the item and opens the document.
-   An element can disappear from the Microsoft UI Automation tree immediately upon being invoked. Requesting information from the element provided by the event callback may fail as a result. Pre-fetching cached information is the recommended workaround.
-   Controls can implement multiple control patterns. For example, the **Fill Color** control on the Microsoft Excel toolbar implements both the Invoke and the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control patterns. The ExpandCollapse control pattern exposes the menu and the **Invoke** control pattern fills the active selection with the chosen color.

## Required Members for **IInvokeProvider**

The following method is required for implementing the [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider) interface.



| Required members                                | Member type | Notes                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Invoke**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iinvokeprovider-invoke) | Method      | **Invoke** is an asynchronous call and must return immediately without blocking.<br/> This behavior is particularly critical for controls that, directly or indirectly, launch a modal dialog when invoked. Any UI Automation client that instigated the event will remain blocked until the modal dialog is closed. <br/> |



 

This control pattern has no associated properties or events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> <dt>

[**UIA\_Invoke\_InvokedEventId**](uiauto-event-ids.md)
</dt> </dl>

 

 





