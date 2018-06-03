---
title: Design Considerations for Custom Devices
description: This topic describes design considerations that can help you determine whether your device needs a custom driver.
ms.assetid: 8AADE304-4841-41E2-968B-DFCB5B954FF1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Design Considerations for Custom Devices

This topic describes design considerations that can help you determine whether your device needs a custom driver.

-   [Determining the type of driver to implement](#determining-the-type-of-driver-to-implement)
-   [Security considerations](#security-considerations)
-   [Related topics](#related-topics)

## Determining the type of driver to implement

This table describes when you should develop a custom driver for your device and communicate with it by using the Device Access API, and when you should use Windows-provided device stacks instead.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>To support</th>
<th>Implementation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Well-known devices, including these:
<ul>
<li>Sensor</li>
<li>Location</li>
<li>Webcam</li>
<li>Proximity</li>
<li>Short message service (SMS)</li>
<li>Mobile broadband</li>
</ul>
<br/></td>
<td>For many types of well-known devices, you don't need a custom driver, because Windows includes APIs and class-extension device driver interfaces (DDIs) that manage the communication between the driver and Windows. Sensor, location, and Windows Portable Device (WPD) devices are some examples of device classes that have this support. If you build a driver that uses one of these Windows-provided DDIs to send and receive data and commands, there's no need for your Windows Store app to use the Device Access API to broker access or send input/output (I/O) control codes directly to the driver. <br/> When a Windows Store app requests access to a well-known device by using the Windows Runtime API for its device class, Windows 8 will handle device access based on the type of device. Apps will always get access to some well-known types of devices (such as accelerometers) that don't reveal any personally identifiable information. Other types of well-known devices must be declared in the application manifest before an app can access them. The user must grant permission for an app to access devices that reveal sensitive information, like location, webcam, and microphone devices, or can cost the user money, like mobile broadband devices. <br/></td>
</tr>
<tr class="even">
<td>A WPD device that implements MTP services<br/></td>
<td>You can use the MTP class driver, or you can build a driver by using the WPD DDI.<br/> Windows 8 provides support for MTP device services.And an app can use the [<strong>Windows.Devices.Portable</strong>](https://msdn.microsoft.com/library/windows/apps/br225657) Windows Runtime API, the Portable Device Component Object Model (COM) API, or WPD Automation to access the device. Your app doesn't need to use the Device Access API. For more information, see the[Windows Store device app design guide](http://go.microsoft.com/fwlink/p/?linkid=242009). <br/></td>
</tr>
<tr class="odd">
<td>A device that doesn't have a Windows-provided class extension or class driver</td>
<td>In this case, consult the [Windows Store device app design guide](http://go.microsoft.com/fwlink/p/?linkid=242009) for specialized devices to determine whether you must implement custom driver access by using the Device Access API.<br/></td>
</tr>
</tbody>
</table>



 

## Security considerations

The following articles provide guidance for writing secure C++ code:

-   [Security Best Practices for C++](http://msdn.microsoft.com/library/k3a3hzw7.aspx)
-   [Patterns & Practices Security Guidance for Applications](http://msdn.microsoft.com/library/ff650760.aspx)

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

 

 





