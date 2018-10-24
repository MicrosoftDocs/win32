---
title: Title Bar (MSAA UI Element Reference)
description: The title bar at the top of a window displays an application-defined icon and line of text.
ms.assetid: f41ab777-6c94-4d8e-b743-c635e93df396
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Title Bar (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Title Bar** objects for purposes of MSAA UI Element Reference. How to create **Title Bar** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

The title bar at the top of a window displays an application-defined icon and line of text. The text specifies the name of the application and indicates the purpose of the window. The title bar also makes it possible for the user to move the window using a mouse or other pointing device.

Title bars contain at least three small buttons that minimize, maximize or restore, and close the window associated with the title bar. Title bars also contain a context-sensitive Help button. Applications running in the Far-East version of the Windows operating system may also contain Input Method Editor (IME) buttons. Microsoft Active Accessibility exposes these buttons as child elements of the title bar.

## IAccessible Methods

Title bars support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)

## IAccessible Properties

Title bars support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount"><strong>get_accChildCount</strong></a></td>
<td>The <strong>ChildCount</strong> property is five. The <strong>ChildCount</strong> property includes the IME and context-sensitive Help buttons even when they are not displayed. Buttons that are not displayed have the <strong>State</strong> property <a href="object-state-constants"><strong>STATE_SYSTEM_INVISIBLE</strong></a>.</td>
</tr>
<tr class="even">
<td><strong>get_accDescription</strong></td>
<td>The <strong>Description</strong> property of the title bar itself is: &quot;Displays the name of the window and contains controls to manipulate it.&quot; The child buttons in the title bar have the following descriptions:<br/>
<ul>
<li>&quot;Moves the window out of</li>
<li>&quot;Makes the window full</li>
<li>&quot;Puts a minimized or</li>
<li>&quot;Closes the window&quot;</li>
<li>&quot;Enters or leaves context-</li>
<li>&quot;Brings up the keyboard when pressed&quot;</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>get_accName</strong></td>
<td>The title bar itself does not support the <strong>Name</strong> property. The child buttons in the title bar have the following names:
<ul>
<li>&quot;Minimize&quot;</li>
<li>&quot;Maximize&quot; or &quot;Restore&quot;,</li>
<li>&quot;Close&quot;</li>
<li>&quot;Context help&quot;</li>
<li>&quot;IME&quot;</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>get_accParent</strong></td>
<td>The <strong>Parent</strong> property of the title bar is the main application window ( <a href="object-roles"><strong>ROLE_SYSTEM_WINDOW</strong></a> ) that has the same application-defined window class name as the title bar.</td>
</tr>
<tr class="odd">
<td><strong>get_accRole</strong></td>
<td>The <strong>Role</strong> property is <a href="object-roles"><strong>ROLE_SYSTEM_TITLEBAR</strong></a>. The child buttons in the title bar have the <strong>Role</strong> property <a href="object-roles"><strong>ROLE_SYSTEM_PUSHBUTTON</strong></a>.</td>
</tr>
<tr class="even">
<td><strong>get_accState</strong></td>
<td>The <strong>State</strong> property for the title bar and the child buttons can be a combination of one or more of the following <a href="object-state-constants">values</a>: <a href="object-state-constants"><strong>STATE_SYSTEM_FOCUSABLE</strong></a> | <a href="object-state-constants"><strong>STATE_SYSTEM_INVISIBLE</strong></a> | <a href="object-state-constants"><strong>STATE_SYSTEM_OFFSCREEN</strong></a> | <a href="object-state-constants"><strong>STATE_SYSTEM_UNAVAILABLE</strong></a> | <a href="object-state-constants"><strong>STATE_SYSTEM_PRESSED</strong></a><br/></td>
</tr>
<tr class="odd">
<td><strong>get_accValue</strong></td>
<td>The <strong>Value</strong> property is a string that is the same as the text displayed in the title bar.</td>
</tr>
</tbody>
</table>



 

## Notes

-   Although an application's title bar has the **State** property flag [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md), it never has the **State** flag [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md). Setting focus to a title bar object focuses the application window.
-   Because the title bar object does not support [**get\_accChild**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchild), the buttons on the title bar are simple elements. They do not support the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface themselves. The title bar object provides information about these child buttons.
-   Because title bars do not get focus and have no default action, the [**accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction) and [**get\_accDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction) methods are not supported for this control.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





