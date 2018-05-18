---
title: DEVICE\_WRITE\_AGGREGATION\_DESCRIPTOR structure
description: Reserved for system use.
ms.assetid: '7AACFA1A-4B56-4B51-91B6-5FA30918E516'
keywords: ["DEVICE_WRITE_AGGREGATION_DESCRIPTOR structure Storage Devices", "PDEVICE_WRITE_AGGREGATION_DESCRIPTOR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DEVICE_WRITE_AGGREGATION_DESCRIPTOR
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# DEVICE\_WRITE\_AGGREGATION\_DESCRIPTOR structure

Reserved for system use.

## Syntax


```C++
typedef struct _DEVICE_WRITE_AGGREGATION_DESCRIPTOR {
  ULONG   Version;
  ULONG   Size;
  BOOLEAN BenefitsFromWriteAggregation;
} DEVICE_WRITE_AGGREGATION_DESCRIPTOR, *PDEVICE_WRITE_AGGREGATION_DESCRIPTOR;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Contains the size, in bytes, of this structure. The value of this member will change as members are added to the structure.

</dd> <dt>

**Size**
</dt> <dd>

Specifies the total size of the descriptor, in bytes.

</dd> <dt>

**BenefitsFromWriteAggregation**
</dt> <dd>

**TRUE** if the device benefits from write aggregation.

</dd> </dl>

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                          |
| Header<br/>                   | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DEVICE_WRITE_AGGREGATION_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






