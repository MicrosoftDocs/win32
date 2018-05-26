---
Description: Enumerating Content
ms.assetid: 86782a09-4fca-4ae0-beaf-296069e061dc
title: Enumerating Content
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Content

The content on a device (whether that content is a folder, a phone book, a video, or a still image) is called an object in the WPD API. These objects are referenced by object identifiers and described by properties. You can enumerate the objects on a device by calling methods in the [**IPortableDevice interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevice?branch=master), the [**IPortableDeviceContent interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent?branch=master), and the [**IEnumPortableDeviceObjectIDs interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-ienumportabledeviceobjectids?branch=master).

The sample application demonstrates content enumeration in the EnumerateAllContent function that is found in the ContentEnumeration.cpp module. This function, in turn, calls a RecursiveEnumerate function that walks the hierarchy of objects found on the selected device and returns an object identifier for each object.

As noted, the RecursiveEnumerate function retrieves an object identifier for each object found on the device. The object identifier is a string value. Once your application retrieves this identifier, it can obtain more descriptive object information (such as the object's name, the identifier for the object's parent, and so on). This descriptive information is referred to as object properties (or metadata). Your application can retrieve these properties by calling members of the [**IPortableDeviceProperties interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledeviceproperties?branch=master).

The EnumerateAllContent function begins by retrieving a pointer to an [**IPortableDeviceContent interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent?branch=master). It retrieves this pointer by calling the [**IPortableDevice::Content**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-content?branch=master) method.


```C++
void EnumerateAllContent(
    IPortableDevice* pDevice)
{
    HRESULT                         hr = S_OK;
    CComPtr<IPortableDeviceContent> pContent;

    if (pDevice == NULL)
    {
        printf("! A NULL IPortableDevice interface pointer was received\n");
        return;
    }

    // Get an IPortableDeviceContent interface from the IPortableDevice interface to
    // access the content-specific methods.
    hr = pDevice->Content(&amp;pContent);
    if (FAILED(hr))
    {
        printf("! Failed to get IPortableDeviceContent from IPortableDevice, hr = 0x%lx\n",hr);
    }

    // Enumerate content starting from the "DEVICE" object.
    if (SUCCEEDED(hr))
    {
        printf("\n");
        RecursiveEnumerate(WPD_DEVICE_OBJECT_ID, pContent);
    }
}
```



Once it retrieves the pointer to the IPortableDeviceContent interface, the EnumerateAllContent function calls the RecursiveEnumerate function, which walks the hierarchy of objects found on the given device and returns an object identifier for each.

The RecursiveEnumerate function begins by retrieving a pointer to an [**IEnumPortableDeviceObjectIDs interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-ienumportabledeviceobjectids?branch=master). This interface exposes the methods that an application uses to navigate the list of objects found on a given device.

In this sample, the RecursiveEnumerate function calls the [**IEnumPortableDeviceObjectIDs::Next**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-ienumportabledeviceobjectids-next?branch=master) method to traverse the list of objects.

Each call to the [**IEnumPortableDeviceObjects::Next**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-ienumportabledeviceobjectids-next?branch=master) method requests a batch of 10 identifiers. (This value is specified by the NUM\_OBJECTS\_TO\_REQUEST constant that is supplied as the first argument.)


```C++
#define NUM_OBJECTS_TO_REQUEST  10

// Recursively called function which enumerates using the specified
// object identifier as the parent.
void RecursiveEnumerate(
    PCWSTR                  pszObjectID,
    IPortableDeviceContent* pContent)
{
    CComPtr<IEnumPortableDeviceObjectIDs> pEnumObjectIDs;

    // Print the object identifier being used as the parent during enumeration.
    printf("%ws\n",pszObjectID);

    // Get an IEnumPortableDeviceObjectIDs interface by calling EnumObjects with the
    // specified parent object identifier.
    HRESULT hr = pContent->EnumObjects(0,               // Flags are unused
                                       pszObjectID,     // Starting from the passed in object
                                       NULL,            // Filter is unused
                                       &amp;pEnumObjectIDs);
    if (FAILED(hr))
    {
        printf("! Failed to get IEnumPortableDeviceObjectIDs from IPortableDeviceContent, hr = 0x%lx\n",hr);
    }

    // Loop calling Next() while S_OK is being returned.
    while(hr == S_OK)
    {
        DWORD  cFetched = 0;
        PWSTR  szObjectIDArray[NUM_OBJECTS_TO_REQUEST] = {0};
        hr = pEnumObjectIDs->Next(NUM_OBJECTS_TO_REQUEST,   // Number of objects to request on each NEXT call
                                  szObjectIDArray,          // Array of PWSTR array which will be populated on each NEXT call
                                  &amp;cFetched);               // Number of objects written to the PWSTR array
        if (SUCCEEDED(hr))
        {
            // Traverse the results of the Next() operation and recursively enumerate
            // Remember to free all returned object identifiers using CoTaskMemFree()
            for (DWORD dwIndex = 0; dwIndex < cFetched; dwIndex++)
            {
                RecursiveEnumerate(szObjectIDArray[dwIndex],pContent);

                // Free allocated PWSTRs after the recursive enumeration call has completed.
                CoTaskMemFree(szObjectIDArray[dwIndex]);
                szObjectIDArray[dwIndex] = NULL;
            }
        }
    }
}
```



## Related topics

<dl> <dt>

[**IEnumPortableDeviceObjectIDs Interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-ienumportabledeviceobjectids?branch=master)
</dt> <dt>

[**IPortableDevice Interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevice?branch=master)
</dt> <dt>

[**IPortableDeviceContent Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent?branch=master)
</dt> <dt>

[**IPortableDeviceProperties Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledeviceproperties?branch=master)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 



