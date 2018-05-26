---
title: SUB\_Q\_HEADER structure
description: The SUB\_Q\_HEADER structure contains audio status information and the length of the Q subchannel data being returned. This structure is used in conjunction with SUB\_Q\_CHANNEL\_DATA.
ms.assetid: 3ee3657d-acdd-4d3f-9cff-eb4a494429b4
keywords:
- SUB_Q_HEADER structure Storage Devices
- PSUB_Q_HEADER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SUB_Q_HEADER
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SUB\_Q\_HEADER structure

The SUB\_Q\_HEADER structure contains audio status information and the length of the Q subchannel data being returned. This structure is used in conjunction with [**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md).

## Syntax


```C++
typedef struct _SUB_Q_HEADER {
  UCHAR Reserved;
  UCHAR AudioStatus;
  UCHAR DataLength[2];
} SUB_Q_HEADER, *PSUB_Q_HEADER;
```



## Members

<dl> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**AudioStatus**
</dt> <dd>

Reports the audio status with one of the following flags:

<dl> <dt>

<span id="AUDIO_STATUS_NOT_SUPPORTED"></span><span id="audio_status_not_supported"></span>AUDIO\_STATUS\_NOT\_SUPPORTED
</dt> <dd>

Audio status byte not supported or not valid.

</dd> </dl>

<dl> <dt>

<span id="AUDIO_STATUS_IN_PROGRESS"></span><span id="audio_status_in_progress"></span>AUDIO\_STATUS\_IN\_PROGRESS
</dt> <dd>

Audio play operation is in progress.

</dd> </dl>

<dl> <dt>

<span id="AUDIO_STATUS_PAUSED"></span><span id="audio_status_paused"></span>AUDIO\_STATUS\_PAUSED
</dt> <dd>

Audio play operation is paused.

</dd> </dl>

<dl> <dt>

<span id="AUDIO_STATUS_PLAY_COMPLETE"></span><span id="audio_status_play_complete"></span>AUDIO\_STATUS\_PLAY\_COMPLETE
</dt> <dd>

Audio play operation completed successfully.

</dd> </dl>

<dl> <dt>

<span id="AUDIO_STATUS_PLAY_ERROR"></span><span id="audio_status_play_error"></span>AUDIO\_STATUS\_PLAY\_ERROR
</dt> <dd>

Audio play operation stopped due to error.

</dd> </dl>

<dl> <dt>

<span id="AUDIO_STATUS_NO_STATUS"></span><span id="audio_status_no_status"></span>AUDIO\_STATUS\_NO\_STATUS
</dt> <dd>

No current audio status to return.

</dd> </dl> </dd> <dt>

**DataLength**
</dt> <dd>

Gives the length of Q subchannel data that follows this header structure. The bytes in this array are arranged in big-endian order. **DataLength**\[0\] contains the most significant byte, and **DataLength**\[1\] contains the least significant byte.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_READ\_Q\_CHANNEL**](ioctl-cdrom-read-q-channel.md)
</dt> <dt>

[**CDROM\_SUB\_Q\_DATA\_FORMAT**](cdrom-sub-q-data-format.md)
</dt> <dt>

[**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SUB_Q_HEADER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






