---
title: Basic Firewall Operation
description: Basic Firewall Operation
ms.assetid: a11358b6-4f95-4a5b-986b-135794be477a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Basic Firewall Operation

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. It is unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The following example code demonstrates several basic API operations:

-   Checks if the IPv6 Firewall is installed.
-   Enables an IPv6 Firewall on an interface.
-   Checks if a port was not opened by another application, then opens the port.


```C++
//
// ICFv6App.cpp : ICF v6 Sample App.
//
// Opens a port on the Teredo interface
//

const _bstr_t cbstrAppName (L"ICFv6SampleApplication");
const _bstr_t cbstrTeredoIfName (L"Teredo Tunneling Pseudo-Interface");
const unsigned short cnPort = 50000;
const PORT_PROTOCOL cProtocol = PORT_PROTOCOL_UDP;

//
// Checks if the specified port was already opened by somebody else
//
HRESULT IsPortInUse (
    USHORT usPort, 
    PORT_PROTOCOL PortProtocol, 
    INetFwV6Connection* pConn,
    bool* pbInUse
    )
{
    if (NULL == pConn || 
        NULL == pbInUse)
    {
        return E_POINTER;
    }

    //
    // Initialize the out variable
    //
    *pbInUse = false;

    HRESULT hr = S_OK;

    //
    // Enumerate all the opened ports
    //
    IEnumNetFwV6OpenPorts* pOpenPorts = NULL;
    hr = pConn->EnumerateOpenPorts (&amp;pOpenPorts);
    if (FAILED (hr))
    {
        return hr;
    }

    INetFwV6OpenPort* pPort = NULL;
    while (S_OK == (hr = pOpenPorts->Next (1, &amp;pPort, NULL)))
    {        
        USHORT nPort = 0;
        PORT_PROTOCOL Protocol;
        //
        // Get the port number
        //
        hr = pPort->get_Port (&amp;nPort);
        if (FAILED (hr))
        {
            break;
        }

        //
        // Get the protocol
        //
        pPort->get_Protocol (&amp;Protocol);
        if (FAILED (hr))
        {
            break;
        }
        
        //
        // See if this is the port we are looking for
        //
        if (usPort == nPort &amp;&amp; PortProtocol == Protocol) 
        {
            //
            // Check the name associated with the port
            // If it is not our tag then somebody else is using it
            //
            BSTR bstrName;
            hr = pPort->get_Name (&amp;bstrName);
            if (FAILED (hr))
            {
                break;
            }

            if (cbstrAppName.operator != (bstrName))
            {
                //
                // Somebody else is using this port
                //
                *pbInUse = true;
            }

            break;
        }
    }
    
    return hr;
}

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
        // Can't initialize COM
        //
        printf ("Can't initialize COM");
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
                (LPVOID*)&amp;pfwmgr);

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
// Step 2. Enable firewall on one interface
//

    //
    // Enumerate connections and find the interface
    // named "Teredo Tunneling Pseudo-Interface"
    //
    IEnumNetFwV6Connections* pConnections = NULL;
    hr = pfwmgr->EnumerateConnections (&amp;pConnections);

    if (FAILED (hr))
    {
        printf ("Can't enumerate connections");
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
            printf ("Can't get the name of the connection");
            goto error;
        }

        if (cbstrTeredoIfName.operator == (bstrName))
        {
            bFound = true;
            break;
        }
    }

    if (!bFound)
    {
        //
        // Couldn't find the interface
        //
        printf ("Can't find the Teredo interface");
        goto error;
    }

    //
    // Check if the interface is firewalled, and enable firewall if it is not.
    //
    // If you just want to make sure that the interface is firewalled,
    // you can call EnableFirewall directly without checking
    //
    VARIANT_BOOL vbIsFirewalled;
    hr = pConn->get_IsFirewalled (&amp;vbIsFirewalled);
    if (FAILED (hr))
    {
        goto error;
    }
    if (false == (bool)_variant_t (vbIsFirewalled))
    {
        //
        // Enable the Firewall
        //
        hr = pConn->EnableFirewall ();
        if (FAILED (hr))
        {
            printf ("Can't enable firewall on interface");
            goto error;
        }
    }


//
// Step 3. Open the port you want to receive traffic on
//
    
    //
    // See if the port was open previously by somebody else
    //
    bool bIsInUse = false;
    hr = IsPortInUse (cnPort, cProtocol, pConn, &amp;bIsInUse);
    if (FAILED (hr))
    {
        goto error;
    }

    
    if (true == bIsInUse)
    {
        //
        // Port was already opened by somebody else
        //
        printf ("Port was already opened by somebody else");
    }
    else
    {

        //
        // Port is available. Let's open it.
        // Tag it with our name.
        //
        hr = pConn->OpenPort (cnPort, cProtocol, cbstrAppName);
        if (FAILED (hr))
        {
            //
            // can't open port
            //
            printf ("Can't open port");
            goto error;
        }
    }

    CoUninitialize ();
    return 0;

error:
    {
        printf ("Error: %x",hr);
        CoUninitialize ();
        return hr;
    }
}

```



 

 




