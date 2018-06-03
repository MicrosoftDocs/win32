---
title: WPD Automation Object Model
description: The WPD Automation object model consists of objects that enable developers to work with a subset of the Windows Portable Devices (WPD) API.
ms.assetid: 0d8cc8ec-197b-4439-814a-0a39c0eb5f94
keywords:
- WPD Automation,object model
- WPD Automation,JScript
- WPD Automation,COM Automation
- Windows Portable Devices (WPD),WPD Automation object model
- WPD (Windows Portable Devices),WPD Automation object model
- Windows Portable Devices (WPD),WPD Automation
- WPD (Windows Portable Devices),WPD Automation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPD Automation Object Model

The WPD Automation object model consists of objects that enable developers to work with a subset of the Windows Portable Devices (WPD) API. Using WPD Automation, developers can write applications using JScript, to access the services and storages on a device.

WPD Automation is built on [Windows Portable Devices (WPD)](http://msdn.microsoft.com/library/ms740786(VS.85).aspx), a technology that enables computers to communicate with attached media and storage devices. WPD Automation uses COM Automation to provide programmatic access to WPD devices through JScript.

COM Automation (formerly called OLE Automation) is a technology that enables software packages to expose their unique features to scripting tools and other applications. This makes it possible for one application to manipulate objects implemented in another application, or to expose objects so they can be manipulated. For more information about COM Automation, see the [MFC Library Reference for Automation](http://go.microsoft.com/fwlink/p/?linkid=130619) and the [Automation Programming Reference](http://go.microsoft.com/fwlink/p/?linkid=130620).

WPD Automation programs are Web applications. Typically, a WPD Automation program uses JScript in conjunction with a scripting host to access a device and discover its capabilities, storages, and services. The program then interacts with the device to update data, or to display data using HTML. For example, a WPD Automation program could interact with a Web Service to enable customers to buy a ringtone and add it to a phone. Other examples might be applications that check a device for problems, or help a customer use a feature on the device.

> [!Note]  
> For Windows 7, the primary scripting language supported by WPD Automation is JScript 5.6. Other scripting languages, such as VBScript or JScript.NET, are not supported.

 

The WPD Automation object model documentation is presented in the following sections.



| Section                                                                            | Description                                                                                    |
|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [About the WPD Automation Object Model](about-the-wpd-automation-object-model.md) | Discusses the architecture of the WPD Automation object model.                                 |
| [WPD Automation Programming Guide](wpd-automation-programming-guide.md)           | Provides information about using WPD Automation objects in a variety of programming scenarios. |
| [WPD Automation Reference](wpd-automation-reference.md)                           | Provides reference pages for the WPD Automation objects, methods, properties, and events.      |



 

## Related topics

<dl> <dt>

[Windows Portable Devices](https://www.bing.com/search?q=Windows Portable Devices)
</dt> </dl>

 

 




