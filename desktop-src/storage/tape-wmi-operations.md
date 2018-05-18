---
title: TAPE\_WMI\_OPERATIONS structure
description: The tape miniclass driver passes this structure to its TapeMiniWMIControl routine to indicate which WMI operation must be performed by the device.
ms.assetid: '430d982e-4740-46ad-8391-aba5813a833a'
keywords: ["TAPE_WMI_OPERATIONS structure Storage Devices", "PTAPE_WMI_OPERATIONS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- TAPE_WMI_OPERATIONS
api_location:
- ntddtape.h
api_type:
- HeaderDef
---

# TAPE\_WMI\_OPERATIONS structure

The tape miniclass driver passes this structure to its [*TapeMiniWMIControl*](https://msdn.microsoft.com/library/windows/hardware/ff567957) routine to indicate which WMI operation must be performed by the device.

## Syntax


```C++
typedef struct _TAPE_WMI_OPERATIONS {
  ULONG Method;
  ULONG DataBufferSize;
  PVOID DataBuffer;
} TAPE_WMI_OPERATIONS, *PTAPE_WMI_OPERATIONS;
```



## Members

<dl> <dt>

**Method**
</dt> <dd>

Indicates the operation to be performed by the tape device. The operations allowed are as follows:

<dl> <dt>

<span id="TAPE_CHECK_FOR_DRIVE_PROBLEM"></span><span id="tape_check_for_drive_problem"></span>TAPE\_CHECK\_FOR\_DRIVE\_PROBLEM
</dt> <dd>

If the tape drive supports commands to return specific device errors, such as tape alerts, the minidriver's [*TapeMiniWMIControl*](https://msdn.microsoft.com/library/windows/hardware/ff567957) routine should execute the TAPE\_QUERY\_DEVICE\_ERROR\_DATA method Otherwise, it should execute the TAPE\_QUERY\_IO\_ERROR\_DATA method.

</dd> </dl>

<dl> <dt>

<span id="TAPE_QUERY_DEVICE_ERROR_DATA"></span><span id="tape_query_device_error_data"></span>TAPE\_QUERY\_DEVICE\_ERROR\_DATA
</dt> <dd>

Returns specific device errors, such as tape alerts. Not all tape drives support this method.

</dd> </dl>

<dl> <dt>

<span id="TAPE_QUERY_IO_ERROR_DATA__"></span><span id="tape_query_io_error_data__"></span>TAPE\_QUERY\_IO\_ERROR\_DATA 
</dt> <dd>

Returns general I/O error data, such as read/write errors, based on the I/O error count. All tape drives support this method.

</dd> </dl> </dd> <dt>

**DataBufferSize**
</dt> <dd>

Indicates the size in bytes of the buffer in which the tape minidriver returns the results of the operation.

</dd> <dt>

**DataBuffer**
</dt> <dd>

Pointer to a buffer in which the tape minidriver returns the results of the operation. The first **sizeof**(ULONG) bytes of **DataBuffer** contain a value of type [**TAPE\_DRIVE\_PROBLEM\_TYPE**](tape-drive-problem-type.md), followed by **DataBufferSize** - **sizeof**(ULONG) bytes of tape data.

</dd> </dl>

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddchgr.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[*TapeMiniWMIControl*](https://msdn.microsoft.com/library/windows/hardware/ff567957)
</dt> <dt>

[**TAPE\_DRIVE\_PROBLEM\_TYPE**](tape-drive-problem-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_WMI_OPERATIONS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






