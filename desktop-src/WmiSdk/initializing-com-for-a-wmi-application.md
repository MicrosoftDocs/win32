---
description: The first step in connecting to WMI is setting up the COM calls to CoInitializeEx and CoInitializeSecurity.
ms.assetid: c9291aa7-702c-4752-8bd0-97d7a6e6dd54
ms.tgt_platform: multiple
title: Initializing COM for a WMI Application
ms.topic: article
ms.date: 05/31/2018
---

# Initializing COM for a WMI Application

The first step in connecting to WMI is setting up the COM calls to [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) and [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity).

The code examples in this topic require the following references and \#include statements to compile correctly.


```C++
#define _WIN32_DCOM
#include <iostream>
using namespace std;
#include <wbemidl.h>
#pragma comment(lib, "wbemuuid.lib")
```



The following procedure describes how to initialize COM from a client application.

**To initialize COM from a client application**

1.  Initialize COM with a call to [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex).

    Calling [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) is a standard procedure for setting up a COM interface. Therefore, WMI does not require that you observe any additional procedures when calling **CoInitializeEx**. For more information, see [COM](../com/component-object-model--com--portal.md).

    The following code example describes how to call [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex).

    ```C++
    HRESULT hr;
    hr = CoInitializeEx(0, COINIT_MULTITHREADED); 
    if (FAILED(hr)) 
    { cout << "Failed to initialize COM library. Error code = 0x"
           << hex << hr << endl; 
      return hr;
    }
    ```

    

2.  Set the general COM security levels with a call to the [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) interface.

    [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) is a standard function you must call when setting up a COM interface for a process. Call **CoInitializeSecurity** if you want to set the default security settings for authentication, impersonation, or authentication service for an entire process. For more information, see [Setting Client Application Process Security](setting-client-application-process-security.md). If you want to set or change the security for a specific proxy, you must call [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket). Use **CoSetProxyBlanket** whenever you must set or change COM security when running inside another process where you cannot control the default security settings for authentication, impersonation, or authentication service. For more information, see [Setting the Security Levels on a WMI Connection](setting-the-security-levels-on-a-wmi-connection.md) and [Setting the Security on IWbemServices and Other Proxies](setting-the-security-on-iwbemservices-and-other-proxies.md).

    WMI has several security issues you should be aware of when programming a WMI client application. For more information, see [Setting Client Application Process Security](setting-client-application-process-security.md).

    The following code example describes how to call [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) to set COM security on the process.

    ```C++
    hr =  CoInitializeSecurity(
        NULL,                        // Security descriptor    
        -1,                          // COM negotiates authentication service
        NULL,                        // Authentication services
        NULL,                        // Reserved
        RPC_C_AUTHN_LEVEL_DEFAULT,   // Default authentication level for proxies
        RPC_C_IMP_LEVEL_IMPERSONATE, // Default Impersonation level for proxies
        NULL,                        // Authentication info
        EOAC_NONE,                   // Additional capabilities of the client or server
        NULL);                       // Reserved

    if (FAILED(hr))
    {
       cout << "Failed to initialize security. Error code = 0x" 
            << hex << hr << endl;
       CoUninitialize();
       return hr;                  // Program has failed.
    }
    ```

    

After you initialize COM, your next step is to create a connection to a WMI namespace. For more information, see [Creating a Connection to a WMI Namespace](creating-a-connection-to-a-wmi-namespace.md).

## Related topics

<dl> <dt>

[Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md)
</dt> <dt>

[Access to WMI Namespaces](access-to-wmi-namespaces.md)
</dt> </dl>

 

 
