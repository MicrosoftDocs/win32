---
title: Creating a Tune Request (C)
description: Creating a Tune Request (C)
ms.assetid: 8e082f6f-91e6-404d-8914-76d7bec26220
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Tune Request (C)

This topic applies to Windows XP or later.

It is preferable to get a preconfigured tune request from a database. However, you can construct a tune request from scratch if you know the particular network type that you want to support.

To create an ATSC tune request, do the following:

1.  Create a system tuning spaces collection.
2.  Enumerate the tuning spaces to find the ATSC tuning space.
3.  Use the ATSC tuning space to create a new tune request.
4.  Create an ATSC locator object.
5.  Set the physical channel property on the locator.
6.  Associate the locator with the tune request.
7.  Give the tune request to the Video Control.
8.  Run the Video Control.

The following example omits any error checking. In working code, you should always check **HRESULT** return codes.


```C++
long lChannel = 46; // Use whatever channel number you like.
HRESULT hr = S_OK;

// Create the tuning space collection.
CComPtr<ITuningSpaceContainer> pTuningSpaceContainer;
hr = pTuningSpaceContainer.CoCreateInstance(CLSID_SystemTuningSpaces,
    NULL, CLSCTX_INPROC_SERVER);

// Find the ATSC tuning space in the tuning spaces collection.
CComPtr<IEnumTuningSpaces> pEnumTuningSpaces;
CComBSTR bstrATSC(L"ATSC");
CComPtr<ITuningSpace> pTuningSpace;

hr = pTuningSpaceContainer->get_EnumTuningSpaces(&amp;pEnumTuningSpaces);
while (S_OK == pEnumTuningSpaces->Next(1, &amp;pTuningSpace, NULL))
{
    CComBSTR bstrTemp;
    hr = pTuningSpace->get_UniqueName(&amp;bstrTemp);
    if (bstrTemp == bstrATSC)
    {
        break;  // Found it.
    }
    pTuningSpace = NULL;  // Release for the next loop.
}

if (pTuningSpace == NULL) // Did not find it.
{
    // Handle the error.
}
    
// Create an ATSC Tune Request.
CComPtr<IATSCTuningSpace> pATSCTuningSpace;
pTuningSpace.QueryInterface(&amp;pATSCTuningSpace);
CComPtr<ITuneRequest> pTuneRequest;
hr = pATSCTuningSpace->CreateTuneRequest(&amp;pTuneRequest);

// Create an ATSC Locator and set the physical channel.
CComPtr<IATSCLocator> pATSCLocator;
pATSCLocator.CoCreateInstance(CLSID_ATSCLocator, NULL, 
    CLSCTX_INPROC_SERVER);
hr = pATSCLocator->put_PhysicalChannel(lChannel);

// Set the channel and minor channel properties on the tune request
// to -1. The network provider will set these properties after it
// tunes to the ATSC channel.
CComPtr<IATSCChannelTuneRequest> pATSCTuneRequest;
pTuneRequest.QueryInterface(&amp;pATSCTuneRequest);
hr = pATSCTuneRequest->put_Channel(-1);
hr = pATSCTuneRequest->put_MinorChannel(-1);

// Bind the locator to the tune request.
hr = pATSCTuneRequest->put_Locator(pATSCLocator);

// Give the tune request to the Video Control.
CComVariant var(pATSCTuneRequest);
hr = pMSVidCtl->View(&amp;var);
hr = pMSVidCtl->Run();
```



As this example shows, when the application builds the tune request, it must target specific network types. On the other hand, if it always gets the tune request from the database, it will function with any supported network type.

 

 




