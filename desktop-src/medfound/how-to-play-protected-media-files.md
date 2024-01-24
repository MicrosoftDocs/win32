---
description: How to play files that contain DRM-protected media.
ms.assetid: 85d98f49-8af2-42ce-9b36-a025aee93f73
title: How to Play Protected Media Files
ms.topic: article
ms.date: 05/31/2018
---

# How to Play Protected Media Files

A protected media file is any media file that has associated rules for using the content. In some cases, a protected media file is encrypted using some form of digital rights management (DRM) encryption. To play a protected media file, playback must occur inside the protected media path (PMP). In addition, the user might have to acquire rights to the content.

The term rights acquisition refers to any action that the application must perform before the user can play the content. The most common example is obtaining a DRM license, but Media Foundation defines a generic mechanism that can support other types of rights acquisition. The [**IMFContentEnabler**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentenabler) interface defines this generic mechanism.

Rights acquisition must be done outside of the PMP, from the application process. The Media Session notifies the application through the [**IMFContentProtectionManager**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentprotectionmanager) interface, which is implemented by the application. The Media Session uses the **IMFContentProtectionManager** interface to forward a content enabler object to the application. Content enablers implement the [**IMFContentEnabler**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentenabler) interface. The application uses this interface to acquire the necessary rights.

A content enabler might support automatic rights acquisition, in which case the content enabler implements the entire process, and the application simply monitors the status. Otherwise, the application must use non-silent rights acquisition, which is a process where the application sends HTTP POST data to a URL provided by the content enabler.

To play protected media, an application follows the same steps given in the topic [How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md), with the following additional steps:

1.  Query whether the media source contains protected content. (Optional.)
2.  Create the Media Session in the PMP process, instead of the application process.
3.  Perform rights acquisition, if notified to do so by the Media Session. This operation is performed asynchronously by the application.
4.  Complete the asynchronous operation.

## Query for Protected Content

To query whether a media source contains protected content, call the [**MFRequireProtectedEnvironment**](/windows/desktop/api/mfidl/nf-mfidl-mfrequireprotectedenvironment) function on the media source's presentation descriptor. If the function returns S\_OK, you must use the PMP to play the content. If the function returns S\_FALSE, the PMP is not required, and you can create the Media Session in the application process. Alternatively, you can use the PMP to play both types of content, protected and unprotected. If you do that, you do not need to call **MFRequireProtectedEnvironment**.

For more information about presentation descriptors, see [Presentation Descriptors](presentation-descriptors.md).

## Create the PMP Media Session

To create the Media Session in the PMP, call [**MFCreatePMPMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatepmpmediasession). This function is similar to [**MFCreateMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatemediasession), but instead of creating the Media Session in the application's process, it creates the Media Session in the PMP process. The application receives a pointer to a proxy object for the Media Session. The application calls [**IMFMediaSession**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasession) methods on the proxy object, just as it would on the Media Session. The proxy object forwards the calls to the Media Session across the process boundary.

Create the PMP Media Session as follows:

1.  Create a new attribute store by calling [**MFCreateAttributes**](/windows/desktop/api/mfapi/nf-mfapi-mfcreateattributes).
2.  Set the [**MF\_SESSION\_CONTENT\_PROTECTION\_MANAGER**](mf-session-content-protection-manager-attribute.md) attribute on the attribute store. The value of this attribute is a pointer to your application's implementation of [**IMFContentProtectionManager**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentprotectionmanager). Call [**IMFAttributes::SetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setunknown) to set the attribute.
3.  Call [**MFCreatePMPMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatepmpmediasession) to create the Media Session in the PMP process. The *pConfiguration* parameter is a pointer to the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface of the attribute store.


```C++
IMFAttributes *pAttributes = NULL;
IMFMediaSession *pSession = NULL;

// Create the attribute store.
hr = MFCreateAttributes(&pAttributes, 1);

// Set the IMFContentProtectionManager pointer.
if (SUCCEEDED(hr))
{
    hr = pAttributes->SetUnknown(
        MF_SESSION_CONTENT_PROTECTION_MANAGER, 
        pCPM  // Your implementation of IMFContentProtectionManager.
        );
}

// Create the Media Session.
if (SUCCEEDED(hr))
{
    hr = MFCreatePMPMediaSession(
        0,
        pAttributes, 
        &pSession,
        NULL
    );
}

SAFE_RELEASE(pAttributes); // Release the attribute store.
// Use the Media Session to control playback (not shown).
```



Next, create a playback topology and queue it on the Media Session, as described in [Creating Playback Topologies](creating-playback-topologies.md).

## Perform Rights Acquisition

If playback requires rights acquisition, the Media Session calls [**IMFContentProtectionManager::BeginEnableContent**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentprotectionmanager-beginenablecontent). The *pEnablerActivate* parameter of this method is a pointer to the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface. Use this interface to create the content enabler object, which exposes the [**IMFContentEnabler**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentenabler) interface. Then use the content enabler to perform the rights acquisition step.

To create the content enabler, call [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject):


```C++
IMFContentEnabler *pEnabler = NULL;
hr = pEnablerActivate->ActivateObject(
    IID_IMFContentEnabler, 
    (void**)&pEnabler
    );
```



Query the returned [**IMFContentEnabler**](/windows/desktop/api/mfidl/nn-mfidl-imfcontentenabler) pointer for the [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface. Use this interface to get events from the content enabler object. For more information about events, see [Media Event Generators](media-event-generators.md).

To find out whether the content enabler supports automatic acquisition, call [**IMFContentEnabler::IsAutomaticSupported**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-isautomaticsupported). If this method returns the value **TRUE**, the application should use automatic acquisition. Otherwise, use non-silent acquisition.

The [**BeginEnableContent**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentprotectionmanager-beginenablecontent) method is asynchronous. The application should perform the acquisition step on the application's thread. One approach is to post a private window message to the application's main window, notifying the application thread to perform the acquisition. While the operation is pending, the application must store the callback pointer and the state object that it received in the *pCallback* and *punkState* parameters of **BeginEnableContent**. These will be used to complete the asynchronous operation.

### Automatic Acquisition

To perform automatic acquisition, call [**IMFContentEnabler::AutomaticEnable**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-automaticenable). This method is asynchronous. When the operation is completed, the content enabler sends an [MEEnablerCompleted](meenablercompleted.md) event. The event's status code indicates whether the operation was successful. If the status code from the MEEnablerCompleted event is NS\_E\_DRM\_LICENSE\_NOTACQUIRED, the application should try using non-silent acquisition.

While the acquisition operation is in progress, the enabler object might send the [MEEnablerProgress](meenablerprogress.md) event to indicate the progress of the operation. To cancel the operation, call [**IMFContentEnabler::Cancel**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-cancel).

### Non-Silent Acquisition

If the [**IsAutomaticSupported**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-isautomaticsupported) method returns **FALSE** or the [**AutomaticEnable**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-automaticenable) method fails with the error code NS\_E\_DRM\_LICENSE\_NOTACQUIRED, the application should perform non-silent acquisition as described in the following steps:

1.  Call [**IMFContentEnabler::GetEnableURL**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-getenableurl) to get the URL for the rights acquisition. This method also returns a flag indicating whether the URL is trusted.
2.  Call [**IMFContentEnabler::GetEnableData**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-getenabledata) to get the HTTP POST data.
3.  Call [**IMFContentEnabler::MonitorEnable**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentenabler-monitorenable). This method causes the content enabler to monitor the progress of the rights acquisition action.

4.  Submit the data to the rights acquisition URL by using an HTTP POST action. You can use the Internet Explorer control or the Windows Internet (WinINet) APIs.

The following code shows steps 1–3. Step 4 depends on your application's particular requirements.


```C++
WCHAR   *sURL = NULL;  // URL.
DWORD   cchURL = 0;    // Size of the URL in characters.

// Trust status of the URL.
MF_URL_TRUST_STATUS  trustStatus = MF_LICENSE_URL_UNTRUSTED;

BYTE    *pPostData = NULL;  // Buffer to hold HTTP POST data.
DWORD   cbPostDataSize = 0; // Size of the buffer, in bytes.

HRESULT hr = S_OK;

// Get the URL. 
hr = m_pEnabler->GetEnableURL(&sURL, &cchURL, &trustStatus);

if (SUCCEEDED(hr))
{
    if (trustStatus != MF_LICENSE_URL_TRUSTED)
    {
        // The URL is not trusted. Do not proceed.
        hr = E_FAIL;
    }
}

// Monitor the rights acquisition. 
if (SUCCEEDED(hr))
{
    hr = m_pEnabler->MonitorEnable();
}

// Get the HTTP POST data.
if (SUCCEEDED(hr))
{
    hr = m_pEnabler->GetEnableData(&pPostData, &cbPostDataSize);
}

// Open the URL and send the HTTP POST data. (Not shown.)

// Release the buffers.
CoTaskMemFree(pPostData);
CoTaskMemFree(sURL);
```



When the operation is completed, the content enabler sends an [MEEnablerCompleted](meenablercompleted.md) event.

## Complete the Asynchronous Operation

When the rights acquisition is completed, successfully or otherwise, the application must notify the Media Session, by invoking the callback pointer given in the [**BeginEnableContent**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentprotectionmanager-beginenablecontent) method.

1.  Create an asynchronous result object by calling [**MFCreateAsyncResult**](/windows/desktop/api/mfapi/nf-mfapi-mfcreateasyncresult).
2.  Invoke the Media Session's callback by calling [**MFInvokeCallback**](/windows/desktop/api/mfapi/nf-mfapi-mfinvokecallback).
3.  The Media Session will call [**IMFContentProtectionManager::EndEnableContent**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentprotectionmanager-endenablecontent). In your implementation of this method, release any pointers or resources that you allocated inside [**BeginEnableContent**](/windows/desktop/api/mfidl/nf-mfidl-imfcontentprotectionmanager-beginenablecontent). Return an **HRESULT** that indicates the overall success of the operation. If the rights acquisition failed or the user canceled before it was completed, return an error code.

The following code shows how to create the asynchronous result and invoke the callback.


```C++
IMFAsyncResult  *pResult = NULL;

// Create the asynchronous result object.
hr = MFCreateAsyncResult(NULL, pCallback, punkState, &pResult);

// Invoke the callback.
if (SUCCEEDED(hr))
{
    pResult->SetStatus(hrStatus);
    hr = MFInvokeCallback(pResult);
}
SAFE_RELEASE(pResult);
```



## Related topics

<dl> <dt>

[Media Session](media-session.md)
</dt> <dt>

[Audio/Video Playback](audio-video-playback.md)
</dt> </dl>

 

 



