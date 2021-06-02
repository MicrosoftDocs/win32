---
title: Description Property (Windows Accessibility features)
description: An object's Description property provides a textual description about an object's visual appearance.
ms.assetid: 1fe3221f-e1dd-44b2-b749-d00bee1b6b89
ms.topic: article
ms.date: 05/31/2018
---

# Description Property (Windows Accessibility features)

> [!Note]  
> The **Description** property is often used incorrectly and is not supported by Microsoft UI Automation. Microsoft Active Accessibility server developers should not use this property. If more information is needed for accessibility and automation scenarios, use the properties supported by UI Automation elements and control patterns.

 

An object's **Description** property provides a textual description about an object's visual appearance. The description is primarily used to provide greater context for low-vision or blind users, but is also used for context searching or other applications. This property can help users understand an icon or the overall visual appearance.

The **Description** property is retrieved by calling [**IAccessible::get\_accDescription**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdescription).

## When to Support the Description Property

Servers support the **Description** property if the description is not obvious, or when it is not redundant based on the object's [**Name**](name-property.md), [**Role**](role-property.md), [**State**](state-property.md), and [**Value**](value-property.md) properties. For example, a button labeled "OK" would not need additional information, whereas a button that shows a picture of a cactus would. The **Name**, **Role**, and [**Help**](help-property.md) properties for such a button describe its purpose, but the **Description** property conveys information that is less tangible; for example, "This button shows a picture of a cactus."

A Microsoft Active Accessibility server can add support for UI Automation by using [Direct Annotation](direct-annotation.md), using the [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) interface, or by implementing Microsoft Active Accessibility and UI Automation side-by-side with both implementations handling the [**WM\_GETOBJECT**](wm-getobject.md) message.

## Related topics

<dl> <dt>

[Using Direct Annotation](using-direct-annotation.md)
</dt> <dt>

[The IAccessibleEx Interface](iaccessibleex.md)
</dt> </dl>

 

 




