---
title: ISCSI\_ENCRYPTION\_TYPES enumeration
description: The ISCSI\_ENCRYPTION\_TYPES enumeration indicates the type of encryption that is supported.
ms.assetid: f1c7a13b-511a-4e9d-a0e6-9fb27126b1d2
keywords:
- ISCSI_ENCRYPTION_TYPES enumeration Storage Devices
- PISCSI_ENCRYPTION_TYPES enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_ENCRYPTION_TYPES
api_location:
- iscsicfg.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISCSI\_ENCRYPTION\_TYPES enumeration

The ISCSI\_ENCRYPTION\_TYPES enumeration indicates the type of encryption that is supported.

## Syntax


```C++
typedef enum  { 
  ISCSI_ENCRYPT_NONE            = 0,
  ISCSI_ENCRYPT_3DES_HMAC_SHA1  = 1,
  ISCSI_ENCRYPT_AES_CTR         = 2
} ISCSI_ENCRYPTION_TYPES, *PISCSI_ENCRYPTION_TYPES;
```



## Constants

<dl> <dt>

<span id="ISCSI_ENCRYPT_NONE"></span><span id="iscsi_encrypt_none"></span>**ISCSI\_ENCRYPT\_NONE**
</dt> <dd>

No type of encryption is supported.

</dd> <dt>

<span id="ISCSI_ENCRYPT_3DES_HMAC_SHA1"></span><span id="iscsi_encrypt_3des_hmac_sha1"></span>**ISCSI\_ENCRYPT\_3DES\_HMAC\_SHA1**
</dt> <dd>

The initiator or target supports triple data encryption standard (DES), hashed message authentication code (HMAC), and the secure hash algorithm, version 1.

</dd> <dt>

<span id="ISCSI_ENCRYPT_AES_CTR"></span><span id="iscsi_encrypt_aes_ctr"></span>**ISCSI\_ENCRYPT\_AES\_CTR**
</dt> <dd>

The initiator or target supports advanced encryption standard (AES) counter mode (CTR).

</dd> </dl>

## Remarks

The ISCSI\_ENCRYPTION\_TYPES enumeration is used with the [MSiSCSI\_SecurityCapabilities WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563131).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsicfg.h (include Iscsicfg.h)</dt> </dl> |



## See also

<dl> <dt>

[**MSiSCSI\_SecurityCapabilities**](msiscsi-securitycapabilities.md)
</dt> <dt>

[MSiSCSI\_SecurityCapabilities WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563131)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_ENCRYPTION_TYPES%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






