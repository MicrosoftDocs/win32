---
title: Header Control (MSAA UI Element Reference)
description: A header control displays headings at the top of columns of information and lets the user sort the information by clicking the headings. Windows Explorer uses a header control when the Details view is selected.
ms.assetid: '669d6bb8-7bc4-4e6f-bf4f-207887f44b83'
---

# Header Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Header Control** objects for purposes of MSAA UI Element Reference. How to create **Header Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A header control displays headings at the top of columns of information and lets the user sort the information by clicking the headings. Windows Explorer uses a header control when the Details view is selected.

The window class name for a header control is WC\_HEADER, which is defined as "SysHeader32" in Commctrl.h.

## IAccessible Methods

A header control supports the following [**IAccessible**](iaccessible.md) methods:



| Method                                                                    | Comments                                                        |
|---------------------------------------------------------------------------|-----------------------------------------------------------------|
| [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) | This method performs the default action by clicking the header. |
| [**accHitTest**](iaccessible-iaccessible--acchittest.md)                 |                                                                 |
| [**accLocation**](iaccessible-iaccessible--acclocation.md)               |                                                                 |
| [**accNavigate**](iaccessible-iaccessible--accnavigate.md)               |                                                                 |
| [**accSelect**](iaccessible-iaccessible--accselect.md)                   |                                                                 |



 

## IAccessible Properties

A header control supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                       | Comments                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)       | The **ChildCount** property is zero.                                                                                                                                                                                                   |
| [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md) | The **DefaultAction** property is "Click".                                                                                                                                                                                             |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                 |                                                                                                                                                                                                                                        |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                   | The **Name** property is the same as the name of the column header.                                                                                                                                                                    |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)               | The **Parent** property is a window ( [**ROLE\_SYSTEM\_LIST**](object-roles.md#role-system-list) ) that surrounds the control and has the same window class name as the control.                                                      |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                   | The **Role** property is [**ROLE\_SYSTEM\_COLUMNHEADER**](object-roles.md#role-system-columnheader).                                                                                                                                  |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                 | The value for the **State** property is always [**STATE\_SYSTEM\_READONLY**](object-state-constants.md#state-system-readonly) and can also include [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible). |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 




