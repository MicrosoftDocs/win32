---
title: HBA\_fc4types structure
description: The HBA\_fc4types structure contains a set of up to 32 values indicating the FC-4 types that the HBA supports.
ms.assetid: 'ef043a97-3ef4-4fd3-93a6-ac1621503713'
keywords: ["HBA_fc4types structure Storage Devices", "HBA_FC4TYPES structure Storage Devices", "PHBA_FC4TYPES structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_FC4TYPES
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_fc4types structure

The HBA\_fc4types structure contains a set of up to 32 values indicating the FC-4 types that the HBA supports.

## Syntax


```C++
typedef struct HBA_fc4types {
  HBA_UINT8 bits[32];
} HBA_FC4TYPES, *PHBA_FC4TYPES;
```



## Members

<dl> <dt>

**bits**
</dt> <dd>

Contains 32 bytes of FC4 type information. Each byte indicates a support FC-4 type. For a complete list of the values that can be assigned to this member, see .the T11 committee's *Fibre Channel Generic Services -4 (FC-GS-4)* specification.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_PortAttributes**](hba-portattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_fc4types%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






