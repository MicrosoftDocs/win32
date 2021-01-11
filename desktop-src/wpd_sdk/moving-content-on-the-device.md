---
description: Moving Content on the Device
ms.assetid: 5072d308-d376-4141-96df-dbef23fb9f9b
title: Moving Content on the Device
ms.topic: article
ms.date: 05/31/2018
---

# Moving Content on the Device

Another common operation accomplished by a WPD application is the transfer of content from one location on the device to another.

Content move operations are accomplished using the interfaces described in the following table.



| Interface                                                                                      | Description                                       |
|------------------------------------------------------------------------------------------------|---------------------------------------------------|
| [**IPortableDeviceContent Interface**](/windows/desktop/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent)                             | Provides access to the content-specific methods.  |
| [**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md) | Provides access to the property-specific methods. |



 

The MoveContentAlreadyOnDevice function in the sample application's ContentTransfer.cpp module demonstrates how an application can move content from one location to another.

The first task accomplished by the MoveContentAlreadyOnDevice function is to query the device driver to see whether it supports content movement. This is accomplished by calling the SupportsCommand helper function and passing WPD\_COMMAND\_OBJECT\_MANAGEMENT\_MOVE\_OBJECTS as the second argument.


```C++
HRESULT                                       hr                               = S_OK;
WCHAR                                         wszSelection[81]                 = {0};
WCHAR                                         wszDestinationFolderObjectID[81] = {0};
CComPtr<IPortableDeviceContent>               pContent;
CComPtr<IPortableDevicePropVariantCollection> pObjectsToMove;
CComPtr<IPortableDevicePropVariantCollection> pObjectsFailedToMove;
if (SupportsCommand(pDevice, WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS) == FALSE)
{
    printf("! This device does not support the move operation (i.e. The WPD_COMMAND_OBJECT_MANAGEMENT_MOVE_OBJECTS command)\n");
    return;
}
```



The next step entails prompting the user to enter two object identifiers. The first is the identifier for the content that will be moved. The second is the identifier for the location to which the application should move this content.


```C++
HRESULT                                       hr                               = S_OK;
WCHAR                                         wszSelection[81]                 = {0};
WCHAR                                         wszDestinationFolderObjectID[81] = {0};
CComPtr<IPortableDeviceContent>               pContent;
CComPtr<IPortableDevicePropVariantCollection> pObjectsToMove;
CComPtr<IPortableDevicePropVariantCollection> pObjectsFailedToMove;
printf("Enter the identifer of the object you wish to move.\n>");
hr = StringCbGetsW(wszSelection,sizeof(wszSelection));
if (FAILED(hr))
{
    printf("An invalid object identifier was specified, aborting content moving\n");
}

// Prompt user to enter an object identifier on the device to move.
printf("Enter the identifer of the object you wish to move '%ws' to.\n>", wszSelection);
hr = StringCbGetsW(wszDestinationFolderObjectID,sizeof(wszDestinationFolderObjectID));
if (FAILED(hr))
{
    printf("An invalid object identifier was specified, aborting content moving\n");
}
```



Next, the sample retrieves an [**IPortableDeviceContent**](/windows/desktop/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent) object that is used to access the [**IPortableDeviceContent::Move**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecontent-move) method.


```C++
HRESULT                                       hr                               = S_OK;
WCHAR                                         wszSelection[81]                 = {0};
WCHAR                                         wszDestinationFolderObjectID[81] = {0};
CComPtr<IPortableDeviceContent>               pContent;
CComPtr<IPortableDevicePropVariantCollection> pObjectsToMove;
CComPtr<IPortableDevicePropVariantCollection> pObjectsFailedToMove;
if (SUCCEEDED(hr))
{
    hr = pDevice->Content(&pContent);
    if (FAILED(hr))
    {
        printf("! Failed to get IPortableDeviceContent from IPortableDevice, hr = 0x%lx\n",hr);
    }
}
```



Finally, the content is moved. This process involves the following:

1.  Creating an [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) object that receives a PROPVARIANT structure for the object to be moved.
2.  Adding the PROPVARIANT to the IPortableDevicePropVariantCollection object.
3.  Invoking the IPortableDeviceContent::Move method.


```C++
HRESULT                                       hr                               = S_OK;
WCHAR                                         wszSelection[81]                 = {0};
WCHAR                                         wszDestinationFolderObjectID[81] = {0};
CComPtr<IPortableDeviceContent>               pContent;
CComPtr<IPortableDevicePropVariantCollection> pObjectsToMove;
CComPtr<IPortableDevicePropVariantCollection> pObjectsFailedToMove;
if (SUCCEEDED(hr))
{
    hr = CoCreateInstance(CLSID_PortableDevicePropVariantCollection,
                          NULL,
                          CLSCTX_INPROC_SERVER,
                          IID_IPortableDevicePropVariantCollection,
                          (VOID**) &pObjectsToMove);
    if (SUCCEEDED(hr))
    {
        if (pObjectsToMove != NULL)
        {
            PROPVARIANT pv = {0};
            PropVariantInit(&pv);

            // Initialize a PROPVARIANT structure with the object identifier string
            // that the user selected above. Notice we are allocating memory for the
            // LPWSTR value.  This memory will be freed when PropVariantClear() is
            // called below.
            pv.vt      = VT_LPWSTR;
            pv.pwszVal = AtlAllocTaskWideString(wszSelection);
            if (pv.pwszVal != NULL)
            {
                // Add the object identifier to the objects-to-move list
                // (We are only moving 1 in this example)
                hr = pObjectsToMove->Add(&pv);
                if (SUCCEEDED(hr))
                {
                    // Attempt to move the object on the device
                    hr = pContent->Move(pObjectsToMove,               // Object(s) to move
                                        wszDestinationFolderObjectID, // Folder to move to
                                        NULL);                        // Object(s) that failed to delete (we are only moving 1, so we can pass NULL here)
                    if (SUCCEEDED(hr))
                    {
                        // An S_OK return lets the caller know that the deletion was successful
                        if (hr == S_OK)
                        {
                            printf("The object '%ws' was moved on the device.\n", wszSelection);
                        }

                        // An S_FALSE return lets the caller know that the move failed.
                        // The caller should check the returned IPortableDevicePropVariantCollection
                        // for a list of object identifiers that failed to be moved.
                        else
                        {
                            printf("The object '%ws' failed to be moved on the device.\n", wszSelection);
                        }
                    }
                    else
                    {
                        printf("! Failed to move an object on the device, hr = 0x%lx\n",hr);
                    }
                }
                else
                {
                    printf("! Failed to move an object on the device because we could no add the object identifier string to the IPortableDevicePropVariantCollection, hr = 0x%lx\n",hr);
                }
            }
            else
            {
                hr = E_OUTOFMEMORY;
                printf("! Failed to move an object on the device because we could no allocate memory for the object identifier string, hr = 0x%lx\n",hr);
            }

            // Free any allocated values in the PROPVARIANT before exiting
            PropVariantClear(&pv);
        }
        else
        {
            printf("! Failed to move an object from the device because we were returned a NULL IPortableDevicePropVariantCollection interface pointer, hr = 0x%lx\n",hr);
        }
    }
    else
    {
        printf("! Failed to CoCreateInstance CLSID_PortableDevicePropVariantCollection, hr = 0x%lx\n",hr);
    }
}
```



## Related topics

<dl> <dt>

[**IPortableDevice Interface**](/windows/desktop/api/PortableDeviceApi/nn-portabledeviceapi-iportabledevice)
</dt> <dt>

[**IPortableDeviceContent Interface**](/windows/desktop/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent)
</dt> <dt>

[**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 



