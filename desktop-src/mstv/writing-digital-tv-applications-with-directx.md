---
title: Writing Digital TV Applications with DirectX
description: Writing Digital TV Applications with DirectX
ms.assetid: 'e0fd0754-7898-4a40-bd62-13dfaea58cc8'
---

# Writing Digital TV Applications with DirectX

This section describes how to build digital TV filter graphs for down-level platforms in which the Video Control is not available. For these platforms, the application must the graph manually, by adding and connecting each filter. Note that the Capture Graph Builder object does not support digital TV graphs.

**Obtain a Tune Request**

Start by obtaining a tune request, either from a guide store or by constructing one programmatically within the application. For more information, see [The Microsoft Unified Tuning Model](the-microsoft-unified-tuning-model.md).

**Create the Network Provider Filter**

The first filter that appears in a digtial TV filter graph is a [BDA Network Provider](bda-network-provider-filter.md) filter. The Network Provider controls tuning and works with the Transport Information Filter (TIF) to get program information from the transport stream. To select a Network Provider filter, query the tuning space for its network type property, which corresponds to the CLSID of the Network Provider for that tuning space. The following code shows how to create the Network Provider and add it to the graph:


```C++
CComPtr<ITuneRequest> pTuneRequest;  // Tune request
CComPtr<ITuningSpace> pTuningSpace;  // Tuning space
CComPtr<IBaseFilter> pNetworkProvider; // Network Provider filter
GUID CLSIDNetworkType; // GUID of the network type.

// Initialize the tune request (not shown).

// Find the tuning space for this tune request.
hr = pTuneRequest->get_TuningSpace(&amp;pTuningSpace);
if (FAILED(hr))
{
    // Handle error.
}

// Find the network type.
hr = pTuningSpace->get__NetworkType(&amp;CLSIDNetworkType);
if (FAILED(hr))
{
    // Handle error.
}
if (CLSID_NetworkType == GUID_NULL)
{
    // This tuning space is analog TV, AuxIn, or some other non-BDA type.
}
else
{
    // Create the network provider filter for this network type.
    hr = pNetworkProvider.CoCreateInstance(CLSIDNetworkType);
    if (SUCCEEDED(hr))
    {
        // Add the network provider to the graph.
        hr = pGraph->AddFilter(pNetworkProvider, L"Network Provider");
    }
}
```



The [**ITuneRequest::get\_TuningSpace**](itunerequest-get-tuningspace.md) method gets a pointer to the tuning space for a particular tune request. Then call [**ITuningSpace::get\_\_NetworkType**](ituningspace-get--networktype.md) to get the network type GUID. Pass this GUID to the **CoCreateInstance** function to create the Network Provider filter.

**Analog Tuning Spaces**

For some tuning spaces, the network type is GUID\_NULL. This means the tuning space does not represent a digital TV network, so it is not handled by a BDA Network Provider filter. In that case, the application should build an analog TV capture graph as described in the sections [Video Capture](https://msdn.microsoft.com/library/windows/desktop/dd407331) and [Analog Television](https://msdn.microsoft.com/library/windows/desktop/dd373516). The channel number on the tuning request indicates which channel to set on the TV Tuner filter.

The **AuxInTuningSpace** tuning space represents an auxiliary video input or "AuxIn". The channel number indicates the input source:



| Channel Number | Input           |
|----------------|-----------------|
| 0              | S-video         |
| 1              | Composite video |



 

To find out if a tune request is an AuxIn type, query the tuning space for the [**IAuxInTuningSpace**](iauxintuningspace.md) interface. If it exposes this interface, build an analog capture graph and use the crossbar filter to select the input source. For more information, see [Working with Crossbars](https://msdn.microsoft.com/library/windows/desktop/dd390991). For S-Video, route the PhysConn\_Video\_SVideo pin to the video output pin. For composite video, route the PhysConn\_Video\_Composite pin to the video output. In both cases, route the PhysConn\_Audio\_Line pin to the audio output.

For analog graphs, ignore the rest of this section.

**Submit the Tune Request to the Network Provider**

After you add the Network Provider to the graph, query it for the [**ITuner**](ituner.md) interface and call [**ITuner::put\_TuneRequest**](ituner-put-tunerequest.md) with a pointer to the tune request:


```C++
// Query for ITuner.
CComQIPtr<ITuner> pTuner(pNetworkProvider);
if (pTuner)
{
    // Submit the tune request to the network provider.
    hr = pTuner->put_TuneRequest(pTuneRequest);
}
```



**Add and Connect the Remaining Filters**

After the Network Provider has been configured with a tune request, you can add the remaining filters to the graph. The Network Provider connects to a tuner filter in the "BDA Source Filters" catgegory (KSCATEGORY\_BDA\_NETWORK\_TUNER). The tuner filter connects to one or more filters "BDA Receiver Components" category (KSCATEGORY\_BDA\_RECEIVER\_COMPONENT). This catgegory includes the capture filter and possibly a demodulator filter, depending on the hardware. The application must enumerate the filters in this category and try connecting them, either by media type or by medium.

Connect the capture filter to the [MPEG-2 Demultiplexer](https://msdn.microsoft.com/library/windows/desktop/dd390715) filter, which automatically configures its the output pins based on the preferred component types. Typically pin 1 connects to the [BDA MPEG-2 Transport Information Filter](bda-mpeg-2-transport-information-filter.md) (TIF). Typically you can simply render all of the output pins on the demux, and the correct renderer filters will be added to the graph. For IP data, connect the output pin on the demux to the [BDA IP Sink](bda-ip-sink-filter.md) filter, via the [BDA MPE](bda-mpe-filter.md) filter.

**Define Default Preferred Component Types**

A "component" refers to a program substream. The default preferred component types are those types of substreams that a user wishes to activate by default. For example, a user may specify that a Spanish audio stream should be played whenever one is available. The application creates a set of preferred components by instantiating an empty components collection object and filling it. The application can then persist and/or submit the components object to the Tuner, which will check it whenever there are changes in the available substreams.

**Select a Substream**

To specify which substreams to activate or inactivate, an application must first submit a tune request to the tuner. Once the tuner tunes to the specified channel or frequency, it will fill in the components collection in the tune request with information about each active and inactive substream. The application can then examine each component in this collection, and use the [**IComponent::put\_Status**](icomponent-put-status.md) method to activate or inactivate a particular substream.

**Digital Tuning**

After the initial tune request has been submitted, subsequent tuning is performed by submitting a new tune request to the Network Provider.

 

 




