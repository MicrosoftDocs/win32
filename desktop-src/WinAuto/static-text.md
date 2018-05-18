---
title: Static Text (MSAA UI Element Reference)
description: Static text controls provide a convenient way to display text on dialog boxes and other windows. Static text controls often serve as labels for other controls.
ms.assetid: '2c4b29bc-54e6-4c96-93a3-1fcb96d68269'
---

# Static Text (MSAA UI Element Reference)

Static text controls provide a convenient way to display text on dialog boxes and other windows. Static text controls often serve as labels for other controls.

The window class name for a static text control is "STATIC".

## IAccessible Methods

Static text controls support the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

Static text controls support the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)                       |                                                                                                                                                                                                                                                                                               |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             | The **ChildCount** property is zero.                                                                                                                                                                                                                                                          |
| [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)           |                                                                                                                                                                                                                                                                                               |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                               |
| [**get\_accHelp**](iaccessible-iaccessible--get-acchelp.md)                         |                                                                                                                                                                                                                                                                                               |
| [**get\_accHelpTopic**](iaccessible-iaccessible--get-acchelptopic.md)               |                                                                                                                                                                                                                                                                                               |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The **KeyboardShortcut** property is the access key, which is the underlined character in the text that activates the control associated with the static text. The returned string contains the access key character appended to the string "Alt+".                                           |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property is the same as the text in the static text control.                                                                                                                                                                                                                     |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                   |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_STATICTEXT**](object-roles.md#role-system-statictext).                                                                                                                                                                                             |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_READONLY**](object-state-constants.md#state-system-readonly) \| [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible)<br/> |



 

## Notes

-   The [**accSelect**](iaccessible-iaccessible--accselect.md) method returns DISP\_E\_MEMBERNOTFOUND when it is called with [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) on a static text object.
-   Static controls with the SS\_ICON style return invalid data in the **Name** property.

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 





