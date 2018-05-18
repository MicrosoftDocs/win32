---
title: Using Server Annotation
description: This topic provides information about using server annotation to specify a callback object.
ms.assetid: 'eeeebddc-2752-4d8f-b4fa-38ce156acc08'
---

# Using Server Annotation

This topic provides information about using server annotation to specify a callback object.

**To override a property that specifies a callback object**

1.  Obtain an [**IAccessible**](iaccessible.md) interface pointer to the accessible element that is to be annotated.
2.  Call [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) on the accessible element to get an [**IAccIdentity**](iaccidentity.md) interface pointer.
3.  Call [**IAccIdentity::GetIdentityString()**](iaccidentity-iaccidentity--getidentitystring.md) on the [**IAccIdentity**](iaccidentity.md) interface pointer to obtain a string that uniquely identifies the accessible element that is to be annotated.
4.  Use [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) or [**CoCreateInstanceEx**](https://msdn.microsoft.com/library/windows/desktop/ms680701) to create the [**IAccPropServices**](iaccpropservices.md) object.
5.  Create a Component Object Model (COM) object that implements [**IAccPropServer**](iaccpropserver.md).
6.  Call [**IAccPropServices::SetPropServer**](iaccpropservices-iaccpropservices--setpropserver.md), passing the identity string, a GUID indicating the property to be overridden, and a pointer to the [**IAccPropServer**](iaccpropserver.md) callback object.
7.  Release interface pointers and free memory.

When a client requests the property of the accessible element, the callback object will be called and will return the value to the client.

As when specifying a value, server developers can alternatively use the [**IAccPropServices::ComposeHwndIdentityString**](iaccpropservices-iaccpropservices--composehwndidentitystring.md) method to obtain an identity string; or they can use the [**IAccPropServices::SetHwndPropServer**](iaccpropservices-iaccpropservices--sethwndpropserver.md) method and specify the *hwnd*, *idObject*, or *idChild* parameters instead of an identity string.

When using either [**SetPropServer**](iaccpropservices-iaccpropservices--setpropserver.md) or [**SetHwndPropServer**](iaccpropservices-iaccpropservices--sethwndpropserver.md) on a container object, server developers can optionally specify that the overriding information should also apply to all element children of that container.

Servers can explicitly clear the annotation at any time by using [**IAccPropServices::ClearProps**](iaccpropservices-iaccpropservices--clearprops.md). This is usually not required, as the annotation service will automatically clean up and release annotation information when the accessible element being annotated disappears.

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



 

 

 





