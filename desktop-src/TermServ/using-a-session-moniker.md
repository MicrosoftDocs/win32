---
title: Using a Session Moniker
description: Session-to-session activation allows a client process to activate a local server process on a specified session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: de4967b6-6a53-4888-84f9-3fa29cbebe34
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using a Session Moniker

Session-to-session activation allows a client process to activate a local server process on a specified session. You can do this on a per-session basis by using a system-supplied session moniker. For more information about creating a session moniker, see [Session-to-Session Activation with a Session Moniker](session-to-session-activation-with-a-session-moniker.md).

The following example shows how to activate a local server process with the class ID "10000013-0000-0000-0000-000000000001" on the session with the session ID 3.

First, the sample calls the [**CoInitialize**](0f171cf4-87b9-43a6-97f2-80ed344fe376) function to initialize the COM library. Then the sample calls [**CreateBindCtx**](0f0ded09-7a7c-40bb-8198-b9f5058827d4) to retrieve a pointer to an implementation of the [**IBindCtx**](e4c8abb5-0c89-44dd-8d95-efbfcc999b46) interface. This object stores information about moniker-binding operations; the pointer is required to call methods of the [**IMoniker**](17f4c1df-7a9c-42ef-a888-70cd8d85f070) interface. Next the sample calls the [MkParseDisplayNameEx](http://go.microsoft.com/fwlink/p/?linkid=157933) function to create the composite session moniker and then the [**IMoniker::BindToObject**](b5ce39ff-3387-4f72-9aea-5a26eed3810c) method to activate the connection between the client and the server process, using the newly created session moniker. At this point you can use the interface pointer to perform the desired operations on the object. Finally, the sample releases the bind context and calls the [**CoUninitialize**](9411cbed-fa3b-46f7-b677-6ada53324edc) function.


```C++
// Initialize COM.

HRESULT hr = CoInitialize(NULL);
if (FAILED(hr)) exit(0);  // Handle errors here.

// Get interface pBindCtx.

IBindCtx* pBindCtx;
hr = CreateBindCtx(NULL, &amp;pBindCtx);
if (FAILED(hr)) exit(0);  // Handle errors here.

// Get moniker pMoniker.

OLECHAR string[] =
    L"Session:3!clsid:10000013-0000-0000-0000-000000000001";
ULONG ulParsed;
IMoniker* pMoniker;
hr = MkParseDisplayNameEx( pBindCtx,
                           string,
                           &amp;ulParsed,
                           &amp;pMoniker
                          );
if (FAILED(hr)) exit(0);  // Handle errors here.

// Get object factory pSessionTestFactory.

IUnknown* pSessionTestFactory;
hr = pMoniker->BindToObject( pBindCtx,
                             NULL,
                             IID_IUnknown,
                             (void**)&amp;pSessionTestFactory
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
> If the same user is logged on to each session during a cross-session activation, you can successfully activate any server process configured to run in the RunAs Interactive User activation mode. If different users are logged on to each session, the server must call the [**CoInitializeSecurity**](e0933741-6b75-4ce1-aa63-6240e4a7130f) function to set the appropriate user rights before a successful activation and connection can occur between the client and the server. One way to accomplish this would be for the server to implement a custom [**IAccessControl**](f7f19a9d-27ed-479f-b5d4-562cab5be12a) interface and pass the implementation to **CoInitializeSecurity**. In any case, the client user must have the appropriate [**Launch**](7b8c1ae4-fbbd-489f-b1b5-60ae5a04f906) and [**Access Permissions**](92518de0-66ca-4d7a-8d91-63b41e6d3c24) that are specified by the application running on the server. For more information see [Security in COM](c9f6d06c-da24-48ea-908a-2462c33f7ee3).

 

For more information about system-supplied monikers and monikers and activation modes, see [Monikers](ae0cd2f3-8ac0-4388-8781-e86fc4a26b3b), the [**IMoniker**](17f4c1df-7a9c-42ef-a888-70cd8d85f070) interface, and [AppId Key](https://msdn.microsoft.com/library/windows/desktop/ms682359) in the COM documentation in the Platform Software Development Kit (SDK).

 

 




