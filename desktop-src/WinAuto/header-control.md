---
title: Header Control (MSAA UI Element Reference)
description: A header control displays headings at the top of columns of information and lets the user sort the information by clicking the headings. Windows Explorer uses a header control when the Details view is selected.
ms.assetid: 669d6bb8-7bc4-4e6f-bf4f-207887f44b83
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Header Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Header Control** objects for purposes of MSAA UI Element Reference. How to create **Header Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A header control displays headings at the top of columns of information and lets the user sort the information by clicking the headings. Windows Explorer uses a header control when the Details view is selected.

The window class name for a header control is WC\_HEADER, which is defined as "SysHeader32" in Commctrl.h.

## IAccessible Methods

A header control supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:



| Method                                                                    | Comments                                                        |
|---------------------------------------------------------------------------|-----------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) | This method performs the default action by clicking the header. |
| [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)                 |                                                                 |
| [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)               |                                                                 |
| [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)               |                                                                 |
| [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)                   |                                                                 |



 

## IAccessible Properties

A header control supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                       | Comments                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)       | The **ChildCount** property is zero.                                                                                                                                                                                                   |
| [**get\_accDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction?branch=master) | The **DefaultAction** property is "Click".                                                                                                                                                                                             |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                 |                                                                                                                                                                                                                                        |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                   | The **Name** property is the same as the name of the column header.                                                                                                                                                                    |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)               | The **Parent** property is a window ( [**ROLE\_SYSTEM\_LIST**](object-roles.md#role-system-list) ) that surrounds the control and has the same window class name as the control.                                                      |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                   | The **Role** property is [**ROLE\_SYSTEM\_COLUMNHEADER**](object-roles.md#role-system-columnheader).                                                                                                                                  |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                 | The value for the **State** property is always [**STATE\_SYSTEM\_READONLY**](object-state-constants.md#state-system-readonly) and can also include [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible). |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 




