---
title: TAPE\_PREPARE structure
description: The TAPE\_PREPARE structure is used in conjunction with the IOCTL\_TAPE\_PREPARE request to load or unload tape, reset the tape's tension, lock or unlock the ejection mechanism, or format the tape.
ms.assetid: '0e016f3a-4f3a-4256-bb7b-10a5f955b930'
keywords: ["TAPE_PREPARE structure Storage Devices", "PTAPE_PREPARE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- TAPE_PREPARE
api_location:
- ntddtape.h
api_type:
- HeaderDef
---

# TAPE\_PREPARE structure

The TAPE\_PREPARE structure is used in conjunction with the [**IOCTL\_TAPE\_PREPARE**](ioctl-tape-prepare.md) request to load or unload tape, reset the tape's tension, lock or unlock the ejection mechanism, or format the tape.

## Syntax


```C++
typedef struct _TAPE_PREPARE {
  ULONG   Operation;
  BOOLEAN Immediate;
} TAPE_PREPARE, *PTAPE_PREPARE;
```



## Members

<dl> <dt>

**Operation**
</dt> <dd>

Indicates the type of operation to perform. This member can be one of the following:



| Operation                | Meaning                                                                                                                                                                                                                  |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TAPE\_LOAD<br/>    | Loads the tape and moves the tape to the beginning. <br/>                                                                                                                                                          |
| TAPE\_UNLOAD<br/>  | Moves the tape to the beginning for removal from the device. After a successful unload operation, the device returns errors to applications that attempt to access the tape, until the tape is loaded again. <br/> |
| TAPE\_TENSION<br/> | Adjusts the tension by moving the tape to the end of the tape and back to the beginning. This option is not supported by all devices. This value is ignored if it is not supported.<br/>                           |
| TAPE\_LOCK<br/>    | Locks the tape ejection mechanism, so that the tape is not ejected accidentally. <br/>                                                                                                                             |
| TAPE\_UNLOCK<br/>  | Unlocks the tape ejection mechanism. <br/>                                                                                                                                                                         |
| TAPE\_FORMAT<br/>  | Performs a low-level format of the tape. Not all devices support this feature. This value is ignored if it is not supported.<br/>                                                                                  |



 

</dd> <dt>

**Immediate**
</dt> <dd>

When set to **TRUE**, indicates that the target device should return status immediately. When set to **FALSE**, indicates that the device should return status after the operation is complete.

</dd> </dl>

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Ntddtape.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_TAPE\_PREPARE**](ioctl-tape-prepare.md)
</dt> <dt>

[**TapeMiniPrepare**](https://msdn.microsoft.com/library/windows/hardware/ff567950)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_PREPARE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






