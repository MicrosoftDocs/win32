---
title: DVD\_COPY\_PROTECT\_KEY structure
description: The DVD\_COPY\_PROTECT\_KEY structure is used in conjunction with the IOCTL\_DVD\_READ\_KEY request to execute a report key command of the specified type.
ms.assetid: 79f3fdaf-e23a-40ba-a1eb-5428a63cc96a
keywords:
- DVD_COPY_PROTECT_KEY structure Storage Devices
- PDVD_COPY_PROTECT_KEY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DVD_COPY_PROTECT_KEY
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DVD\_COPY\_PROTECT\_KEY structure

The **DVD\_COPY\_PROTECT\_KEY** structure is used in conjunction with the [**IOCTL\_DVD\_READ\_KEY**](ioctl-dvd-read-key.md) request to execute a report key command of the specified type.

## Syntax


```C++
typedef struct _DVD_COPY_PROTECT_KEY {
  ULONG          KeyLength;
  DVD_SESSION_ID SessionId;
  DVD_KEY_TYPE   KeyType;
  ULONG          KeyFlags;
  union {
    HANDLE        FileHandle;
    LARGE_INTEGER TitleOffset;
  } Parameters;
  UCHAR          KeyData[];
} DVD_COPY_PROTECT_KEY, *PDVD_COPY_PROTECT_KEY;
```



## Members

<dl> <dt>

**KeyLength**
</dt> <dd>

Indicates the length of the key data to be retrieved.

</dd> <dt>

**SessionId**
</dt> <dd>

Indicates the DVD session ID. The Authentication Grant Identifier (AGID) for a secure Advanced Access Content System (AACS) session is a long integer in the range -1 to 3 inclusive.

</dd> <dt>

**KeyType**
</dt> <dd>

Indicates the key type. The DVD device driver uses this information to determine the key format in a report key command, as defined by the *SCSI Multimedia Commands - 3 (MMC-3)* specification. A report key command either reports key data for a specified key (challenge key, bus key, title key, RPC key, or disk key), reports the state of the authentication success flag (ASF), or invalidates an authentication grant ID (AGID). See the *MMC-3* specification for further information.

</dd> <dt>

**KeyFlags**
</dt> <dd> <dl> <dt>

Contains copy generation management system (CGMS) data. For devices that implement a CGMS protection scheme, the CGMS data is returned with the title key data in the **KeyFlags** member. This member can have any of the following values:
</dt> <dt>





| Value                                     | Meaning                                                                    |
|-------------------------------------------|----------------------------------------------------------------------------|
| DVD\_CGMS\_RESERVED\_MASK<br/>      | Mask of reserved bits. <br/>                                         |
| DVD\_CGMS\_COPY\_PROTECT\_MASK<br/> | Copy protection bitmask. <br/>                                       |
| DVD\_CGMS\_COPY\_PERMITTED<br/>     | Copying is permitted, within limits of copyright restrictions. <br/> |
| DVD\_CGMS\_COPY\_ONCE<br/>          | One generation of copies can be made.<br/>                           |
| DVD\_CGMS\_NO\_COPY<br/>            | No copying is allowed.<br/>                                          |
| DVD\_COPYRIGHT\_MASK<br/>           | Copyright bitmask. <br/>                                             |
| DVD\_NOT\_COPYRIGHTED<br/>          | Copying is permitted without restriction.<br/>                       |
| DVD\_COPYRIGHTED<br/>               | Data is copyrighted. <br/>                                           |
| DVD\_SECTOR\_PROTECT\_MASK<br/>     | Sector protection bitmask. <br/>                                     |
| DVD\_SECTOR\_NOT\_PROTECTED<br/>    | Title key data is not encrypted. No decryption necessary. <br/>      |
| DVD\_SECTOR\_PROTECTED<br/>         | Title key data must be decrypted. <br/>                              |



 


</dt> </dl> </dd> <dt>

**Parameters**
</dt> <dd> <dl> <dt>

**FileHandle**
</dt> <dd>

Pointer to the file handle for the physical device that the copy protection is being negotiated on.

</dd> <dt>

**TitleOffset**
</dt> <dd>

Contains the logical block address on the media of the title.

The upper layers of the operating system use the **FileHandle** member. The file system converts the value in **FileHandle** into a logical block address and stores the result in the **TitleOffset** member. Kernel-mode drivers use the **TitleOffset** member.

</dd> </dl> </dd> <dt>

**KeyData**
</dt> <dd>

Contains the key data that was returned.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**DVD\_KEY\_TYPE**](dvd-key-type.md)
</dt> <dt>

[**IOCTL\_DVD\_READ\_KEY**](ioctl-dvd-read-key.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DVD_COPY_PROTECT_KEY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






