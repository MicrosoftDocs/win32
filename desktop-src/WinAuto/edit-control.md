---
title: Edit Control (MSAA UI Element Reference)
description: Edit controls let a user view and edit text.
ms.assetid: 'a42c73f2-4005-4db9-84bc-637c9c4310f1'
---

# Edit Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Edit Control** objects for purposes of MSAA UI Element Reference. How to create **Edit Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Edit controls let a user view and edit text. Edit controls are created with many different styles such as ES\_MULTILINE. This style creates a multiline edit control, such as the client area of Notepad, and ES\_READONLY, which creates a read-only edit control.

Microsoft Active Accessibility does not make a distinction between edit controls created with the window class name "EDIT" and rich edit controls created with the window class name "RichEdit" or "RichEdit20A".

## IAccessible Methods

Edit controls support the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

Edit controls support the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The **KeyboardShortcut** property is the edit control's access key, which is an underlined character in the text of the edit control's label. For example, on a standard File Open dialog box such as in WordPad, the **KeyboardShortcut** for the edit control labeled "Filename:" is "Alt+n".                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property is the text from a static text control that labels the edit control. For example, on a standard File Open dialog box such as in WordPad, the **Name** property for the edit control is "File name:".                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_TEXT**](object-roles.md#role-system-text).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accSelection**](iaccessible-iaccessible--get-accselection.md)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_READONLY**](object-state-constants.md#state-system-readonly) \| [**STATE\_SYSTEM\_PROTECTED**](object-state-constants.md#state-system-protected) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal)<br/> |
| [**get\_accValue**](iaccessible-iaccessible--get-accvalue.md)                       | The **Value** property is a single string that contains the text in the edit control. However, if the control is password protected, the **Value** property returns E\_ACCESSDENIED. For multiline edit controls, the string contains a carriage return and a newline character at the end of each line.                                                                                                                                                                                                                                                                                                                               |



 

## Notes

-   Microsoft Active Accessibility does not support the selection of the text contained in edit and rich edit controls because the text is exposed as a string in the object's **Value** property.
-   The rich edit control provided by Riched20.dll (which is used in text editors such as WordPad in Windows 98) does not send any WinEvents when the caret position is changed during text selection. When users press SHIFT and arrow keys to select text, the caret object does not trigger the [**EVENT\_OBJECT\_LOCATIONCHANGE**](event-constants.md#event-object-locationchange) WinEvent. When the selection is set programmatically through rich edit messages, the caret object does not send any events to indicate its new position.

    All applications that use Riched20.dll exhibit this problem. Applications using earlier versions of the rich edit control correctly send events based on the selection.

-   The **State** value for password edit controls always includes the bit flag [**STATE\_SYSTEM\_PROTECTED**](object-state-constants.md#state-system-protected).

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 





