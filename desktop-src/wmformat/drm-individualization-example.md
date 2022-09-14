---
title: DRM Individualization Example
description: DRM Individualization Example
ms.assetid: 665a5005-d435-4783-b48e-2d8400aa7638
keywords:
- Windows Media Format SDK,DRM individualization
- Windows Media Format SDK,individualization
- digital rights management (DRM),individualization
- DRM (digital rights management),individualization
- digital rights management (DRM),DRM individualization
- DRM (digital rights management),DRM individualization
- DRM Client Extended APIs,individualization
- Client Extended APIs,individualization
ms.topic: article
ms.date: 05/31/2018
---

# DRM Individualization Example

The following code is an example of forced individualization, and also shows how to use the synchronous event handling model with events that have associated status interfaces.


```C++
HRESULT Individualize(IWMDRMSecurity* pSecurity)
{
    HRESULT hr = S_OK;
    
    IMFMediaEvent*                  pEvent        = NULL;
    IUnknown*                       pCancelCookie = NULL;
    IWMDRMIndividualizationStatus*  pIndivStatus  = NULL;   

    MediaEventType EventType    = MEUnknown;
    HRESULT        EventHR      = E_FAIL;
    PROPVARIANT    EventValue;

    WM_INDIVIDUALIZE_STATUS IndivStatusStruct;

    // Intialize local variables.
    ZeroMemory(&IndivStatusStruct, sizeof(IndivStatusStruct));
    PropVariantInit(&EventValue);

    // Check input pointer.
    if (pSecurity == NULL) return E_POINTER;
    
    // Start the security update.
    hr = pSecurity->PerformSecurityUpdate(WMDRM_SECURITY_PERFORM_FORCE_INDIV,
        &pCancelCookie);

    // Get the EventGenerator from the Security interface; this 
    //  is not neccessary, merely illustrative. 
    if (SUCCEEDED(hr))
    {
        hr = pSecurity->QueryInterface( IID_IWMDRMEventGenerator, (void**)&pEventGenerator);
    }

    // Event loop.
    if (SUCCEEDED(hr))
    { 
        do
        {
            // Release the previous event (if there is one).
            SAFE_RELEASE(pEvent);
            SAFE_RELEASE(pIndivStatus);

            // Check for an event.
            hr = pEventGenerator->GetEvent(MF_EVENT_FLAG_NO_WAIT,
                                           &pEvent);

            // If an event was not found, wait a half second and retry.
            if (FAILED(hr))
            {
                Sleep(500);
                continue;
            }

            // Get the event type.
            hr = pEvent->GetType(&EventType);
            
            // 
            if (FAILED(hr))
            {
                printf("Failed to get event type");
                break;
            }

            // Display a message depending on the event.
            switch (EventType)
            {
            case MEWMDRMIndividualizationProgress:

                printf("Received a progress event.\n");
                
                // Get the value of the event.
                hr = pEvent->GetValue(&EventValue);
                if (!SUCCEEDED(hr))
                    break;

                // The event value should be of type VT_UNKNOWN
                //  (an IUnknown pointer).
                if (EventValue.vt != VT_UNKNOWN)
                {
                    // All progress events should have a value of 
                    //  type VT_UNKNOWN. Note this and continue.
                    printf("Unexpected event value type.\n");
                    PropVariantClear(&EventValue);
                    break;
                }

                // Get the extended status interface.
                hr = EventValue.punkVal->QueryInterface(
                    IID_IWMDRMIndividualizationStatus, 
                    (void**)&pIndivStatus);

                // If the interface can't be retrieved, print a
                //  note and continue.
                if (FAILED(hr))
                {
                    printf("Unable to get the extended status interface.\n");
                    PropVariantClear(&EventValue);
                    break;
                }

                // Get the status structure from the newly
                //  acquired interface.
                hr = pIndivStatus->GetStatus(&IndivStatusStruct);

                // If the structure can't be retrieved, make a
                //  note and continue.
                if (FAILED(hr))
                {
                    printf("Unable to get the status structure.\n");
                    PropVariantClear(&EventValue);
                    break;
                }

                //
                // TODO: Print or log the information in the
                //  structure to track status between events.
                //

                // Clear the event value for the next iteration.
                PropVariantClear(&EventValue);
                break;
            case MEWMDRMIndividualizationCompleted:
                printf("Individualization completed.\n");
                break;
            default:
                printf("Received event number %d.\n", EventType);
                break;
            }

            // Give up CPU time to stay out of a busy loop.
            Sleep(0);

        } while (EventType != MEWMDRMIndividualizationCompleted); 
    }

    SAFE_RELEASE(pEvent);
    SAFE_RELEASE(pCancelCookie);
    SAFE_RELEASE(pIndivStatus);
    SAFE_RELEASE(pEventGenerator);

    return hr;
}
```



## Related topics

<dl> <dt>

[**Performing DRM Individualization**](performing-drm-individualization.md)
</dt> <dt>

[**Using the Media Foundation Event Model**](using-the-media-foundation-model.md)
</dt> </dl>

 

 




