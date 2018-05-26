---
title: Retrieving Properties from UI Automation Elements
description: Properties on IUIAutomationElement objects contain information about UI elements, usually controls.
ms.assetid: e358fd67-22d0-4e43-a138-8afcc45f130e
keywords:
- clients,obtaining UI Automation elements
- clients,UI Automation elements
- clients,properties
- clients,retrieving properties
- clients,UI Automation properties
- UI Automation,obtaining elements
- UI Automation,elements
- UI Automation,properties
- UI Automation,retrieving properties
- retrieving properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Properties from UI Automation Elements

Properties on [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) objects contain information about UI elements, usually controls. The properties of an element are generic; that is, not specific to a control type. Control-specific properties of an element are exposed by its control pattern interfaces.

Microsoft UI Automation properties are read-only. To set properties of a control, you must use the methods of the appropriate control pattern. For example, use [**IUIAutomationScrollPattern::Scroll**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationscrollpattern-scroll?branch=master) to change the position values of a scrolling window.

To improve performance, property values of controls and control patterns can be cached when elements are retrieved. For more information, see [Caching UI Automation Properties and Control Patterns](uiauto-cachingforclients.md).

This topic contains the following sections.

-   [Property IDs](#property-ids)
-   [Property Conditions](#property-conditions)
-   [Retrieving Properties](#retrieving-properties)
-   [Default Property Values](#default-property-values)
-   [Related topics](#related-topics)

## Property IDs

Property identifiers are defined in Uiautomationclient.h. They are used to specify properties when you subscribe to property-changed events, retrieve property values, and construct property conditions. Property identifiers also identify the property that has changed when [**IUIAutomationPropertyChangedEventHandler::HandlePropertyChangedEvent**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationpropertychangedeventhandler-handlepropertychangedevent?branch=master) is called.

For a list of UI Automation property identifiers, see [Property Identifiers](uiauto-entry-propids.md).

## Property Conditions

The property IDs are used in constructing [**IUIAutomationPropertyCondition**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationpropertycondition?branch=master) objects that are used to find UI Automation elements. For example, you might want to find an element that has a certain name, or all controls that are enabled. Each property condition specifies a property identifier and the value that the property must match.

For more information, see the following reference topics:

-   [**IUIAutomation::CreatePropertyCondition**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-createpropertycondition?branch=master)
-   [**IUIAutomation::CreatePropertyConditionEx**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-createpropertyconditionex?branch=master)
-   [**IUIAutomationElement::FindFirst**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findfirst?branch=master)
-   [**IUIAutomationElement::FindAll**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findall?branch=master)

## Retrieving Properties

Some generic properties, and all control pattern properties, are available as properties on the [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) or control pattern interface and can be retrieved by using an accessor, such as [**IUIAutomationElement::CurrentName**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentname?branch=master) or [**CachedDockPosition**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationdockpattern-get_cacheddockposition?branch=master).

In addition, any current or cached property (other than control pattern properties) can be retrieved by using one of the following methods:

-   [**GetCurrentPropertyValue**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpropertyvalue?branch=master)
-   [**GetCurrentPropertyValueEx**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpropertyvalueex?branch=master)
-   [**GetCachedPropertyValue**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedpropertyvalue?branch=master)
-   [**GetCachedPropertyValueEx**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedpropertyvalueex?branch=master)

These methods offer slightly better performance and access to the full range of properties. However, values are returned in [**VARIANT**](https://msdn.microsoft.com/library/windows/desktop/ms221627) structures, whereas the individual property accessors cast the value to the appropriate type.

## Default Property Values

If a UI Automation provider does not implement a property, UI Automation can supply a default value. For example, if the provider for a control does not support the property identified by [**UIA\_HelpTextPropertyId**](uiauto-automation-element-propids.md#uia-helptextpropertyid), UI Automation returns an empty string. Similarly, if the provider does not support the property identified by [**UIA\_IsDockPatternAvailablePropertyId**](uiauto-control-pattern-availability-propids.md#uia-isdockpatternavailablepropertyid), UI Automation returns **FALSE**.

The difference between [**IUIAutomationElement::GetCurrentPropertyValue**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpropertyvalue?branch=master) and [**GetCurrentPropertyValueEx**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpropertyvalueex?branch=master) (and between similar pairs of methods) is that the "Ex" method can specify that no default value is to be returned. In this case, the return value is a special unique constant, indicating that the property is not supported. On receiving this value, the application can supply its own value or simply ignore the property.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Properties Overview](uiauto-propertiesoverview.md)
</dt> <dt>

[Property Identifiers](uiauto-entry-propids.md)
</dt> </dl>

 

 




