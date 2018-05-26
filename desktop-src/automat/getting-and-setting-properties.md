---
title: Getting and Setting Properties
description: Properties are accessed in the same way as methods, except you specify DISPATCH\_PROPERTYGET or DISPATCH\_PROPERTYPUT instead of DISPATCH\_METHOD.
ms.assetid: b96d718b-d0c0-445e-bb04-a4ccbb0d1d83
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting and Setting Properties

Properties are accessed in the same way as methods, except you specify DISPATCH\_PROPERTYGET or DISPATCH\_PROPERTYPUT instead of DISPATCH\_METHOD. Some languages cannot distinguish between retrieving a property and calling a method. In this case, you should set the flags DISPATCH\_PROPERTYGET and DISPATCH\_METHOD.

The following example gets the value of a property named "On". You can assume that the object has been created, and that its interfaces have been queried, as in the previous example.


```C++
VARIANT *pVarResult;
// Code omitted for brevity.
szMember = "On";
hresult = pdisp->GetIDsOfNames(IID_NULL, &amp;szMember, 1, LOCALE_USER_DEFAULT, &amp;dispid);

hresult = pdisp->Invoke(
dispid,
IID_NULL,
LOCALE_USER_DEFAULT,
DISPATCH_PROPERTYGET,
&amp;dispparamsNoArgs, pVarResult, NULL, NULL);
```



As in the previous example, the code calls [**GetIDsOfNames**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-getidsofnames?branch=master) for the DISPID of the "On" property, and then passes the ID to [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master). Then, **Invoke** returns the property's value in pVarResult. In general, the return value does not set VT\_BYREF. However, this bit may be set and a pointer returned to the return value, if the lifetime of the return value is the same as that of the object.

To change the property's value, the call looks like this:


```C++
VARIANT *pVarResult;
DISPPARAMS dispparams; 
DISPID mydispid = DISPID_PROPERTYPUT

// Code omitted for brevity.

szMember = "On";
dispparams.rgvarg[0].vt = VT_BOOL;
dispparams.rgvarg[0].bool = FALSE;
dispparams.rgdispidNamedArgs = &amp;mydispid;
dispparams.cArgs = 1;
dispparams.cNamedArgs = 1;
hresult = pdisp->GetIDsOfNames(IID_NULL, &amp;szMember, 1, LOCALE_USER_DEFAULT, &amp;dispid); 

hresult = pdisp->Invoke(
  dispid,
  IID_NULL,
  LOCALE_USER_DEFAULT,
  DISPATCH_PROPERTYPUT,
  &amp;dispparams, NULL, NULL, NULL);
```



The new value for the property (the Boolean value False) is passed as an argument when the "On" property's **Put** function is invoked. The DISPID for the argument is DISPID\_PROPERTYPUT. This DISPID is defined by Automation to designate the parameter that contains the new value for a property's **Put** function. The remaining details of the DISPPARAMS structure are described in the [Passing Parameters](passing-parameters.md).

The DISPATCH\_PROPERTYPUT flag in the previous example indicates that a property is being set by value. In Visual Basic, the following statement assigns the **Value** property (the default) of YourObj to the **Prop** property:


```C++
MyObj.Prop = YourObj
```



This statement should be flagged as a DISPATCH\_PROPERTYPUT. Similarly, statements like the following assign the **Value** property of one object to the **Value** property of another object.


```C++
Worksheet.Cell(1,1) = Worksheet.Cell(6,6)
MyDoc.Text1 = YourDoc.Text1
```



These statements result in a PROPERTY\_PUT operation on Worksheet.Cell(1,1) and MyDoc.Text1.

Use the DISPATCH\_PROPERTYPUTREF flag to indicate a property or data member that should be set by reference. For example, the following Visual Basic statement assigns the pointer "YourObj" to the property **Prop**, and should be flagged as DISPATCH\_PROPERTYPUTREF.


```C++
Set MyObj.Prop = YourObj
```



The **Set** statement causes a reference assignment, rather than a value assignment.

The parameter on the right side is always passed by name, and should not be accessed positionally.

 

 




