---
title: IOCTL\_EHSTOR\_DEVICE\_SET\_QUEUE\_STATE control code
description: The IOCTL\_EHSTOR\_DEVICE\_SET\_QUEUE\_STATE request is sent by silo drivers and applications to change the state of a storage device queue. IO requests in the storage device queue are held when the device is temporarily unauthorized.
ms.assetid: '83AFAC73-39B8-442A-822E-411D08130F88'
keywords: ["IOCTL_EHSTOR_DEVICE_SET_QUEUE_STATE control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_DEVICE_SET_QUEUE_STATE
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
---

# IOCTL\_EHSTOR\_DEVICE\_SET\_QUEUE\_STATE control code

The **IOCTL\_EHSTOR\_DEVICE\_SET\_QUEUE\_STATE** request is sent by silo drivers and applications to change the state of a storage device queue. IO requests in the storage device queue are held when the device is temporarily unauthorized.

## Input Buffer

The input buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains an **ACT\_QUEUE\_STATE** structure. **ACT\_QUEUE\_STATE** is declared in *ehstorioctl.h* as the following.


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

## Input Buffer Length

The length of an **ACT\_QUEUE\_STATE** structure.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

One of the following values can be returned in the **Status** field.



| Status Value                  | Description                                        |
|-------------------------------|----------------------------------------------------|
| STATUS\_SUCCESS               | The queue state was changed successfully.          |
| STATUS\_INVALID\_BUFFER\_SIZE | The input buffer length is too small.              |
| STATUS\_ACCESS\_DENIED        | The IOCTL request was not issued by a silo driver. |



 

## Remarks

Silo drivers or applications can freeze the storage device IO request queue if temporary unauthorization is needed. Normally, temporary unauthorization occurs during low power states or when a policy requires locking of Enhanced Storage devices such as a locked user session. In such a case, it is preferable to put pending IO requests on hold rather than fail the IO requests and cause data loss.

To prevent abuse of the **IOCTL\_EHSTOR\_DEVICE\_SET\_QUEUE\_STATE** request by applications, only a driver can issue this IOCTL. If sent from a user mode application, this request will fail with STATUS\_ACCESS\_DENIED.

## Requirements



|                    |                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                     |
| Header<br/>  | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_DEVICE\_GET\_QUEUE\_STATE**](ioctl-ehstor-device-get-queue-state.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_DEVICE_SET_QUEUE_STATE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






