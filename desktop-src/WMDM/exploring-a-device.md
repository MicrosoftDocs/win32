---
title: Exploring a Device
description: Exploring a Device
ms.assetid: 8b171b8a-00b7-4873-a4f7-1a0f29ad5cc0
keywords:
- Windows Media Device Manager,exploring devices
- Device Manager,exploring devices
- programming guide,exploring devices
- desktop applications,exploring devices
- creating Windows Media Device Manager applications,exploring devices
- exploring devices
- storages
ms.topic: article
ms.date: 05/31/2018
---

# Exploring a Device

Exploring a device is similar to exploring a disk drive. All objects on a device are called *storages*. A storage can be a file, folder, or abstract object (such as a playlist) on the device. You must examine a storage's attributes and metadata (if supported) to understand what kind of storage it is. Storages are organized hierarchically on the device; every storage has exactly one parent, and all storages ultimately descend from a single root device storage, typically named "\\".

The following steps describe how to explore a device:

1.  Get the [**IWMDMDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice) interface of a device as described in [Enumerating Devices](enumerating-devices.md).
2.  Call [**IWMDMDevice::EnumStorage**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmdevice-enumstorage) to retrieve an [**IWMDMEnumStorage**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmenumstorage) interface. This interface is used to get all child objects of the storage that returns this interface. When getting this interface from the device, as we are here, it will hold only one storage: the root device storage.
3.  Call [**IWMDMEnumStorage::Next**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmenumstorage-next) with a count of 1 to retrieve the [**IWMDMStorage**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmstorage) interface for the root device storage. (You cannot request more than one child from the device.)
4.  Examine all storages on the device by recursively calling [**IWMDMStorage::EnumStorage**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage-enumstorage) and then **IWMDMEnumStorage::Next** to get children of a storage. To see if a storage has children to avoid the calls to **EnumStorage** and **Next**, you can call [**IWMDMStorage::GetAttributes**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage-getattributes) to check for the flags WMDM\_STORAGE\_ATTR\_HAS\_FILES or WMDM\_STORAGE\_ATTR\_HAS\_FOLDERS. For more information about how to get the properties of a storage, see [Getting and Setting Metadata and Attributes](getting-and-setting-metadata-and-attributes.md) and [Getting and Setting Metadata and Attributes in the Application](getting-and-setting-metadata-and-attributes-in-the-application.md).

Windows Media Device Manager does not expose a standard set of folders to hold media of a specific type (for example, a "My Playlists" folder for playlists). Every device has a unique file system, and you will have to decide on an appropriate place to look for, or to send, a specific file.

> [!Note]  
> Windows Explorer can show virtual folders that do not actually exist on the device. Example virtual folders are the "Media" and "Data" folders displayed for MTP devices. These folders are created by Windows to make downloads simpler for end users; they do not actually exist on the device. Your application should not depend on finding these types of general folders. Conversely, Windows Explorer might not show some folders or objects that do exist on the device (for example, playlists).

 

The following C++ example code demonstrates the recursive exploration of a device. It uses two functions:

-   ExploreDevice, a starting function that receives a device pointer and obtains a pointer to the root enumerator for that device.
-   RecursiveExploreStorage, which is called to explore a device recursively.


```C++
// Get the root enumerator and start the recursive function.
HRESULT ExploreDevice(IWMDMDevice* pDevice)
{
    HRESULT hr = S_OK;

    // Get a root enumerator.
    CComPtr<IWMDMEnumStorage> pEnumStorage;
    hr = pDevice->EnumStorage(&pEnumStorage);
    if (SUCCEEDED(hr))
    {
        RecursiveExploreStorage(pEnumStorage);
    }
    return hr;
}

// Recursively explore a storage.
void RecursiveExploreStorage(IWMDMEnumStorage* pEnumStorage)
{
    HRESULT hr = S_OK;
    CComPtr<IWMDMStorage> pStorage;

    ULONG numRetrieved = 0;
    // Loop through all storages in the current storage.
    while((pEnumStorage->Next(1, &pStorage, &numRetrieved) == S_OK) && (numRetrieved == 1))
    {
        // Get the name of the object.
        const UINT MAX_LEN = 255;
        WCHAR name[MAX_LEN];
        hr = pStorage->GetName((LPWSTR)&name, MAX_LEN);
        // TODO: Display the retrieved storage name

        // If this is a folder, recurse into it.
        if (attributes & WMDM_FILE_ATTR_FOLDER)
        {
            CComPtr<IWMDMEnumStorage> pEnumSubStorage;
            hr = pStorage->EnumStorage(&pEnumSubStorage);
            if (SUCCEEDED(hr)
            {
                RecursiveExploreStorage(pEnumSubStorage);
            }
        }
        pStorage.Release();
    } // Get the next storage pointer.
    return;
}
```



## Related topics

<dl> <dt>

[**Creating a Windows Media Device Manager Application**](creating-a-windows-media-device-manager-application.md)
</dt> </dl>

 

 




