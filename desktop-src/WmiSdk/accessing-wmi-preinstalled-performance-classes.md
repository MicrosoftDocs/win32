---
Description: The WMI repository contains preinstalled performance classes for all the performance library objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2158385f-d0dc-4102-84db-ce02d2b0ee53
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Accessing WMI Preinstalled Performance Classes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Accessing WMI Preinstalled Performance Classes

The WMI repository contains preinstalled performance classes for all the performance library objects. For example, instances of the raw data performance class [**Win32\_PerfRawData\_PerfProc\_Process**](https://msdn.microsoft.com/library/dn750765) represent processes. This performance object is visible in System Monitor as the Process object.

The **PageFaultsPerSec** property of [**Win32\_PerfRawData\_PerfProc\_Process**](https://msdn.microsoft.com/library/dn750765) represents the Page Faults per second performance counter for the process. The [**Win32\_PerfFormattedData**](https://msdn.microsoft.com/library/aa394253) classes contain the calculated data values displayed in System Monitor (Perfmon.exe). The value of the **PageFaultsPerSec** property of [**Win32\_PerfFormattedData\_PerfProc\_Process**](https://msdn.microsoft.com/library/dn750765) is the same as when it appears in System Monitor.

Use either the [COM API for WMI](com-api-for-wmi.md) or the [Scripting API for WMI](scripting-api-for-wmi.md) to access performance data through the [Performance Counter Classes](https://msdn.microsoft.com/library/aa392738). In both cases a [*refresher*](gloss-r.md) object is required to obtain each data sample. For more information and script code examples for using refreshers and accessing performance classes, see [WMI Tasks: Performance Monitoring](wmi-tasks--performance-monitoring.md). For more information, see [Accessing Performance Data in Script](accessing-performance-data-in-script.md).

## Accessing Performance Data from C++

The following C++ code example uses the Performance Counter provider to access predefined high-performance classes. It creates a refresher object and adds an object to the refresher. The object is a [**Win32\_PerfRawData\_PerfProc\_Process**](https://msdn.microsoft.com/library/dn750765) instance that monitors the performance of a specific process. The code only reads one counter property in the process object, the **VirtualBytes** property. The code requires the following references and **\#include** statements to compile correctly.


```C++
#define _WIN32_DCOM
#include <iostream>
using namespace std;
#include <wbemidl.h>
#pragma comment(lib, "wbemuuid.lib")
```



The following procedure shows how to access data from a high-performance provider in C++.

**To access data from a high-performance provider in C++**

1.  Establish a connection to the WMI namespace, and set WMI security by using a call to [**IWbemLocator::ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver) and [**CoSetProxyBlanket**](https://msdn.microsoft.com/windows/desktop/c2e5e681-8fa5-4b02-b59d-ba796eb0dccf).

    This step is a standard step for creating any WMI client application. For more information, see [Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md).

2.  Create a refresher object by using [**CoCreateInstance**](https://msdn.microsoft.com/windows/desktop/7295a55b-12c7-4ed0-a7a4-9ecee16afdec) with CLSID\_WbemRefresher. Request an [**IWbemConfigureRefresher**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemconfigurerefresher) interface through the [**QueryInterface**](https://msdn.microsoft.com/windows/desktop/54d5ff80-18db-43f2-b636-f93ac053146d) method. Request an [**IWbemRefresher**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemrefresher) interface through the **QueryInterface** method.

    The [**IWbemRefresher**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemrefresher) interface is the main interface for the WMI [**Refresher**](swbemrefreshableitem-refresher.md) object.

    The following C++ code example shows how to retrieve [**IWbemConfigureRefresher**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemrefresher).

    ```C++
    IWbemRefresher* pRefresher = NULL;

    HRESULT hr = CoCreateInstance(
        CLSID_WbemRefresher,
        NULL,
        CLSCTX_INPROC_SERVER,
        IID_IWbemRefresher,
        (void**) &amp;pRefresher);

    IWbemConfigureRefresher* pConfig = NULL;

    pRefresher->QueryInterface( 
        IID_IWbemConfigureRefresher,
        (void**) &amp;pConfig
      );
    ```

    

3.  Add an object to the refresher through a call to the [**IWbemConfigureRefresher::AddObjectByPath**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemconfigurerefresher-addobjectbypath) method.

    When you add an object to the refresher, WMI refreshes the object whenever you call the [**IWbemRefresher::Refresh**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemrefresher-refresh) method. The object you add designates the provider in its class qualifiers.

    The following C++ code example shows how to call [**AddObjectByPath**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemconfigurerefresher-addobjectbypath).

    ```C++
    IWbemClassObject* pObj = NULL;
    IWbemServices* pNameSpace = NULL;

    // Add the instance to be refreshed.
    hr = pConfig->AddObjectByPath(
         pNameSpace,
         L"Win32_PerfRawData_PerfProc_Process.Name=\"WINWORD\"",
         0L,
         NULL,
         &amp;pObj,
         NULL
    );
    if (FAILED(hr))
    {
       cout << "Could not add object. Error code: 0x"
            << hex << hr << endl;
       pNameSpace->Release();
       return hr;
    }
    ```

    

4.  To set up faster access to the object, connect to the [**IWbemObjectAccess**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjectaccess) interface through [**QueryInterface**](https://msdn.microsoft.com/windows/desktop/54d5ff80-18db-43f2-b636-f93ac053146d) on the [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject) interface.

    The following C++ code example shows how to retrieve a pointer to the object using [**IWbemObjectAccess**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjectaccess) instead of [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject).

    ```C++
        // For quick property retrieval, use IWbemObjectAccess.
        IWbemObjectAccess* pAcc = NULL;
        pObj->QueryInterface( IID_IWbemObjectAccess, (void**) &amp;pAcc );
        // This is not required.
        pObj->Release();
    ```

    

    The [**IWbemObjectAccess**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemobjectaccess) interface increases performance because you can get handles to specific counter properties, and it requires that you lock and unlock the object in your code, which is an operation that [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject) performs for each property access.

5.  Obtain the handles of the properties to examine by using calls to the [**IWbemObjectAccess::GetPropertyHandle**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectaccess-getpropertyhandle) method.

    Property handles are the same for all instances of a class, which means that use the property handle you retrieve from a specific instance for all instances of a specific class. You can also obtain a handle from a class object to retrieve property values from an instance object.

    The following C++ code example shows how to retrieve a property handle.

    ```C++
        // Get a property handle for the VirtualBytes property
        long lVirtualBytesHandle = 0;
        DWORD dwVirtualBytes = 0;
        CIMTYPE variant;

        hr = pAcc->GetPropertyHandle(L"VirtualBytes",
             &amp;variant,
             &amp;lVirtualBytesHandle 
        );
        if (FAILED(hr))
        {
           cout << "Could not get property handle. Error code: 0x"
                << hex << hr << endl;
           return hr;
        }
    ```

    

6.  Create a programming loop that performs the following actions:

    -   Refresh the object with a call to [**IWbemRefresher::Refresh**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemrefresher-refresh) by using the pointer created in the previous call to [**CoCreateInstance**](https://msdn.microsoft.com/windows/desktop/7295a55b-12c7-4ed0-a7a4-9ecee16afdec).

        In this call, the WMI Refresher refreshes the client object by using data that the provider supplies.

    -   Perform any action as necessary on the object, such as retrieving a property name, data type, or value.

        You can access the property through the property handle obtained earlier. Due to the [**Refresh**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemrefresher-refresh) call, WMI refreshes the property each time through the loop.

The following C++ example shows how to use the WMI high-performance API.


```C++
// Get the local locator object
IWbemServices* pNameSpace = NULL;
IWbemLocator* pWbemLocator = NULL;
CIMTYPE variant;
VARIANT VT;

CoCreateInstance( CLSID_WbemLocator, NULL,
    CLSCTX_INPROC_SERVER, IID_IWbemLocator, (void**) &amp;pWbemLocator
);

// Connect to the desired namespace
BSTR bstrNameSpace = SysAllocString( L"\\\\.\\root\\cimv2" );

HRESULT hr = WBEM_S_NO_ERROR;

hr = pWbemLocator->ConnectServer(
     bstrNameSpace,      // Namespace name
     NULL,               // User name
     NULL,               // Password
     NULL,               // Locale
     0L,                 // Security flags
     NULL,               // Authority
     NULL,               // Wbem context
     &amp;pNameSpace         // Namespace
);

if ( SUCCEEDED( hr ) )
{
    // Set namespace security.
    IUnknown* pUnk = NULL;
    pNameSpace->QueryInterface( IID_IUnknown, (void**) &amp;pUnk );

    hr = CoSetProxyBlanket(
         pNameSpace, 
         RPC_C_AUTHN_WINNT, 
         RPC_C_AUTHZ_NONE, 
         NULL, 
         RPC_C_AUTHN_LEVEL_DEFAULT, 
         RPC_C_IMP_LEVEL_IMPERSONATE,
         NULL, 
         EOAC_NONE 
    );
    if (FAILED(hr))
    {
       cout << "Cannot set proxy blanket. Error code: 0x"
            << hex << hr << endl;
       pNameSpace->Release();
       return hr;
    }

    hr = CoSetProxyBlanket(pUnk, 
         RPC_C_AUTHN_WINNT, 
         RPC_C_AUTHZ_NONE, 
         NULL, 
         RPC_C_AUTHN_LEVEL_DEFAULT, 
         RPC_C_IMP_LEVEL_IMPERSONATE,
         NULL, 
         EOAC_NONE 
    );
    if (FAILED(hr))
    {
       cout << "Cannot set proxy blanket. Error code: 0x"
            << hex << hr << endl;
       pUnk->Release();
       return hr;
    }

    // Clean up the IUnknown.
    pUnk->Release();

    IWbemRefresher* pRefresher = NULL;
    IWbemConfigureRefresher* pConfig = NULL;

    // Create a WMI Refresher and get a pointer to the
    // IWbemConfigureRefresher interface.
    CoCreateInstance(CLSID_WbemRefresher, 
                     NULL,
                     CLSCTX_INPROC_SERVER, 
                     IID_IWbemRefresher, 
                     (void**) &amp;pRefresher 
    );
    
    pRefresher->QueryInterface(IID_IWbemConfigureRefresher,
                               (void**) &amp;pConfig );

    IWbemClassObject* pObj = NULL;

    // Add the instance to be refreshed.
    pConfig->AddObjectByPath(
       pNameSpace,
       L"Win32_PerfRawData_PerfProc_Process.Name=\"WINWORD\"",
       0L,
       NULL,
       &amp;pObj,
       NULL 
    );
    if (FAILED(hr))
    {
       cout << "Cannot add object. Error code: 0x"
            << hex << hr << endl;
       pNameSpace->Release();
       
       return hr;
    }

    // For quick property retrieval, use IWbemObjectAccess.
    IWbemObjectAccess* pAcc = NULL;
    pObj->QueryInterface(IID_IWbemObjectAccess, 
                         (void**) &amp;pAcc );

    // This is not required.
    pObj->Release();

    // Get a property handle for the VirtualBytes property.
    long lVirtualBytesHandle = 0;
    DWORD dwVirtualBytes = 0;

    pAcc->GetPropertyHandle(L"VirtualBytes", 
                            &amp;variant, 
                            &amp;lVirtualBytesHandle );

    // Refresh the object ten times and retrieve the value.
    for( int x = 0; x < 10; x++ )
    {
        pRefresher->Refresh( 0L );
        pAcc->ReadDWORD( lVirtualBytesHandle, &amp;dwVirtualBytes );
        printf( "Process is using %lu bytes\n", dwVirtualBytes );
        // Sleep for a second.
        Sleep( 1000 );
    }
    // Clean up all the objects.
    pAcc->Release();
    // Done with these too.
    pConfig->Release();
    pRefresher->Release();
    pNameSpace->Release();
}
SysFreeString( bstrNameSpace );
pWbemLocator->Release();
```



## Related topics

<dl> <dt>

[Performance Counter Classes](https://msdn.microsoft.com/library/aa392738)
</dt> <dt>

[WMI Tasks: Performance Monitoring](wmi-tasks--performance-monitoring.md)
</dt> </dl>

 

 



