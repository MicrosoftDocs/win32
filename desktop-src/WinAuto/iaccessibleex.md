---
title: The IAccessibleEx Interface
description: Controls that do not have a Microsoft UI Automation provider, but that implement IAccessible, can easily be upgraded to provide some UI Automation functionality by implementing the IAccessibleEx interface.
ms.assetid: '5523156e-c9b8-4aad-b568-f3b3c402d33e'
---

# The IAccessibleEx Interface

Controls that do not have a Microsoft UI Automation provider, but that implement [**IAccessible**](iaccessible.md), can easily be upgraded to provide some UI Automation functionality by implementing the [**IAccessibleEx**](uiauto-iaccessibleex.md) interface. This interface enables the control to expose UI Automation properties and control patterns, without the need for a full implementation of UI Automation provider interfaces such as [**IRawElementProviderFragment**](uiauto-irawelementproviderfragment.md). To use **IAccessibleEx**, **IRawElementProviderFragment**, and all other UI Automation interfaces, include the UIAutomation.h header file in your source code.

For example, consider a custom control that has a range value. The Microsoft Active Accessibility server for the control defines the control's role and is able to return its current value. However, because Microsoft Active Accessibility does not define minimum and maximum properties, the server lacks the means to return the minimum and maximum values of the control. A UI Automation client is able to retrieve the control's role, current value, and other Microsoft Active Accessibility properties, because the UI Automation core can obtain these through [**IAccessible**](iaccessible.md). However, without access to an [**IRangeValueProvider**](uiauto-irangevalueprovider.md) interface on the object, UI Automation is also unable to retrieve the maximum and minimum values.

The control developer could supply a complete UI Automation provider for the control, but this would mean duplicating much of the existing functionality of the [**IAccessible**](iaccessible.md) implementation: for example, navigation and common properties. Instead, the developer can continue to rely on **IAccessible** to supply this functionality, while adding support for control-specific properties through [**IRangeValueProvider**](uiauto-irangevalueprovider.md).

## In this section

-   [IAccessibleEx Implementation Guidelines](iaccessibleex-implementation-guidelines.md)
-   [Implementing IAccessibleEx for Providers](implementing-iaccessibleex-for-providers.md)
-   [Using IAccessibleEx from a Client](using-iaccessibleex-from-a-client.md)

## Related topics

<dl> <dt>

[Common Infrastructure](common-infrastructure.md)
</dt> </dl>

 

 




