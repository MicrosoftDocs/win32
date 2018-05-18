---
title: Size Grip (MSAA UI Element Reference)
description: The size grip is a special mouse pointer in the lower-right corner of a window that allows a user to click and drag the size grip to resize the window.
ms.assetid: '886b27b3-e88d-47a1-85f3-a55bd14c7a7c'
---

# Size Grip (MSAA UI Element Reference)

The size grip is a special mouse pointer in the lower-right corner of a window that allows a user to click and drag the size grip to resize the window.

## IAccessible Methods

The size grip supports the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)

## IAccessible Properties

The size grip supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                   | Comments                                                                                                                                                               |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md) | The **Description** property is "Can be used to resize a window's width and height".                                                                                   |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)               | The **Name** property is "Size box".                                                                                                                                   |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)           | The window that contains the size grip.                                                                                                                                |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)               | The **Role** property is [**ROLE\_SYSTEM\_GRIP**](object-roles.md#role-system-grip).                                                                                  |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)             | The value for the **State** property is zero, which means the object is visible, or [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible). |



 

## Related topics

<dl> <dt>

[IAccessible](iaccessible.md)
</dt> </dl>

 

 




