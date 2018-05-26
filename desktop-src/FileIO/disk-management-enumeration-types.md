---
Description: Enumeration types used with disk management.
ms.assetid: ed8fe5c1-dbdf-43bc-a0a7-17e541eba950
title: Disk Management Enumeration Types
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Disk Management Enumeration Types

The following enumeration types are used with disk management.

## In this section



| Enumeration                                                                              | Description                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MEDIA\_TYPE**](/windows/win32/WinIoCtl/?branch=master)<br/>                                         | Represents the various forms of device media.<br/>                                                                                                                                                                                                                                                             |
| [**PARTITION\_STYLE**](/windows/win32/WinIoCtl/?branch=master)<br/>                               | Represents the format of a partition.<br/>                                                                                                                                                                                                                                                                     |
| [**STORAGE\_BUS\_TYPE**](/windows/win32/WinIoCtl/?branch=master)<br/>                                | Provides a symbolic means of representing storage bus types.<br/>                                                                                                                                                                                                                                              |
| [**STORAGE\_COMPONENT\_HEALTH\_STATUS**](/windows/win32/WinIoCtl/ne-winioctl-_storage_component_health_status?branch=master)<br/> | Specifies the health status of a storage component.<br/>                                                                                                                                                                                                                                                       |
| [**STORAGE\_DEVICE\_FORM\_FACTOR**](/windows/win32/WinIoCtl/ne-winioctl-_storage_device_form_factor?branch=master)<br/>           | Specifies the form factor of a device.<br/>                                                                                                                                                                                                                                                                    |
| [**STORAGE\_DEVICE\_POWER\_CAP\_UNITS**](/windows/win32/winioctl/ne-winioctl-_storage_device_power_cap_units?branch=master)<br/>  | The units of the maximum power threshold.<br/>                                                                                                                                                                                                                                                                 |
| [**STORAGE\_PORT\_CODE\_SET**](/windows/win32/WinIoCtl/?branch=master)<br/>                     | Reserved for system use. <br/>                                                                                                                                                                                                                                                                                 |
| [**STORAGE\_PROPERTY\_ID**](/windows/win32/WinIoCtl/?branch=master)<br/>                          | Enumerates the possible values of the **PropertyId** member of the [**STORAGE\_PROPERTY\_QUERY**](/windows/win32/WinIoCtl/ns-winioctl-_storage_property_query?branch=master) structure passed as input to the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_query_property?branch=master) request to retrieve the properties of a storage device or adapter.<br/> |
| [**STORAGE\_PROTOCOL\_TYPE**](/windows/win32/WinIoCtl/ne-winioctl-_storage_protocol_type?branch=master)<br/>                      | Specifies the protocol of a storage device.<br/>                                                                                                                                                                                                                                                               |
| [**STORAGE\_QUERY\_TYPE**](/windows/win32/WinIoCtl/ne-winioctl-_storage_query_type?branch=master)<br/>                            | Used by the [**STORAGE\_PROPERTY\_QUERY**](/windows/win32/WinIoCtl/ns-winioctl-_storage_property_query?branch=master) structure passed to the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_storage_query_property?branch=master) control code to indicate what information is returned about a property of a storage device or adapter.<br/>                             |
| [**WRITE\_CACHE\_CHANGE**](/windows/win32/WinIoCtl/?branch=master)<br/>                            | Indicates whether the write cache features of a device are changeable.<br/>                                                                                                                                                                                                                                    |
| [**WRITE\_CACHE\_ENABLE**](/windows/win32/WinIoCtl/?branch=master)<br/>                            | Indicates whether the write cache is enabled or disabled.<br/>                                                                                                                                                                                                                                                 |
| [**WRITE\_CACHE\_TYPE**](/windows/win32/WinIoCtl/?branch=master)<br/>                                | Specifies the cache type.<br/>                                                                                                                                                                                                                                                                                 |
| [**WRITE\_THROUGH**](/windows/win32/WinIoCtl/?branch=master)<br/>                                       | Specifies whether a storage device supports write-through caching.<br/>                                                                                                                                                                                                                                        |



 

 

 




