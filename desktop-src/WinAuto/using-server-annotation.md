---
title: Using Server Annotation
description: This topic provides information about using server annotation to specify a callback object.
ms.assetid: eeeebddc-2752-4d8f-b4fa-38ce156acc08
ms.topic: article
ms.date: 05/31/2018
---

# Using Server Annotation

This topic provides information about using server annotation to specify a callback object.

**To override a property that specifies a callback object**

1.  Obtain an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer to the accessible element that is to be annotated.
2.  Call [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on the accessible element to get an [**IAccIdentity**](/windows/desktop/api/oleacc/nn-oleacc-iaccidentity) interface pointer.
3.  Call [**IAccIdentity::GetIdentityString()**](/windows/desktop/api/Oleacc/nf-oleacc-iaccidentity-getidentitystring) on the [**IAccIdentity**](/windows/desktop/api/oleacc/nn-oleacc-iaccidentity) interface pointer to obtain a string that uniquely identifies the accessible element that is to be annotated.
4.  Use [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) or [**CoCreateInstanceEx**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstanceex) to create the [**IAccPropServices**](/windows/desktop/api/oleacc/nn-oleacc-iaccpropservices) object.
5.  Create a Component Object Model (COM) object that implements [**IAccPropServer**](/windows/desktop/api/oleacc/nn-oleacc-iaccpropserver).
6.  Call [**IAccPropServices::SetPropServer**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-setpropserver), passing the identity string, a GUID indicating the property to be overridden, and a pointer to the [**IAccPropServer**](/windows/desktop/api/oleacc/nn-oleacc-iaccpropserver) callback object.
7.  Release interface pointers and free memory.

When a client requests the property of the accessible element, the callback object will be called and will return the value to the client.

As when specifying a value, server developers can alternatively use the [**IAccPropServices::ComposeHwndIdentityString**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-composehwndidentitystring) method to obtain an identity string; or they can use the [**IAccPropServices::SetHwndPropServer**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-sethwndpropserver) method and specify the *hwnd*, *idObject*, or *idChild* parameters instead of an identity string.

When using either [**SetPropServer**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-setpropserver) or [**SetHwndPropServer**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-sethwndpropserver) on a container object, server developers can optionally specify that the overriding information should also apply to all element children of that container.

Servers can explicitly clear the annotation at any time by using [**IAccPropServices::ClearProps**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-clearprops). This is usually not required, as the annotation service will automatically clean up and release annotation information when the accessible element being annotated disappears.

Below is a list of properties that can be annotated using this procedure.

## Properties Supported When Specifying a Callback

When specifying a callback, the following properties can be annotated. Currently these properties cannot be annotated directly by specifying a value.



| Property                      | Type                                                             |
|-------------------------------|------------------------------------------------------------------|
| PROPID\_ACC\_NAME             | VT\_BSTR                                                         |
| PROPID\_ACC\_DESCRIPTION      | VT\_BSTR                                                         |
| PROPID\_ACC\_ROLE             | VT\_I4                                                           |
| PROPID\_ACC\_STATE            | VT\_I4                                                           |
| PROPID\_ACC\_HELP             | VT\_BSTR                                                         |
| PROPID\_ACC\_KEYBOARDSHORTCUT | VT\_BSTR                                                         |
| PROPID\_ACC\_DEFAULTACTION    | VT\_BSTR                                                         |
| PROPID\_ACC\_VALUEMAP         | VT\_BSTR                                                         |
| PROPID\_ACC\_ROLEMAP          | VT\_BSTR                                                         |
| PROPID\_ACC\_STATEMAP         | VT\_BSTR                                                         |
| PROPID\_ACC\_FOCUS            | VT\_DISPATCH<br/> VT\_I4<br/>                        |
| PROPID\_ACC\_SELECTION        | VT\_DISPATCH<br/> VT\_I4<br/> VT\_UNKNOWN<br/> |
| PROPID\_ACC\_PARENT           | VT\_DISPATCH                                                     |
| PROPID\_ACC\_NAV\_UP          | VT\_DISPATCH<br/> VT\_I4<br/>                        |
| PROPID\_ACC\_NAV\_DOWN        | VT\_DISPATCH<br/> VT\_I4<br/>                        |
| PROPID\_ACC\_NAV\_LEFT        | VT\_DISPATCH<br/> VT\_I4<br/>                        |
| PROPID\_ACC\_NAV\_RIGHT       | VT\_DISPATCH<br/> VT\_I4<br/>                        |
| PROPID\_ACC\_NAV\_PREV        | VT\_DISPATCH<br/> VT\_I4<br/>                        |
| PROPID\_ACC\_NAV\_NEXT        | VT\_DISPATCH<br/> VT\_I4<br/>                        |
| PROPID\_ACC\_NAV\_FIRSTCHILD  | VT\_DISPATCH<br/> VT\_I4<br/>                        |
| PROPID\_ACC\_NAV\_LASTCHILD   | VT\_DISPATCH<br/> VT\_I4<br/>                        |



 

 

