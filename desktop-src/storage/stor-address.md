---
title: STOR\_ADDRESS structure
description: A general structure for holding a storage device address.
ms.assetid: 464AE3EA-D941-430F-8362-B66F4D00AE50
keywords:
- STOR_ADDRESS structure Storage Devices
- PSTOR_ADDRESS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STOR_ADDRESS
api_location:
- Storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STOR\_ADDRESS structure

A general structure for holding a storage device address.

## Syntax


```C++
typedef struct _STOR_ADDRESS {
  USHORT Type;
  USHORT Port;
  ULONG  AddressLength;
  UCHAR  AddressData[ANYSIZE_ARRAY];
} STOR_ADDRESS, *PSTOR_ADDRESS;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

The address type. This can be one of the following:



| Value                                                                                                                                                                                               | Meaning                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <span id="STOR_ADDRESS_TYPE_UNKNOWN"></span><span id="stor_address_type_unknown"></span><dl> <dt>**STOR\_ADDRESS\_TYPE\_UNKNOWN**</dt> </dl> | The address type is unknown.<br/>                    |
| <span id="STOR_ADDRESS_TYPE_BTL8"></span><span id="stor_address_type_btl8"></span><dl> <dt>**STOR\_ADDRESS\_TYPE\_BTL8**</dt> </dl>          | The address is an 8-bit Bus-Target-LUN address.<br/> |



 

</dd> <dt>

**Port**
</dt> <dd>

The host bus adapter (HBA) port number.

</dd> <dt>

**AddressLength**
</dt> <dd>

The byte length of the **AddressData**. If **Type** is set to **STOR\_ADDRESS\_TYPE\_BTL8**, this value is **STOR\_ADDR\_BTL8\_ADDRESS\_LENGTH**.

</dd> <dt>

**AddressData**
</dt> <dd>

The address data specific to an address type.

</dd> </dl>

## Requirements



|                    |                                                                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                     |
| Header<br/>  | <dl> <dt>Storport.h (include Storport.h, Scsi.h, or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**STOR\_ADDR\_BTL8**](stor-addr-btl8.md)
</dt> <dt>

[**StorPortSetUnitAttributes**](storportsetunitattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_ADDRESS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






