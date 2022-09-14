---
title: UI Automation and Active Accessibility
description: Microsoft Active Accessibility is the legacy API that was introduced in Windows 95, and was designed to make Windows applications accessible.
ms.assetid: 6fc92e67-b94b-4ba3-9f5d-42be6072f110
keywords:
- UI Automation,Microsoft Active Accessibility
- UI Automation,accessibility
- UI Automation,Active Accessibility
- UI Automation,programming languages
- UI Automation,tree views
- UI Automation,navigation
- UI Automation,control types
- accessibility
- Active Accessibility
- Microsoft Active Accessibility
- control types,about
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation and Active Accessibility

Microsoft Active Accessibility is the legacy API that was introduced in Windows 95, and was designed to make Windows applications accessible. Microsoft UI Automation is the new accessibility model for Windows and is intended to address the needs of assistive technology products and automated testing tools. UI Automation offers many improvements over Microsoft Active Accessibility. This topic explains the differences between the two technologies.

This topic contains the following sections.

-   [Programming Languages](#programming-languages)
-   [Servers and Clients](#servers-and-clients)
-   [UI Elements](#ui-elements)
-   [Tree Views and Navigation](#tree-views-and-navigation)
-   [Roles and Control Types](#roles-and-control-types)
-   [States and Properties](#states-and-properties)
-   [Events](#events)
-   [Accessing Active Accessibility Properties and Objects from UI Automation](#accessing-active-accessibility-properties-and-objects-from-ui-automation)
-   [Related topics](#related-topics)

## Programming Languages

Microsoft Active Accessibility is based on the Component Object Model (COM) with support for dual interfaces, and therefore, is programmable in C/C++ and scripting languages.

When UI Automation was introduced, the client API was limited to managed code, while the provider API included both managed and unmanaged implementations. With Windows 7, a new COM-based client API was introduced to make it easier to program UI Automation client applications in C/C++.

## Servers and Clients

In Microsoft Active Accessibility, servers and clients communicate directly, largely through the server implementation of the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface.

In UI Automation, a core service lies between the server (provider) and the client. The core service makes calls to the interfaces implemented by providers and provides additional services, such as generating unique run-time identifiers for UI elements. Client applications gain access to this core service by creating a [**CUIAutomation**](/previous-versions/windows/desktop/legacy/ff384838(v=vs.85)) object. This object supports a set of client interfaces that are separate from the provider interfaces. For more information, see [Creating the CUIAutomation Object](uiauto-creatingcuiautomation.md).

UI Automation providers can provide information to Microsoft Active Accessibility clients, and Microsoft Active Accessibility servers can provide information to UI Automation client applications. However, because Microsoft Active Accessibility does not expose as much information as UI Automation, the two models are not fully compatible.

## UI Elements

Microsoft Active Accessibility presents a UI element as an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface paired with a child identifier. It is difficult to compare two **IAccessible** pointers to determine if they refer to the same element.

In UI Automation, every element is represented as an object that exposes the [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface to clients. Elements can be compared by their run-time identifiers, which are retrieved by using [**IUIAutomationElement::GetRuntimeId**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getruntimeid).

## Tree Views and Navigation

The UI elements on the screen can be seen as a tree structure with the desktop as the root, application windows as immediate children, and elements within applications as further descendants.

In Microsoft Active Accessibility, many UI elements that are irrelevant to end users are exposed in the tree structure. Client applications must examine all elements in the tree to determine which elements are meaningful.

UI Automation client applications see the UI through a filtered view. The view contains only elements that give information to the user or that the user can interact with. Predefined views that include only control elements and only content elements are available, and client applications can define custom views. UI Automation makes it easier to describe the UI to the user, and to help the user interact with applications.

In Microsoft Active Accessibility, navigation between elements is spatial, for example, moving to the element that lies to the left on the screen, logical, for example, moving to the next menu item or the next item in the tab order in a dialog box, or hierarchical, for example, moving to the first child element in a container or from a child element to its parent element. Hierarchical navigation is complicated by the fact that child elements are not always objects that implement [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible).

In UI Automation, all UI elements are COM objects that expose the [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface and support the same basic functionality. From the standpoint of the provider, COM objects implement an interface that is inherited from [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple). Navigation is mainly hierarchical; that is, from parents to children, and from one sibling to the next. However, navigation between siblings has a logical element, as it may follow the tab order. A client can navigate from any starting-point, using any filtered view of the tree, by using [**IUIAutomationTreeWalker**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtreewalker). A client can also navigate to particular children or descendants by using [**IUIAutomationElement::FindFirst**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findfirst) and [**IUIAutomationElement::FindAll**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findall). For example, it is easy to retrieve all elements in a dialog box that support a specified control pattern.

Navigation in UI Automation is more consistent than in Microsoft Active Accessibility. Some elements, such as drop-down lists and pop-up windows, appear twice in the Microsoft Active Accessibility tree, and navigation from those elements may have unexpected results. It is difficult to implement Microsoft Active Accessibility properly for a rebar control. UI Automation enables reparenting and repositioning, so that an element can be placed anywhere in the tree, despite the hierarchy imposed by ownership of windows.

## Roles and Control Types

Microsoft Active Accessibility uses the accRole property ([**IAccessible::get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)) to retrieve a description of the element role in the UI, such as [**ROLE\_SYSTEM\_SLIDER**](object-roles.md) or [**ROLE\_SYSTEM\_MENUITEM**](object-roles.md). The role of an element is the main clue to its available functionality. Interaction with a control is achieved by using fixed methods such as [**IAccessible::accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect) and [**IAccessible::accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction). The interaction between the client application and the UI is limited to what can be done through [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible).

In contrast, UI Automation decouples the control type of the element, which is described by the [**IUIAutomationElement::CurrentControlType**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentcontroltype) (or [**IUIAutomationElement::CachedControlType**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_cachedcontroltype)) property, from its expected functionality. Functionality is determined by the control patterns that are supported by the provider through its implementation of specialized interfaces. Control patterns can be combined to describe the full set of functionality that is supported by a particular UI element. Some providers are required to support a particular control pattern. For example, the provider for a check box must support the [Toggle](uiauto-implementingtoggle.md) control pattern. Other providers are required to support one or more of a set of control patterns. For example, a button must support either the Toggle or the [Invoke](uiauto-implementinginvoke.md) control pattern. Still others support no control patterns. For example, a pane that cannot be moved, resized, or docked has no control patterns.

UI Automation supports custom controls, which are identified by the [**UIA\_CustomControlTypeId**](uiauto-controltype-ids.md) constant and can be described by the [**IUIAutomationElement::CurrentLocalizedControlType**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentlocalizedcontroltype) (or [**IUIAutomationElement::CachedLocalizedControlType**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_cachedlocalizedcontroltype)) property.

The following table maps Microsoft Active Accessibility[object roles](object-roles.md) to UI Automation control types.



| Active Accessibility role                                                   | UI Automation control type                                                                     |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md)     | [Button](uiauto-supportbuttoncontroltype.md)                                                  |
| [**ROLE\_SYSTEM\_CLIENT**](object-roles.md)             | [Calendar](uiauto-supportcalendarcontroltype.md)                                              |
| [**ROLE\_SYSTEM\_CHECKBUTTON**](object-roles.md)   | [CheckBox](uiauto-supportcheckboxcontroltype.md)                                              |
| [**ROLE\_SYSTEM\_COMBOBOX**](object-roles.md)         | [ComboBox](uiauto-supportcomboboxcontroltype.md)                                              |
| [**ROLE\_SYSTEM\_CLIENT**](object-roles.md)             | See [Custom Control Types](uiauto-designingcustompropseventpatterns.md). |
| [**ROLE\_SYSTEM\_LIST**](object-roles.md)                 | [DataGrid](uiauto-supportdatagridcontroltype.md)                                              |
| [**ROLE\_SYSTEM\_LISTITEM**](object-roles.md)         | [DataItem](uiauto-supportdataitemcontroltype.md)                                              |
| [**ROLE\_SYSTEM\_DOCUMENT**](object-roles.md)         | [Document](uiauto-supportdocumentcontroltype.md)                                              |
| [**ROLE\_SYSTEM\_TEXT**](object-roles.md)                 | [Edit](uiauto-supporteditcontroltype.md)                                                      |
| [**ROLE\_SYSTEM\_GROUPING**](object-roles.md)         | [Group](uiauto-supportgroupcontroltype.md)                                                    |
| [**ROLE\_SYSTEM\_LIST**](object-roles.md)                 | [Header](uiauto-supportheadercontroltype.md)                                                  |
| [**ROLE\_SYSTEM\_COLUMNHEADER**](object-roles.md) | [HeaderItem](uiauto-supportheaderitemcontroltype.md)                                          |
| [**ROLE\_SYSTEM\_LINK**](object-roles.md)                 | [Hyperlink](uiauto-supporthyperlinkcontroltype.md)                                            |
| [**ROLE\_SYSTEM\_GRAPHIC**](object-roles.md)           | [Image](uiauto-supportimagecontroltype.md)                                                    |
| [**ROLE\_SYSTEM\_LIST**](object-roles.md)                 | [List](uiauto-supportlistcontroltype.md)                                                      |
| [**ROLE\_SYSTEM\_LISTITEM**](object-roles.md)         | [ListItem](uiauto-supportlistitemcontroltype.md)                                              |
| [**ROLE\_SYSTEM\_MENUPOPUP**](object-roles.md)       | [Menu](uiauto-supportmenucontroltype.md)                                                      |
| [**ROLE\_SYSTEM\_MENUBAR**](object-roles.md)           | [MenuBar](uiauto-supportmenubarcontroltype.md)                                                |
| [**ROLE\_SYSTEM\_MENUITEM**](object-roles.md)         | [MenuItem](uiauto-supportmenuitemcontroltype.md)                                              |
| [**ROLE\_SYSTEM\_PANE**](object-roles.md)                 | [Pane](uiauto-supportpanecontroltype.md)                                                      |
| [**ROLE\_SYSTEM\_PROGRESSBAR**](object-roles.md)   | [ProgressBar](uiauto-supportprogressbarcontroltype.md)                                        |
| [**ROLE\_SYSTEM\_RADIOBUTTON**](object-roles.md)   | [RadioButton](uiauto-supportradiobuttoncontroltype.md)                                        |
| [**ROLE\_SYSTEM\_SCROLLBAR**](object-roles.md)       | [ScrollBar](uiauto-supportscrollbarcontroltype.md)                                            |
| [**ROLE\_SYSTEM\_SEPARATOR**](object-roles.md)       | [Separator](uiauto-supportseparatorcontroltype.md)                                            |
| [**ROLE\_SYSTEM\_SLIDER**](object-roles.md)             | [Slider](uiauto-supportslidercontroltype.md)                                                  |
| [**ROLE\_SYSTEM\_SPINBUTTON**](object-roles.md)     | [Spinner](uiauto-supportspinnercontroltype.md)                                                |
| [**ROLE\_SYSTEM\_SPLITBUTTON**](object-roles.md)   | [SplitButton](uiauto-supportsplitbuttoncontroltype.md)                                        |
| [**ROLE\_SYSTEM\_STATUSBAR**](object-roles.md)       | [StatusBar](uiauto-supportstatusbarcontroltype.md)                                            |
| [**ROLE\_SYSTEM\_PAGETABLIST**](object-roles.md)   | [Tab](uiauto-supporttabcontroltype.md)                                                        |
| [**ROLE\_SYSTEM\_PAGETAB**](object-roles.md)           | [TabItem](uiauto-supporttabitemcontroltype.md)                                                |
| [**ROLE\_SYSTEM\_TABLE**](object-roles.md)               | [Table](uiauto-supporttablecontroltype.md)                                                    |
| [**ROLE\_SYSTEM\_STATICTEXT**](object-roles.md)     | [Text](uiauto-supporttextcontroltype.md)                                                      |
| [**ROLE\_SYSTEM\_INDICATOR**](object-roles.md)       | [Thumb](uiauto-supportthumbcontroltype.md)                                                    |
| [**ROLE\_SYSTEM\_TITLEBAR**](object-roles.md)         | [TitleBar](uiauto-supporttitlebarcontroltype.md)                                              |
| [**ROLE\_SYSTEM\_TOOLBAR**](object-roles.md)           | [ToolBar](uiauto-supporttoolbarcontroltype.md)                                                |
| [**ROLE\_SYSTEM\_TOOLTIP**](object-roles.md)           | [ToolTip](uiauto-supporttooltipcontroltype.md)                                                |
| [**ROLE\_SYSTEM\_OUTLINE**](object-roles.md)           | [Tree](uiauto-supporttreecontroltype.md)                                                      |
| [**ROLE\_SYSTEM\_OUTLINEITEM**](object-roles.md)   | [TreeItem](uiauto-supporttreeitemcontroltype.md)                                              |
| [**ROLE\_SYSTEM\_WINDOW**](object-roles.md)             | [Window](uiauto-supportwindowcontroltype.md)                                                  |



 

## States and Properties

Microsoft Active Accessibility elements support a common set of properties. Some properties, such as accState, must describe different conditions, depending on the element role. Servers must implement all methods of [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) that return a property, even those properties that are not relevant to the element.

UI Automation defines additional properties, some of which correspond to states in Microsoft Active Accessibility. Some properties are common to all elements, but other properties are specific to control types and control patterns. A UI Automation provider does not have to implement irrelevant properties, but can return a null value for any properties it does not support. The UI Automation core service can obtain some properties from the default window provider, and these are amalgamated with properties explicitly implemented by the provider.

As well as supporting many more properties, UI Automation enables better performance by allowing properties to be cached.

The following table shows the correspondence between some properties in the two models. For descriptions of the UI Automation property IDs, see [Automation Element Property Identifiers](uiauto-automation-element-propids.md).



| Active Accessibility property accessor                                               | UI Automation property ID                                                                                                                                                                                | Remarks                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) | [**UIA\_AccessKeyPropertyId**](uiauto-automation-element-propids.md) or [**UIA\_AcceleratorKeyPropertyId**](uiauto-automation-element-propids.md) | [**UIA\_AccessKeyPropertyId**](uiauto-automation-element-propids.md) takes precedence if both are present.                                                                                                                                                                                                         |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)                         | [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                                                                                                      |                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)                         | [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                                                                                                        | See the previous table for mapping roles to control types.                                                                                                                                                                                                                                                                                  |
| [**get\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accvalue)                       | [**UIA\_ValueValuePropertyId**](uiauto-control-pattern-propids.md) or [**UIA\_RangeValueValuePropertyId**](uiauto-control-pattern-propids.md)   | Valid only for control types that support [**IUIAutomationValuePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationvaluepattern) or [**IUIAutomationRangeValuePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationrangevaluepattern). Range values are normalized to 0-100, to be consistent with Microsoft Active Accessibility behavior. Values are represented as strings. |
| [**get\_accHelp**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelp)                         | [**UIA\_HelpTextPropertyId**](uiauto-automation-element-propids.md)                                                                                                              |                                                                                                                                                                                                                                                                                                                                             |
| [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)                          | [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)                                                                                            |                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accDescription**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdescription)           | Not supported.                                                                                                                                                                                           | accDescription did not have a clear specification in Microsoft Active Accessibility, which resulted in servers placing different pieces of information in this property.                                                                                                                                                                    |
| [**get\_accHelpTopic**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelptopic)               | Not supported.                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                             |



 

The following table shows the UI Automation property IDs that correspond to Microsoft Active Accessibility [object state constants](object-state-constants.md).



| Active Accessibility state                                                                    | UI Automation property                                                                                                                                                                                                                                                                                                                                                               | Triggers WinEvent state change? |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| [**STATE\_SYSTEM\_CHECKED**](object-state-constants.md)                 | [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md) for check box. [**UIA\_SelectionItemIsSelectedPropertyId**](uiauto-control-pattern-propids.md) for radio button.                                                                                                                   | Y                               |
| [**STATE\_SYSTEM\_COLLAPSED**](object-state-constants.md)             | [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](uiauto-control-pattern-propids.md) (value = [**ExpandCollapseState\_Collapsed**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-expandcollapsestate)).                                                                                                                         | Y                               |
| [**STATE\_SYSTEM\_EXPANDED**](object-state-constants.md)               | [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](uiauto-control-pattern-propids.md) (value = [**ExpandCollapseState\_Expanded**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-expandcollapsestate) or [**ExpandCollapseState\_PartiallyExpanded**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-expandcollapsestate)). | Y                               |
| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md)             | [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md).                                                                                                                                                                                                                                                                   | N                               |
| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md)                 | [**UIA\_HasKeyboardFocusPropertyId**](uiauto-automation-element-propids.md).                                                                                                                                                                                                                                                                         | N                               |
| [**STATE\_SYSTEM\_HASPOPUP**](object-state-constants.md)               | [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](uiauto-control-pattern-propids.md) for menu items.                                                                                                                                                                                                                           | N                               |
| [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md)             | [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) (value = True and [**IUIAutomationElement::GetClickablePoint**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getclickablepoint) fails).                                                                                                                                                         | N                               |
| [**STATE\_SYSTEM\_LINKED**](object-state-constants.md)                   | [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md) (value = [**UIA\_HyperlinkControlTypeId**](uiauto-controltype-ids.md)).                                                                                                                                                                                | N                               |
| [**STATE\_SYSTEM\_MIXED**](object-state-constants.md)                     | [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md) (value = [**ToggleState\_Indeterminate**](/windows/desktop/api/UIAutomationCore/ne-uiautomationcore-togglestate).                                                                                                                                                                              | N                               |
| [**STATE\_SYSTEM\_MOVEABLE**](object-state-constants.md)               | [**UIA\_TransformCanMovePropertyId**](uiauto-control-pattern-propids.md).                                                                                                                                                                                                                                                                            | N                               |
| [**STATE\_SYSTEM\_MULTISELECTABLE**](object-state-constants.md) | [**UIA\_SelectionCanSelectMultiplePropertyId**](uiauto-control-pattern-propids.md).                                                                                                                                                                                                                                                        | N                               |
| [**STATE\_SYSTEM\_OFFSCREEN**](object-state-constants.md)             | [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md).                                                                                                                                                                                                                                                                                   | N                               |
| [**STATE\_SYSTEM\_PROTECTED**](object-state-constants.md)             | [**UIA\_IsPasswordPropertyId**](uiauto-automation-element-propids.md).                                                                                                                                                                                                                                                                                     | N                               |
| [**STATE\_SYSTEM\_READONLY**](object-state-constants.md)               | [**UIA\_RangeValueIsReadOnlyPropertyId**](uiauto-control-pattern-propids.md) and [**UIA\_ValueIsReadOnlyPropertyId**](uiauto-control-pattern-propids.md).                                                                                                                                                         | N                               |
| [**STATE\_SYSTEM\_SELECTABLE**](object-state-constants.md)           | [**UIA\_IsSelectionItemPatternAvailablePropertyId**](uiauto-control-pattern-availability-propids.md) .                                                                                                                                                                                                                                | N                               |
| [**STATE\_SYSTEM\_SELECTED**](object-state-constants.md)               | [**UIA\_SelectionItemIsSelectedPropertyId**](uiauto-control-pattern-propids.md).                                                                                                                                                                                                                                                              | N                               |
| [**STATE\_SYSTEM\_SIZEABLE**](object-state-constants.md)               | [**UIA\_TransformCanResizePropertyId**](uiauto-control-pattern-propids.md).                                                                                                                                                                                                                                                                        | N                               |
| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md)         | [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md).                                                                                                                                                                                                                                                                                       | Y                               |



 

For a complete list of property IDs, see [Property Identifiers](uiauto-entry-propids.md).

## Events

Unlike Microsoft Active Accessibility, the event mechanism in UI Automation, does not rely on Windows event routing, which is closely tied to window handles, and does not require the client application to set up hooks. Subscriptions to events can be fine-tuned to particular parts of the tree, not just to particular events. Providers can also fine-tune raising events by keeping track of which events are being listened for.

It is also easier for clients to retrieve the elements that raise events because these are passed directly to the event callback. Properties of the element are prefetched automatically, if a cache request was supplied when the client subscribed to the event.

The following table shows the correspondence of Microsoft Active Accessibility [event constants](event-constants.md) and UI Automation event IDs.



| WinEvent                                                                                   | UI Automation Event ID                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EVENT\_OBJECT\_ACCELERATORCHANGE**](event-constants.md) | [**UIA\_AcceleratorKeyPropertyId**](uiauto-automation-element-propids.md) property change.                                                                                                                                                                                            |
| [**EVENT\_OBJECT\_CONTENTSCROLLED**](event-constants.md)     | [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) or [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property change on the associated scroll bars. |
| [**EVENT\_OBJECT\_CREATE**](event-constants.md)                       | [**UIA\_StructureChangedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                               |
| [**EVENT\_OBJECT\_DEFACTIONCHANGE**](event-constants.md)     | No equivalent.                                                                                                                                                                                                                                                                                                      |
| [**EVENT\_OBJECT\_DESCRIPTIONCHANGE**](event-constants.md) | No exact equivalent; perhaps [**UIA\_HelpTextPropertyId**](uiauto-automation-element-propids.md) or [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) property change.                                                    |
| [**EVENT\_OBJECT\_DESTROY**](event-constants.md)                     | [**UIA\_StructureChangedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                               |
| [**EVENT\_OBJECT\_FOCUS**](event-constants.md)                         | [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                   |
| [**EVENT\_OBJECT\_HELPCHANGE**](event-constants.md)               | [**UIA\_HelpTextPropertyId**](uiauto-automation-element-propids.md) change.                                                                                                                                                                                                                 |
| [**EVENT\_OBJECT\_HIDE**](event-constants.md)                           | [**UIA\_StructureChangedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                               |
| [**EVENT\_OBJECT\_LOCATIONCHANGE**](event-constants.md)       | [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property change.                                                                                                                                                                                      |
| [**EVENT\_OBJECT\_NAMECHANGE**](event-constants.md)               | [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) property change.                                                                                                                                                                                                                |
| [**EVENT\_OBJECT\_PARENTCHANGE**](event-constants.md)           | [**UIA\_StructureChangedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                               |
| [**EVENT\_OBJECT\_REORDER**](event-constants.md)                     | Not consistently used in Microsoft Active Accessibility. No directly corresponding event is defined in UI Automation.                                                                                                                                                                                               |
| [**EVENT\_OBJECT\_SELECTION**](event-constants.md)                 | [**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                    |
| [**EVENT\_OBJECT\_SELECTIONADD**](event-constants.md)           | [**UIA\_SelectionItem\_ElementAddedToSelectionEventId**](uiauto-event-ids.md).                                                                                                                                                                                    |
| [**EVENT\_OBJECT\_SELECTIONREMOVE**](event-constants.md)     | [**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md).                                                                                                                                                                            |
| [**EVENT\_OBJECT\_SELECTIONWITHIN**](event-constants.md)     | No equivalent.                                                                                                                                                                                                                                                                                                      |
| [**EVENT\_OBJECT\_SHOW**](event-constants.md)                           | [**UIA\_StructureChangedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                               |
| [**EVENT\_OBJECT\_STATECHANGE**](event-constants.md)             | Various property-changed events.                                                                                                                                                                                                                                                                                    |
| [**EVENT\_OBJECT\_VALUECHANGE**](event-constants.md)             | [**UIA\_RangeValueValuePropertyId**](uiauto-control-pattern-propids.md) and [**UIA\_ValueValuePropertyId**](uiauto-control-pattern-propids.md) changed.                                                                                                    |
| [**EVENT\_SYSTEM\_ALERT**](event-constants.md)                         | No equivalent.                                                                                                                                                                                                                                                                                                      |
| [**EVENT\_SYSTEM\_CAPTUREEND**](event-constants.md)               | No equivalent.                                                                                                                                                                                                                                                                                                      |
| [**EVENT\_SYSTEM\_CAPTURESTART**](event-constants.md)           | No equivalent.                                                                                                                                                                                                                                                                                                      |
| [**EVENT\_SYSTEM\_CONTEXTHELPEND**](event-constants.md)       | No equivalent.                                                                                                                                                                                                                                                                                                      |
| [**EVENT\_SYSTEM\_CONTEXTHELPSTART**](event-constants.md)   | No equivalent.                                                                                                                                                                                                                                                                                                      |
| [**EVENT\_SYSTEM\_DIALOGEND**](event-constants.md)                 | [**UIA\_Window\_WindowClosedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                        |
| [**EVENT\_SYSTEM\_DIALOGSTART**](event-constants.md)             | [**UIA\_Window\_WindowOpenedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                        |
| [**EVENT\_SYSTEM\_DRAGDROPEND**](event-constants.md)             | No equivalent.                                                                                                                                                                                                                                                                                                      |
| [**EVENT\_SYSTEM\_DRAGDROPSTART**](event-constants.md)         | No equivalent.                                                                                                                                                                                                                                                                                                      |
| [**EVENT\_SYSTEM\_FOREGROUND**](event-constants.md)               | [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                   |
| [**EVENT\_SYSTEM\_MENUEND**](event-constants.md)                     | [**UIA\_MenuModeEndEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                                         |
| [**EVENT\_SYSTEM\_MENUPOPUPEND**](event-constants.md)           | [**UIA\_MenuClosedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                                           |
| [**EVENT\_SYSTEM\_MENUPOPUPSTART**](event-constants.md)       | [**UIA\_MenuOpenedEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                                           |
| [**EVENT\_SYSTEM\_MENUSTART**](event-constants.md)                 | [**UIA\_MenuModeStartEventId**](uiauto-event-ids.md).                                                                                                                                                                                                                                     |
| [**EVENT\_SYSTEM\_MINIMIZEEND**](event-constants.md)             | [**UIA\_WindowWindowVisualStatePropertyId**](uiauto-control-pattern-propids.md) property change.                                                                                                                                                                             |
| [**EVENT\_SYSTEM\_MINIMIZESTART**](event-constants.md)         | [**UIA\_WindowWindowVisualStatePropertyId**](uiauto-control-pattern-propids.md) property change.                                                                                                                                                                             |
| [**EVENT\_SYSTEM\_MOVESIZEEND**](event-constants.md)             | [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property change.                                                                                                                                                                                      |
| [**EVENT\_SYSTEM\_MOVESIZESTART**](event-constants.md)         | [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property change.                                                                                                                                                                                      |
| [**EVENT\_SYSTEM\_SCROLLINGEND**](event-constants.md)           | [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) or [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property change.                               |
| [**EVENT\_SYSTEM\_SCROLLINGSTART**](event-constants.md)       | [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) or [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property change.                               |
| [**EVENT\_SYSTEM\_SOUND**](event-constants.md)                         | No equivalent.                                                                                                                                                                                                                                                                                                      |
| [**EVENT\_SYSTEM\_SWITCHEND**](event-constants.md)                 | No equivalent, but a [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md) event signals that a new application has received the focus.                                                                                                                                  |
| [**EVENT\_SYSTEM\_SWITCHSTART**](event-constants.md)             | No equivalent.                                                                                                                                                                                                                                                                                                      |
| No equivalent.                                                                             | [**UIA\_MultipleViewCurrentViewPropertyId**](uiauto-control-pattern-propids.md) property change.                                                                                                                                                                             |
| No equivalent.                                                                             | [**UIA\_ScrollHorizontallyScrollablePropertyId**](uiauto-control-pattern-propids.md) property change.                                                                                                                                                                   |
| No equivalent.                                                                             | [**UIA\_ScrollVerticallyScrollablePropertyId**](uiauto-control-pattern-propids.md) property change.                                                                                                                                                                       |
| No equivalent.                                                                             | [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property change.                                                                                                                                                                 |
| No equivalent.                                                                             | [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property change.                                                                                                                                                                     |
| No equivalent.                                                                             | [**UIA\_ScrollHorizontalViewSizePropertyId**](uiauto-control-pattern-propids.md) property change.                                                                                                                                                                           |
| No equivalent.                                                                             | [**UIA\_ScrollVerticalViewSizePropertyId**](uiauto-control-pattern-propids.md) property change.                                                                                                                                                                               |
| No equivalent.                                                                             | [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md) property change.                                                                                                                                                                                         |
| No equivalent.                                                                             | [**UIA\_WindowWindowVisualStatePropertyId**](uiauto-control-pattern-propids.md) property change                                                                                                                                                                              |
| No equivalent.                                                                             | [**UIA\_AsyncContentLoadedEventId**](uiauto-event-ids.md) event.                                                                                                                                                                                                                     |
| No equivalent.                                                                             | [**UIA\_ToolTipOpenedEventId**](uiauto-event-ids.md) event.                                                                                                                                                                                                                               |



 

## Accessing Active Accessibility Properties and Objects from UI Automation

A key feature of UI Automation that is not available in Microsoft Active Accessibility is the ability to fetch multiple properties with a single cross-process operation.

Existing Microsoft Active Accessibility clients can take advantage of this ability by using the [**IUIAutomationLegacyIAccessiblePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationlegacyiaccessiblepattern) interface. This interface represents a *control pattern* that exposes Microsoft Active Accessibility properties and methods on UI elements. When retrieving elements, an application can request that this control pattern and its properties be cached.

[**IUIAutomationLegacyIAccessiblePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationlegacyiaccessiblepattern) also enables clients to obtain Microsoft Active Accessibility properties from elements that have no native support for [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible).

Changes in the properties of an [**IUIAutomationLegacyIAccessiblePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationlegacyiaccessiblepattern) do not raise UI Automation events.

## Related topics

<dl> <dt>

[Adding UI Automation Functionality to Active Accessibility Servers](uiauto-usingiaccessibleex.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> <dt>

[UI Automation Properties Overview](uiauto-propertiesoverview.md)
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Events Overview](uiauto-eventsoverview.md)
</dt> <dt>

[Microsoft Active Accessibility](microsoft-active-accessibility.md)
</dt> </dl>

 

 
