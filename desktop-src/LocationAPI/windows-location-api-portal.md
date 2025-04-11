---
description: Location API
ms.assetid: 0182461a-df06-46ea-a9c2-7aedbde5033b
title: Location API
ms.topic: concept-article
ms.date: 08/28/2024
---

# Location API

> [!IMPORTANT]
> This documentation is for the Win32/COM Location API. It's available for use in the operating systems (OSes) that are specified in the Requirements section of each individual API reference topic. This API might be altered or unavailable in later OS versions. So we recommend that you use the Windows Runtime [**Windows.Devices.Geolocation**](/uwp/api/Windows.Devices.Geolocation) API instead. To access location from a website, you can use the W3C Geolocation API (see [Introduction to the Geolocation API](/previous-versions/windows/internet-explorer/ie-developer/samples/gg589513(v=vs.85))).

## Purpose

Computers today are more mobile than ever. From small laptops to Tablet PCs, many computers can go wherever the user wants to go. Programs that take advantage of the computer's mobility can add significant value to people's lives. For example, a program that can find nearby restaurants and provide driving directions would seem to be a natural fit for a portable computer. But while the technology to determine the user's current location is common and affordable, building solutions on this technology can be a daunting task.

To create a location-aware program, you might need to overcome a variety of issues, including:

-   Global positioning system (GPS) devices that use virtual COM ports, which provide access for only one program at a time.
-   Understanding and programming for protocols, such as the National Marine Electronics Association (NMEA) specification, as well as proprietary vendor extensions.
-   Being confined to programming for known, vertical hardware solutions.
-   Implementing logic to handle transitions between various location providers, such as GPS receivers, connected networks, cellular telephone networks, the Internet, and user settings.

This documentation describes the Windows Location application programming interface (API). The Location API helps to simplify location-aware programming by providing a standard way to retrieve data about user location and standardizing formats for location data reports. The Location API automatically handles transitions between location data providers and always chooses the most accurate provider for the current situation.

## Developer audience

The Location API provides its functionality through a set of COM interfaces. Location API functionality can be used by programmers who are familiar with using COM through the C++ programming language, or with using COM objects in scripting languages, such as Microsoft JScript.

## In this section

* [Location API C++ programming reference](./windows-location-programming-reference.md)
* [Location API object model reference](./windows-location-script-programming-reference.md)
