---
description: Windows Portable Devices supports the following storage properties.
ms.assetid: 234078c3-e703-41f3-9b18-ae61d8a36784
title: Storage Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Storage
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Storage Properties

Windows Portable Devices supports the following storage properties.



| Property                                   | VarType        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_STORAGE\_CAPACITY**                 | **VT\_UI8**    | The total storage capacity, in bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **WPD\_STORAGE\_CAPACITY\_IN\_OBJECTS**    | **VT\_UI8**    | Indicates the total storage capacity in objects; for example, the available slots on a SIM card.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **WPD\_STORAGE\_DESCRIPTION**              | **VT\_LPWSTR** | A human-readable description of the storage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **WPD\_STORAGE\_FILE\_SYSTEM\_TYPE**       | **VT\_LPWSTR** | A string description of the file system used by the storage, for example, "FAT32", "NTFS", "Contoso File System", and so on.                                                                                                                                                                                                                                                                                                                                                                                                         |
| **WPD\_STORAGE\_FREE\_SPACE\_IN\_BYTES**   | **VT\_UI8**    | The available storage space, in bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **WPD\_STORAGE\_FREE\_SPACE\_IN\_OBJECTS** | **VT\_UI8**    | The number of additional objects that can be written to the device. For example, if a device only allows a single object, this would be zero if the object already existed.                                                                                                                                                                                                                                                                                                                                                          |
| **WPD\_STORAGE\_SERIAL\_NUMBER**           | **VT\_LPWSTR** | A vendor-specific serial number for the storage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **WPD\_STORAGE\_MAX\_OBJECT\_SIZE**        | **VT\_UI8**    | Specifies the maximum size of a single object, in bytes, that can be placed on this storage.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **WPD\_STORAGE\_TYPE**                     | **VT\_UI4**    | Describes the physical type of a memory storage medium.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **WPD\_STORAGE\_ACCESS\_CAPABILITY**       | **VT\_UI4**    | Identifies any write-protection that globally affects this storage. This takes precedence over access specified on individual objects. Possible values are from the **WPD\_STORAGE\_ACCESS\_CAPABILITY\_VALUES** enumeration defined in PortableDevice.h. For example, if **WPD\_STORAGE\_TYPE** is ROM (that is **WPD\_STORAGE\_TYPE\_FIXED\_ROM** or **WPD\_STORAGE\_TYPE\_REMOVABLE\_ROM**), then **WPD\_STORAGE\_ACCESS\_CAPABILITY** value must be **WPD\_STORAGE\_ACCESS\_CAPABILITY\_READ\_ONLY\_WITHOUT\_OBJECT\_DELETION**. |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




