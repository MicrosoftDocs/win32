---
title: Querying an ICF Port
description: Querying an ICF Port
ms.assetid: 99d469fb-70cf-422a-a5dc-00a5b59f2955
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying an ICF Port

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. It is unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The following example code demonstrates the interaction between per interface settings and global settings.

-   Checks if the IPv6 Firewall is installed.
-   Enables an IPv6 Firewall on an interface.
-   Evaluates port status using both per interface and global setting values.


```C++
//
// Checks if port is opened for traffic coming over an interface
//

#define WIN32_LEAN_AND_MEAN        // Exclude rarely-used stuff from Windows headers
#include <windows.h>
#include <stdio.h>
#include <tchar.h>


// COM
#include <objbase.h>
#include <comdef.h>
#include <comutil.h>

#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "oleaut32.lib")


// Firewall
#include "netfwv6.h"


// Friendly name of the connection
const _bstr_t cbstrConnectionName (L"Teredo Tunneling Pseudo-Interface");

// Parameters of the port to check
const unsigned short cnPort = 50000;
const PORT_PROTOCOL cProtocol = PORT_PROTOCOL_UDP;


int _tmain()
{
    HRESULT hr;
    INetFwV6Mgr*   pfwmgr;

//
// Step 1. Check if the Internet Connection Firewall for IPv6 is installed
//

    //
    // Initialize COM
    //
    hr = CoInitializeEx(
            NULL,
            COINIT_DISABLE_OLE1DDE | COINIT_APARTMENTTHREADED
            );

    if (FAILED(hr))
    {
        //
        // Cannot initialize COM
        //
        printf ("Cannot initialize COM");
        goto error;
    }

    //
    // Create firewall Configuration Manager COM Instance
    //
    hr = CoCreateInstance(
                CLSID_NetFwV6Mgr,
                NULL,
                CLSCTX_INPROC_SERVER,
                __uuidof(INetFwV6Mgr), 
                (LPVOID*)&amp;pfwmgr
                );

    if (REGDB_E_CLASSNOTREG == hr)
    {
        //
        // Firewall is not installed on the machine
        //
        printf("Firewall is not installed on the machine");
        return 0;
    }

    if (FAILED(hr) || NULL == pfwmgr)
    {
        //
        // Cannot get a hold of the firewall manager
        //
        goto error;
    }


//
// Step 2. Find the interface
//

    //
    // Enumerate connections and find the interface
    // named "Teredo Tunneling Pseudo-Interface"
    //
    IEnumNetFwV6Connections* pConnections = NULL;
    hr = pfwmgr->EnumerateConnections(&amp;pConnections);

    if (FAILED (hr))
    {
        printf ("Cannot enumerate connections");
        goto error;
    }

    INetFwV6Connection* pConn = NULL;
    bool bFound = false;
    while (S_OK == (hr = pConnections->Next (1, &amp;pConn, NULL)))
    {
        BSTR bstrName;
        hr = pConn->get_Name (&amp;bstrName);
        if (FAILED (hr))
        {
            printf ("Cannot get the name of the connection");
            goto error;
        }

        if (cbstrConnectionName.operator == (bstrName))
        {
            bFound = true;
            break;
        }
    }

    if (!bFound)
    {
        //
        // Could not find the interface
        //
        printf ("Cannot find the Teredo interface");
        goto error;
    }

//
// Step 3. Check if port is opened
//
    //
    // Get the per interface setting
    //
    VARIANT_BOOL vbIsPortOpenPerInterface;
    hr = pConn->IsPortOpen (cnPort, cProtocol, &amp;vbIsPortOpenPerInterface);
    if (FAILED (hr))
    {
        goto error;
    }

    //
    // Get the global setting
    //
    VARIANT_BOOL vbIsPortGloballyOpen;
    hr = pfwmgr->IsPortGloballyOpen(cnPort, cProtocol, &amp;vbIsPortGloballyOpen);
    if (FAILED (hr))
    {
        goto error;
    }
    
    //
    // Get the per interface ignore setting
    //
    VARIANT_BOOL vbIsPortGloballyIgnored;
    hr = pConn->IsGlobalPortIgnored (cnPort, cProtocol, &amp;vbIsPortGloballyIgnored);
    if (FAILED (hr))
    {
        goto error;
    }
    
    //
    // Do the evaluation
    //
    if ( true == (bool)_variant_t (vbIsPortOpenPerInterface) || 
            (true == (bool)_variant_t (vbIsPortGloballyOpen) &amp;&amp;
             false == (bool)_variant_t (vbIsPortGloballyIgnored)) )
    {
        printf ("Port is opened");
    }
    else
    {
        printf ("Port is closed");
    }



    CoUninitialize ();
    return 0;

error:
    {
        printf ("Error: %x.",hr);
        CoUninitialize ();
        return hr;
    }
}

```



 

 




