---
title: Window Control Pattern
description: Describes guidelines and conventions for implementing IWindowProvider, including information about properties, methods, and events. The Window control pattern supports controls that provide fundamental window-based functionality within a traditional GUI.
ms.assetid: bfd37d27-fcec-4d25-841c-63e14e48c6c8
keywords:
- UI Automation,implementing Window control pattern
- UI Automation,Window control pattern
- UI Automation,IWindowProvider
- IWindowProvider
- implementing UI Automation Window control patterns
- Window control patterns
- control patterns,IWindowProvider
- control patterns,implementing UI Automation Window
- control patterns,Window
- interfaces,IWindowProvider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Window Control Pattern

Describes guidelines and conventions for implementing [**IWindowProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iwindowprovider?branch=master), including information about properties, methods, and events. The **Window** control pattern supports controls that provide fundamental window-based functionality within a traditional GUI.

Examples of controls that must implement this control pattern include top-level application windows, multiple-document interface (MDI) child windows, resizable split pane controls, modal dialogs and balloon help windows. For examples of controls that implement this control pattern, see [Control Pattern Mapping for UI Automation Clients](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IWindowProvider**](#required-members-for-iwindowprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **Window** control pattern, note the following guidelines and conventions:

-   To support the ability to modify both window size and screen position using Microsoft UI Automation, a control must implement [**ITransformProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-itransformprovider?branch=master) in addition to [**IWindowProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iwindowprovider?branch=master).
-   Controls that contain title bars, and title bar elements that enable the control to be moved, resized, maximized, minimized, or closed, are typically required to implement [**IWindowProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iwindowprovider?branch=master).
-   Controls such as tooltip pop-ups and combo-box or menu drop-downs do not typically implement [**IWindowProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iwindowprovider?branch=master).
-   Balloon help windows are differentiated from basic tooltip pop-ups by the provision of a window-like **Close** button.
-   Full-screen mode is not supported by [**IWindowProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iwindowprovider?branch=master) as it is feature-specific to an application and is not typical window behavior.

## Required Members for **IWindowProvider**

The following properties, methods, and events are required for implementing the [**IWindowProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iwindowprovider?branch=master) interface.



| Required members                                                                            | Member type | Notes                                                                       |
|---------------------------------------------------------------------------------------------|-------------|-----------------------------------------------------------------------------|
| [**WindowInteractionState**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iwindowprovider-get_windowinteractionstate?branch=master)             | Property    | Is not guaranteed to be **WindowInteractionState\_ReadyForUserInteraction** |
| [**IsModal**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iwindowprovider-get_ismodal?branch=master)                                           | Property    | None                                                                        |
| [**IsTopmost**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iwindowprovider-get_istopmost?branch=master)                                       | Property    | None                                                                        |
| [**CanMaximize**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iwindowprovider-get_canmaximize?branch=master)                                   | Property    | None                                                                        |
| [**CanMinimize**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iwindowprovider-get_canminimize?branch=master)                                   | Property    | None                                                                        |
| [**WindowVisualState**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iwindowprovider-get_windowvisualstate?branch=master)                       | Property    | None                                                                        |
| [**Close**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iwindowprovider-close?branch=master)                                               | Method      | None                                                                        |
| [**SetVisualState**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iwindowprovider-setvisualstate?branch=master)                             | Method      | None                                                                        |
| [**WaitForInputIdle**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iwindowprovider-waitforinputidle?branch=master)                         | Method      | None                                                                        |
| [**UIA\_Window\_WindowClosedEventId**](uiauto-event-ids.md#uia-window-windowclosedeventid) | Event       | None                                                                        |
| [**UIA\_Window\_WindowOpenedEventId**](uiauto-event-ids.md#uia-window-windowopenedeventid) | Event       | None                                                                        |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[Control Pattern Mapping for UI Automation Clients](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




