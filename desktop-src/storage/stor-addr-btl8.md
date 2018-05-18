---
title: STOR\_ADDR\_BTL8 structure
description: The STOR\_ADDR\_BTL8 address structure contains the addressing information for an 8-bit Bus-Target-LUN (BTL8) address.
ms.assetid: '53C8A5D4-4D8B-4D3E-A350-B3BBAC7F8C71'
keywords: ["STOR_ADDR_BTL8 structure Storage Devices", "PSTOR_ADDR_BTL8 structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STOR_ADDR_BTL8
api_location:
- Storport.h
api_type:
- HeaderDef
---

# STOR\_ADDR\_BTL8 structure

The **STOR\_ADDR\_BTL8** address structure contains the addressing information for an 8-bit Bus-Target-LUN (BTL8) address.

## Syntax


```C++
typedef struct _STOR_ADDR_BTL8 {
  USHORT Type;
  USHORT Port;
  ULONG  AddressLength;
  UCHAR  Path;
  UCHAR  Target;
  UCHAR  Lun;
  UCHAR  Reserved;
} STOR_ADDR_BTL8, *PSTOR_ADDR_BTL8;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

The address type. This member is set to **STOR\_ADDRESS\_TYPE\_BTL8**.

</dd> <dt>

**Port**
</dt> <dd>

The host bus adapter (HBA) port number.

</dd> <dt>

**AddressLength**
</dt> <dd>

The byte length of the address. This value is set to **STOR\_ADDR\_BTL8\_ADDRESS\_LENGTH**.

</dd> <dt>

**Path**
</dt> <dd>

The bus number for the target device.

</dd> <dt>

**Target**
</dt> <dd>

The target device number.

</dd> <dt>

**Lun**
</dt> <dd>

The logical unit on the target device.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved, set to 0.

</dd> </dl>

## Requirements



|                    |                                                                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                     |
| Header<br/>  | <dl> <dt>Storport.h (include Storport.h, Scsi.h, or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**STOR\_ADDRESS**](stor-address.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_ADDR_BTL8%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






