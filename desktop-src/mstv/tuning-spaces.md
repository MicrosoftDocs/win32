---
title: Tuning Spaces
description: Tuning Spaces
ms.assetid: 627e8aaf-7638-4d17-97b5-0aeaad304b98
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Tuning Spaces

A tuning space repesents a specific network type, such as ATSC digital antenna or DVB cable. A tuning space object performs several functions:

-   It stores information about the network, such as the range of physical channels.
-   It is a factory for tune requests.
-   It is persistable, so it can be stored in the system registry.

Default tuning spaces are provided for analog cable, analog antenna, ATSC digital cable, ATSC digital antenna, and analog auxiliary input. See [Default Tuning Spaces](default-tuning-spaces.md) for more information. Third parties can create their own tuning spaces to support DVB-T, DVB-S, or other network types.

Every tuning space object exposes the [**ITuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ituningspace) interface. Additional network-specific interfaces are derived from **ITuningSpace**. For example, an ATSC tuning space exposes the [**IATSCTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iatsctuningspace) interface.

### System Tuning Spaces Collection

The [SystemTuningSpaces](systemtuningspaces-object.md) object is a collection of all the tuning spaces available on the local system. Use this object to enumerate available tuning spaces and to add new tuning spaces. The SystemTuningSpaces object exposes the [**ITuningSpaceContainer**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ituningspacecontainer) interface.

The following code shows how to create the [SystemTuningSpaces](systemtuningspaces-object.md) object and enumerate the tuning spaces using the [**ITuningSpaceContainer::get\_EnumTuningSpaces**](/previous-versions/windows/desktop/api/tuner/nf-tuner-ituningspacecontainer-get_enumtuningspaces) method:


```C++
// Create the SystemTuningSpaces container.
CComPtr <ITuningSpaceContainer> pTuningSpaceContainer;
hr = pITuningSpaceContainer.CoCreateInstance(CLSID_SystemTuningSpaces);
if (SUCCEEDED(hr))
{
    // Get the enumerator for the collection.
    CComPtr<IEnumTuningSpaces> pTuningSpaceEnum;
    hr = pTuningSpaceContainer->get_EnumTuningSpaces(&amp;pTuningSpaceEnum);
    if (SUCCEEDED(hr))
    {
        // Loop through the collection.
        CComPtr<ITuningSpace> pTuningSpace;
        while (S_OK == pTuningSpaceEnum->Next(1, &amp;pTuningSpace, NULL))
        {
            // pTuningSpace points to the next tuning space.
            // You can query this pointer for derived interfaces.
        }
    }
}
```



Every tuning space has a UniqueName property, which is unique within a given computer's [SystemTuningSpaces](systemtuningspaces-object.md) collection. Use this property to find a particular tuning space; call [**ITuningSpace::get\_UniqueName**](/previous-versions/windows/desktop/api/tuner/nf-tuner-ituningspace-get_uniquename) to get the property.

### Creating Tune Requests

To create a new tune request, call the [**ITuningSpace::CreateTuneRequest**](/previous-versions/windows/desktop/api/tuner/nf-tuner-ituningspace-createtunerequest) method on the tuning space. This method returns a tune request object that corresponds to the network type for that tuning space. The new tune request object is unitialized; tuning information for a specific channel or program must be added by calling methods on the tune request. For more information, see [Tune Requests](tune-requests.md).

### Creating New Tuning Spaces

Default tuning spaces are provided for analog cable, analog antenna, ATSC cable, ATSC digital antenna, analog auxiliary input, DVBT, DVB-S, ISDB-T, ISDB-S and FM radio. See [Default Tuning Spaces](default-tuning-spaces.md) for more information. Third parties can create their own tuning spaces to support other network types, as follows:

1.  Create a tuning space object.
2.  Set properties on the tuning space, using [**ITuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ituningspace) and derived interfaces.
3.  Create a locator object. (See [Locator Objects](tuning-model-objects.md#locator-objects).)
4.  Set properties on the locator, using [**ILocator**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ilocator) and derived interfaces. For more information about locators, see [Locators](locators.md).
5.  Assign the locator as the default locator for the tuning space, by calling the [**ITuningSpace::put\_DefaultLocator**](/previous-versions/windows/desktop/api/tuner/nf-tuner-ituningspace-put_defaultlocator) method.
6.  Optionally, create default component types. Assign them as the perferred component types for the tuning space by calling the [**ITuningSpace::put\_DefaultPreferredComponentTypes**](/previous-versions/windows/desktop/api/tuner/nf-tuner-ituningspace-put_defaultpreferredcomponenttypes) method. For more information, see [Components](components.md).
7.  Add the tuning space to the [SystemTuningSpaces](systemtuningspaces-object.md) collection, by calling the [**ITuningSpaceContainer::Add**](/previous-versions/windows/desktop/api/tuner/nf-tuner-ituningspacecontainer-add) method. The SystemTuningSpaces object automatically persists the tuning space in the registry.

You can also modify an existing tuning space. To do so, retrieve the tuning space from the [SystemTuningSpaces](systemtuningspaces-object.md) collection, set the desired properties, and call [**ITuningSpaceContainer::put\_Item**](/previous-versions/windows/desktop/api/tuner/nf-tuner-ituningspacecontainer-put_item) to save the modified tuning space back into the collection.

## Related topics

<dl> <dt>

[The Microsoft Unified Tuning Model](the-microsoft-unified-tuning-model.md)
</dt> </dl>

 

 




