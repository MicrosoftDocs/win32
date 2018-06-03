---
title: IOCTL\_EHSTOR\_DEVICE\_GET\_QUEUE\_STATE control code
description: The IOCTL\_EHSTOR\_DEVICE\_GET\_QUEUE\_STATE request is sent by silo drivers and applications to determine the state of a storage device queue.
ms.assetid: 1BF7E7B3-26CF-41BB-B2E9-8EDC6872CF34
keywords:
- IOCTL_EHSTOR_DEVICE_GET_QUEUE_STATE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_DEVICE_GET_QUEUE_STATE
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

# IOCTL\_EHSTOR\_DEVICE\_GET\_QUEUE\_STATE control code

The **IOCTL\_EHSTOR\_DEVICE\_GET\_QUEUE\_STATE** request is sent by silo drivers and applications to determine the state of a storage device queue. IO requests in the storage device queue are held when the device is temporarily unauthorized. A storage device may become temporarily unauthorized in low power states or when there is a policy that requires locking Enhanced Storage devices such as when the user session is locked.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The output buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains an **ACT\_QUEUE\_STATE** structure. **ACT\_QUEUE\_STATE** is declared in *ehstorioctl.h* as the following.


```
typedef struct tagACT_QUEUE_STATE
{
    BOOLEAN fFrozen;
} ACT_QUEUE_STATE;
```



<dl> <dt>

<span id="fFrozen"></span><span id="ffrozen"></span><span id="FFROZEN"></span>fFrozen
</dt> <dd>

The freeze state of the IO request queue for a storage device. If set to TRUE, the queue is frozen and all IO requests sent to the storage device are held. Otherwise, IO requests in the device queue are processed.

</dd> </dl>

## Output Buffer Length

The length of an **ACT\_QUEUE\_STATE** structure.

## Status block

One of the following values can be returned in the **Status** field.



| Status Value               | Description                                |
|----------------------------|--------------------------------------------|
| STATUS\_SUCCESS            | The queue state was returned successfully. |
| STATUS\_BUFFER\_TOO\_SMALL | The output buffer length is too small.     |



 

## Requirements



|                    |                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                     |
| Header<br/>  | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_DEVICE\_SET\_QUEUE\_STATE**](ioctl-ehstor-device-set-queue-state.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_DEVICE_GET_QUEUE_STATE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






