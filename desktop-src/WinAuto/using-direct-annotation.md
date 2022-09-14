---
title: Using Direct Annotation
description: Using Direct Annotation
ms.assetid: d9d78e74-dcab-4974-945f-e8c5d42c04b7
ms.topic: article
ms.date: 05/31/2018
---

# Using Direct Annotation

**To use direct annotation to override the value of a property**

1.  Use the [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) or [CoCreateInstanceEx](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstanceex) function to create the [**IAccPropServices**](/windows/desktop/api/oleacc/nn-oleacc-iaccpropservices) object.
2.  Call [**IAccPropServices::SetHwndProp**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-sethwndprop), passing the **HWND**, object ID, child ID, the property to be overridden, and a [VARIANT](/windows/win32/api/oaidl/ns-oaidl-variant) containing the new value of the property. This step annotates the value.
3.  Release the interface pointers and free memory.

The following example shows how to annotate the [**Role**](role-property.md) property of a static text control.


```C++
HRESULT CMyTextControl::SetAccessibleProperties()
{
  // COM is assumed to be initialized...
  IAccPropServices* pAccPropServices = NULL;

  HRESULT hr = CoCreateInstance(CLSID_AccPropServices,
    NULL, CLSCTX_SERVER, IID_IAccPropServices, 
    (void**)&pAccPropServices);

  if (SUCCEEDED(hr))
  {
    // Annotating the Role of this object to be STATICTEXT
    VARIANT var;
    var.vt = VT_I4;
    var.lVal = ROLE_SYSTEM_STATICTEXT;

    hr = pAccPropServices->SetHwndProp(_hwnd,
      OBJID_CLIENT,
      CHILDID_SELF,
      PROPID_ACC_ROLE,
      var);

    pAccPropServices->Release();
  }
  return hr;
}
```



## Properties Supported When Specifying a Value

The following Microsoft Active Accessibility properties can be annotated when specifying a value (where the value must be of the noted type) for direct annotation. To override or add a Microsoft UI Automation property to a control, you can specify the UI Automation property ID instead of the Microsoft Active Accessibility property ID. For a list of UI Automation IDs, see [Property Identifiers](uiauto-entry-propids.md).



| Property                      | Type     |
|-------------------------------|----------|
| PROPID\_ACC\_NAME             | VT\_BSTR |
| PROPID\_ACC\_DESCRIPTION      | VT\_BSTR |
| PROPID\_ACC\_ROLE             | VT\_I4   |
| PROPID\_ACC\_STATE            | VT\_I4   |
| PROPID\_ACC\_HELP             | VT\_BSTR |
| PROPID\_ACC\_KEYBOARDSHORTCUT | VT\_BSTR |
| PROPID\_ACC\_DEFAULTACTION    | VT\_BSTR |
| PROPID\_ACC\_VALUEMAP         | VT\_BSTR |
| PROPID\_ACC\_ROLEMAP          | VT\_BSTR |
| PROPID\_ACC\_STATEMAP         | VT\_BSTR |



 

 

 