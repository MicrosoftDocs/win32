---
description: Frees the Plug and Play (PnP) identifiers that are retrieved by the IPortableDeviceManager::GetDevices or IPortableDeviceServiceManager::GetDeviceServices methods.
ms.assetid: b86f7733-81a3-4b60-bb7c-840c75f8d03f
title: FreePortableDevicePnPIDs function (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FreePortableDevicePnPIDs
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# FreePortableDevicePnPIDs function

The **FreePortableDevicePnPIDs** helper function frees the Plug and Play (PnP) identifiers that are retrieved by the [**IPortableDeviceManager::GetDevices**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicemanager-getdevices) or [**IPortableDeviceServiceManager::GetDeviceServices**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicemanager-getdeviceservices) methods.

## Syntax


```C++
void FreePortableDevicePnPIDs(
   LPWSTR *pPnPIDs,
   DWORD  cPnPIDs
);
```



## Parameters

<dl> <dt>

*pPnPIDs* 
</dt> <dd>

The array of Plug and Play (PnP) identifiers to be freed.

</dd> <dt>

*cPnPIDs* 
</dt> <dd>

The number of identifiers in the array specified by the *pPnPIDs* parameter.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The application is responsible for freeing the array of pointers that it allocates.

## Examples


```C++
// Allocate an array of LPWSTR pointers.
    LPWSTR* pPnpDeviceIDs = new LPWSTR[cPnpDeviceIDs];
if (pPnpDeviceIDs != NULL)
{
    hr = pPortableDeviceManager->;GetDevices(pPnpDeviceIDs, &cPnpDeviceIDs);
    if (SUCCEEDED(hr))
    {
        // Free all returned PnPDeviceID strings allocated by IPortableDeviceManager::GetDevices.
     FreePortableDevicePnPIDs(pPnpDeviceIDs, cPnpDeviceIDs);
     // Application is responsible for deleting the array of LPWSTR pointers.
     delete [] pPnpDeviceIDs;
     pPnpDeviceIDs = NULL;      
 }
} 
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                                   |
| Header<br/>                   | <dl> <dt>PortableDevice.h</dt> </dl> |



 

 




