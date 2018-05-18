---
Description: 'When a fax device has been added or removed from the fax server, or when a new fax device has been installed, the fax service calls the FaxRouteDeviceChangeNotification function to notify the fax routing extension.'
ms.assetid: '59e5a4cd-d824-4f1d-bbca-e43857de844c'
title: Managing Fax Devices
---

# Managing Fax Devices

When a fax device has been added or removed from the fax server, or when a new fax device has been installed, the fax service calls the [**FaxRouteDeviceChangeNotification**](-mfax-faxroutedevicechangenotification.md) function to notify the fax routing extension. The extension should perform required initialization procedures or cleanup routines at this time.

A call to the [**FaxRouteDeviceEnable**](-mfax-faxroutedeviceenable.md) function can enable or disable a specified fax routing method on a particular fax device. The function also allows a fax routing extension to query the status of a routing method on a fax device.

A fax routing extension must export the [**FaxRouteDeviceChangeNotification**](-mfax-faxroutedevicechangenotification.md) and [**FaxRouteDeviceEnable**](-mfax-faxroutedeviceenable.md) functions.

Because fax routing extensions cannot enumerate the available fax devices on a fax server, it is recommended that extensions create an empty device table. The extension can add device information to the table when one of the functions it exports receives a new fax device ID.

 

 



