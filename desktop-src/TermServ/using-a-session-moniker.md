---
title: Using a Session Moniker
description: Session-to-session activation allows a client process to activate a local server process on a specified session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: de4967b6-6a53-4888-84f9-3fa29cbebe34
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using a Session Moniker

Session-to-session activation allows a client process to activate a local server process on a specified session. You can do this on a per-session basis by using a system-supplied session moniker. For more information about creating a session moniker, see [Session-to-Session Activation with a Session Moniker](session-to-session-activation-with-a-session-moniker.md).

The following example shows how to activate a local server process with the class ID "10000013-0000-0000-0000-000000000001" on the session with the session ID 3.

First, the sample calls the [**CoInitialize**](https://msdn.microsoft.com/en-us/library/ms678543(v=VS.85).aspx) function to initialize the COM library. Then the sample calls [**CreateBindCtx**](https://msdn.microsoft.com/en-us/library/ms678542(v=VS.85).aspx) to retrieve a pointer to an implementation of the [**IBindCtx**](https://msdn.microsoft.com/en-us/library/ms693755(v=VS.85).aspx) interface. This object stores information about moniker-binding operations; the pointer is required to call methods of the [**IMoniker**](https://msdn.microsoft.com/en-us/library/ms679705(v=VS.85).aspx) interface. Next the sample calls the [MkParseDisplayNameEx](http://go.microsoft.com/fwlink/p/?linkid=157933) function to create the composite session moniker and then the [**IMoniker::BindToObject**](https://msdn.microsoft.com/en-us/library/ms691433(v=VS.85).aspx) method to activate the connection between the client and the server process, using the newly created session moniker. At this point you can use the interface pointer to perform the desired operations on the object. Finally, the sample releases the bind context and calls the [**CoUninitialize**](https://msdn.microsoft.com/en-us/library/ms688715(v=VS.85).aspx) function.


```C++
// Initialize COM.

HRESULT hr = CoInitialize(NULL);
if (FAILED(hr)) exit(0);  // Handle errors here.

// Get interface pBindCtx.

IBindCtx* pBindCtx;
hr = CreateBindCtx(NULL, &pBindCtx);
if (FAILED(hr)) exit(0);  // Handle errors here.

// Get moniker pMoniker.

OLECHAR string[] =
    L"Session:3!clsid:10000013-0000-0000-0000-000000000001";
ULONG ulParsed;
IMoniker* pMoniker;
hr = MkParseDisplayNameEx( pBindCtx,
                           string,
                           &ulParsed,
                           &pMoniker
                          );
if (FAILED(hr)) exit(0);  // Handle errors here.

// Get object factory pSessionTestFactory.

IUnknown* pSessionTestFactory;
hr = pMoniker->BindToObject( pBindCtx,
                             NULL,
                             IID_IUnknown,
                             (void**)&pSessionTestFactory
                            );
if (FAILED(hr)) exit(0);  // Handle errors here.

//
// Make, use, and destroy object here.
//
pSessionTestFactory->Release();
pSessionTestFactory = NULL;

pMoniker->Release();  // Release moniker.

pBindCtx->Release();  // Release interface.

CoUninitialize();  // Release COM.
```



Because "{class id of the class moniker}" is also a way to name a class moniker, you can use the following string to name the composite moniker (the session moniker composed with the class moniker) instead of the way show in the preceding example.

``` syntax
OLECHAR string[] = 
    L"Session:3!{0000031A-0000-0000-C000-000000000046}:
    10000013-0000-0000-0000-000000000001";
```

> [!Note]  
> If the same user is logged on to each session during a cross-session activation, you can successfully activate any server process configured to run in the RunAs Interactive User activation mode. If different users are logged on to each session, the server must call the [**CoInitializeSecurity**](https://msdn.microsoft.com/en-us/library/ms693736(v=VS.85).aspx) function to set the appropriate user rights before a successful activation and connection can occur between the client and the server. One way to accomplish this would be for the server to implement a custom [**IAccessControl**](https://msdn.microsoft.com/en-us/library/ms694421(v=VS.85).aspx) interface and pass the implementation to **CoInitializeSecurity**. In any case, the client user must have the appropriate [**Launch**](https://msdn.microsoft.com/en-us/library/ms687202(v=VS.85).aspx) and [**Access Permissions**](https://msdn.microsoft.com/en-us/library/ms688679(v=VS.85).aspx) that are specified by the application running on the server. For more information see [Security in COM](https://msdn.microsoft.com/en-us/library/ms693319(v=VS.85).aspx).

 

For more information about system-supplied monikers and monikers and activation modes, see [Monikers](https://msdn.microsoft.com/en-us/library/ms691261(v=VS.85).aspx), the [**IMoniker**](https://msdn.microsoft.com/en-us/library/ms679705(v=VS.85).aspx) interface, and [AppId Key](https://msdn.microsoft.com/library/windows/desktop/ms682359) in the COM documentation in the Platform Software Development Kit (SDK).

 

 




