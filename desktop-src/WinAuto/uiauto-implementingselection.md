---
title: Selection Control Pattern
description: Describes guidelines and conventions for implementing ISelectionProvider, including information about properties, methods, and events.
ms.assetid: 9371e656-6f93-4a43-bd0c-c6977348b16a
keywords:
- UI Automation,implementing Selection control pattern
- UI Automation,Selection control pattern
- UI Automation,ISelectionProvider
- ISelectionProvider
- implementing UI Automation Selection control patterns
- Selection control patterns
- control patterns,ISelectionProvider
- control patterns,implementing UI Automation Selection
- control patterns,Selection
- interfaces,ISelectionProvider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Selection Control Pattern

Describes guidelines and conventions for implementing [**ISelectionProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionprovider?branch=master), including information about properties, methods, and events. The **Selection** control pattern is used to support controls that act as containers for a collection of selectable child items. The children of this element must implement [**ISelectionItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider?branch=master).

For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **ISelectionProvider**](#required-members-for-iselectionprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **Selection** control pattern, note the following guidelines and conventions:

-   Controls that implement [**ISelectionProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionprovider?branch=master) allow either single or multiple child items to be selected. For example, list boxes, list views, and tree views support multiple selections, whereas combo boxes, sliders, and radio button groups support single selection.
-   Controls that have a minimum, maximum, and continuous range, such as the **Volume** slider control of a media player, should implement [**IRangeValueProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irangevalueprovider?branch=master) instead of [**ISelectionProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionprovider?branch=master).
-   Single-selection controls that manage child controls that implement [**IRawElementProviderFragmentRoot**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragmentroot?branch=master), such as the **Screen Resolution** slider in the **Display Properties** dialog for Windows, or the **Color Picker** selection control from Microsoft Word (see the following image), should implement [**ISelectionProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionprovider?branch=master); their children should implement both [**IRawElementProviderFragment**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragment?branch=master) and [**ISelectionItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider?branch=master).

    ![image showing an example of color swatch string mapping](images/uia-valuepattern-colorpicker.jpg)

-   Menus do not support the **Selection** control pattern. If you are working with menu items that include both graphics and text (such as the **Preview Pane** items in the **View** menu in Microsoft Outlook) and need to convey state, you should implement [**IToggleProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-itoggleprovider?branch=master).

## Required Members for **ISelectionProvider**

The following properties, methods, and events are required for implementing the [**ISelectionProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionprovider?branch=master) interface.



| Required members                                                                                | Member type | Notes                                                                       |
|-------------------------------------------------------------------------------------------------|-------------|-----------------------------------------------------------------------------|
| [**CanSelectMultiple**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionprovider-get_canselectmultiple?branch=master)                        | Property    | None                                                                        |
| [**IsSelectionRequired**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionprovider-get_isselectionrequired?branch=master)                    | Property    | None                                                                        |
| [**GetSelection**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionprovider-getselection?branch=master)                                  | Method      | None                                                                        |
| [**UIA\_Selection\_InvalidatedEventId**](uiauto-event-ids.md#uia-selection-invalidatedeventid) | Event       | Raise this event when a selection in a container has changed significantly. |



 

The [**ISelectionProvider::IsSelectionRequired**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionprovider-get_isselectionrequired?branch=master) and [**CanSelectMultiple**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionprovider-get_canselectmultiple?branch=master) properties can be dynamic. For example, the initial state of a control might not have any items selected by default, indicating that **IsSelectionRequired** is false. However, after an item is selected, the control must always have at least one item selected. Similarly, in rare cases, a control might allow multiple items to be selected on initialization, but subsequently allow only single selections to be made.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[SelectionItem Control Pattern](uiauto-implementingselectionitem.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




