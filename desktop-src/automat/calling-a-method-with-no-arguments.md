---
title: Calling a Method with No Arguments
description: The simplest use of Invoke is to call a method that does not have any arguments. You only need to pass the DISPID of the method, a LCID, the DISPATCH\_METHOD flag, and an empty DISPPARAMS structure.
ms.assetid: 'b2d18dcb-2e3c-43d1-8692-33caebc66086'
---

# Calling a Method with No Arguments

The simplest use of [**Invoke**](idispatch-invoke.md) is to call a method that does not have any arguments. You only need to pass the DISPID of the method, a LCID, the DISPATCH\_METHOD flag, and an empty DISPPARAMS structure.

The following example demonstrates the simplest use of [**Invoke**](idispatch-invoke.md). Error handling has been omitted for brevity.


```C++
HRESULT hresult;
IUnknown * punk;
IDispatch * pdisp = (IDispatch *)NULL;
OLECHAR * szMember = L"Simple";
DISPID dispid;
DISPPARAMS dispparamsNoArgs = {NULL, NULL, 0, 0};

hresult = CoCreateInstance(
            CLSID_CMyObject, 
            NULL, 
            CLSCTX_SERVER, 
            IID_IUnknown, 
            (void **)&amp;punk);

hresult = punk->QueryInterface(IID_IDispatch, (void **)&amp;pdisp);

hresult = pdisp->GetIDsOfNames(IID_NULL, &amp;szMember, 1, LOCALE_USER_DEFAULT, &amp;dispid);

hresult = pdisp->Invoke(
            dispid,
            IID_NULL,
            LOCALE_USER_DEFAULT,
            DISPATCH_METHOD,
            &amp;dispparamsNoArgs, NULL, NULL, NULL);
```



The example invokes a method named "Simple" on an object of the class CMyObject. First, it calls **CoCreateInstance**, which instantiates the object and returns a pointer to the object's **IUnknown** interface (punk). Next, it calls **QueryInterface**, receiving a pointer to the object's [**IDispatch**](idispatch.md) interface (pdisp). It then uses pdisp to call the object's [**GetIDsOfNames**](idispatch-getidsofnames.md) function, passing the string "Simple" in szMember to get the DISPID for the **Simple** method. With the DISPID for **Simple** in dispid, it calls [**Invoke**](idispatch-invoke.md) to invoke the method, specifying DISPATCH\_METHOD for the wFlags parameter and using the system default locale.

To further simplify the code, the example declares a DISPPARAMS structure named dispparamsNoArgs that is appropriate to an [**Invoke**](idispatch-invoke.md) call with no arguments.

Because the **Simple** method does not take any arguments and does not return a result, the puArgErr and pVarResult parameters are Null. In addition, the example passes Null for pExcepInfo, indicating that it is not prepared to handle exceptions and will handle only HRESULT errors.

Most methods, however, take one or more arguments. To invoke these methods, the DISPPARAMS structure should be filled in, as described in [Passing Parameters](passing-parameters.md).

Automation defines special DISPIDs for invoking an object's **Value** property (the default), and the members **\_NewEnum**, and **Evaluate**. For details, see [**DISPID Data Type**](dispid-constants.md) and [Data Types, Structures, and Enumerations](882167ac-2710-43e9-a203-02b59e7d8ea4).

 

 




