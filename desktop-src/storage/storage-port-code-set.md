---
title: STORAGE\_PORT\_CODE\_SET enumeration
description: Reserved for system use.
ms.assetid: C7067D03-840D-4C69-BF30-48C7AD4651EF
keywords:
- STORAGE_PORT_CODE_SET enumeration Storage Devices
- PSTORAGE_PORT_CODE_SET enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_PORT_CODE_SET
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_PORT\_CODE\_SET enumeration

Reserved for system use.

## Syntax


```C++
typedef enum _STORAGE_PORT_CODE_SET { 
  StoragePortCodeSetReserved   = 0,
  StoragePortCodeSetStorport   = 1,
  StoragePortCodeSetSCSIport   = 2,
  StoragePortCodeSetSpaceport  = 3,
  StoragePortCodeSetATAport    = 4,
  StoragePortCodeSetUSBport    = 5,
  StoragePortCodeSetSBP2port   = 6,
  StoragePortCodeSetSDport     = 7
} STORAGE_PORT_CODE_SET, *PSTORAGE_PORT_CODE_SET;
```



## Constants

<dl> <dt>

<span id="StoragePortCodeSetReserved"></span><span id="storageportcodesetreserved"></span><span id="STORAGEPORTCODESETRESERVED"></span>**StoragePortCodeSetReserved**
</dt> <dd>

Indicates an unknown storage adapter driver type.

</dd> <dt>

<span id="StoragePortCodeSetStorport"></span><span id="storageportcodesetstorport"></span><span id="STORAGEPORTCODESETSTORPORT"></span>**StoragePortCodeSetStorport**
</dt> <dd>

Storage adapter driver is a Storport-miniport driver.

</dd> <dt>

<span id="StoragePortCodeSetSCSIport"></span><span id="storageportcodesetscsiport"></span><span id="STORAGEPORTCODESETSCSIPORT"></span>**StoragePortCodeSetSCSIport**
</dt> <dd>

Storage adapter driver is a SCSI Port-miniport driver.

</dd> <dt>

<span id="StoragePortCodeSetSpaceport"></span><span id="storageportcodesetspaceport"></span><span id="STORAGEPORTCODESETSPACEPORT"></span>**StoragePortCodeSetSpaceport**
</dt> <dd>

Storage adapter driver is the Spaceport driver.

</dd> <dt>

<span id="StoragePortCodeSetATAport"></span><span id="storageportcodesetataport"></span><span id="STORAGEPORTCODESETATAPORT"></span>**StoragePortCodeSetATAport**
</dt> <dd>

Storage adapter driver is an ATA-port miniport driver.

</dd> <dt>

<span id="StoragePortCodeSetUSBport"></span><span id="storageportcodesetusbport"></span><span id="STORAGEPORTCODESETUSBPORT"></span>**StoragePortCodeSetUSBport**
</dt> <dd>

Storage adapter driver is the USB-storage port driver.

</dd> <dt>

<span id="StoragePortCodeSetSBP2port"></span><span id="storageportcodesetsbp2port"></span><span id="STORAGEPORTCODESETSBP2PORT"></span>**StoragePortCodeSetSBP2port**
</dt> <dd>

Storage adapter driver is the SBP2 port driver.

</dd> <dt>

<span id="StoragePortCodeSetSDport"></span><span id="storageportcodesetsdport"></span><span id="STORAGEPORTCODESETSDPORT"></span>**StoragePortCodeSetSDport**
</dt> <dd>

Storage adapter driver is an SD-port miniport driver.

</dd> </dl>

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_MINIPORT\_DESCRIPTOR**](storage-miniport-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PORT_CODE_SET%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






