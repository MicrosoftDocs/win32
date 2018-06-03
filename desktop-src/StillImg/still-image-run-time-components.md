---
title: Still Image Run-Time Components
description: The STI system is composed of two run-time components
ms.assetid: 084ad33d-fee6-4cad-9402-4b81120b629b
keywords:
- architecture,STI run-time components
- STI architecture,run-time components
- Still Image (STI),run-time components
- STI (Still Image),run-time components
- Still Image API,run-time components
- still images,run-time components
- Still Image (STI),Event Monitor
- STI (Still Image),Event Monitor
- Still Image (STI),Control Panel
- STI (Still Image),Control Panel
- still images,Still Image Event Monitor
- still images,Still Image Control Panel
- Still Image Event Monitor
- Still Image Control Panel
- Still Image API,Event Monitor
- Still Image API,Control Panel
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Still Image Run-Time Components

The STI system is composed of two run-time components:

-   [Still Image Event Monitor](#still-image-event-monitor)
-   [Still Image Control Panel](#still-image-control-panel)

The STI architecture components provide the following services for use by the Still Image Control Panel, the Still Image Event Monitor, and applications that use Still Image:

-   Maintain the event types that are associated with devices. These events are identified by the IHV as push events for their device.
-   Dispatch push events to the Event Monitor.
-   Maintain a list of all push model-aware applications that use the push model.
-   Launch or notify an application on behalf of the Event Monitor and provide information to the application as to which device and event initiated the notification.

## Still Image Event Monitor

The Event Monitor maintains a list of active push model devices. Devices have a capability that indicates they support push model events. When devices are installed or removed, they can be added to or deleted from the Event Monitor's device list using Plug and Play messages. They can also be added or deleted by the Add Hardware Wizard.

The Event Monitor opens all devices that support the push model in control mode. Since the Event Monitor should be the only component receiving push model events, it is the only component able to open the devices in control mode. Other software, such as application programs, can open the devices in data mode. When a device is opened in data mode, it is functioning under the pull model of data acquisition. The Event Monitor does not place a restriction on the number of programs that open a device in data mode.

For all devices that support the push model of image data acquisition, the Event Monitor waits for events. For each older device that only supports the pull model, the Event Monitor creates a separate thread. Each thread simulates push model behavior by polling the device and generating a push event when the device becomes active.

In addition, the Event Monitor implements a specific policy for how device push events are interpreted. It uses the list of applications that use the push model , and the list of those applications that are running.

It also maintains a list of device events that are associated with applications. The user creates the list that associates device events and applications with the **Still Image Control Panel**. Registering an application as one that utilizes the push model using the [**RegisterLaunchAppliction**](istillimage-registerlaunchapplication.md) method does not connect it with particular device events. The user must create the association between a device event and an application with the Control Panel. If this is not done, the application does not receive push events from a device.

When the device event occurs, the Event Monitor launches the application associated with that device event. The application is launched with arguments of **Event:event\_name** and **Device:STI\_device\_friendly\_name** on the command line. However, the application does not parse these arguments. Instead, it invokes a method called [**GetSTILaunchInformation**](istillimage-getstilaunchinformation.md) that returns the device event and the device-friendly name.

The Event Monitor uses the following simple policy to dispatch device events:

-   Upon receiving a device event, the Event Monitor obtains the subset of all registered applications the user has selected to respond to this device event. This list is referred to as PREFERREDAPPS. The Event Monitor maintains this information.
-   If there are PREFERREDAPPS selected for this device event and PREFERREDAPPS has only one item, it is launched. Otherwise, a dialog box that contains PREFERREDAPPS is displayed and you select the application to be launched.
-   Otherwise, the user is informed that no application is associated with the event. If this is the case, the device has been disabled for push model behavior.

## Still Image Control Panel

The STI Control Panel provides you with a common interface that directs some of the behavior of the Event Monitor. This includes:

**Enumerate devices:** Lists the installed still-image devices.

**Add or remove devices:** Still-image devices can be added or removed.

**Test devices:** Allows verification of still-image device installation and operation.

**Configure or control devices:** For each device, the Event Monitor adds a Microsoft or vendor property sheet to the Control Panel. The property sheet allows you to alter the behavior of the Event Monitor.

**Associate device events with applications:** Using the Control Panel, you select a device and one of the push model events for this device. You then select the subset of applications that use the push model to which the event will be directed with this device and event pair. In this way, the Control Panel is used to associate device events with applications.

Application programs must not have to access the STI Control Panel. When an image acquisition device is installed, a property page for the device is added to the control panel. The property page is supplied by the vendor. Use it to manually associate device events with applications.

 

 




