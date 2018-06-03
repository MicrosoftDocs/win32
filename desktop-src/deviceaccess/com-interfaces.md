---
title: COM Interfaces
description: Component Object Model (COM)interfaces in the Device Access API.
ms.assetid: 96F532B7-5CF9-4341-932B-7F8BEDA9551F
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# COM Interfaces

Component Object Model (COM)interfaces in the Device Access API.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICreateDeviceAccessAsync**](/previous-versions/windows/desktop/api/Deviceaccess/nn-deviceaccess-icreatedeviceaccessasync)<br/>                 | The [**ICreateDeviceAccessAsync**](/previous-versions/windows/desktop/api/Deviceaccess/nn-deviceaccess-icreatedeviceaccessasync) interface is returned from a call to CreateDeviceAccessInstance. It enables the caller to control the operation of binding to an instance of a device in order to retrieve another interface that can be used to interact with that device.<br/> |
| [**IDeviceIoControl**](/previous-versions/windows/desktop/api/Deviceaccess/nn-deviceaccess-ideviceiocontrol)<br/>                                 | Sends a control code to a device driver.This action causes the device to perform the corresponding operation. <br/>                                                                                                                                                                                               |
| [**IDeviceRequestCompletionCallback**](/previous-versions/windows/desktop/api/Deviceaccess/nn-deviceaccess-idevicerequestcompletioncallback)<br/> | Provides a method to handle the completion of calls to the [**DeviceIoControlAsync**](/previous-versions/windows/desktop/api/Deviceaccess/nf-deviceaccess-ideviceiocontrol-deviceiocontrolasync)method.<br/>                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

**Samples**
</dt> <dt>

[Custom Driver Access Sample](http://go.microsoft.com/fwlink/p/?linkid=242014)
</dt> <dt>

**White papers**
</dt> <dt>

[Windows Store device app Design Guide for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009)
</dt> <dt>

**Other resources**
</dt> <dt>

[Device Experience for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009)
</dt> <dt>

[Device Experience for Windows 8](http://go.microsoft.com/fwlink/p/?linkid=241442)
</dt> </dl>

 

 





