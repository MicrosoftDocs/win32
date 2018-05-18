---
title: Implementing the IDispatch Interface
description: ActiveX or OLE objects can implement the IDispatch interface for access by ActiveX clients, such as Visual Basic.
ms.assetid: '0e171f7f-0022-4e9b-ac8e-98192828e945'
---

# Implementing the IDispatch Interface

ActiveX or OLE objects can implement the [**IDispatch**](idispatch.md) interface for access by ActiveX clients, such as Visual Basic. The object's properties and methods can be accessed using [IDispatch::GetIDsOfNames](6F6CF233-3481-436E-8D6A-51F93BF91619) and [IDispatch::Invoke](964ADE8E-9D8A-4D32-BD47-AA678912A54D).

The following examples show how to access an ActiveX or OLE object through the [**IDispatch**](idispatch.md) interface. Portions of the code are omitted for brevity, including handling any errors returned by function calls.


```C++
// Declarations of variables used.
   DEFINE_GUID(CLSID_Hello,      // Portions omitted for brevity.

   HRESULT hresult;
   IUnknown * punk;
   IDispatch * pdisp;
   OLECHAR * szMember = "SayHello";
   DISPID dispid;
   DISPPARAMS dispparamsNoArgs = {NULL, NULL, 0, 0};
   EXCEPINFO excepinfo;
   UINT nArgErr;
```



In the following code, the **OleInitialize** function loads the OLE dynamic-link libraries (DLLs), and the **CoCreateInstance** function initializes the ActiveX or OLE object's class factory. For more information on these two functions, see the *COM Programmer's Reference*.


```C++
// Initialize OLE DLLs.
hresult = OleInitialize(NULL);

// OLE function CoCreateInstance starts application using GUID.
hresult = CoCreateInstance(CLSID_Hello, NULL, CLSCTX_SERVER, IID_IUnknown, (void **)&amp;punk);
```



**QueryInterface** checks whether the object supports [**IDispatch**](idispatch.md). (As with any call to **QueryInterface**, the returned pointer must be released when it is no longer needed.)


```C++
// Call QueryInterface to see if object supports IDispatch.
hresult = punk->QueryInterface(IID_IDispatch, &amp;pdisp);
```



[**GetIDsOfNames**](idispatch-getidsofnames.md) retrieves the DISPID for the indicated method or property, in this case, szMember.


```C++
// Retrieve the dispatch identifier for the SayHello method.
// Use defaults where possible.
hresult = pdisp->GetIDsOfNames(
   IID_NULL,
   &amp;szMember,
   1,
   LOCALE_USER_DEFAULT,
   &amp;dispid);
```



In the following call to [**Invoke**](idispatch-invoke.md), the DISPID indicates the property or method to invoke. The `SayHello` method does not take any parameters, so the fifth argument (&*dispparamsNoArgs*), contains a Null and 0, as initialized at declaration.

To invoke a property or method that requires parameters, supply the parameters in the DISPPARAMS structure.


```C++
// Invoke the method. Use defaults where possible.
hresult = pdisp->Invoke(
   dispid,
   IID_NULL,
   LOCALE_SYSTEM_DEFAULT,
   DISPATCH_METHOD,
   &amp;dispparamsNoArgs,
   NULL,
   NULL,
   NULL);
```



 

 




