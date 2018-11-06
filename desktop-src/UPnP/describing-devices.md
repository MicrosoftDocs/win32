---
title: Describing Devices
description: There are two ways to obtain device objects.
ms.assetid: a83fbf21-586e-4b92-9875-476d820c377d
ms.topic: article
ms.date: 05/31/2018
---

# Describing Devices

There are two ways to obtain device objects:

-   Using the [**IUPnPDescriptionDocument**](/windows/desktop/api/Upnp/nn-upnp-iupnpdescriptiondocument) interface. The **IUPnPDescriptionDocument** interface is the only interface that is safe for scripting.
-   Using the [**IUPnPDeviceFinder**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevicefinder) interface to obtain an [**IUPnPDevices**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevices) interface.

Both methods return Devices collections. Applications then use the Device methods to retrieve properties about devices.

Applications are able to retrieve the following types of information:

-   Device hierarchy information, including root devices, parent devices, and child devices.
-   Device properties, including UDNs, uniform resource identifiers (URIs), and user-readable names.
-   Manufacturer information, including names and related Web pages.
-   Model information, including the name, number, UPC, serial numbers and device descriptions.
-   Display information, including the URL to control the device, and URLs from which icons are downloaded.
-   Services provided by a particular device.

Applications also obtain the URL of the device description document using the [**IUPnPDeviceDocumentAccess**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevicedocumentaccess) interface. The application then load the description document and work with device and service properties that are not exposed by the [**IUPnPDevice**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevice) interface. This interface cannot be used in scripting, because it is not the default interface.

## Visual Basic Example

The following sample code shows the usage of [**IUPnPDeviceDocumentAccess::GetDocumentURL**](/windows/desktop/api/Upnp/nf-upnp-iupnpdevicedocumentaccess-getdocumenturl).


```VB
Sub GetDocumentURL()
Dim pDescDoc As IUPnPDeviceDocumentAccess
Dim strDescDocURL As String

'currentDevice is UPnPDevice object containing the current UPnP Device 
'We are trying to get IUPnPDeviceDocumentAccess interface in the UPnP Device object
Set pDescDoc = currentDevice

If Not (pDescDoc is Nothing) Then
  'Description Document URL is got from device
  strDescDocURL = pDescDoc.GetDocumentURL 
End If
```



## C++ Example

The following sample code shows the usage of [**IUPnPDeviceDocumentAccess::GetDocumentURL**](/windows/desktop/api/Upnp/nf-upnp-iupnpdevicedocumentaccess-getdocumenturl).


```C++
#include <windows.h>
#include <upnp.h>
#include <stdio.h>

#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "oleaut32.lib")

int GetDeviceDocumentUrl () 
{
  HRESULT hr = S_OK;
  // List of interfaces needed
  IUPnPDeviceFinder *pDevFinder=NULL;
  IUPnPDevice *pDevice =NULL;
  IUPnPDeviceDocumentAccess* pDeviceDocument=NULL;
  BSTR bstrDeviceUDN =NULL;
  BSTR bstrDeviceDocumentURL = NULL; 

  bstrDeviceUDN = SysAllocString(L"uuid:234324234324");
  if(bstrDeviceUDN == NULL){
    printf("ERROR: Could not allocate memory\n");
    return -1;
  }  

  //CoInitialize the program so that we can create COM objects
  CoInitializeEx(NULL, COINIT_MULTITHREADED);

  //now try to instantiate the DeviceFinder object
  hr = CoCreateInstance(  CLSID_UPnPDeviceFinder, 
              NULL,
              CLSCTX_INPROC_SERVER,
              IID_IUPnPDeviceFinder,
              (LPVOID *) &pDevFinder); 

  if(!SUCCEEDED(hr)){
    printf("\nERROR: CoCreateInstance on IUPnPDeviceFinder returned HRESULT %x",hr);
    goto cleanup;
  }

  printf("\nGot a pointer to the IUPnPDeviceFinder Interface");

  printf("\n Finding the device of given UDN\n");
  hr =pDevFinder->FindByUDN(bstrDeviceUDN, &pDevice);
  if(hr!=S_OK)
  {
    printf("\nERROR: FindByUDN for %S returned HRESULT %x", bstrDeviceUDN, hr);
    goto cleanup;
  }

  printf("\n\tFindByUDN for device of UDN %S succeeded", bstrDeviceUDN);
  //Now query pDevice for IUPnPDeviceDocumentAccess
  hr = pDevice->QueryInterface(IID_IUPnPDeviceDocumentAccess, (VOID **)&pDeviceDocument);
  if(SUCCEEDED(hr)){
    // We have got a pointer to the IUPnPDeviceDocumentAccess interface.
    // GetDocumentURL is available only in Windows XP. 
    hr = pDeviceDocument->GetDocumentURL(&bstrDeviceDocumentURL);
    if(SUCCEEDED(hr))
      printf("\nThe Device Document URL is %S \n", bstrDeviceDocumentURL);
  }
    
cleanup:
  //release references to all interfaces 
  if(pDevFinder)
    pDevFinder->Release();
  if(pDevice)
    pDevice->Release();
  if(pDeviceDocument)
    pDeviceDocument->Release();
  
  // Free the bstr strings
  if(bstrDeviceDocumentURL)
    SysFreeString(bstrDeviceDocumentURL);
  if(bstrDeviceUDN)
    SysFreeString(bstrDeviceUDN);
  CoUninitialize();
  return 0;
}
```



 

 




