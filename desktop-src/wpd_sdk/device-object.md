---
Description: Device Object
ms.assetid: 0d403a6e-c22e-4b77-9be4-b8d53092f279
title: Device Object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Device Object

The device object supports the following properties. An application can request these properties by querying the root object (specifying the defined **WPD\_DEVICE\_OBJECT\_ID** constant object ID). All values of the device object are read-only.

If a given device implements the [WPD\_FUNCTIONAL\_CATEGORY\_DEVICE](wpd-functional-category-device.md) category, it must also support the properties associated with that category.



| Property Name                                                                                                         | Required or Optional                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_ID)                                                                | Required. The value is **WPD\_DEVICE\_OBJECT\_ID**.                                                         |
| [WPD\_OBJECT\_PARENT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PARENT\_ID)                                                 | Required. The value is an empty string.                                                                     |
| [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                                                            | Required if the object represents a file.                                                                   |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID)                          | Required.                                                                                                   |
| [WPD\_OBJECT\_ISHIDDEN](https://www.bing.com/search?q=WPD\_OBJECT\_ISHIDDEN)                                                    | Required if the device object should not be shown to the user.                                              |
| [WPD\_OBJECT\_REFERENCES](https://www.bing.com/search?q=WPD\_OBJECT\_REFERENCES)                                                | Required if the device object has references to other objects.                                              |
| [WPD\_OBJECT\_KEYWORDS](https://www.bing.com/search?q=WPD\_OBJECT\_KEYWORDS)                                                    | Optional.                                                                                                   |
| [WPD\_OBJECT\_SYNC\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_SYNC\_ID)                                                     | Optional.                                                                                                   |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](https://www.bing.com/search?q=WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE) | Optional.                                                                                                   |
| [WPD\_DEVICE\_SYNC\_PARTNER](https://www.bing.com/search?q=WPD\_DEVICE\_SYNC\_PARTNER)                                           | Optional.                                                                                                   |
| [WPD\_DEVICE\_FIRMWARE\_VERSION](https://www.bing.com/search?q=WPD\_DEVICE\_FIRMWARE\_VERSION)                                   | Required.                                                                                                   |
| [WPD\_DEVICE\_POWER\_LEVEL](https://www.bing.com/search?q=WPD\_DEVICE\_POWER\_LEVEL)                                             | Recommended if the device has a battery.                                                                    |
| [WPD\_DEVICE\_POWER\_SOURCE](https://www.bing.com/search?q=WPD\_DEVICE\_POWER\_SOURCE)                                           | Recommended.                                                                                                |
| [WPD\_DEVICE\_PROTOCOL](https://www.bing.com/search?q=WPD\_DEVICE\_PROTOCOL)                                                    | Recommended.                                                                                                |
| [WPD\_DEVICE\_MANUFACTURER](https://www.bing.com/search?q=WPD\_DEVICE\_MANUFACTURER)                                            | Required.                                                                                                   |
| [WPD\_DEVICE\_MODEL](https://www.bing.com/search?q=WPD\_DEVICE\_MODEL)                                                          | Required.                                                                                                   |
| [WPD\_DEVICE\_SERIAL\_NUMBER](https://www.bing.com/search?q=WPD\_DEVICE\_SERIAL\_NUMBER)                                         | Required.                                                                                                   |
| [WPD\_DEVICE\_SUPPORTS\_NON\_CONSUMABLE](https://www.bing.com/search?q=WPD\_DEVICE\_SUPPORTS\_NON\_CONSUMABLE)                    | Required if the device supports non-consumable objects; that is, if it can be used for simple data storage. |
| [WPD\_DEVICE\_DATETIME](https://www.bing.com/search?q=WPD\_DEVICE\_DATETIME)                                                    | Optional.                                                                                                   |
| [WPD\_DEVICE\_FRIENDLY\_NAME](https://www.bing.com/search?q=WPD\_DEVICE\_FRIENDLY\_NAME)                                         | Recommended.                                                                                                |
| [WPD\_DEVICE\_SUPPORTED\_DRM\_SCHEME](https://www.bing.com/search?q=WPD\_DEVICE\_SUPPORTED\_DRM\_SCHEME)                          | Recommended if the device supports Digital Rights Management (DRM).                                         |
| [WPD\_DEVICE\_SUPPORTED\_FORMATS\_ARE\_ORDERED](https://www.bing.com/search?q=WPD\_DEVICE\_SUPPORTED\_FORMATS\_ARE\_ORDERED)       | Recommended if the device supports preferred format ordering.                                               |
| [WPD\_DEVICE\_TYPE](https://www.bing.com/search?q=WPD\_DEVICE\_TYPE)                                                            | Recommended.                                                                                                |
| [WPD\_DEVICE\_FUNCTIONAL\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_DEVICE\_FUNCTIONAL\_UNIQUE\_ID)                          | Optional.                                                                                                   |
| [WPD\_DEVICE\_MODEL\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_DEVICE\_MODEL\_UNIQUE\_ID)                                    | Optional.                                                                                                   |
| [WPD\_DEVICE\_TRANSPORT](https://www.bing.com/search?q=WPD\_DEVICE\_TRANSPORT)                                                  | Recommended.                                                                                                |
| [WPD\_DEVICE\_USE\_DEVICE\_STAGE](https://www.bing.com/search?q=WPD\_DEVICE\_USE\_DEVICE\_STAGE)                                  | Optional.                                                                                                   |
| [WPD\_FUNCTIONAL\_OBJECT\_CATEGORY](https://www.bing.com/search?q=WPD\_FUNCTIONAL\_OBJECT\_CATEGORY)                             | Required.                                                                                                   |



 

## Typical Resources

These objects typically do not host resources.

## Commands

In addition to properties, devices should support a specific set of commands defined by Windows Portable Devices. What commands an object or device supports depends on its type, functionality, and capabilities.

The following table describes the command classes that apply to devices, by functionality. Typically, a device falls under several categories, and it should support the commands for all applicable categories. For example, a mobile phone with a camera would fall under three categories: all devices, SMS devices, and still image capture devices. A custom driver and client application can support additional commands or properties that you define, but must support the following commands. For a description of the specific commands that fall under each command category, see [Commands](commands.md).



| Description                                                                                                                                                                                                                      | Command categories                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All devices.                                                                                                                                                                                                                     | **WPD\_CATEGORY\_CAPABILITIESWPD\_CATEGORY\_COMMON**<br/> **WPD\_CATEGORY\_OBJECT\_ENUMERATION**<br/> **WPD\_CATEGORY\_OBJECT\_MANAGEMENT**<br/> **WPD\_CATEGORY\_OBJECT\_PROPERTIES**<br/> **WPD\_CATEGORY\_OBJECT\_PROPERTIES\_BULK**<br/> **WPD\_CATEGORY\_OBJECT\_RESOURCES**<br/> |
| Devices that can capture still images, such as digital cameras.                                                                                                                                                                  | **WPD\_CATEGORY\_STILL\_IMAGE\_CAPTURE**                                                                                                                                                                                                                                                                                   |
| Devices that can send short message service (SMS) messages, such as cellular phones. Sending SMS messages is often called "text messaging".                                                                                      | **WPD\_CATEGORY\_SMS**                                                                                                                                                                                                                                                                                                     |
| Devices that function as storage devices. These include external drives.If a device supports the ability to format a store or to move objects from one location to another, your driver should support this category.<br/> | **WPD\_CATEGORY\_STORAGE**                                                                                                                                                                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 




