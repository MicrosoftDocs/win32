---
title: VARIANT Structure
description: Most of the Microsoft Active Accessibility functions and the IAccessible properties and methods take a VARIANT structure as a parameter. Essentially, the VARIANT structure is a container for a large union that carries many types of data.
ms.assetid: 774dfac8-e258-4266-b81e-072eb3961fb1
ms.topic: article
ms.date: 05/31/2018
---

# VARIANT Structure

Most of the Microsoft Active Accessibility functions and the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties and methods take a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) structure as a parameter. Essentially, the **VARIANT** structure is a container for a large union that carries many types of data.

The value in the first member of the structure, **vt**, describes which of the union members is valid. Although the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) structure supports many different data types, Microsoft Active Accessibility uses only the following types.



| vt Value     | Corresponding value member name |
|--------------|---------------------------------|
| VT\_I4       | **lVal**                        |
| VT\_DISPATCH | **pdispVal**                    |
| VT\_BSTR     | **bstrVal**                     |
| VT\_EMPTY    | none                            |



 

When you receive information in a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) structure, check the **vt** member to find out which member contains valid data. Similarly, when you send information using a **VARIANT** structure, always set **vt** to reflect the union member that contains the information.

Before using the structure, initialize it by calling the [**VariantInit**](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-variantinit) Component Object Model (COM) function. When finished with the structure, clear it before the memory that contains the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) is freed by calling [**VariantClear**](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-variantclear).

 

 