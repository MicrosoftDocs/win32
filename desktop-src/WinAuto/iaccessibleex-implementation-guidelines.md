---
title: IAccessibleEx Implementation Guidelines
description: The Microsoft UI Automation core can retrieve all Microsoft Active Accessibility properties for any accessible object exposed by a server through the IAccessible interface.
ms.assetid: 'd047127c-1be2-4f34-bb97-330b5509ca0d'
---

# IAccessibleEx Implementation Guidelines

The Microsoft UI Automation core can retrieve all Microsoft Active Accessibility properties for any accessible object exposed by a server through the [**IAccessible**](iaccessible.md) interface. When implementing [**IAccessibleEx**](uiauto-iaccessibleex.md), you must expose only those aspects of UI functionality that cannot otherwise be exposed through existing Microsoft Active Accessibility properties. This topic identifies the UI Automation properties and control patterns that represent UI functionality that has no counterpart in Microsoft Active Accessibility—they are the properties and control patterns that you can expose in an **IAccessibleEx** implementation.

This topic contains the following sections:

-   [Properties](#properties)
-   [Control Patterns](#control-patterns)
-   [WinEvents for UI Automation Property Changed Events](#winevents-for-ui-automation-property-changed-events)
-   [Related topics](#related-topics)

## Properties

The following UI Automation properties do not overlap with Microsoft Active Accessibility functionality. They can be used in an [**IAccessibleEx**](uiauto-iaccessibleex.md) implementation:

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

Although the AcceleratorKey and AccessKey UI Automation properties do overlap with the accKeyboardShortcut Microsoft Active Accessibility property, you can still use them in an [**IAccessibleEx**](uiauto-iaccessibleex.md) implementation for controls that have both an access key and an accelerator. Similarly, the ControlType UI Automation property overlaps with the Microsoft Active Accessibility accRole property, but you can still use it in an **IAccessibleEx** implementation to define a more specific role for a control.

Because the following UI Automation element properties are already covered by Microsoft Active Accessibility properties, there is no need to use them in an [**IAccessibleEx**](uiauto-iaccessibleex.md) implementation.



| UI Automation Property | Microsoft Active Accessibility Equivalent                                                                                                                                     |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BoundingRectangle      | accLocation                                                                                                                                                                   |
| HasKeyboardFocus       | accState, [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused)                                                                                       |
| IsEnabled              | accState, [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable)                                                                               |
| IsKeyboardFocusable    | accState, [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)                                                                                   |
| IsPassword             | accState, [**STATE\_SYSTEM\_PROTECTED**](object-state-constants.md#state-system-protected)                                                                                   |
| HelpText               | accHelp                                                                                                                                                                       |
| Name                   | accName                                                                                                                                                                       |
| NativeWindowHandle     | [**WindowFromAccessibleObject**](windowfromaccessibleobject.md)                                                                                                              |
| IsOffscreen            | accState, [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible)/[**STATE\_SYSTEM\_OFFSCREEN**](object-state-constants.md#state-system-offscreen) |
| ProcessId              | Provided by UI Automation core                                                                                                                                                |



 

For any unsupported UI Automation property, your implementation of the [**IRawElementProviderSimple::GetPropertyValue**](uiauto-irawelementprovidersimple-getpropertyvalue.md) method should set the *pRetVal* parameter to VT\_EMPTY, and return S\_OK. Returning [**UIA\_E\_NOTSUPPORTED**](uiauto-error-codes.md#uia-e-notsupported) may cause the MSAA-to-UIA Proxy to remove the default mapping for the corresponding property.

## Control Patterns

The following UI Automation control patterns do not overlap with Microsoft Active Accessibility functionality. They can be used in an [**IAccessibleEx**](uiauto-iaccessibleex.md) implementation:

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

For the RangeValue and Transform control patterns, some methods overlap between the UI Automation control pattern and Microsoft Active Accessibility methods. In these cases, both must be implemented. For example, both Microsoft Active Accessibility's [**IAccessible::get\_accValue**](iaccessible-iaccessible--get-accvalue.md) and [**IAccessible::put\_accValue**](iaccessible-iaccessible--put-accvalue.md) methods must both be implemented, as must the UI Automation[**IRangeValueProvider::Value**](uiauto-irangevalueprovider-value.md) and [**IRangeValueProvider::SetValue**](uiauto-irangevalueprovider-setvalue.md) methods. Internally, an implementation can share code for these. This requirement to implement both sets avoids having a partial implementation of a pattern interface while keeping the [**IAccessible**](iaccessible.md) interface usable by existing Microsoft Active Accessibility clients.

The following UI Automation control patterns are not required when the control has one of the roles outlined below; otherwise, they should be explicitly supported if relevant.



| UI Automation Control Pattern | Microsoft Active Accessibility Role                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InvokePattern                 | [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md#role-system-pushbutton), [**ROLE\_SYSTEM\_MENUITEM**](object-roles.md#role-system-menuitem), [**ROLE\_SYSTEM\_BUTTONDROPDOWN**](object-roles.md#role-system-buttondropdown), [**ROLE\_SYSTEM\_SPLITBUTTON**](object-roles.md#role-system-splitbutton), and any other role where the value of the accDefaultAction property is not **NULL**. |
| SelectionItemPattern          | [**ROLE\_SYSTEM\_LISTITEM**](object-roles.md#role-system-listitem), [**ROLE\_SYSTEM\_RADIOBUTTON**](object-roles.md#role-system-radiobutton)                                                                                                                                                                                                                                                 |
| SelectionPattern              | [**ROLE\_SYSTEM\_LIST**](object-roles.md#role-system-list)                                                                                                                                                                                                                                                                                                                                    |
| TogglePattern                 | [**ROLE\_SYSTEM\_CHECKBUTTON**](object-roles.md#role-system-checkbutton)                                                                                                                                                                                                                                                                                                                      |
| ValuePattern                  | [**ROLE\_SYSTEM\_TEXT**](object-roles.md#role-system-text) (when it is not read-only), [**ROLE\_SYSTEM\_PROGRESSBAR**](object-roles.md#role-system-progressbar), [**ROLE\_SYSTEM\_COMBOBOX**](object-roles.md#role-system-combobox), and any other role when the value of the accValue property is not **NULL**.                                                                            |
| WindowPattern                 | Automatically supported on top-level Microsoft Win32 **HWND**s.                                                                                                                                                                                                                                                                                                                                |



 

## WinEvents for UI Automation Property Changed Events

In addition to the events defined for [**IAccessible**](iaccessible.md), the following event identifiers are also defined and may be used with an [**IAccessibleEx**](uiauto-iaccessibleex.md) implementation as property changed events for corresponding UI Automation properties. These use the same mechanism as the events defined for **IAccessible**. For more information, see [WinEvents](winevents-collision169.md).



| WinEvent ID for IAccessibleEx Implementations                                                                                              | Related WinEvent Id from Microsoft Active Accessibility                                |
|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**UIA\_AriaPropertiesPropertyId**](uiauto-automation-element-propids.md#uia-ariapropertiespropertyid)                                    | None                                                                                   |
| [**UIA\_AriaRolePropertyId**](uiauto-automation-element-propids.md#uia-ariarolepropertyid)                                                | None                                                                                   |
| [**UIA\_ControllerForPropertyId**](uiauto-automation-element-propids.md#uia-controllerforpropertyid)                                      | None                                                                                   |
| [**UIA\_DescribedByPropertyId**](uiauto-automation-element-propids.md#uia-describedbypropertyid)                                          | None                                                                                   |
| [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](uiauto-control-pattern-propids.md#uia-expandcollapseexpandcollapsestatepropertyid) | [**EVENT\_OBJECT\_STATECHANGE**](event-constants.md#event-object-statechange)         |
| [**UIA\_FlowsToPropertyId**](uiauto-automation-element-propids.md#uia-flowstopropertyid)                                                  | None                                                                                   |
| [**UIA\_InputDiscardedEventId**](uiauto-event-ids.md#uia-inputdiscardedeventid)                                                           | None                                                                                   |
| [**UIA\_InputReachedOtherElementEventId**](uiauto-event-ids.md#uia-inputreachedotherelementeventid)                                       | None                                                                                   |
| [**UIA\_InputReachedTargetEventId**](uiauto-event-ids.md#uia-inputreachedtargeteventid)                                                   | None                                                                                   |
| [**UIA\_IsDataValidForFormPropertyId**](uiauto-automation-element-propids.md#uia-isdatavalidforformpropertyid)                            | None                                                                                   |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md#uia-isenabledpropertyid)                                              | [**EVENT\_OBJECT\_STATECHANGE**](event-constants.md#event-object-statechange)         |
| [**UIA\_ItemStatusPropertyId**](uiauto-automation-element-propids.md#uia-itemstatuspropertyid)                                            | None                                                                                   |
| [**UIA\_MultipleViewCurrentViewPropertyId**](uiauto-control-pattern-propids.md#uia-multipleviewcurrentviewpropertyid)                     | None                                                                                   |
| [**UIA\_ScrollHorizontallyScrollablePropertyId**](uiauto-control-pattern-propids.md#uia-scrollhorizontallyscrollablepropertyid)           | None                                                                                   |
| [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md#uia-scrollhorizontalscrollpercentpropertyid)         | [**EVENT\_OBJECT\_CONTENTSCROLLED**](event-constants.md#event-object-contentscrolled) |
| [**UIA\_ScrollHorizontalViewSizePropertyId**](uiauto-control-pattern-propids.md#uia-scrollhorizontalviewsizepropertyid)                   | None                                                                                   |
| [**UIA\_ScrollVerticallyScrollablePropertyId**](uiauto-control-pattern-propids.md#uia-scrollverticallyscrollablepropertyid)               | None                                                                                   |
| [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md#uia-scrollverticalscrollpercentpropertyid)             | [**EVENT\_OBJECT\_CONTENTSCROLLED**](event-constants.md#event-object-contentscrolled) |
| [**UIA\_ScrollVerticalViewSizePropertyId**](uiauto-control-pattern-propids.md#uia-scrollverticalviewsizepropertyid)                       | None                                                                                   |
| [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md#uia-toggletogglestatepropertyid)                                 | [**EVENT\_OBJECT\_STATECHANGE**](event-constants.md#event-object-statechange)         |



 

For the events above that have an EVENT\_OBJECT\_ value listed after them, and [**IAccessibleEx**](uiauto-iaccessibleex.md) implementation should fire this event in addition to the listed changed event. This enables existing **IAccessibleEx** client code to continue working, while conveying more granular event information to interested clients.

## Related topics

<dl> <dt>

[WinEvents](winevents-collision169.md)
</dt> <dt>

[The IAccessibleEx Interface](iaccessibleex.md)
</dt> </dl>

 

 




