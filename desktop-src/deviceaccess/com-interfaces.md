---
title: COM Interfaces - Device Access
description: Component Object Model (COM)interfaces in the Device Access API.
ms.assetid: 96F532B7-5CF9-4341-932B-7F8BEDA9551F
ms.topic: article
ms.date: 02/11/2020
---

# COM Interfaces - Device Access

Component Object Model (COM)interfaces in the Device Access API.

## In this section

| Topic | Description |
|---|---|
| [**ICreateDeviceAccessAsync**](/windows/win32/api/Deviceaccess/nn-deviceaccess-icreatedeviceaccessasync)<br/> | The [**ICreateDeviceAccessAsync**](/windows/win32/api/Deviceaccess/nn-deviceaccess-icreatedeviceaccessasync) interface is returned from a call to CreateDeviceAccessInstance. It enables the caller to control the operation of binding to an instance of a device in order to retrieve another interface that can be used to interact with that device.<br/> |
| [**IDeviceIoControl**](/windows/win32/api/Deviceaccess/nn-deviceaccess-ideviceiocontrol)<br/> | Sends a control code to a device driver.This action causes the device to perform the corresponding operation. <br/> |
| [**IDeviceRequestCompletionCallback**](/windows/win32/api/Deviceaccess/nn-deviceaccess-idevicerequestcompletioncallback)<br/> | Provides a method to handle the completion of calls to the [**DeviceIoControlAsync**](/windows/win32/api/Deviceaccess/nf-deviceaccess-ideviceiocontrol-deviceiocontrolasync)method.<br/> |

## Related topics

[Custom Driver Access Sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/411c271e537727d737a53fa2cbe99eaecac00cc0/Official%20Windows%20Platform%20Sample/Custom%20driver%20access%20sample), [UWP device apps for internal devices](/windows-hardware/drivers/devapps/uwp-device-apps-for-specialized-devices), [Hardware Dev Center](/windows-hardware/drivers/)
