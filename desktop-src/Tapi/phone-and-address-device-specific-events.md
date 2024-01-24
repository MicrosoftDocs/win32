---
description: The following code example illustrates an event handler for address and phone device events. The code for each event shows how to create the event interface and how to retrieve the event data.
ms.assetid: 236d4e7f-865f-4b26-8da6-c86476588c47
title: Phone and Address Device-specific Events
ms.topic: article
ms.date: 05/31/2018
---

# Phone and Address Device-specific Events

The following code example illustrates an event handler for address and phone device events. The code for each event shows how to create the event interface and how to retrieve the event data.

``` syntax
HRESULT STDMETHODCALLTYPE CMyEventNotification::Event(
   TAPI_EVENT TapiEvent,
   IDispatch * pEvent
)
{
    HRESULT hr = S_OK;
    //...
    switch (TapiEvent) 
    {
        case TE_ADDRESSDEVSPECIFIC:
        {
            ITAddressDeviceSpecificEvent* pITADSEvent = NULL;

            hr = pEvent->QueryInterface( 
                               IID_ITAddressDeviceSpecificEvent,
                               (void **)(&pITADSEvent) );
            // If (hr != S_OK) process the error here...

            // Retrieve data received from the TSP.
            long lParam1=0;
            hr = pITADSEvent->get_lParam1(&lParam1);
            // If (hr != S_OK) process the error here...

            long lParam2=0;
            hr = pITADSEvent->get_lParam2(&lParam2);
            // If (hr != S_OK) process the error here...

            long lParam3=0; 
            hr = pITADSEvent->get_lParam3(&lParam3);
            // If (hr !=S_OK) process the error here...

            // Process the data here.
            // ...
            pITADSEvent->Release();
            break;
        }

        case TE_PHONEDEVSPECIFIC:
        {
            ITPhoneDeviceSpecificEvent* pITPhEvent = NULL;

            hr = pEvent->QueryInterface( 
                            IID_ITPhoneDeviceSpecificEvent,
                            (void **)(&pITPhEvent) );
            // If (hr != S_OK) process the error here...

            // Retrieve data received from the TSP.
            long lParam1=0;
            hr = pITPhEvent->get_lParam1(&lParam1);
            // If (hr != S_OK) process the error here...

            long lParam2=0;
            hr = pITPhEvent->get_lParam2(&lParam2);
            // If (hr != S_OK) process the error here...

            long lParam3=0;
            hr = pITPhEvent->get_lParam3(&lParam3);
            // If (hr != S_OK) process the error here...

            // Process the data here.
            //...
            pITPhEvent->Release();
            break;
        }
        //...
    } // end of switch 
    //...
}
```

 

 



