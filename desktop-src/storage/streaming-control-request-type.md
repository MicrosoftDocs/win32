---
title: STREAMING\_CONTROL\_REQUEST\_TYPE enumeration
description: The STREAMING\_CONTROL\_REQUEST\_TYPE enumeration defines the CDROM streaming modes.
ms.assetid: A17F0E3C-402B-4484-B4AE-0583773AEDA8
keywords:
- STREAMING_CONTROL_REQUEST_TYPE enumeration Storage Devices
- PSTREAMING_CONTROL_REQUEST_TYPE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- STREAMING_CONTROL_REQUEST_TYPE
api_location:
- Ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STREAMING\_CONTROL\_REQUEST\_TYPE enumeration

The STREAMING\_CONTROL\_REQUEST\_TYPE enumeration defines the CDROM streaming modes. This enumeration is a member of the [**CDROM\_STREAMING\_CONTROL**](cdrom-streaming-control.md) structure, the input parameter to the [**IOCTL\_CDROM\_ENABLE\_STREAMING**](ioctl-cdrom-enable-streaming.md) I/O control code, which is used to enable or disable CDROM streaming.

## Syntax


```C++
typedef enum _STREAMING_CONTROL_REQUEST_TYPE { 
  CdromStreamingDisable                  = 1,
  CdromStreamingEnableForReadOnly        = 2,
      CdromStreamingEnableForWriteOnly   = 3,
  CdromStreamingEnableForReadWrite       = 4
} STREAMING_CONTROL_REQUEST_TYPE, *PSTREAMING_CONTROL_REQUEST_TYPE;
```



## Constants

<dl> <dt>

<span id="CdromStreamingDisable"></span><span id="cdromstreamingdisable"></span><span id="CDROMSTREAMINGDISABLE"></span>**CdromStreamingDisable**
</dt> <dd>

Streaming read and streaming write requests will be disabled for the requested file handle.

</dd> <dt>

<span id="CdromStreamingEnableForReadOnly"></span><span id="cdromstreamingenableforreadonly"></span><span id="CDROMSTREAMINGENABLEFORREADONLY"></span>**CdromStreamingEnableForReadOnly**
</dt> <dd>

Streaming read requests will be enabled, and streaming write requests will be disabled, for the requested file handle.

</dd> <dt>

<span id="____CdromStreamingEnableForWriteOnly_"></span><span id="____cdromstreamingenableforwriteonly_"></span><span id="____CDROMSTREAMINGENABLEFORWRITEONLY_"></span> **CdromStreamingEnableForWriteOnly** 
</dt> <dd>

Streaming read requests will be disabled, and streaming write requests will be enabled, for the requested file handle.

</dd> <dt>

<span id="CdromStreamingEnableForReadWrite"></span><span id="cdromstreamingenableforreadwrite"></span><span id="CDROMSTREAMINGENABLEFORREADWRITE"></span>**CdromStreamingEnableForReadWrite**
</dt> <dd>

Streaming read and streaming write requests will be enabled for the requested file handle.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_STREAMING\_CONTROL**](cdrom-streaming-control.md)
</dt> <dt>

[**IOCTL\_CDROM\_ENABLE\_STREAMING**](ioctl-cdrom-enable-streaming.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STREAMING_CONTROL_REQUEST_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






