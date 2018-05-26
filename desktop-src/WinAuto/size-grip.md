---
title: Size Grip (MSAA UI Element Reference)
description: The size grip is a special mouse pointer in the lower-right corner of a window that allows a user to click and drag the size grip to resize the window.
ms.assetid: 886b27b3-e88d-47a1-85f3-a55bd14c7a7c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Size Grip (MSAA UI Element Reference)

The size grip is a special mouse pointer in the lower-right corner of a window that allows a user to click and drag the size grip to resize the window.

## IAccessible Methods

The size grip supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)

## IAccessible Properties

The size grip supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                   | Comments                                                                                                                                                               |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accDescription**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdescription?branch=master) | The **Description** property is "Can be used to resize a window's width and height".                                                                                   |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)               | The **Name** property is "Size box".                                                                                                                                   |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)           | The window that contains the size grip.                                                                                                                                |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)               | The **Role** property is [**ROLE\_SYSTEM\_GRIP**](object-roles.md#role-system-grip).                                                                                  |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)             | The value for the **State** property is zero, which means the object is visible, or [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible). |



 

## Related topics

<dl> <dt>

[IAccessible](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 




