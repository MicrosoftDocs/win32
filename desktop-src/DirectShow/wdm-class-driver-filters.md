---
description: WDM Class Driver Filters
ms.assetid: 864fc5ad-5aeb-4dc7-bdd2-2ad2bfb57741
title: WDM Class Driver Filters
ms.topic: article
ms.date: 05/31/2018
---

# WDM Class Driver Filters

If a capture device uses a Windows Driver Model (WDM) driver, the graph might require certain filters upstream from the capture filter. These filters are called stream-class driver filters or WDM filters. They support additional functionality provided by the hardware. For example, a TV tuner card has functions for setting the channel. The corresponding filter is the [TV Tuner](tv-tuner-filter.md) filter, which exposes the [**IAMTVTuner**](/windows/desktop/api/Strmif/nn-strmif-iamtvtuner) interface. To make this functionality available to the application, you must connect the TV Tuner filter to the capture filter.

The [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) interface provides the easiest way to add WDM filters to the graph. At some point while building the graph, call [**FindInterface**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-findinterface) or [**RenderStream**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-renderstream). Either one of these methods will automatically locate the necessary WDM filters and connect them to the capture filter. The rest of this section describes how to add WDM filters manually. However, be aware that the recommend approach is simply to call one of these **ICaptureGraphBuilder2** methods.

The pins on a WDM filter support one or more mediums. A medium defines a method of communication, such as a bus. You must connect pins that support the same medium. The [**REGPINMEDIUM**](/windows/desktop/api/strmif/ns-strmif-regpinmedium) structure, which is equivalent to the **KSPIN\_MEDIUM** structure used for kernel streaming drivers, defines a medium in DirectShow. The **clsMedium** member of the **REGPINMEDIUM** structure specifies the class identifier (CLSID) for the medium. To retrieve a pin's medium, call the [**IKsPin::KsQueryMediums**](ikspin-ksquerymediums.md) method. This method returns a pointer to a block of memory that contains a [**KSMULTIPLE\_ITEM**](ksmultiple-item.md) structure, followed by zero or more **REGPINMEDIUM** structures. Each **REGPINMEDIUM** structure identifies a medium the pin supports.

Do not connect a pin if the medium has a CLSID of GUID\_NULL or KSMEDIUMSETID\_Standard. These are default values indicating that the pin does not support mediums.

Also, do not connect a pin unless the filter requires exactly one connected instance of that pin. Otherwise, your application might try to connect various pins that shouldn't have connections, which can cause the program to stop responding. To find out the number of required instances, retrieve the KSPROPERTY\_PIN\_NECESSARYINSTANCES property set, as shown in the following code example. (For brevity, this example does not test any return codes or release any interfaces. Your application should do both, of course.)


```C++
// Obtain the pin factory identifier.
IKsPinFactory *pPinFactory;
hr = pPin->QueryInterface(IID_IKsPinFactory, (void **)&pPinFactory);

ULONG ulFactoryId;
hr = pPinFactory->KsPinFactory(&ulFactoryId);

// Get the "instance" property from the filter.
IKsControl *pKsControl;
hr = pFilter->QueryInterface(IID_IKsControl, (void **)&pKsControl);

KSP_PIN ksPin;
ksPin.Property.Set = KSPROPSETID_Pin;
ksPin.Property.Id = KSPROPERTY_PIN_NECESSARYINSTANCES;
ksPin.Property.Flags = KSPROPERTY_TYPE_GET;
ksPin.PinId = ulFactoryId;
ksPin.Reserved = 0; 

KSPROPERTY ksProp;
ULONG ulInstances, bytes;
pKsControl->KsProperty((PKSPROPERTY)&ksPin, sizeof(ksPin), 
    &ulInstances, sizeof(ULONG), &bytes);

if (hr == S_OK && bytes == sizeof(ULONG)) 
{
    if (ulInstances == 1) 
    {
        // Filter requires one instance of this pin.
        // This pin is OK.
    } 
}
```



The following pseudocode is an extremely brief outline showing how to find and connect the WDM filters. It omits many details, and is only meant to show the general steps your application would need to take.


```C++
Add supporting filters:
{
    foreach input pin:
        skip if (pin is connected)
    
        Get pin medium
        skip if (medium is GUID_NULL or KSMEDIUMSETID_Standard)
    
        Query filter for KSPROPERTY_PIN_NECESSARYINSTANCES property
        skip if (necessary instances != 1)

        Match an existing pin || Find a matching filter
}    

Match an existing pin:
{
    foreach filter in the graph
        foreach unconnected pin
            Get pin medium
            if (mediums match)
                connect the pins    
}

Find a matching filter:
{    
    Query the filter graph manager for IFilterMapper2.
    Find a filter with an output pin that matches the medium.
    Add the filter to the graph.
    Connect the pins.
    Add supporting filters. (Recursive call.)
}
```



## Related topics

<dl> <dt>

[Advanced Capture Topics](advanced-capture-topics.md)
</dt> </dl>

 

 



