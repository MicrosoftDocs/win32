---
title: Returning Errors
description: Invoke returns DISP\_E\_MEMBERNOTFOUND if one of the following conditions occurs
ms.assetid: 8eaff01a-f038-4fca-8951-7d0efcfdf1e1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Returning Errors

[**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master) returns DISP\_E\_MEMBERNOTFOUND if one of the following conditions occurs:

-   A member or parameter with the specified DISPID and matching cArgs cannot be found, and the parameter is not optional.

-   The member is a void function, and the caller did not set pVarResult to Null.

-   The member is a read-only property, and the caller set wFlags to DISPATCH\_PROPERTYPUT or DISPATCH\_PROPERTYPUTREF.

If [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master) finds the member, but uncovers errors in the argument list, it returns one of several other errors. DISP\_E\_BAD\_PARAMCOUNT means that the DISPPARAMS structure contains an incorrect number of parameters for the property or method. DISP\_E\_NONAMEDARGS means that **Invoke** received named arguments, but they are not supported by the member.

DISP\_E\_PARAMNOTFOUND means that the correct number of parameters was passed, but the DISPID for one or more parameters was incorrect. If [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master) cannot convert one of the arguments to the desired type, it returns DISP\_E\_TYPEMISMATCH. In these two cases, if it can identify which argument is incorrect, **Invoke** sets \*puArgErr to the index within rgvarg of the argument with the error. For example, if an Automation method expects a reference to a double-precision number as an argument, but receives a reference to an integer, the argument is coerced. However, if the method receives a date, **Invoke** returns DISP\_E\_TYPEMISMATCH and sets \*puArgErr to the index of the integer in the argument array.

Automation provides functions to perform standard conversions of VARIANT, and these functions should be used for consistent operation. DISP\_E\_TYPEMISMATCH is returned only when these functions fail. For more information about converting arguments, see [Conversion and Manipulation Functions](conversion-and-manipulation-functions.md).

## Example

This code from the Lines sample file Lines.cpp implements the [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master) member function for the CLines class.


```C++
STDMETHODIMP
CLines::Invoke(
 DISPID dispidMember,
 REFIID riid,
 LCID lcid,
 WORD wFlags,
 DISPPARAMS * pDispParams,
 VARIANT * pVarResult,
 EXCEPINFO * pExcepInfo,
 UINT * puArgErr)
{ 
  return DispInvoke(
   this, m_ptinfo,
   dispidMember, wFlags, pDispParams,
   pVarResult, pExcepInfo, puArgErr
  ); 
}
```



The next code example calls the **CLines::Invoke** member function to get the value of the **Color** property:


```C++
HRESULT hr;
EXCEPINFO excepinfo;
UINT nArgErr;
VARIANT vRet;
DISPPARAMS * pdisp;
OLECHAR * szMember;
DISPPARAMS dispparamsNoArgs = {NULL, NULL, 0, 0};

// Initialization code omitted for brevity.
szMember = "Color";
hr = pdisp->GetIDsOfNames(IID_NULL, &amp;szMember, 1, LOCALE_USER_DEFAULT, &amp;dispid);

// Get Color property.
hr = pdisp->Invoke(dispid, IID_NULL, LOCALE_SYSTEM_DEFAULT,
DISPATCH_PROPERTYGET, &amp;dispparams, &amp;vRet, &amp;excepinfo, &amp;nArgErr);
```



## Related topics

<dl> <dt>

[**CreateStdDispatch**](/windows/previous-versions/OleAuto/nf-oleauto-createstddispatch?branch=master)
</dt> <dt>

[**DispInvoke**](/windows/previous-versions/OleAuto/nf-oleauto-dispinvoke?branch=master)
</dt> <dt>

[**DispGetParam**](/windows/previous-versions/OleAuto/nf-oleauto-dispgetparam?branch=master)
</dt> <dt>

[**ITypeInfo::Invoke**](/windows/previous-versions/oaidl/nf-oaidl-itypeinfo-invoke?branch=master)
</dt> <dt>

[**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master)
</dt> </dl>

 

 




