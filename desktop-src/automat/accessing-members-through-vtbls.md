---
title: Accessing Members Through VTBLs
description: Demonstrates how to access a member through its vtable.
ms.assetid: ad374979-d7a8-47a9-985c-3d9b5f188b5c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Accessing Members Through VTBLs

For objects that have dual interfaces, the first seven members of the VTBL are the members of **IUnknown** and [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master), and the subsequent members are standard COM entries for the interface's member functions. You can call these entries directly from C++.

## To access a method or property through the VTBL

1.  Initialize OLE.

2.  Create an instance of the exposed object.

3.  Manipulate the properties and methods of the object.

4.  Uninitialize OLE.

The code sample that follows shows how to access a property of the Hello object. Error handling has been omitted for brevity.


```C++
HRESULT hr;
CLSID clsid;                      // Class ID of Hello object.
LPUNKNOWN punk = NULL;            // Unknown of Hello object.
IHello* phello = NULL;            // IHello interface of Hello object.

// Initialize OLE.
hr = OleInitialize(NULL);

// Retrieve CLSID from the ProgID for Hello.
hr = CLSIDFromProgID("Hello.Application", &amp;clsid);

// Create an instance of the Hello object and ask for its
// IDispatch interface.
hr = CoCreateInstance(clsid, NULL, CLSCTX_SERVER, 
                        IID_IUnknown, (void **)&amp;punk);

hr = punk->QueryInterface(IID_IHello, (void **)&amp;pHello);

punk->Release();                // Release when no longer needed.

hr = pHello->put_Visible (TRUE);

// Additional code to work with other methods and properties 
// (omitted).

pHello->Release();                  // Release when no longer needed.
OleUninitialize();
```



The example initializes OLE, and then calls the **CLSIDFromProgID** function to obtain the class identifier (CLSID) for the Hello application. With the CLSID, the example can call **CoCreateInstance** to create an instance of the Hello Application object. **CoCreateInstance** returns a pointer to the object's **IUnknown** interface (punk), and this, in turn, is used to call **QueryInterface** to get pHello, a pointer to the IID\_IHello dual interface. The punk is no longer needed, so the example releases it. The example then sets the value of the **Visible** property to **True**.

The values returned in the hr variable should be tested for error codes. If any of the function calls return an error HRESULT, you can get detailed, contextual information through the [**IErrorInfo**](/windows/previous-versions/oaidl/nn-oaidl-ierrorinfo?branch=master) interface. For details see [Error Handling Interfaces](error-handling-interfaces.md).

 

 




