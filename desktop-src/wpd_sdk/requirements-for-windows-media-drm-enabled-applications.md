---
description: Requirements for Windows Media DRM-Enabled Applications
ms.assetid: 67f872dc-79ef-4799-bb7b-b84d7dc11c71
title: Requirements for Windows Media DRM-Enabled Applications
ms.topic: article
ms.date: 05/31/2018
---

# Requirements for Windows Media DRM-Enabled Applications

To create a Windows Media Digital Rights Management (DRM)-enabled application, you must have the headers and libraries described in the [General Requirements for Application Development](general-requirements-for-application-development.md) section of this document. In addition, the application will need to supply additional properties in the client information when opening the device.

The two additional properties that are required to enable Windows Media DRM-protected content transfers are described in the following table.



| Property                                      | Description                              |
|-----------------------------------------------|------------------------------------------|
| WPD\_CLIENT\_WMDRM\_APPLICATION\_PRIVATE\_KEY | Specifies the application's private key. |
| WPD\_CLIENT\_WMDRM\_APPLICATION\_CERTIFICATE  | Specifies the application's certificate. |



 

These properties must be supplied in the application's client information when the device is opened with the [**IPortableDevice::Open**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-open) method. When these properties are supplied, the WPD API allows protected content transfers. If the application has provided a certificate and private key, the API will create a secure channel to transfer protected WMDRM content to the device.

For information about creating and distributing Windows-based applications that support Windows Media DRM, see the following [Licensing Windows-based Applications](https://www.microsoft.com/windows/windowsmedia/licensing/licensing_drm_apps.aspx) topic.

## Transferring Content

To transfer WMDRM protected content, use [**IPortableDeviceContent::CreateObjectWithPropertiesAndData**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecontent-createobjectwithpropertiesanddata). This method can be used for both protected and clear content without additional options. The WPD API will automatically select the protected or clear channel depending on whether the content is protected or clear. It interfaces with the WMDRM Secure Content Provider to process the WMDRM licenses.

## Transferring Known Clear Content

If you've enabled your application to handle protected content, but you know that a specific file is not protected, you can tell WPD to skip the DRM processing by setting **WPD\_API\_OPTION\_USE\_CLEAR\_DATA\_STREAM** option to TRUE in the input **IPortableDeviceValues** when calling [**IPortableDeviceContent::CreateObjectWithPropertiesAndData**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecontent-createobjectwithpropertiesanddata) for clear content.

## Accessing Metering Operations using IWMDRMDeviceApp

WPD provides a mechanism to access the **IWMDRMDeviceApp** APIs for license updates and metering data retrieval. To access this API through WPD, call **QueryInterface** on **IID\_IWMDRMDeviceApp** from the **IStream** returned from [**IPortableDeviceContent::CreateObjectWithPropertiesAndData**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecontent-createobjectwithpropertiesanddata). This **IWMDRMDeviceApp** instance tied to the **IPortableDevice** connection to your WMDRM-compatible device, and not the specific content where the **IStream** was obtained. WPD internally wraps the metering APIs and makes it accessible to your application. Your application should use the WMDRMDEVICEAPP\_USE\_WPD\_DEVICE\_PTR constant for the *IWMDMDevice*\* parameter.

The following code snippet demonstrates this.


```C++
IStream*               pDataStream = NULL;

IWMDRMDeviceApp*       pWMDRMApp   = NULL;

  

// ... Initialization 

 

hr = pPortableDeviceContent->CreateObjectWithPropertiesAndData(pValues,

                              &pDataStream,

                              &dwOptimalWriteBufferSize,

                              NULL);

 

// ... Transfer the protected WMDRM content 

pDataStream->Write(pData, cbData, &cbWritten);

 

pDataStream->Commit(0);

 

hr = pDataStream->QueryInterface(IID_IWMDRMDeviceApp, 

                                 (void**)&pWMDRMApp);

 

if (SUCCEEDED(hr))

{

   DWORD dwStatus = 0;

 

   // Call metering operations on the current device using the WPD device pointer

   hr = pWMDRMApp->QueryDeviceStatus((IWMDMDevice *)WMDRMDEVICEAPP_USE_WPD_DEVICE_PTR, 

                                     &dwStatus);

}

```



The same pre-requisite with the application private key and certificate applies here as well. If the key/certificate is invalid or if the WMDRM system fails to initialize, the **QueryInferface** call will fail.

The above method to acquire the **IWMDRMDeviceApp** interface from the **IStream** pointer is just a convenience if your application is already doing a prior protected content transfer, before proceeding on to do metering and license synchronization operations.

Our recommendation for most applications that need to access **IWMDRMDeviceApp** is to initialize **IWMDRMDeviceApp** directly as this does not require your application to transfer protected content or hold on to the transfer interfaces in order to do device metering and license sync. This method will require usage of Windows Media Device Manager (WMDM) APIs. For details and sample code, refer to the [Accessing WMDRM APIs from a WPD Application](../windows-portable-devices.md) whitepaper on the WHDC site.

## Related topics

<dl> <dt>

[**Windows Portable Devices**](/windows/desktop/windows-portable-devices)
</dt> </dl>

 

 
