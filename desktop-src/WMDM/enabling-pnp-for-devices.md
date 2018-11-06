---
title: Enabling PnP for Devices
description: Enabling PnP for Devices
ms.assetid: 510237a9-2b74-4c2e-ad45-3f45117289a6
keywords:
- Windows Media Device Manager,PnP devices
- Device Manager,PnP devices
- programming guide,PnP devices
- service providers,PnP devices
- creating service providers,PnP devices
- PnP devices
ms.topic: article
ms.date: 05/31/2018
---

# Enabling PnP for Devices

Windows Media Device Manager monitors arrival and removal notifications of devices that advertise a Portable Audio Player device interface. On the arrival of such a device, Windows Media Device Manager queries a device parameter named *WMDMSPCLSID* for the class ID of the service provider responsible for this device. Windows Media Device Manager calls [**IMDServiceProvider2::CreateDevice**](/windows/desktop/api/mswmdm/nf-mswmdm-imdserviceprovider2-createdevice) on this service provider to create a device object, which is exposed to the application as an [**IWMDMDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice) object.

A service provider can either handle PnP devices, or non-PnP devices; it cannot handle both types.

For a device to work with the preceding mechanism (and thus enable arrival and removal notifications for the device under Windows Media Device Manager applications), the following requirements must be met:

-   The device driver of this device must advertise the Windows Media Device Manager Portable Audio Player device interface. The GUID for this device interface is defined as:

    ```
    {0xf33fdc04, 0xd1ac, 0x4e8e, {0x9a, 0x30, 0x19, 0xbb, 0xd4, 0xb1, 0x8, 0xae} }
    ```

    

    > [!Note]  
    > A device should not advertise this interface if the device advertises the Volume interface (defined as VolumeClassGuid or GUID\_DEVINTERFACE\_VOLUME in winioctl.h). If the device advertises the Volume Interface, it is already PnP-enabled under Windows Media Device Manager.

     

    -AND/OR-

    A new registry subkey for the service provider must be created inside the subkey HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows Media Device Manager\\KnownDevices. This key should have the name of your service provider and must have the following two Reg\_SZ value entries:

    ```
    DeviceInterface         {25DBCE51-6C8F-4A72-8A6D-B54C2B4FC835}
    WMDMSPCLSID             {067B4B81-B1EC-489F-B111-940EBDC44EBE}
    ```

    

-   The device must have a device parameter named WMDMSPCLSID. The value of this parameter should be set as the CLSID of the service provider in a string form. For more information about device parameters, see [Device Parameters](device-parameters.md).

    > [!Note]  
    > The parameter value must be the CLSID, not the ProgID of the service provider.

     

-   The service provider for this device must implement the IMDServiceProvider2 interface.
-   The service provider key under HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows Media Device Manager\\Plugins\\SP\\SPName must contain the following DWORD value
    ```
    PnPAware    1
    ```

    

## Related topics

<dl> <dt>

[**Creating a Service Provider**](creating-a-service-provider.md)
</dt> </dl>

 

 




