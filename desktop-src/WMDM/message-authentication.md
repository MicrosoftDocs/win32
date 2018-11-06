---
title: Message Authentication
description: Message Authentication
ms.assetid: 6cb49f6b-e303-4840-9343-9891e75e07a4
keywords:
- Windows Media Device Manager,message authentication
- Device Manager,message authentication
- desktop applications,message authentication
- service providers,message authentication
- programming guide,message authentication
- message authentication
- message authentication code (MAC)
- MAC (message authentication code)
ms.topic: article
ms.date: 05/31/2018
---

# Message Authentication

Message authentication is a process that enables applications and service providers to verify that data passed between them has not been tampered with. Windows Media Device Manager allows applications and service providers to perform message authentication by using message authentication codes (MACs). Here is how MAC authentication works:

The data sender, usually the service provider, passes one or more pieces of data through a one-way cryptographic function that produces a single signature, the MAC, for all the data. The sender then sends all the signed pieces of data together with the MAC to the receiver (usually the application). The receiver passes the data through the same cryptographic function to generate a MAC and compares it to the MAC that was sent. If the MAC matches, the data has not been modified.

To perform MAC authentication, the application or service provider requires an encryption key and a matching certificate. For information on where to get these, see [Tools for Development](tools-for-development.md).

The following steps describe how data is signed by the sender, and later checked by the receiver. In Windows Media Device Manager, the service provider uses the [CSecureChannelServer](csecurechannelserver-class.md) class to generate MACs, and the application uses the [CSecureChannelClient](csecurechannelclient-class.md) class. Both classes provide identical functions with identical parameters, so the following steps apply to both classes.

The sender (typically the service provider):

1.  Get the data to be signed.
2.  Create a new MAC handle by calling **MACInit**.
3.  Add a piece of data to be signed to the handle by calling **MACUpdate**. This function accepts the previously created handle, plus a piece of data that must be signed.
4.  Repeat step 3 with each additional piece of data that must be signed. It does not matter in what order data is added to the MAC.
5.  Copy the MAC from the handle to a new byte buffer by calling **MACFinal**. This function accepts the MAC handle and a buffer that you allocate, and copies the MAC from the handle into the provided buffer.

When performing MAC authentication, it is important that both the sender and the receiver are putting the same data into the MAC. For the application methods that provide a MAC, typically all parameters are included in the MAC value (except for the MAC itself, of course). For example, consider the **IWMDMOperation::TransferObjectData** method:

`HRESULT TransferObjectData(BYTE* pData, DWORD* pdwSize, BYTE[WMDM_MAC_LENGTH] abMac);`

In this method, the MAC would include *pData* and *pdwSize*. If you do not include both the parameters, the MAC you create will not match the MAC passed to *abMac*. A service provider must be sure to put all the required parameters in the application method into the MAC value.

The following C++ code demonstrates creating a MAC in a service provider's implementation of [**IMDSPStorageGlobals::GetSerialNumber**](/windows/desktop/api/mswmdm/nf-mswmdm-imdspstorageglobals-getserialnumber).


```C++
HRESULT CMyDevice::GetSerialNumber(
    PWMDMID pSerialNumber, 
    BYTE abMac[WMDM_MAC_LENGTH])
{
    HRESULT hr;

    // g_pSecureChannelServer is a global CSecureChannelServer object
    // created earlier.

    // Standard check that the CSecureChannelServer was authenticated previously.
    if ( !(g_pSecureChannelServer->fIsAuthenticated()) )
    {
        return WMDM_E_NOTCERTIFIED;
    }

    // Call a helper function to get the device serial number.
    hr = UtilGetSerialNumber(m_wcsName, pSerialNumber, TRUE);
    if(hr == HRESULT_FROM_WIN32(ERROR_NOT_SUPPORTED))
    {
        hr = WMDM_E_NOTSUPPORTED;
    }

    if(hr == S_OK)
    {
        // Create the MAC handle.
        HMAC hMAC;
        hr = g_pSecureChannelServer->MACInit(&hMAC);
        if(FAILED(hr))
            return hr;

        // Add the serial number to the MAC.
        g_pSecureChannelServer->MACUpdate(hMAC, (BYTE*)(pSerialNumber), sizeof(WMDMID));
        if(FAILED(hr))
            return hr;

        // Get the created MAC value from the handle.
        g_pSecureChannelServer->MACFinal(hMAC, abMac);
        if(FAILED(hr))
            return hr;
    }

    return hr;
}
```



The receiver (typically the application):

If the receiver has not implemented the [**IWMDMOperation3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmoperation3) interface, it should perform the same steps as the sender, and then compare the two MAC values. The following C++ code example shows how an application would check the MAC received in a call to [**IWMDMStorageGlobals::GetSerialNumber**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorageglobals-getserialnumber) to ensure that the serial number was not tampered with in transit.


```C++
//
// Get and verify the serial number.
//
WMDMID serialNumber;
BYTE receivedMAC[WMDM_MAC_LENGTH];
hr = pIWMDMDevice->GetSerialNumber(&serialNumber, receivedMAC);

// Check the MAC to guarantee the serial number has not been tampered with.
if (hr == S_OK)
{
    // Initialize a MAC handle, 
    // add all parameters to the MAC,
    // and retrieve the calculated MAC value.
    // m_pSAC is a global CSecureChannelClient object created earlier.
    HMAC hMAC;
    BYTE calculatedMAC[WMDM_MAC_LENGTH];
    hr = m_pSAC->MACInit(&hMAC);
    if(FAILED(hr))
        return hr;

    hr = m_pSAC->MACUpdate(hMAC, (BYTE*)(&serialNumber), sizeof(serialNumber));
    if(FAILED(hr))
        return hr;

    hr = m_pSAC->MACFinal(hMAC, (BYTE*)calculatedMAC);
    if(FAILED(hr))
        return hr;

    // If the two MAC values match, the MAC is authentic. 
    if (memcmp(calculatedMAC, receivedMAC, sizeof(calculatedMAC)) == 0)
    {
        // The MAC is authentic; print the serial number.
        CHAR* serialNumberBuffer = 
            new CHAR[serialNumber.SerialNumberLength + 1];
        ZeroMemory(serialNumberBuffer, 
            (serialNumber.SerialNumberLength + 1) * sizeof(CHAR));
        memcpy(serialNumberBuffer, serialNumber.pID, 
            serialNumber.SerialNumberLength * sizeof(CHAR));
        // TODO: Display the serial number.
        delete serialNumberBuffer;
    }
    else
    {
        // TODO: Display a message indicating that the serial number MAC 
        // does not match.
    }
}
```



## Related topics

<dl> <dt>

[**Using Secure Authenticated Channels**](using-secure-authenticated-channels.md)
</dt> </dl>

 

 




