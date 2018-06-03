---
title: IAccessibleEx Implementation Guidelines
description: The Microsoft UI Automation core can retrieve all Microsoft Active Accessibility properties for any accessible object exposed by a server through the IAccessible interface.
ms.assetid: d047127c-1be2-4f34-bb97-330b5509ca0d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAccessibleEx Implementation Guidelines

The Microsoft UI Automation core can retrieve all Microsoft Active Accessibility properties for any accessible object exposed by a server through the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface. When implementing [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex), you must expose only those aspects of UI functionality that cannot otherwise be exposed through existing Microsoft Active Accessibility properties. This topic identifies the UI Automation properties and control patterns that represent UI functionality that has no counterpart in Microsoft Active Accessibility—they are the properties and control patterns that you can expose in an **IAccessibleEx** implementation.

This topic contains the following sections:

-   [Properties](#properties)
-   [Control Patterns](#control-patterns)
-   [WinEvents for UI Automation Property Changed Events](#winevents-for-ui-automation-property-changed-events)
-   [Related topics](#related-topics)

## Properties

The following UI Automation properties do not overlap with Microsoft Active Accessibility functionality. They can be used in an [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) implementation:

-   AriaProperties
-   AriaRole
-   AutomationId
-   ClassName
-   ClickablePoint
-   ControllerFor
-   Culture
-   DescribedBy
-   FlowsTo
-   FrameworkId
-   IsContentElement
-   IsControlElement
-   IsDataValidForForm
-   IsRequiredForForm
-   ItemStatus
-   ItemType
-   LabeledBy
-   LocalizedControlType
-   Orientation

Although the AcceleratorKey and AccessKey UI Automation properties do overlap with the accKeyboardShortcut Microsoft Active Accessibility property, you can still use them in an [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) implementation for controls that have both an access key and an accelerator. Similarly, the ControlType UI Automation property overlaps with the Microsoft Active Accessibility accRole property, but you can still use it in an **IAccessibleEx** implementation to define a more specific role for a control.

Because the following UI Automation element properties are already covered by Microsoft Active Accessibility properties, there is no need to use them in an [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) implementation.



| UI Automation Property | Microsoft Active Accessibility Equivalent                                                                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BoundingRectangle      | accLocation                                                                                                                                                                   |
| HasKeyboardFocus       | accState, [**STATE\_SYSTEM\_FOCUSED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_FOCUSED**)                                                                                       |
| IsEnabled              | accState, [**STATE\_SYSTEM\_UNAVAILABLE**](https://www.bing.com/search?q=**STATE\_SYSTEM\_UNAVAILABLE**)                                                                               |
| IsKeyboardFocusable    | accState, [**STATE\_SYSTEM\_FOCUSABLE**](https://www.bing.com/search?q=**STATE\_SYSTEM\_FOCUSABLE**)                                                                                   |
| IsPassword             | accState, [**STATE\_SYSTEM\_PROTECTED**](https://www.bing.com/search?q=**STATE\_SYSTEM\_PROTECTED**)                                                                                   |
| HelpText               | accHelp                                                                                                                                                                       |
| Name                   | accName                                                                                                                                                                       |
| NativeWindowHandle     | [**WindowFromAccessibleObject**](/windows/desktop/api/Oleacc/nf-oleacc-windowfromaccessibleobject)                                                                                                              |
| IsOffscreen            | accState, [**STATE\_SYSTEM\_INVISIBLE**](https://www.bing.com/search?q=**STATE\_SYSTEM\_INVISIBLE**)/[**STATE\_SYSTEM\_OFFSCREEN**](https://www.bing.com/search?q=**STATE\_SYSTEM\_OFFSCREEN**) |
| ProcessId              | Provided by UI Automation core                                                                                                                                                |



 

For any unsupported UI Automation property, your implementation of the [**IRawElementProviderSimple::GetPropertyValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-getpropertyvalue) method should set the *pRetVal* parameter to VT\_EMPTY, and return S\_OK. Returning [**UIA\_E\_NOTSUPPORTED**](https://www.bing.com/search?q=**UIA\_E\_NOTSUPPORTED**) may cause the MSAA-to-UIA Proxy to remove the default mapping for the corresponding property.

## Control Patterns

The following UI Automation control patterns do not overlap with Microsoft Active Accessibility functionality. They can be used in an [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) implementation:

-   Dock
-   ExpandCollapse
-   Grid
-   GridItem
-   MultipleView
-   RangeValue
-   Scroll
-   ScrollItem
-   SynchronizedInput
-   Table
-   TableItem
-   Transform

For the RangeValue and Transform control patterns, some methods overlap between the UI Automation control pattern and Microsoft Active Accessibility methods. In these cases, both must be implemented. For example, both Microsoft Active Accessibility's [**IAccessible::get\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accvalue) and [**IAccessible::put\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-put_accvalue) methods must both be implemented, as must the UI Automation[**IRangeValueProvider::Value**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_value) and [**IRangeValueProvider::SetValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-setvalue) methods. Internally, an implementation can share code for these. This requirement to implement both sets avoids having a partial implementation of a pattern interface while keeping the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface usable by existing Microsoft Active Accessibility clients.

The following UI Automation control patterns are not required when the control has one of the roles outlined below; otherwise, they should be explicitly supported if relevant.



| UI Automation Control Pattern | Microsoft Active Accessibility Role                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InvokePattern                 | [**ROLE\_SYSTEM\_PUSHBUTTON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_PUSHBUTTON**), [**ROLE\_SYSTEM\_MENUITEM**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_MENUITEM**), [**ROLE\_SYSTEM\_BUTTONDROPDOWN**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_BUTTONDROPDOWN**), [**ROLE\_SYSTEM\_SPLITBUTTON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_SPLITBUTTON**), and any other role where the value of the accDefaultAction property is not **NULL**. |
| SelectionItemPattern          | [**ROLE\_SYSTEM\_LISTITEM**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_LISTITEM**), [**ROLE\_SYSTEM\_RADIOBUTTON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_RADIOBUTTON**)                                                                                                                                                                                                                                                 |
| SelectionPattern              | [**ROLE\_SYSTEM\_LIST**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_LIST**)                                                                                                                                                                                                                                                                                                                                    |
| TogglePattern                 | [**ROLE\_SYSTEM\_CHECKBUTTON**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_CHECKBUTTON**)                                                                                                                                                                                                                                                                                                                      |
| ValuePattern                  | [**ROLE\_SYSTEM\_TEXT**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_TEXT**) (when it is not read-only), [**ROLE\_SYSTEM\_PROGRESSBAR**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_PROGRESSBAR**), [**ROLE\_SYSTEM\_COMBOBOX**](https://www.bing.com/search?q=**ROLE\_SYSTEM\_COMBOBOX**), and any other role when the value of the accValue property is not **NULL**.                                                                            |
| WindowPattern                 | Automatically supported on top-level Microsoft Win32 **HWND**s.                                                                                                                                                                                                                                                                                                                                |



 

## WinEvents for UI Automation Property Changed Events

In addition to the events defined for [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible), the following event identifiers are also defined and may be used with an [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) implementation as property changed events for corresponding UI Automation properties. These use the same mechanism as the events defined for **IAccessible**. For more information, see [WinEvents](winevents-collision169.md).



| WinEvent ID for IAccessibleEx Implementations                                                                                              | Related WinEvent Id from Microsoft Active Accessibility                                |
|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**UIA\_AriaPropertiesPropertyId**](https://www.bing.com/search?q=**UIA\_AriaPropertiesPropertyId**)                                    | None                                                                                   |
| [**UIA\_AriaRolePropertyId**](https://www.bing.com/search?q=**UIA\_AriaRolePropertyId**)                                                | None                                                                                   |
| [**UIA\_ControllerForPropertyId**](https://www.bing.com/search?q=**UIA\_ControllerForPropertyId**)                                      | None                                                                                   |
| [**UIA\_DescribedByPropertyId**](https://www.bing.com/search?q=**UIA\_DescribedByPropertyId**)                                          | None                                                                                   |
| [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](https://www.bing.com/search?q=**UIA\_ExpandCollapseExpandCollapseStatePropertyId**) | [**EVENT\_OBJECT\_STATECHANGE**](https://www.bing.com/search?q=**EVENT\_OBJECT\_STATECHANGE**)         |
| [**UIA\_FlowsToPropertyId**](https://www.bing.com/search?q=**UIA\_FlowsToPropertyId**)                                                  | None                                                                                   |
| [**UIA\_InputDiscardedEventId**](https://www.bing.com/search?q=**UIA\_InputDiscardedEventId**)                                                           | None                                                                                   |
| [**UIA\_InputReachedOtherElementEventId**](https://www.bing.com/search?q=**UIA\_InputReachedOtherElementEventId**)                                       | None                                                                                   |
| [**UIA\_InputReachedTargetEventId**](https://www.bing.com/search?q=**UIA\_InputReachedTargetEventId**)                                                   | None                                                                                   |
| [**UIA\_IsDataValidForFormPropertyId**](https://www.bing.com/search?q=**UIA\_IsDataValidForFormPropertyId**)                            | None                                                                                   |
| [**UIA\_IsEnabledPropertyId**](https://www.bing.com/search?q=**UIA\_IsEnabledPropertyId**)                                              | [**EVENT\_OBJECT\_STATECHANGE**](https://www.bing.com/search?q=**EVENT\_OBJECT\_STATECHANGE**)         |
| [**UIA\_ItemStatusPropertyId**](https://www.bing.com/search?q=**UIA\_ItemStatusPropertyId**)                                            | None                                                                                   |
| [**UIA\_MultipleViewCurrentViewPropertyId**](https://www.bing.com/search?q=**UIA\_MultipleViewCurrentViewPropertyId**)                     | None                                                                                   |
| [**UIA\_ScrollHorizontallyScrollablePropertyId**](https://www.bing.com/search?q=**UIA\_ScrollHorizontallyScrollablePropertyId**)           | None                                                                                   |
| [**UIA\_ScrollHorizontalScrollPercentPropertyId**](https://www.bing.com/search?q=**UIA\_ScrollHorizontalScrollPercentPropertyId**)         | [**EVENT\_OBJECT\_CONTENTSCROLLED**](https://www.bing.com/search?q=**EVENT\_OBJECT\_CONTENTSCROLLED**) |
| [**UIA\_ScrollHorizontalViewSizePropertyId**](https://www.bing.com/search?q=**UIA\_ScrollHorizontalViewSizePropertyId**)                   | None                                                                                   |
| [**UIA\_ScrollVerticallyScrollablePropertyId**](https://www.bing.com/search?q=**UIA\_ScrollVerticallyScrollablePropertyId**)               | None                                                                                   |
| [**UIA\_ScrollVerticalScrollPercentPropertyId**](https://www.bing.com/search?q=**UIA\_ScrollVerticalScrollPercentPropertyId**)             | [**EVENT\_OBJECT\_CONTENTSCROLLED**](https://www.bing.com/search?q=**EVENT\_OBJECT\_CONTENTSCROLLED**) |
| [**UIA\_ScrollVerticalViewSizePropertyId**](https://www.bing.com/search?q=**UIA\_ScrollVerticalViewSizePropertyId**)                       | None                                                                                   |
| [**UIA\_ToggleToggleStatePropertyId**](https://www.bing.com/search?q=**UIA\_ToggleToggleStatePropertyId**)                                 | [**EVENT\_OBJECT\_STATECHANGE**](https://www.bing.com/search?q=**EVENT\_OBJECT\_STATECHANGE**)         |



 

For the events above that have an EVENT\_OBJECT\_ value listed after them, and [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) implementation should fire this event in addition to the listed changed event. This enables existing **IAccessibleEx** client code to continue working, while conveying more granular event information to interested clients.

## Related topics

<dl> <dt>

[WinEvents](winevents-collision169.md)
</dt> <dt>

[The IAccessibleEx Interface](iaccessibleex.md)
</dt> </dl>

 

 




