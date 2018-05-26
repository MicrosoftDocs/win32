---
title: Static Text (MSAA UI Element Reference)
description: Static text controls provide a convenient way to display text on dialog boxes and other windows. Static text controls often serve as labels for other controls.
ms.assetid: 2c4b29bc-54e6-4c96-93a3-1fcb96d68269
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Static Text (MSAA UI Element Reference)

Static text controls provide a convenient way to display text on dialog boxes and other windows. Static text controls often serve as labels for other controls.

The window class name for a static text control is "STATIC".

## IAccessible Methods

Static text controls support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

## IAccessible Properties

Static text controls support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchild?branch=master)                       |                                                                                                                                                                                                                                                                                               |
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)             | The **ChildCount** property is zero.                                                                                                                                                                                                                                                          |
| [**get\_accDescription**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdescription?branch=master)           |                                                                                                                                                                                                                                                                                               |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                               |
| [**get\_accHelp**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelp?branch=master)                         |                                                                                                                                                                                                                                                                                               |
| [**get\_accHelpTopic**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelptopic?branch=master)               |                                                                                                                                                                                                                                                                                               |
| [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) | The **KeyboardShortcut** property is the access key, which is the underlined character in the text that activates the control associated with the static text. The returned string contains the access key character appended to the string "Alt+".                                           |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | The **Name** property is the same as the text in the static text control.                                                                                                                                                                                                                     |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                   |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_STATICTEXT**](object-roles.md#role-system-statictext).                                                                                                                                                                                             |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_READONLY**](object-state-constants.md#state-system-readonly) \| [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible)<br/> |



 

## Notes

-   The [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master) method returns DISP\_E\_MEMBERNOTFOUND when it is called with [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) on a static text object.
-   Static controls with the SS\_ICON style return invalid data in the **Name** property.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 





