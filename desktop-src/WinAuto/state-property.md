---
title: State Property
description: The State property describes an object's status at a moment in time. All objects support the State property.
ms.assetid: 6a56070f-7913-45b2-b693-3c0a8b7fa2f4
ms.topic: article
ms.date: 05/31/2018
---

# State Property

The **State** property describes an object's status at a moment in time. All objects support the **State** property.

The **State** property is retrieved by calling [**IAccessible::get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate).

Microsoft Active Accessibility provides [object state constants](object-state-constants.md), defined in oleacc.h, that are combined to identify an object's state. It is recommended that server developers use these predefined state values. If predefined state values are returned, clients use [**GetStateText**](/windows/desktop/api/Oleacc/nf-oleacc-getstatetexta) to retrieve a localized string that describes the state.

Graphics that are occasionally animated should have the **State** property set to [**STATE\_SYSTEM\_ANIMATED**](object-state-constants.md) and the [**Role**](role-property.md) property set to [**ROLE\_SYSTEM\_GRAPHIC**](object-roles.md).

 

 




