---
title: STORAGE\_DEVICE\_FORM\_FACTOR enumeration
description: Indicates the form factor of a storage device.
ms.assetid: EE59767B-2504-4E5F-A442-60EEBEE70B59
keywords:
- STORAGE_DEVICE_FORM_FACTOR enumeration Storage Devices
- PSTORAGE_DEVICE_FORM_FACTOR enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_DEVICE_FORM_FACTOR
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STORAGE\_DEVICE\_FORM\_FACTOR enumeration

Indicates the form factor of a storage device.

## Syntax


```C++
typedef enum _STORAGE_DEVICE_FORM_FACTOR { 
  FormFactorUnknown     = 0, // 0x0
  FormFactor3_5,
  FormFactor2_5,
  FormFactor1_8,
  FormFactor1_8Less,
  FormFactorEmbedded,
  FormFactorMemoryCard,
  FormFactormSata,
  FormFactorM_2,
  FormFactorPCIeBoard,
  FormFactorDimm
} STORAGE_DEVICE_FORM_FACTOR, *PSTORAGE_DEVICE_FORM_FACTOR;
```



## Constants

<dl> <dt>

<span id="FormFactorUnknown"></span><span id="formfactorunknown"></span><span id="FORMFACTORUNKNOWN"></span>**FormFactorUnknown**
</dt> <dd>

Unknown form factor.

</dd> <dt>

<span id="FormFactor3_5"></span><span id="formfactor3_5"></span><span id="FORMFACTOR3_5"></span>**FormFactor3\_5**
</dt> <dd>

3.5 inch nominal form factor.

</dd> <dt>

<span id="FormFactor2_5"></span><span id="formfactor2_5"></span><span id="FORMFACTOR2_5"></span>**FormFactor2\_5**
</dt> <dd>

2.5 inch nominal form factor.

</dd> <dt>

<span id="FormFactor1_8"></span><span id="formfactor1_8"></span><span id="FORMFACTOR1_8"></span>**FormFactor1\_8**
</dt> <dd>

1.8 inch nominal form factor.

</dd> <dt>

<span id="FormFactor1_8Less"></span><span id="formfactor1_8less"></span><span id="FORMFACTOR1_8LESS"></span>**FormFactor1\_8Less**
</dt> <dd>

Less than 1.8 inch nominal form factor.

</dd> <dt>

<span id="FormFactorEmbedded"></span><span id="formfactorembedded"></span><span id="FORMFACTOREMBEDDED"></span>**FormFactorEmbedded**
</dt> <dd>

The storage device is embedded on a board.

</dd> <dt>

<span id="FormFactorMemoryCard"></span><span id="formfactormemorycard"></span><span id="FORMFACTORMEMORYCARD"></span>**FormFactorMemoryCard**
</dt> <dd>

A memory card, such as SmartMedia or CompactFlash.

</dd> <dt>

<span id="FormFactormSata"></span><span id="formfactormsata"></span><span id="FORMFACTORMSATA"></span>**FormFactormSata**
</dt> <dd>

Mini-SATA (mSATA) form factor.

</dd> <dt>

<span id="FormFactorM_2"></span><span id="formfactorm_2"></span><span id="FORMFACTORM_2"></span>**FormFactorM\_2**
</dt> <dd>

M.2 form factor.

</dd> <dt>

<span id="FormFactorPCIeBoard"></span><span id="formfactorpcieboard"></span><span id="FORMFACTORPCIEBOARD"></span>**FormFactorPCIeBoard**
</dt> <dd>

PCI Express (PCIe) card form factor.

</dd> <dt>

<span id="FormFactorDimm"></span><span id="formfactordimm"></span><span id="FORMFACTORDIMM"></span>**FormFactorDimm**
</dt> <dd>

Dual in-line memory module (DIMM) slot form factor.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_DEVICE_FORM_FACTOR%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





