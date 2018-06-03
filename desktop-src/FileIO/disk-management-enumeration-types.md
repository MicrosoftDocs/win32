---
Description: Enumeration types used with disk management.
ms.assetid: ed8fe5c1-dbdf-43bc-a0a7-17e541eba950
title: Disk Management Enumeration Types
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Disk Management Enumeration Types

The following enumeration types are used with disk management.

## In this section



| Enumeration                                                                              | Description                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MEDIA\_TYPE**](/windows/desktop/api/WinIoCtl/)<br/>                                         | Represents the various forms of device media.<br/>                                                                                                                                                                                                                                                             |
| [**PARTITION\_STYLE**](/windows/desktop/api/WinIoCtl/)<br/>                               | Represents the format of a partition.<br/>                                                                                                                                                                                                                                                                     |
| [**STORAGE\_BUS\_TYPE**](/windows/desktop/api/WinIoCtl/)<br/>                                | Provides a symbolic means of representing storage bus types.<br/>                                                                                                                                                                                                                                              |
| [**STORAGE\_COMPONENT\_HEALTH\_STATUS**](/windows/desktop/api/WinIoCtl/ne-winioctl-_storage_component_health_status)<br/> | Specifies the health status of a storage component.<br/>                                                                                                                                                                                                                                                       |
| [**STORAGE\_DEVICE\_FORM\_FACTOR**](/windows/desktop/api/WinIoCtl/ne-winioctl-_storage_device_form_factor)<br/>           | Specifies the form factor of a device.<br/>                                                                                                                                                                                                                                                                    |
| [**STORAGE\_DEVICE\_POWER\_CAP\_UNITS**](/windows/desktop/api/winioctl/ne-winioctl-_storage_device_power_cap_units)<br/>  | The units of the maximum power threshold.<br/>                                                                                                                                                                                                                                                                 |
| [**STORAGE\_PORT\_CODE\_SET**](/windows/desktop/api/WinIoCtl/)<br/>                     | Reserved for system use. <br/>                                                                                                                                                                                                                                                                                 |
| [**STORAGE\_PROPERTY\_ID**](/windows/desktop/api/WinIoCtl/)<br/>                          | Enumerates the possible values of the **PropertyId** member of the [**STORAGE\_PROPERTY\_QUERY**](/windows/desktop/api/WinIoCtl/ns-winioctl-_storage_property_query) structure passed as input to the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_query_property) request to retrieve the properties of a storage device or adapter.<br/> |
| [**STORAGE\_PROTOCOL\_TYPE**](/windows/desktop/api/WinIoCtl/ne-winioctl-_storage_protocol_type)<br/>                      | Specifies the protocol of a storage device.<br/>                                                                                                                                                                                                                                                               |
| [**STORAGE\_QUERY\_TYPE**](/windows/desktop/api/WinIoCtl/ne-winioctl-_storage_query_type)<br/>                            | Used by the [**STORAGE\_PROPERTY\_QUERY**](/windows/desktop/api/WinIoCtl/ns-winioctl-_storage_property_query) structure passed to the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](/windows/desktop/api/WinIoCtl/ni-winioctl-ioctl_storage_query_property) control code to indicate what information is returned about a property of a storage device or adapter.<br/>                             |
| [**WRITE\_CACHE\_CHANGE**](/windows/desktop/api/WinIoCtl/)<br/>                            | Indicates whether the write cache features of a device are changeable.<br/>                                                                                                                                                                                                                                    |
| [**WRITE\_CACHE\_ENABLE**](/windows/desktop/api/WinIoCtl/)<br/>                            | Indicates whether the write cache is enabled or disabled.<br/>                                                                                                                                                                                                                                                 |
| [**WRITE\_CACHE\_TYPE**](/windows/desktop/api/WinIoCtl/)<br/>                                | Specifies the cache type.<br/>                                                                                                                                                                                                                                                                                 |
| [**WRITE\_THROUGH**](/windows/desktop/api/WinIoCtl/)<br/>                                       | Specifies whether a storage device supports write-through caching.<br/>                                                                                                                                                                                                                                        |



 

 

 




