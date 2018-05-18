---
title: Combo Box (MSAA UI Element Reference)
description: A combo box is a list box combined with a static control or an edit control that displays the currently selected item in the list box portion of the combo box.
ms.assetid: '3fb2c0b0-507f-4520-845b-b3fbfd9e7b60'
---

# Combo Box (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Combo Box** objects for purposes of MSAA UI Element Reference. How to create **Combo Box** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A combo box is a list box combined with a static control or an edit control that displays the currently selected item in the list box portion of the combo box. The list box portion of the control is displayed at all times or only drop down when the user selects the drop-down arrow (which is a push button) next to the control. If the selection field is an edit control, the user can enter information not in the list; otherwise, the user can only select items in the list.

The window class name for a combo box is "COMBOBOX".

The contents of the [**IAccessible**](iaccessible.md) properties depend on which of the following parts of the combo box is queried by the client:

-   The combo box window
-   The edit control or static text control
-   The drop-down arrow (which is a push button)
-   The list box
-   The list items in the list box

## IAccessible Methods

Combo boxes support the following [**IAccessible**](iaccessible.md) methods:

-   [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md)
-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

Combo boxes support the following [**IAccessible**](iaccessible.md) properties:

-   [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)
-   [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)—The following table shows the child count value for different parts of the combo box. 

    | Combo box part   | ChildCount               |
    |------------------|--------------------------|
    | Combo box window | 3                        |
    | Edit control     | 0                        |
    | Drop-down arrow  | 0                        |
    | List box         | The number of list items |
    | List item        | 0                        |

    

     

-   [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md)—The following table shows the **DefaultAction** property for different parts of a combo box. 

    | Combo box part   | DefaultAction                                                  |
    |------------------|----------------------------------------------------------------|
    | Combo box window | None                                                           |
    | Edit control     | None                                                           |
    | Drop-down arrow  | "Open" or "Close" depending on the state of the drop-down list |
    | List box         | None                                                           |
    | List item        | "Double Click"                                                 |

    

     

-   [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)
-   [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)
-   [**get\_accHelp**](iaccessible-iaccessible--get-acchelp.md)
-   [**get\_accHelpTopic**](iaccessible-iaccessible--get-acchelptopic.md)
-   [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md)—The following table shows the **KeyboardShortcut** property for different parts of a combo box. 

    | Combo box part   | KeyboardShortcut               |
    |------------------|--------------------------------|
    | Combo box window | Access key of associated label |
    | Edit control     | None                           |
    | Drop-down arrow  | "Alt+Down Arrow"               |
    | List box         | None                           |
    | List item        | None                           |

    

     

    The access key for a combo box is the underlined character in the text from an associated static text control that labels the combo box. For example, on a standard Open dialog box that opens files, such as in Microsoft WordPad, the combo box labeled "Files of type:" has the **KeyboardShortcut** "Alt+t".

-   [**get\_accName**](iaccessible-iaccessible--get-accname.md)—The following table shows the **Name** property for different parts of a combo box. 

    | Combo box part   | Name                                                           |
    |------------------|----------------------------------------------------------------|
    | Combo box window | Static text control used as a label                            |
    | Edit control     | Static text control used as a label                            |
    | Drop-down arrow  | "Open" or "Close" depending on the state of the drop-down list |
    | List box         | Associated label                                               |
    | List item        | Text of the list item                                          |

    

     

    The **Name** property of a combo box, its child edit control, and its child list box is the text from an associated static text control that labels the combo box. For example, on a standard Open dialog box that opens files, such as in WordPad, the **Name** properties for the two combo boxes are "Look in:" and "Files of type:".

-   [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)—The following table shows the parent value for different parts of a combo box. 

    | Combo box part                        | Parent                                                                                                                                                                                                         |
    |---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Combo box window                      | A window with the **Role** property of [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) that surrounds the combo box and has the same **Name** property and window class name as the combo box. |
    | Edit control (or static text control) | The combo box window.                                                                                                                                                                                          |
    | Drop-down arrow                       | The combo box window.                                                                                                                                                                                          |
    | List box parent window                | The combo box window. This window surrounds the list box.                                                                                                                                                      |
    | List box                              | The list box parent window.                                                                                                                                                                                    |
    | List item                             | The list box.                                                                                                                                                                                                  |

    

     

-   [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)—The following table shows the **Role** property for different parts of a combo box. 

    | Combo box part                        | [Role](object-roles.md)                                                                                                               |
    |---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
    | Combo box window                      | [**ROLE\_SYSTEM\_COMBOBOX**](object-roles.md#role-system-combobox)                                                                    |
    | Edit control (or static text control) | [**ROLE\_SYSTEM\_TEXT**](object-roles.md#role-system-text) or [**ROLE\_SYSTEM\_STATICTEXT**](object-roles.md#role-system-statictext) |
    | Drop-down arrow                       | [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md#role-system-pushbutton)                                                                |
    | List box                              | [**ROLE\_SYSTEM\_LIST**](object-roles.md#role-system-list)                                                                            |
    | List item                             | [**ROLE\_SYSTEM\_LISTITEM**](object-roles.md#role-system-listitem)                                                                    |

    

     

-   [**get\_accState**](iaccessible-iaccessible--get-accstate.md)—The following table shows the **State** property for different parts of a combo box. 

    | Combo box part   | [Possible states](object-state-constants.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    |------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Combo box window | [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal) \| [**STATE\_SYSTEM\_EXPANDED**](object-state-constants.md#state-system-expanded) \| [**STATE\_SYSTEM\_COLLAPSED**](object-state-constants.md#state-system-collapsed) |
    | Edit control     | [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal)                                                                                                                                                                         |
    | Drop-down arrow  | 0, which means the button is visible and not pressed; or [**STATE\_SYSTEM\_PRESSED**](object-state-constants.md#state-system-pressed) \| [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| STATE\_SYSTEM\_NORMAL                                                                                                                                                                                                                                                                                                                                                    |
    | List box         | [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_FLOATING**](object-state-constants.md#state-system-floating) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal)                                                                                      |
    | List item        | [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_SELECTABLE**](object-state-constants.md#state-system-selectable) \| [**STATE\_SYSTEM\_SELECTED**](object-state-constants.md#state-system-selected) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal)                                                                                        |

    

     

-   [**get\_accValue**](iaccessible-iaccessible--get-accvalue.md)—The following table shows the **Value** property for different parts of a combo box. 

    | Combo box part   | Value                                |
    |------------------|--------------------------------------|
    | Combo box window | Text of currently selected list item |
    | Edit control     | Text of currently selected list item |
    | Drop-down arrow  | None                                 |
    | List box         | None                                 |
    | List item        | None                                 |

    

     

## Notes

-   When [**accNavigate**](iaccessible-iaccessible--accnavigate.md) is called with the [**NAVDIR\_NEXT**](navigation-constants.md#navdir-next) flag on the list box part of a combo box, it incorrectly navigates to the tray window when it should return **VT\_EMPTY**.

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 




