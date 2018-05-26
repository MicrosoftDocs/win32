---
title: Components
description: Components
ms.assetid: 5ce61dd9-b610-43c9-aaa6-b8ff42e7d91e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Components

In the context of MPEG-2, the term *component* refers to an elementary stream within a program. For example, a program might contain a video stream, two audio streams, a data stream, and so forth.

Components are represented by the [**IComponent**](/windows/previous-versions/tuner/nn-tuner-icomponent?branch=master) interface. Each component has a type associated with it, represented by the [**IComponentType**](/windows/previous-versions/tuner/nn-tuner-icomponenttype?branch=master) interface. The component type describes the component, and may include the media type of the stream. The **IComponent** interface is also used to activate or deactivate a given component. For example, if a program has two audio streams (say, English and Spanish), typically only one stream is active at a time.

Each tune request has a list of components. Initially this list might be empty, because the actual components have not been identified yet. After the Network Provider tunes to the program, the Transport Information Filter (TIF) begins to receive PSI tables, and is able to fill in some of the component information.

> [!Note]  
> Components and component types are not used for analog network types.

 

To get the components list from a tune request, call the [**ITuneRequest::get\_Components**](/windows/previous-versions/tuner/nf-tuner-itunerequest-get_components?branch=master) method, which returns a pointer to the **IComponents** interface. Then call [**IComponents::EnumComponents**](/windows/previous-versions/tuner/nf-tuner-icomponents-enumcomponents?branch=master), which returns a pointer to the [**IEnumComponents**](/windows/previous-versions/tuner/nn-tuner-ienumcomponents?branch=master) interface. Use this interface to iterate through the collection:


```C++
CComPtr<IComponents> pComponents;
hr = pTuneRequest->get_Components(&amp;pComponents);
if (SUCCEEDED(hr) &amp;&amp; (pComponents != NULL))
{
    CComPtr<IEnumComponents> pEnum;
    hr = pComps->EnumComponents(&amp;pEnum);
    if (SUCCEEDED(hr))
    {
        CComPtr<IComponent> pComponent;
        ULONG cFetched;
        while (S_OK == pEnum->Next(1, &amp;pComponent, &amp;cFetched))
        {
            // pComponent contains a pointer to the next component.
        }
        pComponent.Release();
    }
}
```



After the tune request is submitted to the Network Provider and data is moving through the filter graph, you can get the updated tune request by calling the Network Provider filter's [**ITuner::get\_TuneRequest**](/windows/previous-versions/tuner/nf-tuner-ituner-get_tunerequest?branch=master) method. Use the returned **ITuneRequest** pointer to examine the updated component information. To change which components are active or inactive, update the component list and resubmit the tune request. [**IComponent::put\_Status**](/windows/previous-versions/tuner/nf-tuner-icomponent-put_status?branch=master) to change a component's active/inactive status.

**Default Preferred Component Types**

A tuning space can have a list of preferred component types. If so, the Network Provider uses the list to configure the output pins on the MPEG-2 Demultiplexer filter. Otherwise, the Network Provider creates a default set of output pins:



| Pin   | Description                                                                        |
|-------|------------------------------------------------------------------------------------|
| Pin 1 | PSI Tables. This pin connects to the BDA MPEG-2 Transport Information Filter (TIF) |
| Pin 2 | Video                                                                              |
| Pin 3 | Audio                                                                              |
| Pin 4 | Data                                                                               |
| Pin 5 | PSI Tables. This pin connects to the MPEG-2 Sections and Tables filter             |



 

To override the preferred component types for a tuning space, do the following:

1.  Get the tuning space from the **SystemTuningSpaces** collection, as described in [Tuning Spaces](tuning-spaces.md).
2.  Create a new [ComponentTypes](componenttypes-object.md) collection object.
3.  Create one or more component type objects of the appropriate type. For MPEG-2 streams, use the [MPEG2ComponentType](mpeg2componenttype-object.md) object.
4.  Set the desired properties on each component type. At a minimum, set the category (audio, video, and so forth) by calling the [**IComponentType::put\_Category**](/windows/previous-versions/tuner/nf-tuner-icomponenttype-put_category?branch=master) method.
5.  Add each component to the collection by calling [**IComponents::Add**](/windows/previous-versions/tuner/nf-tuner-icomponents-add?branch=master).
6.  Call [**ITuningSpace::put\_DefaultPreferredComponentTypes**](/windows/previous-versions/tuner/nf-tuner-ituningspace-put_defaultpreferredcomponenttypes?branch=master) with a pointer to the component types collection.
7.  Persist the changes by putting the tuning space back into the **SystemTuningSpaces** collection. Call the [**ITuningSpaceContainer::put\_Item**](/windows/previous-versions/tuner/nf-tuner-ituningspacecontainer-put_item?branch=master) method with a pointer to the tuning space object.

The following code shows these steps:


```C++
CComPtr <ITuningSpace> pTuningSpace;  // Pointer to the tuning space.
// Use the SystemTuningSpaces collection to get the tuning space 
// (not shown).

// Create a new component types collection object.
CComPtr<IComponentTypes> pTypes;
hr = pTypes.CoCreateInstance(CLSID_ComponentTypes);

// Create a new MPEG-2 component type.
CComPtr<IMpeg2ComponentType> pType;
hr = pType.CoCreateInstance(CLSID_MPEG2ComponentType);

// Set the category. 
hr = pType->put_Category(CategoryVideo);

// Add the new type to the collection.
CComVariant var;  // Receives the index into the collection.
hr = pTypes->Add(pType, &amp;var);

// (Repeat for each component type.)

// Set the component type collection as the list of default types 
// for the tuning space.
hr = pTuningSpace->put_DefaultPreferredComponentTypes(pTypes);
```



One reason to set the default component types is to specify a preferred language for an audio stream. Do this by calling the [**ILanguageComponentType::put\_LangID**](/windows/previous-versions/tuner/nf-tuner-ilanguagecomponenttype-put_langid?branch=master) method on the component type.

 

 




