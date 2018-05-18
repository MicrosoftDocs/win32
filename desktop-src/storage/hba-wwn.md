---
title: HBA\_wwn structure
description: The HBA\_wwn structure contains a 64 bit world-wide name (WWN) that uniquely identifies an HBA.
ms.assetid: '84441fde-1d66-4f76-86b7-dccd792afd0f'
keywords: ["HBA_wwn structure Storage Devices", "HBA_WWN structure Storage Devices", "PHBA_WWN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_WWN
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_wwn structure

The HBA\_wwn structure contains a 64 bit world-wide name (WWN) that uniquely identifies an HBA.

## Syntax


```C++
typedef struct HBA_wwn {
  HBA_UINT8 wwn[8];
} HBA_WWN, *PHBA_WWN;
```



## Members

<dl> <dt>

**wwn**
</dt> <dd>

Contains a 64 bit world-wide name (WWN) that uniquely identifies an HBA. .

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_AdapterAttributes**](hba-adapterattributes.md)
</dt> <dt>

[**HBA\_MgmtInfo**](hba-mgmtinfo.md)
</dt> <dt>

[**HBA\_PortAttributes**](hba-portattributes.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_wwn%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






