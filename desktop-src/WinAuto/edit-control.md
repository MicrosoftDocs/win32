---
title: Edit Control (MSAA UI Element Reference)
description: Edit controls let a user view and edit text.
ms.assetid: a42c73f2-4005-4db9-84bc-637c9c4310f1
ms.topic: article
ms.date: 05/31/2018
---

# Edit Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Edit Control** objects for purposes of MSAA UI Element Reference. How to create **Edit Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Edit controls let a user view and edit text. Edit controls are created with many different styles such as ES\_MULTILINE. This style creates a multiline edit control, such as the client area of Notepad, and ES\_READONLY, which creates a read-only edit control.

Microsoft Active Accessibility does not make a distinction between edit controls created with the window class name "EDIT" and rich edit controls created with the window class name "RichEdit" or "RichEdit20A".

## IAccessible Methods

Edit controls support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)

## IAccessible Properties

Edit controls support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchild)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accDescription**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdescription)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) | The **KeyboardShortcut** property is the edit control's access key, which is an underlined character in the text of the edit control's label. For example, on a standard File Open dialog box such as in WordPad, the **KeyboardShortcut** for the edit control labeled "Filename:" is "Alt+n".                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)                         | The **Name** property is the text from a static text control that labels the edit control. For example, on a standard File Open dialog box such as in WordPad, the **Name** property for the edit control is "File name:".                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)                         | The **Role** property is [**ROLE\_SYSTEM\_TEXT**](object-roles.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accSelection**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accselection)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_READONLY**](object-state-constants.md) \| [**STATE\_SYSTEM\_PROTECTED**](object-state-constants.md) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md)<br/> |
| [**get\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accvalue)                       | The **Value** property is a single string that contains the text in the edit control. However, if the control is password protected, the **Value** property returns E\_ACCESSDENIED. For multiline edit controls, the string contains a carriage return and a newline character at the end of each line.                                                                                                                                                                                                                                                                                                                               |



 

## Notes

-   Microsoft Active Accessibility does not support the selection of the text contained in edit and rich edit controls because the text is exposed as a string in the object's **Value** property.
-   The rich edit control provided by Riched20.dll (which is used in text editors such as WordPad in Windows 98) does not send any WinEvents when the caret position is changed during text selection. When users press SHIFT and arrow keys to select text, the caret object does not trigger the [**EVENT\_OBJECT\_LOCATIONCHANGE**](event-constants.md) WinEvent. When the selection is set programmatically through rich edit messages, the caret object does not send any events to indicate its new position.

    All applications that use Riched20.dll exhibit this problem. Applications using earlier versions of the rich edit control correctly send events based on the selection.

-   The **State** value for password edit controls always includes the bit flag [**STATE\_SYSTEM\_PROTECTED**](object-state-constants.md).

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





