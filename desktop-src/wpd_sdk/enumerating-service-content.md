---
Description: Enumerating Service Content
ms.assetid: '4af4201c-d3f6-4630-91ec-6509c51871a5'
title: Enumerating Service Content
---

# Enumerating Service Content

After your application opens a service, it can begin performing service-related operations. In the case of the WpdServicesApiSample application, one of these operations is the enumeration of content for a given Contacts service. The following table describes the interfaces used.



|                                                                      |                                                                                                  |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Interface                                                            | Description                                                                                      |
| [**IPortableDeviceService**](iportabledeviceservice.md)             | Used to retrieve the IPortableDeviceContent2 interface to access content on the service.         |
| [**IPortableDeviceContent2**](iportabledevicecontent2.md)           | Used to retrieve the IEnumPortableDeviceObjectIDs interface to enumerate objects on the service. |
| [**IEnumPortableDeviceObjectIDs**](ienumportabledeviceobjectids.md) | Used to enumerate objects on the service.                                                        |



 

The content enumeration code is found in the ContentEnumeration.cpp module. This code resides in the **EnumerateAllContent** and the **RecursiveEnumerate** methods. The former method calls the latter.

The **EnumerateContent** method takes a pointer to an [**IPortableDeviceService**](iportabledeviceservice.md) object as its one parameter. This object corresponds to a service that the application opened earlier when it called the [**IPortableDeviceService::Open**](iportabledeviceservice-open.md) method.

The **EnumerateContent** method creates an [**IPortableDeviceContent2**](iportabledevicecontent2.md) object and passes this object to the [**IPortableDeviceService::Content**](iportabledeviceservice-content.md) method. This method, in turn, retrieves the content at the root level of the service, and then recursively begins to retrieve content found beneath the root.

The following code corresponds to the **EnumerateContent** method.


```C++
// Enumerate all content on the service starting with the
// "DEVICE" object
void EnumerateAllContent(
    IPortableDeviceService* pService)
{
    HRESULT                          hr = S_OK;
    CComPtr<IPortableDeviceContent2> pContent;

    if (pService == NULL)
    {
        printf("! A NULL IPortableDeviceService interface pointer was received\n");
        return;
    }

    // Get an IPortableDeviceContent2 interface from the IPortableDeviceService interface to
    // access the content-specific methods.
    hr = pService->Content(&amp;pContent);
    if (FAILED(hr))
    {
        printf("! Failed to get IPortableDeviceContent2 from IPortableDeviceService, hr = 0x%lx\n",hr);
    }

    // Enumerate content starting from the "DEVICE" object.
    if (SUCCEEDED(hr))
    {
        printf("\n");
        RecursiveEnumerate(WPD_DEVICE_OBJECT_ID, pContent);
    }
}
```



The following code corresponds to the **RecursiveEnumerate** method. The RecursiveEnumerate method instantiates an **IEnumPortableDeviceObjectIDs** interface for the supplied parent object, and calls **IEnumPortableDeviceObjectIDs::Next**, retrieving a batch of immediate child objects. For each child object, RecursiveEnumerate is called again to return its descendent child objects, and so on.


```C++
// Recursively called function which enumerates using the specified
// object identifier as the parent.
void RecursiveEnumerate(
    PCWSTR                   pszObjectID,
    IPortableDeviceContent2* pContent)
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
        printf("! Failed to get IEnumPortableDeviceObjectIDs from IPortableDeviceContent2, hr = 0x%lx\n",hr);
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

[**IEnumPortableDeviceObjectIDs**](ienumportabledeviceobjectids.md)
</dt> <dt>

[**IPortableDeviceContent2 Interface**](iportabledevicecontent2.md)
</dt> <dt>

[**IPortableDeviceService Interface**](iportabledeviceservice.md)
</dt> <dt>

[Opening a Service](opening-a-service.md)
</dt> <dt>

[WpdServicesApiSample](wpdapisample-sample-service-application.md)
</dt> </dl>

 

 



