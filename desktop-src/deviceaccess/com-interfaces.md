---
title: COM Interfaces
description: Component Object Model (COM)interfaces in the Device Access API.
ms.assetid: 96F532B7-5CF9-4341-932B-7F8BEDA9551F
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# COM Interfaces

Component Object Model (COM)interfaces in the Device Access API.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICreateDeviceAccessAsync**](/windows/previous-versions/Deviceaccess/nn-deviceaccess-icreatedeviceaccessasync?branch=master)<br/>                 | The [**ICreateDeviceAccessAsync**](/windows/previous-versions/Deviceaccess/nn-deviceaccess-icreatedeviceaccessasync?branch=master) interface is returned from a call to CreateDeviceAccessInstance. It enables the caller to control the operation of binding to an instance of a device in order to retrieve another interface that can be used to interact with that device.<br/> |
| [**IDeviceIoControl**](/windows/previous-versions/Deviceaccess/nn-deviceaccess-ideviceiocontrol?branch=master)<br/>                                 | Sends a control code to a device driver.This action causes the device to perform the corresponding operation. <br/>                                                                                                                                                                                               |
| [**IDeviceRequestCompletionCallback**](/windows/previous-versions/Deviceaccess/nn-deviceaccess-idevicerequestcompletioncallback?branch=master)<br/> | Provides a method to handle the completion of calls to the [**DeviceIoControlAsync**](/windows/previous-versions/Deviceaccess/nf-deviceaccess-ideviceiocontrol-deviceiocontrolasync?branch=master)method.<br/>                                                                                                                                                                      |



 

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

 

 





