---
title: IOCTL\_EHSTOR\_TCGDRV\_RELINQUISH\_SILO control code
description: The IOCTL\_EHSTOR\_TCGDRV\_RELINQUISH\_SILO request relinquishes control of band management by the Trusted Computing Group (TCG) Storage Silo driver.
ms.assetid: '4D3DA81A-D79A-4299-A743-AFB0118DDF3F'
keywords: ["IOCTL_EHSTOR_TCGDRV_RELINQUISH_SILO control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_TCGDRV_RELINQUISH_SILO
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
---

# IOCTL\_EHSTOR\_TCGDRV\_RELINQUISH\_SILO control code

The **IOCTL\_EHSTOR\_TCGDRV\_RELINQUISH\_SILO** request relinquishes control of band management by the Trusted Computing Group (TCG) Storage Silo driver. Applications issue this request to manage a storage silo directly. The band management functionality and API provided by the TCG Storage Silo driver are disabled.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

On return, the **Status** field will contain STATUS\_SUCCESS if the operation was successful. Otherwise, another appropriate status code is returned.

## Remarks

When the TCG Storage Silo driver relinquishes control, all band management IOCTLs registered by an [**IOCTL\_EHSTOR\_DRIVER\_REPORT\_CAPABILITIES**](ioctl-ehstor-driver-report-capabilities.md) request are unregistered. Any band management IOCTL requests received are returned with STATUS\_INVALID\_DEVICE\_REQUEST.

After relinquishing control, the TCG Storage Silo driver can regain control of a storage device when the device is stopped and restarted.

To prevent the TCG Storage Silo driver from reconfiguring the TCG subsystem in a mode compatible with Windows after restart, the SID credential should be changed to a nondefault value or SID authority should be disabled. This will also allow direct management of a storage silo.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_DRIVER\_REPORT\_CAPABILITIES**](ioctl-ehstor-driver-report-capabilities.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_TCGDRV_RELINQUISH_SILO%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






