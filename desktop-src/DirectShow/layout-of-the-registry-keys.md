---
description: Layout of the Registry Keys
ms.assetid: c041d094-8165-446f-bf77-0d53b728fe7a
title: Layout of the Registry Keys
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Layout of the Registry Keys

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DirectShow filters are registered in two places:

-   The DLL that contains the filter is registered as the filter's COM server. When an application calls **CoCreateInstance** to create the filter, the Microsoft Windows COM library uses this registry entry to locate the DLL.
-   Additional information about the filter can be registered within a filter category. This information enables the [System Device Enumerator](system-device-enumerator.md) and the [Filter Mapper](filter-mapper.md) to locate the filter.

Filters are not required to register the additional filter information. As long as the DLL is registered as the COM server, an application can create the filter and add it to a filter graph. However, if you want your filter to be discoverable by the System Device Enumerator or the Filter Mapper, you must register the additional information.

The registry entry for the DLL has the following keys:


```
HKEY_CLASSES_ROOT
    CLSID
        Filter CLSID 
            REG_SZ: (Default) = Friendly name

            InprocServer32
                REG_SZ: (Default) = File name of the DLL
                REG_SZ: ThreadingModel = Both
```



The registry entry for the filter information has the following keys:


```
HKEY_CLASSES_ROOT
    CLSID
        Category
            Instance
                Filter CLSID
                    REG_SZ: CLSID = Filter CLSID
                    REG_BINARY: FilterData = Filter information
                    REG_SZ: FriendlyName = Friendly name
```




```
Category
```



is the GUID of a filter category. (See [Filter Categories](filter-categories.md).) The filter information is packed into a binary format. The [**IFilterMapper2**](/windows/desktop/api/Strmif/nn-strmif-ifiltermapper2) interface unpacks this data when it searches the registry for a filter.

All of the filter category GUIDs are listed in the registry under the following key:


```C++
HKEY_CLASSES_ROOT\CLSID\{DA4E3DA0-D07D-11d0-BD50-00A0C911CE86}\Instance
```



 

 



