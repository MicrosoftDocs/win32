---
Description: The fax service calls the fax service provider (FSP)'s FaxLineCallback function to inform the service provider when an end user enables or disables the sending or receiving of faxes on a virtual fax device.
ms.assetid: b8a758fa-e7a8-41e9-b572-bbd5108a97bd
title: Signaling Changes in the Status of a Virtual Device
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Signaling Changes in the Status of a Virtual Device

The fax service calls the fax service provider (FSP)'s [**FaxLineCallback**](/previous-versions/windows/desktop/api/FaxDev/nc-faxdev-pfax_linecallback) function to inform the service provider when an end user enables or disables the sending or receiving of faxes on a virtual fax device. The FSP registers the callback function by passing its address when the fax service calls the [**FaxDevInitialize**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevinitialize) function.

The fax service calls the [**FaxDevInitialize**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevinitialize) function using the following values.



| Parameter    | Value                                                                                                                                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *FaxHandle*  | **NULL**                                                                                                                                                                                                        |
| *hDevice*    | The identifier of the virtual fax device.                                                                                                                                                                       |
| *dwMessage*  | **LINE\_DEVSPECIFIC**                                                                                                                                                                                           |
| *dwInstance* | Zero                                                                                                                                                                                                            |
| *dwParam1*   | The fax service generates a value for this parameter. If the virtual fax device is enabled to receive faxes, this parameter has a nonzero value. If fax reception is disabled, this parameter is equal to zero. |
| *dwParam2*   | The fax service generates a value for this parameter. If the virtual fax device is enabled to send faxes, this parameter has a nonzero value. If fax sending is disabled, this parameter is equal to zero.      |
| *dwParam3*   | Zero                                                                                                                                                                                                            |



 

The fax service calls [**FaxLineCallback**](/previous-versions/windows/desktop/api/FaxDev/nc-faxdev-pfax_linecallback) multiple times, once for each virtual device the FSP supports, even if the status of only one virtual device changes.

For more information about identifiers for virtual fax devices, see the description of the *DeviceIdPrefix* parameter of the [**FaxDevVirtualDeviceCreation**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevvirtualdevicecreation) function.

For more information about enabling or disabling the transmission and reception of faxes on a fax device, see [**FaxEnumPorts**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumportsa), [**FaxGetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetporta), [**FaxSetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetporta), [**FAX\_PORT\_INFO**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_port_infoa), and [Fax Device Management](-mfax-fax-device-management.md) in the [Fax Service Client API](-mfax-about-the-fax-service-client-api.md) documentation.

 

 



