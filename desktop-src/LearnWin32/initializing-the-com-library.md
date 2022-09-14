---
title: Initializing the COM Library
description: Initializing the COM Library
ms.assetid: b044e146-8409-4f8d-87d3-52f21ebc2255
ms.topic: article
ms.date: 05/31/2018
---

# Initializing the COM Library

Any Windows program that uses COM must initialize the COM library by calling the [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex) function. Each thread that uses a COM interface must make a separate call to this function. **CoInitializeEx** has the following signature:


```C++
HRESULT CoInitializeEx(LPVOID pvReserved, DWORD dwCoInit);
```



The first parameter is reserved and must be **NULL**. The second parameter specifies the threading model that your program will use. COM supports two different threading models, *apartment threaded* and *multithreaded*. If you specify apartment threading, you are making the following guarantees:

-   You will access each COM object from a single thread; you will not share COM interface pointers between multiple threads.
-   The thread will have a message loop. (See [Window Messages](window-messages.md) in Module 1.)

If either of these constraints is not true, use the multithreaded model. To specify the threading model, set one of the following flags in the *dwCoInit* parameter.



| Flag                          | Description         |
|-------------------------------|---------------------|
| **COINIT\_APARTMENTTHREADED** | Apartment threaded. |
| **COINIT\_MULTITHREADED**     | Multithreaded.      |



 

You must set exactly one of these flags. Generally, a thread that creates a window should use the **COINIT\_APARTMENTTHREADED** flag, and other threads should use **COINIT\_MULTITHREADED**. However, some COM components require a particular threading model. The MSDN documentation should tell you when that is the case.

> [!Note]  
> Actually, even if you specify apartment threading, it is still possible to share interfaces between threads, by using a technique called *marshaling*. Marshaling is beyond the scope of this module. The important point is that with apartment threading, you must never simply copy an interface pointer to another thread. For more information about the COM threading models, see [Processes, Threads, and Apartments](/windows/desktop/com/processes--threads--and-apartments).

 

In addition to the flags already mentioned, it is a good idea to set the **COINIT\_DISABLE\_OLE1DDE** flag in the *dwCoInit* parameter. Setting this flag avoids some overhead associated with Object Linking and Embedding (OLE) 1.0, an obsolete technology.

Here is how you would initialize COM for apartment threading:


```C++
HRESULT hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED | COINIT_DISABLE_OLE1DDE);
```



The **HRESULT** return type contains an error or success code. We'll look at COM error handling in the next section.

## Uninitializing the COM Library

For every successful call to [**CoInitializeEx**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex), you must call [**CoUninitialize**](/windows/desktop/api/combaseapi/nf-combaseapi-couninitialize) before the thread exits. This function takes no parameters and has no return value.


```C++
CoUninitialize();
```



## Next

[Error Codes in COM](error-codes-in-com.md)

 

 