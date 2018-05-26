---
Description: Setting Properties for Multiple Objects
ms.assetid: 0686ba54-4782-42a4-8fdb-2325fc8d8bc2
title: Setting Properties for Multiple Objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting Properties for Multiple Objects

Some device drivers support setting properties for multiple objects in a single function call—this is referred to as a bulk write. Your application can perform a bulk write using the interfaces described in the following table.



| Interface                                                                                      | Description                                                  |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [**IPortableDeviceContent Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent?branch=master)                             | Provides access to the content-specific methods.             |
| [**IPortableDeviceProperties Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledeviceproperties?branch=master)                       | Provides access to the property-specific methods.            |
| [**IPortableDevicePropertiesBulk Interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevicepropertiesbulk?branch=master)               | Supports the bulk write operation.                           |
| [**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md) | Used to store the object identifiers for the bulk operation. |
| [**IPortableDeviceValuesCollection Interface**](iportabledevicevaluescollection.md)           | Used to identify the properties to be written.               |



 

The `WriteContentPropertiesBulk` function in the sample application's ContentProperties.cpp module demonstrates a bulk write operation.

The first task accomplished in this sample is determining whether or not the given driver supports bulk operations. This is accomplished by calling QueryInterface on an **IPortableDeviceProperties** object and checking for the existence of **IPortableDevicePropertiesBulk**.


```C++
HRESULT                                       hr                = S_OK;
GUID                                          guidContext       = GUID_NULL;
CSetBulkValuesCallback*                       pCallback         = NULL;
CComPtr<IPortableDeviceProperties>            pProperties;
CComPtr<IPortableDevicePropertiesBulk>        pPropertiesBulk;
CComPtr<IPortableDeviceValues>                pObjectProperties;
CComPtr<IPortableDeviceContent>               pContent;
CComPtr<IPortableDeviceValuesCollection>      pPropertiesToWrite;
CComPtr<IPortableDevicePropVariantCollection> pObjectIDs;
DWORD                                         cObjectIDs        = 0;
if (SUCCEEDED(hr))
{
    hr = pDevice->Content(&amp;pContent);
    if (FAILED(hr))
    {
        printf("! Failed to get IPortableDeviceContent from IPortableDevice, hr = 0x%lx\n",hr);
    }
}



if (SUCCEEDED(hr))
{
    hr = pContent->Properties(&amp;pProperties);
    if (FAILED(hr))
    {
        printf("! Failed to get IPortableDeviceProperties from IPortableDevice, hr = 0x%lx\n",hr);
    }
}



if (SUCCEEDED(hr))
{
    hr = pProperties->QueryInterface(IID_PPV_ARGS(&amp;pPropertiesBulk));
    if (FAILED(hr))
    {
        printf("This driver does not support BULK property operations.\n");
    }
}
```



The next task entails creating an **IPortableDeviceValuesCollection** object. This is the object that contains the property values that the sample will write.


```C++
HRESULT                                       hr                = S_OK;
GUID                                          guidContext       = GUID_NULL;
CSetBulkValuesCallback*                       pCallback         = NULL;
CComPtr<IPortableDeviceProperties>            pProperties;
CComPtr<IPortableDevicePropertiesBulk>        pPropertiesBulk;
CComPtr<IPortableDeviceValues>                pObjectProperties;
CComPtr<IPortableDeviceContent>               pContent;
CComPtr<IPortableDeviceValuesCollection>      pPropertiesToWrite;
CComPtr<IPortableDevicePropVariantCollection> pObjectIDs;
DWORD                                         cObjectIDs        = 0;
if (SUCCEEDED(hr))
{
    hr = CoCreateInstance(CLSID_PortableDeviceValuesCollection,
                          NULL,
                          CLSCTX_INPROC_SERVER,
                          IID_IPortableDeviceValuesCollection,
                          (VOID**) &amp;pPropertiesToWrite);
    if (FAILED(hr))
    {
        printf("! Failed to CoCreate IPortableDeviceValuesCollection for bulk property values, hr = 0x%lx\n", hr);
    }
}
```



After this, the sample creates an instance of the [**IPortableDevicePropertiesBulkCallback interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevicepropertiesbulk?branch=master). The application will use the methods in this interface to track the progress of the asynchronous bulk-write operation.


```C++
HRESULT                                       hr                = S_OK;
GUID                                          guidContext       = GUID_NULL;
CSetBulkValuesCallback*                       pCallback         = NULL;
CComPtr<IPortableDeviceProperties>            pProperties;
CComPtr<IPortableDevicePropertiesBulk>        pPropertiesBulk;
CComPtr<IPortableDeviceValues>                pObjectProperties;
CComPtr<IPortableDeviceContent>               pContent;
CComPtr<IPortableDeviceValuesCollection>      pPropertiesToWrite;
CComPtr<IPortableDevicePropVariantCollection> pObjectIDs;
DWORD                                         cObjectIDs        = 0;
if (SUCCEEDED(hr))
{
    pCallback = new CSetBulkValuesCallback();
    if (pCallback == NULL)
    {
        hr = E_OUTOFMEMORY;
        printf("! Failed to allocate CSetBulkValuesCallback, hr = 0x%lx\n", hr);
    }
}
```



The next function that the sample application calls is the `CreateIPortableDevicePropVariantCollectionWithAllObjectIDs` helper function. This function recursively enumerates all objects on a given device and returns an [**IPortableDevicePropVariantCollection interface**](iportabledevicepropvariantcollection.md) that contains an identifier for each object that it found. This function is defined in the module ContentEnumeration.cpp.


```C++
// 7) Call our helper function CreateIPortableDevicePropVariantCollectionWithAllObjectIDs
// to enumerate and create an IPortableDevicePropVariantCollection with the object
// identifiers needed to perform the bulk operation on.
if (SUCCEEDED(hr))
{
    hr = CreateIPortableDevicePropVariantCollectionWithAllObjectIDs(pDevice,
                                                                    pContent,
                                                                    &amp;pObjectIDs);
}
```



The **IPortableDevicePropVariantCollection** object holds a collection of indexed **PROPVARIANT** values of the same VARTYPE. In this case, these values contain a given object identifier for each object found on the device.

The object identifiers and their respective name properties are stored in an [**IPortableDeviceValuesCollection**](iportabledevicevalues.md) object. The name properties are organized so that the first object is assigned a name property of "NewName0", the second object is assigned a name property of "NewName1", and so on.

The following excerpt from the sample demonstrates how the **IPortableDeviceValuesCollection** object was initialized with object identifiers and new name strings.


```C++
HRESULT                                       hr                = S_OK;
GUID                                          guidContext       = GUID_NULL;
CSetBulkValuesCallback*                       pCallback         = NULL;
CComPtr<IPortableDeviceProperties>            pProperties;
CComPtr<IPortableDevicePropertiesBulk>        pPropertiesBulk;
CComPtr<IPortableDeviceValues>                pObjectProperties;
CComPtr<IPortableDeviceContent>               pContent;
CComPtr<IPortableDeviceValuesCollection>      pPropertiesToWrite;
CComPtr<IPortableDevicePropVariantCollection> pObjectIDs;
DWORD                                         cObjectIDs        = 0;
if (SUCCEEDED(hr))
{
    hr = pObjectIDs->GetCount(&amp;cObjectIDs);
    if (FAILED(hr))
    {
        printf("! Failed to get number of objectIDs from IPortableDevicePropVariantCollection, hr = 0x%lx\n", hr);
    }
}


if (SUCCEEDED(hr))
{
    for(DWORD dwIndex = 0; (dwIndex < cObjectIDs) &amp;&amp; (hr == S_OK); dwIndex++)
    {
        CComPtr<IPortableDeviceValues>  pValues;
        PROPVARIANT                     pv = {0};

        PropVariantInit(&amp;pv);
        hr = CoCreateInstance(CLSID_PortableDeviceValues,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IPortableDeviceValues,
                              (VOID**) &amp;pValues);
        if (FAILED(hr))
        {
            printf("! Failed to CoCreate CLSID_PortableDeviceValues, hr = 0x%lx\n", hr);
        }

        // Get the Object ID whose properties we will set
        if (hr == S_OK)
        {
            hr = pObjectIDs->GetAt(dwIndex, &amp;pv);
            if (FAILED(hr))
            {
                printf("! Failed to get next Object ID from list, hr = 0x%lx\n", hr);
            }
        }

        // Save them into the IPortableDeviceValues so the driver knows which object this proeprty set belongs to
        if (hr == S_OK)
        {
            hr = pValues->SetStringValue(WPD_OBJECT_ID, pv.pwszVal);
            if (FAILED(hr))
            {
                printf("! Failed to set WPD_OBJECT_ID, hr = 0x%lx\n", hr);
            }
        }

        // Set the new values.  In this sample, we attempt to set the name property.
        if (hr == S_OK)
        {
            CAtlStringW strValue;
            strValue.Format(L"NewName%d", dwIndex);

            hr = pValues->SetStringValue(WPD_OBJECT_NAME, strValue.GetString());
            if (FAILED(hr))
            {
                printf("! Failed to set WPD_OBJECT_NAME, hr = 0x%lx\n", hr);
            }
        }

        // Add this property set to the collection
        if (hr == S_OK)
        {
            hr = pPropertiesToWrite->Add(pValues);
            if (FAILED(hr))
            {
                printf("! Failed to add values to collection, hr = 0x%lx\n", hr);
            }
        }
        PropVariantClear(&amp;pv);
    }
}
```



Once the sample creates the **IPortableDeviceValuesCollection** object that contains the object identifier and name pairs, it can begin the asynchronous operation.

The asynchronous write operation begins when the sample calls the [**IPortableDevicePropertiesBulk::QueueSetValuesByObjectList**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevicepropertiesbulk-queuesetvaluesbyobjectlist?branch=master) method. This method notifies the driver that a bulk operation is about to begin. After this, the sample calls the [**IPortableDeviceBulk::Start**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevicepropertiesbulk-start?branch=master) method to begin actually writing the new name values.


```C++
   HRESULT                                       hr                = S_OK;
   GUID                                          guidContext       = GUID_NULL;
   CSetBulkValuesCallback*                       pCallback         = NULL;
   CComPtr<IPortableDeviceProperties>            pProperties;
   CComPtr<IPortableDevicePropertiesBulk>        pPropertiesBulk;
   CComPtr<IPortableDeviceValues>                pObjectProperties;
   CComPtr<IPortableDeviceContent>               pContent;
   CComPtr<IPortableDeviceValuesCollection>      pPropertiesToWrite;
   CComPtr<IPortableDevicePropVariantCollection> pObjectIDs;
   DWORD                                         cObjectIDs        = 0;
   if (SUCCEEDED(hr))
   {
       hr = pPropertiesBulk->QueueSetValuesByObjectList(pPropertiesToWrite,
                                                        pCallback,
                                                        &amp;guidContext);


       if(SUCCEEDED(hr))
       {
           // Cleanup any previously created global event handles.
           if (g_hBulkPropertyOperationEvent != NULL)
           {
               CloseHandle(g_hBulkPropertyOperationEvent);
               g_hBulkPropertyOperationEvent = NULL;
           }

           // In order to create a simpler to follow example we create and wait infinitly
           // for the bulk property operation to complete and ignore any errors.
           // Production code should be written in a more robust manner.
           // Create the global event handle to wait on for the bulk operation
           // to complete.
           g_hBulkPropertyOperationEvent = CreateEvent(NULL, FALSE, FALSE, NULL);
           if (g_hBulkPropertyOperationEvent != NULL)
           {
               // Call Start() to actually being the Asynchronous bulk operation.
               hr = pPropertiesBulk->Start(guidContext);
               if(FAILED(hr))
               {
                   printf("! Failed to start property operation, hr = 0x%lx\n", hr);
               }
           }
           else
           {
               printf("! Failed to create the global event handle to wait on for the bulk operation. Aborting operation.\n");
           }
       }
       else
       {
           printf("! QueueSetValuesByObjectList Failed, hr = 0x%lx\n", hr);
       }
   }
```



Note that the sample waits an infinitely long period of time for the operation to complete. If this were a production application, the code would need to be modified.

## Related topics

<dl> <dt>

[**IPortableDevice Interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevice?branch=master)
</dt> <dt>

[**IPortableDeviceContent Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent?branch=master)
</dt> <dt>

[**IPortableDeviceProperties Interface**](/windows/win32/portabledeviceapi/nn-portabledeviceapi-iportabledeviceproperties?branch=master)
</dt> <dt>

[**IPortableDevicePropertiesBulk Interface**](/windows/win32/PortableDeviceApi/nn-portabledeviceapi-iportabledevicepropertiesbulk?branch=master)
</dt> <dt>

[**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 



