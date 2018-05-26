---
title: Creating the Global Interface Table
description: Creating the Global Interface Table
ms.assetid: e8e46642-ef41-4322-97d0-8dd5b7c72992
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating the Global Interface Table

Use the following call to create the global interface table object and get a pointer to [**IGlobalInterfaceTable**](/windows/win32/ObjIdl/nn-objidl-iglobalinterfacetable?branch=master):

``` syntax
HRESULT hr;
hr = CoCreateInstance(CLSID_StdGlobalInterfaceTable,
                 NULL,
                 CLSCTX_INPROC_SERVER,
                 IID_IGlobalInterfaceTable,
                 (void **)&gpGIT);
if (hr != S_OK) {
  exit(0); // Handle errors here.
}
```

> [!Note]  
> When creating the global interface table object using the preceding call, it is necessary to link to the library uuid.lib. This will resolve the external symbols CLSID\_StdGlobalInterfaceTable and IID\_IGlobalInterfaceTable.

 

There is a single instance of the global interface table per process, so all calls to this function in a process return the same instance.

After the call to the [**CoCreateInstance**](/windows/win32/combaseapi/nf-combaseapi-cocreateinstance?branch=master) function, register the interface from the apartment in which it resides with a call to the [**RegisterInterfaceInGlobal**](/windows/win32/objidlbase/nf-objidl-iglobalinterfacetable-registerinterfaceinglobal?branch=master) method. This method supplies a cookie that identifies the interface and its location. An apartment seeking a pointer to this interface then calls the [**GetInterfaceFromGlobal**](/windows/win32/objidlbase/nf-objidl-iglobalinterfacetable-getinterfacefromglobal?branch=master) method with this cookie, and the implementation then supplies an interface pointer to the calling apartment. To revoke the interface's global registration, any apartment can call the [**RevokeInterfaceFromGlobal**](/windows/win32/objidlbase/nf-objidl-iglobalinterfacetable-revokeinterfacefromglobal?branch=master) method.

A simple example of using [**IGlobalInterfaceTable**](/windows/win32/ObjIdl/nn-objidl-iglobalinterfacetable?branch=master) would be when you want to pass an interface pointer on an object in a single-threaded apartment (STA) to a worker thread in another apartment. Rather than having to marshal it into a stream and pass the stream to the worker thread as a thread parameter, **IGlobalInterfaceTable** allows you simply to pass a cookie.

When you register the interface in the global interface table, you get a cookie that you can use instead of passing the actual pointer (whenever you need to pass the pointer), either to a nonmethod parameter that is going to another apartment (as a parameter to [*ThreadProc*](https://msdn.microsoft.com/library/windows/desktop/ms686736) through [**CreateThread**](https://msdn.microsoft.com/library/windows/desktop/ms682453)) or to in-process memory accessible outside your apartment.

Care is required because using global interfaces places the extra burden on the programmer of managing problems such as race conditions and mutual exclusion, which are associated with accessing global state from multiple threads simultaneously.

COM provides a standard implementation of the [**IGlobalInterfaceTable**](/windows/win32/ObjIdl/nn-objidl-iglobalinterfacetable?branch=master) interface. It is highly recommended that you use this standard implementation because it provides complete thread-safe functionality.

## Related topics

<dl> <dt>

[When to Use the Global Interface Table](when-to-use-the-global-interface-table.md)
</dt> </dl>

 

 




