---
description: Asynchronous calls present serious security risks because a callback to the sink may not be a result of the asynchronous call by the original application or script.
ms.assetid: 2b839ea9-e1e6-4123-a98a-04ebee907b3b
ms.tgt_platform: multiple
title: Setting Security on an Asynchronous Call
ms.topic: article
ms.date: 05/31/2018
---

# Setting Security on an Asynchronous Call

Asynchronous calls present serious security risks because a callback to the [*sink*](gloss-s.md) may not be a result of the asynchronous call by the original application or script. Security in remote connections is based on encryption of the communication between the client and the provider on the remote computer. In C++ you can set encryption through the authentication level parameter in the call to [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity). In scripting, set the *AuthenticationLevel* in the moniker connection or on an [**SWbemSecurity**](swbemsecurity.md) object. For more information, see [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

The security risks for asynchronous calls exist because WMI lowers the authentication level on a callback until the callback succeeds. On an outgoing asynchronous call, the client can set the authentication level on the connection to WMI. WMI retrieves the security settings on the client call and attempts to call back with the same authentication level. The callback is always initiated at the **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY** level. If the callback fails, WMI lowers the authentication level to a level where the callback can succeed, if necessary, to **RPC\_C\_AUTHN\_LEVEL\_NONE**. In the context of calls within the local system where the authentication service is not Kerberos, the callback is always returned at **RPC\_C\_AUTHN\_LEVEL\_NONE**.

The minimum authentication level is **RPC\_C\_AUTHN\_LEVEL\_PKT** (**wbemAuthenticationLevelPkt**for scripting). However, you can specify a higher level, such as **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY** (**wbemAuthenticationLevelPktPrivacy**). It is recommended that client applications or scripts set the authentication level to **RPC\_C\_AUTHN\_LEVEL\_DEFAULT** (**wbemAuthenticationLevelDefault**) which allows the authentication level to be negotiated to the level specified by the server.

The **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM**\\**CIMOM**\\**UnsecAppAccessControlDefault** registry value controls whether WMI checks for an acceptable authentication level in callbacks. This is the only mechanism for protecting sink security for asynchronous calls made in scripting or Visual Basic. By default, this registry key is set to zero. If the registry key is zero then WMI does not verify authentication levels. To secure asynchronous calls in scripting, set the registry key to 1. C++ clients can call [**IWbemUnsecuredApartment::CreateSinkStub**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemunsecuredapartment-createsinkstub) to control access to the sink. The value is created anywhere by default.

The following topics provide examples of setting asynchronous call security:

-   [Setting Security on an Asynchronous Call in VBScript](setting-security-on-an-asynchronous-call-in-vbscript.md)
-   Setting Asynchronous Call Security in C++

## Setting Asynchronous Call Security in C++

The [**IWbemUnsecuredApartment::CreateSinkStub**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemunsecuredapartment-createsinkstub) method is similar to [**IUnsecuredApartment::CreateObjectStub**](/windows/desktop/api/Wbemcli/nf-wbemcli-iunsecuredapartment-createobjectstub) method and creates a sink in a separate process, Unsecapp.exe, to receive callbacks. However, the **CreateSinkStub** method has a *dwFlag*parameter that specifies how the separate process handles access control.

The *dwFlag* parameter specifies one of the following actions for Unsecapp.exe:

-   Use the registry key setting to determine whether or not to check access.
-   Ignore the registry key and always check access.
-   Ignore the registry key and never check access.

The code example in this topic requires the following \#include statement to correctly compile.


```C++
#include <wbemidl.h>
```



The following procedure describes how to perform an asynchronous call with [**IWbemUnsecuredApartment**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemunsecuredapartment).

**To perform an asynchronous call with IWbemUnsecuredApartment**

1.  Create a dedicated process with a call to [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance).

    The following code example calls [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) to create a dedicated process.

    ```C++
    CLSID                    CLSID_WbemUnsecuredApartment;
    IWbemUnsecuredApartment* pUnsecApp = NULL;

    CoCreateInstance(CLSID_WbemUnsecuredApartment, 
                     NULL, 
                     CLSCTX_LOCAL_SERVER, 
                     IID_IWbemUnsecuredApartment, 
                     (void**)&pUnsecApp);
    ```

    

2.  Instantiate the sink object.

    The following code example creates a new sink object.

    ```C++
    CMySink* pSink = new CMySink;
    pSink->AddRef();
    ```

    

3.  Create a stub for the sink.

    A stub is a wrapper function produced from the sink.

    The following code example creates a stub for the sink.

    ```C++
    LPCWSTR          wszReserved = NULL;           
    IWbemObjectSink* pStubSink   = NULL;
    IUnknown*        pStubUnk    = NULL; 

    pUnsecApp->CreateSinkStub(pSink,
                              WBEM_FLAG_UNSECAPP_CHECK_ACCESS,  //Authenticate callbacks regardless of registry key
                              wszReserved,
                              &pStubSink);
    ```

    

4.  Release the sink object pointer.

    You can release the object pointer because the stub now owns the pointer.

    The following code example releases the object pointer.

    ```C++
    pSink->Release();
    ```

    

5.  Use the stub in any asynchronous call.

    When finished with the call, release the local reference count.

    The following code example uses the stub in an asynchronous call.

    ```C++
    // pServices is an IWbemServices* object
    pServices->CreateInstanceEnumAsync(strClassName, 0, NULL, pStubSink);
    ```

    

    At times you may have to cancel an asynchronous call after you make the call. If you need to cancel the call, cancel the call with the same pointer that originally made the call.

    The following code example describes how to cancel an asynchronous call.

    ```C++
    pServices->CancelAsyncCall(pStubSink);
    ```

    

6.  Release the local reference count when you are done using the asynchronous call.

    Make sure to release the *pStubSink* pointer only after you confirm that the asynchronous call does not must be canceled. Further, do not release *pStubSink* after WMI releases the *pSink* sink pointer. Releasing *pStubSink* after *pSink* creates a circular reference count in which both the sink and the stub stay in memory forever. Instead, a possible location to release the pointer is in the [**IWbemObjectSink::SetStatus**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectsink-setstatus) call, made by WMI to report that the original asynchronous call is complete.

7.  When finished, uninitialize COM with a call to [**Release()**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release).

    The following code example shows how to call [**Release()**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) on the *pUnsecApp* pointer.

    ```C++
    pUnsecApp->Release();
    ```

    

For more information about the [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) function and parameters, see the [COM](../cossdk/component-services-portal.md) documentation.

 

 
