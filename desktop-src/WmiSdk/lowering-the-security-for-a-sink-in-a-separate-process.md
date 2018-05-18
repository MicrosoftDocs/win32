---
Description: 'Windows Management Instrumentation (WMI) can create the sink to receive asynchronous callbacks for a client application in a separate process.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '3d3111ac-7d83-48d6-94e4-36cb46a506fa'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Lowering the Security for a Sink in a Separate Process
---

# Lowering the Security for a Sink in a Separate Process

Windows Management Instrumentation (WMI) can create the sink to receive asynchronous callbacks for a client application in a separate process. The separate process is Unsecapp.exe. Use the [**IWbemUnsecuredApartment**](iwbemunsecuredapartment.md) interface. **IWbemUnsecuredApartment** allows you to control whether Unsecapp.exe authenticates callbacks to the sink. For more information, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

You can then lower the security on that process and WMI can access the sink without restriction. To assist with this technique WMI provides the Unsecapp.exe process to function as the separate process. You can host Unsecapp.exe with a call to the [**IUnsecuredApartment**](iunsecuredapartment.md) interface.

The [**IUnsecuredApartment**](iunsecuredapartment.md) interface allows a client application to create a separate dedicated process running Unsecapp.exe for hosting a [**IWbemObjectSink**](iwbemobjectsink.md) implementation. The dedicated process can call [**CoInitializeSecurity**](_com_coinitializesecurity) to grant WMI access to the dedicated process without compromising the security of the main process. After initialization, the dedicated process acts as an intermediary between the main process and WMI.

The following procedure describes how to perform an asynchronous call with [**IUnsecuredApartment**](iunsecuredapartment.md).

**To perform an asynchronous call with IUnsecuredApartment**

1.  Create a dedicated process with a call to [**CoCreateInstance**](_com_cocreateinstance).

    The following code example calls [**CoCreateInstance**](_com_cocreateinstance) to create a dedicated process.

    ```C++
    IUnsecuredApartment* pUnsecApp = NULL;

    CoCreateInstance(CLSID_UnsecuredApartment, NULL, 
      CLSCTX_LOCAL_SERVER, IID_IUnsecuredApartment, 
      (void**)&amp;pUnsecApp);
    ```

    

2.  Instantiate the sink object.

    The following code example creates a new sink object.

    ```C++
    CMySink* pSink = new CMySink;
    pSink->AddRef();
    ```

    

3.  Create a stub for the sink.

    A stub is a wrapper function produced from the sink.

    The following code example calls [**CreateObjectStub**](iunsecuredapartment-createobjectstub.md) to create a stub for the sink.

    ```C++
    IUnknown* pStubUnk = NULL; 
    pUnsecApp->CreateObjectStub(pSink, &amp;pStubUnk);
    ```

    

4.  Call [**QueryInterface**](_com_iunknown_queryinterface) for the wrapper, and request a pointer to the [**IWbemObjectSink**](iwbemobjectsink.md) interface.

    The following code example calls [**QueryInterface**](_com_iunknown_queryinterface) and requests a pointer to the [**IWbemObjectSink**](iwbemobjectsink.md) interface.

    ```C++
    IWbemObjectSink* pStubSink = NULL;
    pStubUnk->QueryInterface(IID_IWbemObjectSink, (void **)&amp;pStubSink); pStubUnk->Release();
    ```

    

5.  Release the sink object pointer.

    You can release the object pointer because the stub now owns the pointer.

    The following code example releases the sink object pointer.

    ```C++
    pSink->Release();
    ```

    

6.  Use the stub in any asynchronous call.

    When finished with the call, release the local reference count.

    The following code example uses the stub in an asynchronous call.

    ```C++
    // pServices is an IWbemServices* object
    pServices->CreateInstanceEnumAsync(strClassName, 0, NULL, pStubSink);
    ```

    

    At times you may have to cancel an asynchronous call after you make the call. If you need to cancel the call, cancel the call with the same pointer that originally made the call.

    The following code example shows how to cancel an asynchronous call.

    ```C++
    pServices->CancelAsyncCall(pStubSink);
    ```

    

7.  Release the local reference count when you are done using the asynchronous call.

    Make sure to release the *pStubSink* pointer only after you confirm that the asynchronous call does not need to be canceled. Further, do not release *pStubSink* after WMI releases the *pSink* sink pointer. Releasing *pStubSink* after *pSink* creates a circular reference count in which both the sink and the stub stay in memory forever. Instead, a possible location to release the pointer is in the [**IWbemObjectSink::SetStatus**](iwbemobjectsink-setstatus.md) call, made by WMI to report that the original asynchronous call is complete.

8.  When finished, uninitialize COM with a call to [**Release()**](_com_iunknown_release).

    The following code example shows how to call [**Release()**](_com_iunknown_release) on the *pUnsecApp* pointer.

    ```C++
    pUnsecApp->Release();
    ```

    

    The code examples in this topic require the following reference and \#include statement to correctly compile.

    ```C++
    #include <wbemidl.h>
    #pragma comment(lib, "wbemuuid.lib")
    ```

    

For more information about the [**CoInitializeSecurity**](_com_coinitializesecurity) function and parameters, see the [COM](_cos_com_start_page) documentation in the Platform Software Development Kit (SDK).

 

 



