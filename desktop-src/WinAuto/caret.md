---
title: Caret (MSAA UI Element Reference)
description: The caret is a flashing line, block, or bitmap in the client area of a window or in a control that accepts keyboard input.
ms.assetid: 'f2c48c36-1859-4e0a-8833-3ca90b4da323'
---

# Caret (MSAA UI Element Reference)

> [!Note]  
> This topic describes carets for purposes of MSAA UI Element Reference. How to use carets in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

The caret is a flashing line, block, or bitmap in the client area of a window or in a control that accepts keyboard input. It indicates the place at which text or graphics are inserted. Because only one window at a time has the keyboard focus, there is only one caret in the system.

## IAccessible Methods

The caret supports the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)

## IAccessible Properties

The caret supports the following [**IAccessible**](iaccessible.md) properties:



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
<td>[<strong>get_accChildCount</strong>](iaccessible-iaccessible--get-accchildcount.md)</td>
<td>The <strong>ChildCount</strong> property is zero.</td>
</tr>
<tr class="even">
<td>[<strong>get_accName</strong>](iaccessible-iaccessible--get-accname.md)</td>
<td>The <strong>Name</strong> property is &quot;Edit&quot;.</td>
</tr>
<tr class="odd">
<td>[<strong>get_accRole</strong>](iaccessible-iaccessible--get-accrole.md)</td>
<td>The <strong>Role</strong> property is [<strong>ROLE_SYSTEM_CARET</strong>](object-roles.md#role-system-caret).</td>
</tr>
<tr class="even">
<td>[<strong>get_accState</strong>](iaccessible-iaccessible--get-accstate.md)</td>
<td>Possible values for the <strong>State</strong> property include:
<ul>
<li>Zero, which means the caret is visible</li>
<li>[<strong>STATE_SYSTEM_INVISIBLE</strong>](object-state-constants.md#state-system-invisible)</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Notes

-   Unlike other UI elements, the caret object does not have an associated window handle. To obtain access to the caret object, clients must set a [*WinEventProc*](wineventproc-callback-function.md) and wait for the caret object to generate events.
-   The caret object in the rich edit control provided by Riched20.dll (which is used in text editors such as Microsoft WordPad in Windows 98) does not send any [WinEvents](winevents-collision169.md) when its position is changed during text selection. When users press SHIFT and arrow keys to select text, the caret object does not trigger the [**EVENT\_OBJECT\_LOCATIONCHANGE**](event-constants.md#event-object-locationchange) WinEvent. Similarly, when the selection is set programmatically through rich edit messages, the caret object does not send any events to indicate its new position.

    All applications that use Riched20.dll exhibit this problem. Applications using earlier versions of the rich edit control correctly send events based on the selection.

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 




