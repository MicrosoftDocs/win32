---
title: UFS\_INTERCONNECT\_DESCRIPTOR structure
description: UFS\_INTERCONNECT\_DESCRIPTOR contains the MIPI M-PHY® specification version number and the MIPI 6338 UniPro specification version number.
ms.assetid: '6C6EAA96-40E9-467F-903B-AE44CE5B77CF'
keywords: ["UFS_INTERCONNECT_DESCRIPTOR structure Storage Devices", "PUFS_INTERCONNECT_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- UFS_INTERCONNECT_DESCRIPTOR
api_location:
- Ufs.h
api_type:
- HeaderDef
---

# UFS\_INTERCONNECT\_DESCRIPTOR structure

**UFS\_INTERCONNECT\_DESCRIPTOR** contains the MIPI M-PHY® specification version number and the MIPI 6338 UniPro? specification version number.

## Syntax


```C++
typedef struct _UFS_INTERCONNECT_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR bcdUniproVersion[2];
  UCHAR bcdMphyVersion[2];
} UFS_INTERCONNECT_DESCRIPTOR, *PUFS_INTERCONNECT_DESCRIPTOR;
```



## Members

<dl> <dt>

**bLength**
</dt> <dd>

Specifies the length, in bytes, of this descriptor.

</dd> <dt>

**bDescriptorIDN**
</dt> <dd>

Specifies the type of the descriptor. This descriptor will have a value of **UFS\_DESC\_INTERCONNECT\_IDN**.

</dd> <dt>

**bcdUniproVersion**
</dt> <dd>

Specifies the MIPI UniPro? version number in Binary Coded Decimal (BCD) format.

</dd> <dt>

**bcdMphyVersion**
</dt> <dd>

Specifies the MIPI M-PHY® version number in BCD format.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709<br/>                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ufs.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20UFS_INTERCONNECT_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





