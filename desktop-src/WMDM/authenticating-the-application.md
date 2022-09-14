---
title: Authenticating the Application
description: Authenticating the Application
ms.assetid: 011815fa-d55c-4abc-9ec8-55d754827342
keywords:
- Windows Media Device Manager,authentication
- Device Manager,authentication
- programming guide,authentication
- desktop applications,authentication
- creating Windows Media Device Manager applications,authentication
- authentication
ms.topic: article
ms.date: 05/31/2018
---

# Authenticating the Application

The first step your application must perform is authentication. Authentication verifies the application's identity to Windows Media Device Manager. Once you authenticate your application, you can call **QueryInterface** to get the root [**IWMDeviceManager**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdevicemanager) interface, which can be queried for other required interfaces, which can themselves be queried for all other interfaces. Authentication need only take place once, on startup.

To authenticate your application, perform these steps:

1.  CoCreate the **MediaDevMgr** object (class ID MediaDevMgr), and request an [**IComponentAuthenticate**](/windows/desktop/api/mswmdm/nn-mswmdm-icomponentauthenticate) interface.
2.  Create a [CSecureChannelClient](csecurechannelclient-class.md) object to handle the authentication.
3.  Pass your application key and transfer certificate to the secure channel object. You can use the dummy key/certificate shown in the following example code to get basic functionality from SDK functions. However, to get full functionality (important for passing files to and from the device), you must request a key and certificate from Microsoft as described in [Tools for Development](tools-for-development.md).
4.  Pass the **IComponentAuthenticate** interface you created in step 1 to the secure channel object.
5.  Call [**CSecureChannelClient::Authenticate**](/previous-versions/ms983906(v=msdn.10)) to authenticate your application.
6.  Query **IComponentAuthenticate** for the **IWMDeviceManager** interface.

These steps are shown in the following C++ code.


```C++
HRESULT CWMDMController::Authenticate()
{
    // Use a dummy key/certificate pair to allow basic functionality.
    // An authentic keypair is required for full SDK functionality.
    BYTE abPVK[] = {0x00};
    BYTE abCert[] = {0x00};
    HRESULT hr;
    CComPtr<IComponentAuthenticate> pAuth;

    // Create the WMDM object and acquire 
    // its authentication interface.
    hr = CoCreateInstance(
        __uuidof(MediaDevMgr),
        NULL,
        CLSCTX_INPROC_SERVER,
        __uuidof(IComponentAuthenticate),
        (void**)&pAuth);

    if (FAILED(hr)) return hr;

    // Create the secure channel client class needed to authenticate the application.
    // We'll use a global member variable to hold the secure channel client
    // in case we need to handle encryption, decryption, or MAC verification
    // during this session.
    m_pSAC = new CSecureChannelClient;
    if (m_pSAC == NULL) return E_FAIL;

    // Send the application's transfer certificate and the associated 
    // private key to the secure channel client.
    hr = m_pSAC->SetCertificate(
        SAC_CERT_V1,
        (BYTE *)abCert, sizeof(abCert),
        (BYTE *)abPVK,  sizeof(abPVK));
    if (FAILED(hr)) return hr;
            
    // Send the authentication interface we created to the secure channel 
    // client and authenticate the application with the V1 protocol.
    // (This is the only protocol currently supported.)
    m_pSAC->SetInterface(pAuth);
    hr = m_pSAC->Authenticate(SAC_PROTOCOL_V1);
    if (FAILED(hr)) return hr;

    // Authentication succeeded, so we can use WMDM.
    // Query for the root WMDM interface.
    hr = pAuth->QueryInterface( __uuidof(IWMDeviceManager), (void**)&m_IWMDMDeviceMgr);

    return hr;
}
```



## Related topics

<dl> <dt>

[**Creating a Windows Media Device Manager Application**](creating-a-windows-media-device-manager-application.md)
</dt> </dl>

 

 