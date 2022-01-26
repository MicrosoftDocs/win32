---
title: UPnP APIs
description: The UPnP  framework enables dynamic networking of intelligent appliances, wireless devices, and PCs.
ms.assetid: 1dc05d6e-19ae-45e2-82c2-d3b63b16bf9d
keywords:
- UPnP
ms.topic: article
ms.date: 05/31/2018
---

# UPnP APIs

## Purpose

The UPnP  framework enables dynamic networking of intelligent appliances, wireless devices, and PCs. There are two APIs for working with UPnP-certified devices:

-   The Control Point API, which consists of a set of COM interfaces used to find and control devices.
-   The Device Host API, which consists of a set of COM interfaces used to implement devices that are hosted by a computer.

## Where applicable

The Control Point API enables developers to write applications that search for and control UPnP-certified devices. The Device Host API enables developers to implement the functionality of UPnP-certified devices, and use the device host to manage the discovery, description, control, presentation, and eventing functions of a UPnP-certified device.

## Developer audience

Developers using the Control Point APIs and Device Host APIs must be familiar with the UPnP device architecture. For more information, see the [UPnP Implementation Documentation](https://openconnectivity.org/wp-content/uploads/2017/05/upnpresources.zip) and the [UPnP Forum](https://openconnectivity.org/).

Developers who are using the Device Host APIs should be familiar with the Active Template Library (ATL) and COM interfaces.

The Control Point APIs and Device Host APIs are used by a variety of applications, from scripts embedded in HTML pages to full-fledged C++ and Microsoft Visual Basic programs.

Only the Control Point API supports Visual Basic Scripting Edition (VBScript).

## Run-time requirements

The Control Point API is used on computers running Microsoft Windows Millennium Edition, Windows XP, Windows XP Professional, and Windows CE .NET.

The Device Host API is used on computers running Windows XP, Windows XP Professional, and Windows CE .NET.

For more specific information about which operating systems support a particular function, refer to "Requirements" in the documentation.

## In this section



| Topic                                                                                          | Description                                                                                        |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [Overview of UPnP Architecture](overview-of-universal-plug-and-play.md)<br/>            | General information and background.<br/>                                                     |
| [Control Point Overview](control-point-api.md)<br/>                                     | General information about the Control Point API.<br/>                                        |
| [Using the Control Point API](using-the-control-point-api-with-upnp-technology.md)<br/> | Sample code that shows how to develop applications that control UPnP-certified devices.<br/> |
| [Control Point API Reference](control-point-api-with-upnp-technology-reference.md)<br/> | Documentation of Control Point component interfaces, methods, and events.<br/>               |
| [Device Host API Overview](device-host-api.md)<br/>                                     | General information about the Device Host API.<br/>                                          |
| [Using the Device Host API](using-the-device-host-api-with-upnp-technology.md)<br/>     | Sample code that shows how to develop an application for UPnP-certified devices.<br/>        |
| [Device Host API Reference](device-host-api-with-upnp-technology-reference.md)<br/>     | Documentation of Device Host component interfaces, methods, and events.<br/>                 |



 

 

 





