---
title: Header Control (MSAA UI Element Reference)
description: A header control displays headings at the top of columns of information and lets the user sort the information by clicking the headings. Windows Explorer uses a header control when the Details view is selected.
ms.assetid: 669d6bb8-7bc4-4e6f-bf4f-207887f44b83
ms.topic: article
ms.date: 05/31/2018
---

# Header Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Header Control** objects for purposes of MSAA UI Element Reference. How to create **Header Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A header control displays headings at the top of columns of information and lets the user sort the information by clicking the headings. Windows Explorer uses a header control when the Details view is selected.

The window class name for a header control is WC\_HEADER, which is defined as "SysHeader32" in Commctrl.h.

## IAccessible Methods

A header control supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:



| Method                                                                    | Comments                                                        |
|---------------------------------------------------------------------------|-----------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction) | This method performs the default action by clicking the header. |
| [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)                 |                                                                 |
| [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)               |                                                                 |
| [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)               |                                                                 |
| [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)                   |                                                                 |



 

## IAccessible Properties

A header control supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                       | Comments                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount)       | The **ChildCount** property is zero.                                                                                                                                                                                                   |
| [**get\_accDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction) | The **DefaultAction** property is "Click".                                                                                                                                                                                             |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)                 |                                                                                                                                                                                                                                        |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)                   | The **Name** property is the same as the name of the column header.                                                                                                                                                                    |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)               | The **Parent** property is a window ( [**ROLE\_SYSTEM\_LIST**](object-roles.md) ) that surrounds the control and has the same window class name as the control.                                                      |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)                   | The **Role** property is [**ROLE\_SYSTEM\_COLUMNHEADER**](object-roles.md).                                                                                                                                  |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)                 | The value for the **State** property is always [**STATE\_SYSTEM\_READONLY**](object-state-constants.md) and can also include [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md). |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 




