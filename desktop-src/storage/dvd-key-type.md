---
title: DVD\_KEY\_TYPE enumeration
description: The DVD\_KEY\_TYPE enumeration type is used in conjunction with the DVD\_COPY\_PROTECT\_KEY structure to indicate a key to be read, to invalidate an authentication grant ID (AGID), and to request state information or region settings.
ms.assetid: 'ec080043-a147-4002-8d0c-ed383182ec40'
keywords: ["DVD_KEY_TYPE enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- DVD_KEY_TYPE
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
---

# DVD\_KEY\_TYPE enumeration

The DVD\_KEY\_TYPE enumeration type is used in conjunction with the [**DVD\_COPY\_PROTECT\_KEY**](dvd-copy-protect-key.md) structure to indicate a key to be read, to invalidate an authentication grant ID (AGID), and to request state information or region settings.

## Syntax


```C++
typedef enum  { 
  DvdChallengeKey    = 0x01,
  DvdBusKey1         = 0x2,
  DvdBusKey2         = 0x3,
  DvdTitleKey        = 0x4,
  DvdAsf             = 0x5,
  DvdSetRpcKey       = 0x6,
  DvdGetRpcKey       = 0x8,
  DvdDiskKey         = 0x80,
  DvdInvalidateAGID  = 0x3f
} DVD_KEY_TYPE;
```



## Constants

<dl> <dt>

<span id="DvdChallengeKey"></span><span id="dvdchallengekey"></span><span id="DVDCHALLENGEKEY"></span>**DvdChallengeKey**
</dt> <dd>

Gets a challenge key. This is used during the authentication key exchange process.

</dd> <dt>

<span id="DvdBusKey1"></span><span id="dvdbuskey1"></span><span id="DVDBUSKEY1"></span>**DvdBusKey1**
</dt> <dd>

Gets the first bus key.

</dd> <dt>

<span id="DvdBusKey2"></span><span id="dvdbuskey2"></span><span id="DVDBUSKEY2"></span>**DvdBusKey2**
</dt> <dd>

Gets the second bus key.

</dd> <dt>

<span id="DvdTitleKey"></span><span id="dvdtitlekey"></span><span id="DVDTITLEKEY"></span>**DvdTitleKey**
</dt> <dd>

Gets a title key that is obfuscated by a bus key.

</dd> <dt>

<span id="DvdAsf"></span><span id="dvdasf"></span><span id="DVDASF"></span>**DvdAsf**
</dt> <dd>

Gets the current state of the authentication success flag (ASF).

</dd> <dt>

<span id="DvdSetRpcKey"></span><span id="dvdsetrpckey"></span><span id="DVDSETRPCKEY"></span>**DvdSetRpcKey**
</dt> <dd>

Sets the region playback contents (RPC) for the logical unit.

</dd> <dt>

<span id="DvdGetRpcKey"></span><span id="dvdgetrpckey"></span><span id="DVDGETRPCKEY"></span>**DvdGetRpcKey**
</dt> <dd>

Gets the region playback contents (RPC) for the logical unit.

</dd> <dt>

<span id="DvdDiskKey"></span><span id="dvddiskkey"></span><span id="DVDDISKKEY"></span>**DvdDiskKey**
</dt> <dd>

Gets the disc key.

</dd> <dt>

<span id="DvdInvalidateAGID"></span><span id="dvdinvalidateagid"></span><span id="DVDINVALIDATEAGID"></span>**DvdInvalidateAGID**
</dt> <dd>

Invalidates the specified authentication grant ID (AGID).

</dd> </dl>

## Remarks

The driver for the DVD device uses the key type specified in this enumeration type to determine the key format in a report key command, as defined by the *SCSI Multimedia Commands - 3 (MMC-3)* specification. A report key command can either report key data for a specified key (challenge key, bus key, title key, RPC key, or disc key), or the state of the ASF flag. It can also invalidate an AGID. See the *MMC-3* specification for further information.

Drivers can issue a report key command to retrieve key data by means of an [**IOCTL\_DVD\_READ\_KEY**](ioctl-dvd-read-key.md) request.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**DVD\_COPY\_PROTECT\_KEY**](dvd-copy-protect-key.md)
</dt> <dt>

[**IOCTL\_DVD\_READ\_KEY**](ioctl-dvd-read-key.md)
</dt> <dt>

[**IOCTL\_DVD\_SEND\_KEY**](ioctl-dvd-send-key.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DVD_KEY_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






