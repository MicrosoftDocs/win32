---
title: Adding and Removing Port Mappings (C++)
description: Adding and Removing Port Mappings (C++)
ms.assetid: f3d7eb27-f0cd-4bd2-beb0-7bc1fe473489
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Adding and Removing Port Mappings (C++)

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The following C++ code demonstrates adding and removing port mappings from network connections. First the code adds a port mapping to every shared or firewalled connection on the local computer. The code then enumerates the connections in order to identify those that have port mappings added, and removes the port mappings from those connections.


```C++
// Copyright (C) Microsoft.  All rights reserved.

#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <objbase.h>
#include <netcon.h>
#include <stdio.h>

#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "oleaut32.lib")

// as in winsock.h
#define NAT_PROTOCOL_TCP 6

HRESULT DeletePortMapping (INetSharingManager * pNSM, UCHAR ucIPProtocol, short usExternalPort)
{   // this is done in 2 parts:
    // 1:  enum connections until we get one that we can convert into an INetSharingConfiguration
    // 2:  then, enum portmappings, and delete if we find a match.

    // PART 1: find a valid connection
    INetConnection * pNC = NULL; // fill this out for part 2 below

    INetSharingEveryConnectionCollection * pNSECC = NULL;
    HRESULT hr = pNSM->get_EnumEveryConnection (&amp;pNSECC);
    if (!pNSECC)
        wprintf (L"failed to get EveryConnectionCollection!\r\n");
    else {
        // enumerate connections
        IEnumVARIANT * pEV = NULL;
        IUnknown * pUnk = NULL;
        hr = pNSECC->get__NewEnum (&amp;pUnk);
        if (pUnk) {
            hr = pUnk->QueryInterface (__uuidof(IEnumVARIANT),
                                       (void**)&amp;pEV);
            pUnk->Release();
        }
        if (pEV) {
            VARIANT v;
            VariantInit (&amp;v);
            BOOL bFoundIt = FALSE;
            while (S_OK == pEV->Next (1, &amp;v, NULL)) {
                if (V_VT (&amp;v) == VT_UNKNOWN) {
                    V_UNKNOWN (&amp;v)->QueryInterface (__uuidof(INetConnection),
                                                     (void**)&amp;pNC);
                    if (pNC) {
                        INetConnectionProps * pNCP = NULL;
                        pNSM->get_NetConnectionProps (pNC, &amp;pNCP);
                        if (!pNCP)
                            wprintf (L"failed to get NetConnectionProps!\r\n");
                        else {
                            // check properties for firewalled or shared connection
                            DWORD dwCharacteristics = 0;
                            pNCP->get_Characteristics (&amp;dwCharacteristics);
                            if (dwCharacteristics & (NCCF_SHARED | NCCF_FIREWALLED)) {
                                NETCON_MEDIATYPE MediaType = NCM_NONE;
                                pNCP->get_MediaType (&amp;MediaType);
                                if ((MediaType != NCM_SHAREDACCESSHOST_LAN) &amp;&amp;
                                    (MediaType != NCM_SHAREDACCESSHOST_RAS) ){
                                    // got a shared/firewalled connection
                                    bFoundIt = TRUE;
                                }
                            }
                            pNCP->Release();
                        }
                        if (bFoundIt == FALSE) {
                            pNC->Release();
                            pNC = NULL;
                        }
                    }
                }
                VariantClear (&amp;v);
                if (bFoundIt == TRUE)
                    break;
            }
            pEV->Release();
        }
        pNSECC->Release();
    }
    if (pNC == NULL) {
        wprintf (L"failed to find a valid connection!\r\n");
        return E_FAIL;
    }
    INetSharingConfiguration * pNSC = NULL;
    hr = pNSM->get_INetSharingConfigurationForINetConnection (pNC, &amp;pNSC);
    pNC->Release(); // don't need this anymore
    if (!pNSC) {
        wprintf (L"can't make INetSharingConfiguration object!\r\n");
        return hr;
    }

    // PART 2:  enum port mappings, deleting match, if any
    INetSharingPortMappingCollection * pNSPMC = NULL;
    hr = pNSC->get_EnumPortMappings (ICSSC_DEFAULT, &amp;pNSPMC);
    if (!pNSPMC)
        wprintf (L"can't get PortMapping collection!\r\n");
    else {

        // this is the interface to be filled out by the code below
        INetSharingPortMapping * pNSPM = NULL;

        IEnumVARIANT * pEV = NULL;
        IUnknown * pUnk = NULL;
        hr = pNSPMC->get__NewEnum (&amp;pUnk);
        if (pUnk) {
            hr = pUnk->QueryInterface (__uuidof(IEnumVARIANT),
                                       (void**)&amp;pEV);
            pUnk->Release();
        }
        if (pEV) {
            VARIANT v;
            VariantInit (&amp;v);
            BOOL bFoundIt = FALSE;
            while (S_OK == pEV->Next (1, &amp;v, NULL)) {
                if (V_VT (&amp;v) == VT_DISPATCH) {
                    V_DISPATCH (&amp;v)->QueryInterface (__uuidof(INetSharingPortMapping),
                                                     (void**)&amp;pNSPM);
                    if (pNSPM) {
                        INetSharingPortMappingProps * pNSPMP = NULL;
                        hr = pNSPM->get_Properties (&amp;pNSPMP);
                        if (pNSPMP) {
                            UCHAR uc = 0;
                            pNSPMP->get_IPProtocol (&amp;uc);
                            long usExternal = 0;
                            pNSPMP->get_ExternalPort (&amp;usExternal);
                            if ((uc         == ucIPProtocol) &amp;&amp; 
                                (usExternal == usExternalPort))
                                bFoundIt = TRUE;

                            pNSPMP->Release();
                        }
                        if (bFoundIt == FALSE) {    // hang onto reference to pNSPM iff found (used below)
                            pNSPM->Release();
                            pNSPM = NULL;
                        }
                    }
                }
                VariantClear (&amp;v);
                if (bFoundIt == TRUE)
                    break;  // bail out if we've found one
            }
            pEV->Release();
        }

        if (pNSPM) {
            hr = pNSPM->Delete();   // or pNSC->RemovePortMapping (pNSPM);
            wprintf (L"just deleted a port mapping!\r\n");

            pNSPM->Release();
        }
        pNSPMC->Release();
    }
    pNSC->Release();
    return hr;
}

HRESULT AddAsymmetricPortMapping (INetSharingConfiguration * pNSC)
{
    HRESULT hr = S_OK;
    VARIANT_BOOL vb1 = VARIANT_FALSE;
    VARIANT_BOOL vb2 = VARIANT_FALSE;
    pNSC->get_SharingEnabled  (&amp;vb1);
    pNSC->get_InternetFirewallEnabled (&amp;vb2);
    if ((vb1 == VARIANT_FALSE) &amp;&amp;
        (vb2 == VARIANT_FALSE))
        wprintf (L"sharing and/or firewall not enabled on this connection!\r\n");
    else {
        INetSharingPortMapping * pNSPM = NULL;
        hr = pNSC->AddPortMapping (L"Ben's Port Mapping",
                             NAT_PROTOCOL_TCP,
                             555,
                             444,
                             0,
                             L"192.168.0.2",
                             ICSTT_IPADDRESS,
                             &amp;pNSPM);
        if (pNSPM) {
            wprintf (L"just added NAT_PROTOCOL_TCP, 555, 444!\r\n");
            
            hr = pNSPM->Enable();
            wprintf (L"just enabled port mapping!\r\n");

            pNSPM->Release();
        } else
            wprintf (L"failed to add asymmetric port mapping!\r\n");
    }
    return hr;
}

HRESULT DoTheWork (INetSharingManager * pNSM)
{   // add a port mapping to every firewalled or shared connection 

    INetSharingEveryConnectionCollection * pNSECC = NULL;
    HRESULT hr = pNSM->get_EnumEveryConnection (&amp;pNSECC);
    if (!pNSECC)
        wprintf (L"failed to get EveryConnectionCollection!\r\n");
    else {

        // enumerate connections
        IEnumVARIANT * pEV = NULL;
        IUnknown * pUnk = NULL;
        hr = pNSECC->get__NewEnum (&amp;pUnk);
        if (pUnk) {
            hr = pUnk->QueryInterface (__uuidof(IEnumVARIANT),
                                       (void**)&amp;pEV);
            pUnk->Release();
        }
        if (pEV) {
            VARIANT v;
            VariantInit (&amp;v);
            while (S_OK == pEV->Next (1, &amp;v, NULL)) {
                if (V_VT (&amp;v) == VT_UNKNOWN) {
                    INetConnection * pNC = NULL;
                    V_UNKNOWN (&amp;v)->QueryInterface (__uuidof(INetConnection),
                                                     (void**)&amp;pNC);
                    if (pNC) {
                        INetConnectionProps * pNCP = NULL;
                        pNSM->get_NetConnectionProps (pNC, &amp;pNCP);
                        if (!pNCP)
                            wprintf (L"failed to get NetConnectionProps!\r\n");
                        else {
                            // check properties for firewalled or shared connection
                            DWORD dwCharacteristics = 0;
                            pNCP->get_Characteristics (&amp;dwCharacteristics);
                            if (dwCharacteristics & (NCCF_SHARED | NCCF_FIREWALLED)) {
                                NETCON_MEDIATYPE MediaType = NCM_NONE;
                                pNCP->get_MediaType (&amp;MediaType);
                                if ((MediaType != NCM_SHAREDACCESSHOST_LAN) &amp;&amp;
                                    (MediaType != NCM_SHAREDACCESSHOST_RAS) ){
                                    // got a shared/firewalled connection
                                    INetSharingConfiguration * pNSC = NULL;
                                    hr = pNSM->get_INetSharingConfigurationForINetConnection (pNC, &amp;pNSC);
                                    if (!pNSC)
                                        wprintf (L"can't make INetSharingConfiguration object!\r\n");
                                    else {
                                        hr = AddAsymmetricPortMapping (pNSC);
                                        pNSC->Release();
                                    }
                                }
                            }
                            pNCP->Release();
                        }
                        pNC->Release();
                    }
                }
                VariantClear (&amp;v);
            }
            pEV->Release();
        }
        pNSECC->Release();
    }
    return hr;
}

int main()
{
    CoInitialize (NULL);

    // init security to enum RAS connections
    CoInitializeSecurity (NULL, -1, NULL, NULL, 
                          RPC_C_AUTHN_LEVEL_PKT, 
                          RPC_C_IMP_LEVEL_IMPERSONATE,
                          NULL, EOAC_NONE, NULL);

    INetSharingManager * pNSM = NULL;    
    HRESULT hr = ::CoCreateInstance (__uuidof(NetSharingManager),
                                     NULL,
                                     CLSCTX_ALL,
                                     __uuidof(INetSharingManager),
                                     (void**)&amp;pNSM);
    if (!pNSM)
        wprintf (L"failed to create NetSharingManager object\r\n");
    else {
        // in case it exists already
        DeletePortMapping (pNSM, NAT_PROTOCOL_TCP, 555);

        // add a port mapping to every shared or firewalled connection.
        hr = DoTheWork (pNSM);
        if (SUCCEEDED(hr)) {

            // do other work here.
            // when you're done,
            // clean up port mapping

            hr = DeletePortMapping (pNSM, NAT_PROTOCOL_TCP, 555);
        }

        pNSM->Release();
    }

    CoUninitialize ();
    return (int)hr;
}
```



 

 




