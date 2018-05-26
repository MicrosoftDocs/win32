---
Description: After you have set the standard calls to COM, you must then connect to WMI through a call to the IWbemLocatorConnectServer method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f0b33ff0-47b0-4aea-ab0f-9220ae367f67
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Creating a Connection to a WMI Namespace
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating a Connection to a WMI Namespace

After you have set the standard calls to COM, you must then connect to WMI through a call to the [**IWbemLocator::ConnectServer**](/windows/win32/Wbemcli/nf-wbemcli-iwbemlocator-connectserver?branch=master) method. The **ConnectServer** method returns a proxy of an [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) interface. Through **IWbemServices**, you can access the different capabilities of WMI.

The code examples in this topic require the following references and \#include statements to compile correctly.


```C++
#define _WIN32_DCOM
#include <iostream>
using namespace std;
#include <windows.h>
#include <wbemidl.h>
#pragma comment(lib, "wbemuuid.lib")
```



The following procedure describes how to create a connection to a WMI namespace.

**To create a connection to a WMI namespace**

-   Initialize the [**IWbemLocator**](/windows/win32/Wbemcli/nn-wbemcli-iwbemlocator?branch=master) interface through a call to [**CoCreateInstance**](_com_cocreateinstance).

    WMI does not require that you perform any additional procedures when calling [**CoCreateInstance**](_com_cocreateinstance) on [**IWbemLocator**](/windows/win32/Wbemcli/nn-wbemcli-iwbemlocator?branch=master).

    The following code example describes how to initialize [**IWbemLocator**](/windows/win32/Wbemcli/nn-wbemcli-iwbemlocator?branch=master).

    ```C++
        IWbemLocator *pLoc = 0;
        HRESULT hr;

        hr = CoCreateInstance(CLSID_WbemLocator, 0, 
            CLSCTX_INPROC_SERVER, IID_IWbemLocator, (LPVOID *) &amp;pLoc);
     
        if (FAILED(hr))
        {
            cout << "Failed to create IWbemLocator object. Err code = 0x"
                 << hex << hr << endl;
            CoUninitialize();
            return hr;     // Program has failed.
        }
    ```

    

    -   Connect to WMI through a call to the [**IWbemLocator::ConnectServer**](/windows/win32/Wbemcli/nf-wbemcli-iwbemlocator-connectserver?branch=master) method.

        The [**ConnectServer**](/windows/win32/Wbemcli/nf-wbemcli-iwbemlocator-connectserver?branch=master) method returns a proxy to an [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) interface that use to access the local or remote WMI namespace specified in your call to **ConnectServer**.

        The following code example describes how to call [**ConnectServer**](/windows/win32/Wbemcli/nf-wbemcli-iwbemlocator-connectserver?branch=master).

        ```C++
        IWbemServices *pSvc = 0;

            // Connect to the root\default namespace with the current user.
            hr = pLoc->ConnectServer(
                    BSTR(L"ROOT\\DEFAULT"),  //namespace
                    NULL,       // User name 
                    NULL,       // User password
                    0,         // Locale 
                    NULL,     // Security flags
                    0,         // Authority 
                    0,        // Context object 
                    &amp;pSvc);   // IWbemServices proxy


            if (FAILED(hr))
            {
                cout << "Could not connect. Error code = 0x" 
                     << hex << hr << endl;
                pLoc->Release();
                CoUninitialize();
                return hr;      // Program has failed.
            }

            cout << "Connected to WMI" << endl;
        ```

        

After you have received a pointer to the [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) proxy, you must set the security on the proxy to access WMI. For more information, see [Setting the Security Levels on a WMI Connection](setting-the-security-levels-on-a-wmi-connection.md).

## Related topics

<dl> <dt>

[Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md)
</dt> <dt>

[IPv6 and IPv4 Support in WMI](ipv6-and-ipv4-support-in-wmi.md)
</dt> </dl>

 

 



