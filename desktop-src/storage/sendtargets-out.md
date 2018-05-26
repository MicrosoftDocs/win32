---
title: SendTargets\_OUT structure
description: The SendTargets\_OUT structure holds the output data for the SendTargets method.
ms.assetid: 82efeeb9-1167-4114-9d88-7ef66f613f80
keywords:
- SendTargets_OUT structure Storage Devices
- PSendTargets_OUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SendTargets_OUT
api_location:
- iscsiop.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SendTargets\_OUT structure

The SendTargets\_OUT structure holds the output data for the [SendTargets](https://msdn.microsoft.com/library/windows/hardware/ff565526) method.

## Syntax


```C++
typedef struct _SendTargets_OUT {
  ULONG Status;
  ULONG ResponseSize;
  UCHAR Response[1];
} SendTargets_OUT, *PSendTargets_OUT;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

The status of the **SendTargets** method. This member will contain 0 if the SEND TARGETS operation succeeds and ISDSC\_SCSI\_REQUEST\_FAILED if the operation fails. If the SEND TARGETS operation fails, **ScsiStatus** will contain the SCSI status of the SCSI command. SCSI status qualifiers are documented in the *SCSI Primary Commands* specification. For a list of status qualifiers, see [ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568).

</dd> <dt>

**ResponseSize**
</dt> <dd>

The size, in bytes, of the buffer at Response.

</dd> <dt>

**Response**
</dt> <dd>

A buffer that holds the response data that the target returns. Response to SendTargets in UTF8 characters. NOTE: This field is a variable length array.

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568)
</dt> <dt>

[SendTargets](https://msdn.microsoft.com/library/windows/hardware/ff565526)
</dt> <dt>

[**SendTargets\_IN**](sendtargets-in.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SendTargets_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






