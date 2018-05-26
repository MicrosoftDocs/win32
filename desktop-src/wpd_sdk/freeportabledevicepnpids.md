---
Description: Frees the Plug and Play (PnP) identifiers that are retrieved by the IPortableDeviceManagerGetDevices or IPortableDeviceServiceManagerGetDeviceServices methods.
ms.assetid: b86f7733-81a3-4b60-bb7c-840c75f8d03f
title: FreePortableDevicePnPIDs function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FreePortableDevicePnPIDs function

The **FreePortableDevicePnPIDs** helper function frees the Plug and Play (PnP) identifiers that are retrieved by the [**IPortableDeviceManager::GetDevices**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevicemanager-getdevices?branch=master) or [**IPortableDeviceServiceManager::GetDeviceServices**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicemanager-getdeviceservices?branch=master) methods.

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
    hr = pPortableDeviceManager->;GetDevices(pPnpDeviceIDs, &amp;cPnpDeviceIDs);
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



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                                   |
| Header<br/>                   | <dl> <dt>PortableDevice.h</dt> </dl> |



 

 




