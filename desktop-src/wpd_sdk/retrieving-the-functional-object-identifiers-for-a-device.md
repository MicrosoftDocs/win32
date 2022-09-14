---
description: Retrieving the Functional Object Identifiers for a Device
ms.assetid: 9a13071a-95a1-4330-92d5-11fa72a8f211
title: Retrieving the Functional Object Identifiers for a Device
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving the Functional Object Identifiers for a Device

As noted in the [Retrieving the Functional Categories Supported by a Device](retrieving-the-functional-categories-supported-by-a-device.md) topic, Windows Portable Devices may support one or more functional categories. Any given functional category may support one or more functional objects. For example, the storage category may support three functional storage objects, each of which is identified by a unique identifier string. The first storage object may then be identified by the string "Storage1", the second by the string "Storage2", and the third by the string "Storage3".

The ListFunctionalObjects function in the DeviceCapabilities.cpp module demonstrates the retrieval of content types for the functional categories supported by a selected device.

Your application can retrieve the functional categories supported by a device using the interfaces described in the following table.



| Interface                                                                                      | Description                                                   |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| [**IPortableDeviceCapabilities Interface**](/windows/desktop/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicecapabilities)                   | Provides access to the functional-category retrieval methods. |
| [**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md) | Used to enumerate and store functional-category data.         |



 

The code found in the ListFunctionalObjects function is almost identical to the code found in the ListFunctionalCategories function. (See the [Retrieving Functional Categories Supported by a Device](retrieving-the-functional-categories-supported-by-a-device.md) topic.) The one difference is the call to the [**IPortableDeviceCapabilities::GetFunctionalObjects**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecapabilities-getfunctionalobjects) method, which appears within the loop that iterates through the functional categories.


```C++
HRESULT hr = S_OK;
CComPtr<IPortableDeviceCapabilities>            pCapabilities;
CComPtr<IPortableDevicePropVariantCollection>   pCategories;
DWORD dwNumCategories = 0;

if (pDevice == NULL)
{
    printf("! A NULL IPortableDevice interface pointer was received\n");
    return;
}

// Get an IPortableDeviceCapabilities interface from the IPortableDevice interface to
// access the device capabilities-specific methods.
hr = pDevice->Capabilities(&pCapabilities);
if (FAILED(hr))
{
    printf("! Failed to get IPortableDeviceCapabilities from IPortableDevice, hr = 0x%lx\n",hr);
}

// Get all functional categories supported by the device.
// We will use these categories to enumerate functional objects
// that fall within them.
if (SUCCEEDED(hr))
{
    hr = pCapabilities->GetFunctionalCategories(&pCategories);
    if (FAILED(hr))
    {
        printf("! Failed to get functional categories from the device, hr = 0x%lx\n",hr);
    }
}

// Get the number of functional categories found on the device.
if (SUCCEEDED(hr))
{
    hr = pCategories->GetCount(&dwNumCategories);
    if (FAILED(hr))
    {
        printf("! Failed to get number of functional categories, hr = 0x%lx\n",hr);
    }
}

printf("\n%d Functional Categories Found on the device\n\n", dwNumCategories);

// Loop through each functional category and get the list of
// functional object identifiers associated with a particular
// category.
if (SUCCEEDED(hr))
{
    for (DWORD dwIndex = 0; dwIndex < dwNumCategories; dwIndex++)
    {
        PROPVARIANT pv = {0};
        PropVariantInit(&pv);
        hr = pCategories->GetAt(dwIndex, &pv);
        if (SUCCEEDED(hr))
        {
            // We have a functional category.  It is assumed that
            // functional categories are returned as VT_CLSID
            // VarTypes.
            if ((pv.puuid != NULL)      &&
                (pv.vt    == VT_CLSID))
            {
                // Display the functional category name
                printf("Functional Category: ");
                DisplayFunctionalCategory(*pv.puuid);
                printf("\n");

                // Display the object identifiers for all
                // functional objects within this category
                CComPtr<IPortableDevicePropVariantCollection> pFunctionalObjectIds;
                hr = pCapabilities->GetFunctionalObjects(*pv.puuid, &pFunctionalObjectIds);
                if (SUCCEEDED(hr))
                {
                    printf("Functional Objects: ");
                    DisplayFunctionalObjectIDs(pFunctionalObjectIds);
                    printf("\n\n");
                }
                else
                {
                    printf("! Failed to get functional objects, hr = 0x%lx\n", hr);
                }
            }
            else
            {
                printf("! Invalid functional category found\n");
            }
        }

        PropVariantClear(&pv);
    }
}
```



## Related topics

<dl> <dt>

[**IPortableDevice Interface**](/windows/desktop/api/PortableDeviceApi/nn-portabledeviceapi-iportabledevice)
</dt> <dt>

[**IPortableDeviceCapabilities Interface**](/windows/desktop/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicecapabilities)
</dt> <dt>

[**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 



