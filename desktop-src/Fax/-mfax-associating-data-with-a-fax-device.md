---
Description: Fax extensions can associate an unlimited number of named data items with each fax device because each data item must have a GUID.
ms.assetid: 73365a3a-5adf-46bf-8e05-eba712f9b515
title: Associating Data with a Fax Device
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Associating Data with a Fax Device

Fax extensions can associate an unlimited number of named data items with each fax device because each data item must have a GUID. It is the responsibility of the extension to assign a GUID to the named data. The fax service does not generate GUIDs; the service only verifies that the GUID provided by the extension for a device has a valid GUID format.

The fax service regards device-configuration data as an opaque collection of bits. That is, the fax service stores and reads the named data, but the service does not manipulate the data.

To store named data that is associated with an entire extension (rather than named data that is associated with a particular device) you can use the special device ID zero (ID = 0). For more information, see [Storing Global Configuration Data](-mfax-storing-global-configuration-data.md) and [Device Identifier Types](-mfax-device-identifier-types.md).

Fax extensions should not access configuration data directly; rather, they should use the functions provided by the fax extension configuration mechanism. The fax service currently uses the system registry to store persistent configuration data, but this may change in future versions. For more information about how an extension can access configuration data, see [Accessing Extension Configuration Data](-mfax-accessing-extension-configuration-data.md).

 

 



