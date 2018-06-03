---
title: IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE control code
description: This IOCTL is used to inform the enhanced storage (EHSTOR) class driver of changes to the LBA filter table.
ms.assetid: 295EE3CC-4244-4411-9684-7C5D38B10EA9
keywords:
- IOCTL_EHSTOR_DRIVER_UPDATE_LBA_FILTER_TABLE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_DRIVER_UPDATE_LBA_FILTER_TABLE
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE control code

This IOCTL is used to inform the enhanced storage (EHSTOR) class driver of changes to the LBA filter table. Bands managed by the silo driver are composed of LBA ranges. The silo driver notifies the EHSTOR class driver of updates to the set of bands it controls with this IOCTL.

## Input Buffer

The input buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** must contain a structure of type [**LBA\_FILTER\_TABLE**](lba-filter-table.md). This structure contains the filter table and the total entries it contains. An array [**LBA\_FILTER\_TABLE\_ENTRY**](lba-filter-table-entry.md) structure follows **LBA\_FILTER\_TABLE**.

## Input Buffer Length

The length of the buffer.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

One of the following values can be returned in the **Status** field.



| Status Value                    | Description                                                          |
|---------------------------------|----------------------------------------------------------------------|
| STATUS\_SUCCESS                 | The LBA filter table was successfully updated.                       |
| STATUS\_INVALID\_BUFFER\_SIZE   | The input buffer length supplied is of incorrect size.               |
| STATUS\_INVALID\_PARAMETER      | The LBA filter count or an LBA range is specified incorrectly.       |
| STATUS\_INSUFFICIENT\_RESOURCES | The IOCTL redirection list cannot be copied.                         |
| STATUS\_NOT\_SUPPORTED          | The sending device is not a silo device or banding is not supported. |



 

## Remarks

The LBA filters cannot overlap or be empty. The LBA filters do not have to be sorted in any way. If an LBA range is being unlocked, an **IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE** request should be sent after the LBA range is unlocked on the storage device. Also, if an LBA range is currently being locked, **IOCTL\_EHSTOR\_DRIVER\_UPDATE\_LBA\_FILTER\_TABLE** must be sent before the LBA range has been locked on the storage device.

## Requirements



|                    |                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                     |
| Header<br/>  | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**LBA\_FILTER\_TABLE**](lba-filter-table.md)
</dt> <dt>

[**LBA\_FILTER\_TABLE\_ENTRY**](lba-filter-table-entry.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_DRIVER_UPDATE_LBA_FILTER_TABLE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






