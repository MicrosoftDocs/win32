---
title: IOCTL\_MOUNTMGR\_DELETE\_POINTS\_DBONLY control code
description: This IOCTL is identical in input and output to IOCTL\_MOUNTMGR\_QUERY\_POINTS.
ms.assetid: '507e42a0-e5f6-4864-a665-d06eb4d1a77b'
keywords: ["IOCTL_MOUNTMGR_DELETE_POINTS_DBONLY control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_MOUNTMGR_DELETE_POINTS_DBONLY
api_location:
- Mountmgr.h
api_type:
- HeaderDef
---

# IOCTL\_MOUNTMGR\_DELETE\_POINTS\_DBONLY control code

This IOCTL is identical in input and output to [**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md). The difference is that **IOCTL\_MOUNTMGR\_DELETE\_POINTS\_DBONLY** has the side effect of deleting the mount manager database entries for the triples returned. However, the mount manager does not delete the symbolic links corresponding to the database entries.

If the input to this IOCTL is ("\\DosDevices\\X:", **NULL**, **NULL**), where X is the current drive letter for the volume indicated in the input triple, the mount manager adds a special entry to its database indicating that the client does not require a drive letter. On subsequent reboots, the mount manager will not assign a default drive letter to the volume.

## Input Buffer

See [**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md).

## Input Buffer Length

See [**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md).

## Output Buffer

See [**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md).

## Output Buffer Length

See [**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md).

## Status block

See [**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mountmgr.h (include Mountmgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_MOUNTMGR\_QUERY\_POINTS**](ioctl-mountmgr-query-points.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_MOUNTMGR_DELETE_POINTS_DBONLY%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






