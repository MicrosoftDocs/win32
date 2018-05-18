---
title: IDEREGISTERS structure
description: The IDEREGISTERS structure is used to report the contents of the IDE controller registers.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 'a3df8ce0-4414-49d1-a02c-3f5a3efc0de2'
keywords: ["IDEREGISTERS structure Storage Devices", "PIDEREGISTERS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- IDEREGISTERS
api_location:
- irb.h
api_type:
- HeaderDef
---

# IDEREGISTERS structure

The IDEREGISTERS structure is used to report the contents of the IDE controller registers.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDEREGISTERS {
  UCHAR bFeaturesReg;
  UCHAR bSectorCountReg;
  UCHAR bSectorNumberReg;
  UCHAR bCylLowReg;
  UCHAR bCylHighReg;
  UCHAR bDriveHeadReg;
  UCHAR bCommandReg;
  UCHAR bReserved;
} IDEREGISTERS, *PIDEREGISTERS;
```



## Members

<dl> <dt>

**bFeaturesReg**
</dt> <dd>

Specifies the contents of the ATA features register.

</dd> <dt>

**bSectorCountReg**
</dt> <dd>

Specifies the contents of the ATA Sector Count register.

</dd> <dt>

**bSectorNumberReg**
</dt> <dd>

Specifies the contents of the ATA Sector Number register.

</dd> <dt>

**bCylLowReg**
</dt> <dd>

Specifies the contents of the ATA Cylinder Low register.

</dd> <dt>

**bCylHighReg**
</dt> <dd>

Specifies the contents of the ATA Cylinder High register.

</dd> <dt>

**bDriveHeadReg**
</dt> <dd>

Specifies the contents of the ATA Device/Head register.

</dd> <dt>

**bCommandReg**
</dt> <dd>

Specifies the contents of the ATA Command register.

</dd> <dt>

**bReserved**
</dt> <dd>

Reserved for future use. The miniport driver shall not use this field.

</dd> </dl>

## Remarks

The information reported in the IDEREGISTERS structure is intended to be a superset of the information contained in [**IDEREGS**](ideregs.md). Microsoft might expand the contents of the IDEREGISTERS structure in the future. If you need a structure whose size is stable across different versions of the operating system, you should use **IDEREGS**.

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDEREGS**](ideregs.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDEREGISTERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






