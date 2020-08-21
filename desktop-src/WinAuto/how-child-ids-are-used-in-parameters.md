---
title: How Child IDs Are Used in Parameters
description: This topic describes input parameters, output parameters, and special cases for interpreting child IDs returned from IAccessible methods.
ms.assetid: 051ec5ba-540c-4ae1-b917-4c229557ca2f
ms.topic: article
ms.date: 05/31/2018
---

# How Child IDs Are Used in Parameters

This topic describes input parameters, output parameters, and special cases for interpreting child IDs returned from [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods.

## Input Parameters

Many of the Microsoft Active Accessibility functions and most of the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties take a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) structure as an input parameter. For most of the **IAccessible** properties, this parameter allows client developers to specify whether they want information about the object itself or about one of the object's simple elements.

Microsoft Active Accessibility provides the constant **CHILDID\_SELF** to indicate that information is needed about the object itself. To obtain information about a simple element, client developers specify its child ID in the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) parameter.

When initializing a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) parameter, be sure to specify **VT\_I4** in the **vt** member in addition to specifying the child ID value (or **CHILDID\_SELF**) in the **lVal** member.

For example, to get the name of an object, and not one of the object's child elements, initialize the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) for the first parameter of [**IAccessible::get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname) ( **CHILDID\_SELF** in the **lVal** member and **VT\_I4** in the **vt** member), and then call **IAccessible::get\_accName**.

## Output Parameters

Several [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) functions and methods have a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant)\* output parameter that contains a child ID or an [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface pointer to a child object. There are different steps that a client must take depending on whether they receive a **VT\_I4** child ID (simple element) or an **IDispatch** interface pointer with **CHILDID\_SELF** (full object). Following these steps will provide an **IAccessible** interface pointer and child ID that together allow clients to use the **IAccessible** methods and properties. These steps apply to the [**IAccessible::accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest), [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus), and [**get\_accSelection**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accselection) methods. They also apply to the [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent), [**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint), and [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow) client functions.

The following table lists the possible result returned and the required post-processing steps so that clients will have an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer and child ID.



| Result returned                                      | Post-processing for the return value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface pointer | This is a full object.Call [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) to access the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer.<br/> Use the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer with **CHILDID\_SELF** to access **IAccessible** methods and properties.<br/>                                                                                                                                                                                                                                                                                                                                                                                               |
| VT\_I4 child ID                                      | Call [**IAccessible::get\_accChild**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchild) using the child ID to see if you have an [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface pointer.If you get an [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface pointer, use it with **CHILDID\_SELF** to access [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface methods and properties.<br/> If the call to [**get\_accChild**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchild) fails, you have a simple element. Use the original [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer (the one you used in your call to the method or function mentioned above) with the **VT\_I4** child ID that the call returned.<br/> |



 

Before you can use a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) parameter, you must initialize it by calling the [**VariantInit**](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-variantinit) Component Object Model (COM) function. When finished with the structure, call [**VariantClear**](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-variantclear) to free the memory reserved for that **VARIANT**.

## Special Cases

There are exceptions to the guidelines in the above table, such as when a child ID is returned by the [**IAccessible::accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest) method. Servers must return an [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface if the child is an accessible object. If a child ID is returned by **IAccessible::accHitTest**, the child is a simple element.

In addition, there are special cases for [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate). For more information, see **IAccessible::accNavigate** and [Spatial and Logical Navigation](spatial-and-logical-navigation.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[IDispatch Interface](idispatch-interface.md)
</dt> <dt>

[VARIANT Structure](variant-structure.md)
</dt> </dl>

 

