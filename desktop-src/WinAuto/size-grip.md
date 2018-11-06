---
title: Size Grip (MSAA UI Element Reference)
description: The size grip is a special mouse pointer in the lower-right corner of a window that allows a user to click and drag the size grip to resize the window.
ms.assetid: 886b27b3-e88d-47a1-85f3-a55bd14c7a7c
ms.topic: article
ms.date: 05/31/2018
---

# Size Grip (MSAA UI Element Reference)

The size grip is a special mouse pointer in the lower-right corner of a window that allows a user to click and drag the size grip to resize the window.

## IAccessible Methods

The size grip supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)

## IAccessible Properties

The size grip supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                   | Comments                                                                                                                                                               |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accDescription**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdescription) | The **Description** property is "Can be used to resize a window's width and height".                                                                                   |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)               | The **Name** property is "Size box".                                                                                                                                   |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)           | The window that contains the size grip.                                                                                                                                |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)               | The **Role** property is [**ROLE\_SYSTEM\_GRIP**](object-roles.md).                                                                                  |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)             | The value for the **State** property is zero, which means the object is visible, or [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md). |



 

## Related topics

<dl> <dt>

[IAccessible](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 




