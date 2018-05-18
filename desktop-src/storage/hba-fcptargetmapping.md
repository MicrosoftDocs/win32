---
title: HBA\_FCPTargetMapping structure
description: The HBA\_FCPTargetMapping structure contains an array of bindings between operating system and fibre channel protocol (FCP) identifiers for a set of target devices.
ms.assetid: '666f4aea-2fcb-46cf-8d25-d1322c0517c9'
keywords: ["HBA_FCPTargetMapping structure Storage Devices", "HBA_FCPTARGETMAPPING structure Storage Devices", "PHBA_FCPTARGETMAPPING structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_FCPTARGETMAPPING
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_FCPTargetMapping structure

The HBA\_FCPTargetMapping structure contains an array of bindings between operating system and fibre channel protocol (FCP) identifiers for a set of target devices.

## Syntax


```C++
typedef struct HBA_FCPTargetMapping {
  HBA_UINT32       NumberOfEntries;
  HBA_FCPSCSIENTRY entry[1];
} HBA_FCPTARGETMAPPING, *PHBA_FCPTARGETMAPPING;
```



## Members

<dl> <dt>

**NumberOfEntries**
</dt> <dd>

Indicates the number of bindings.

</dd> <dt>

**entry**
</dt> <dd>

Contains a variable length array of structures of type [**HBA\_FcpScsiEntry**](hba-fcpscsientry.md) each of which defines a mapping between an operating system identifier for a logical unit and the corresponding fibre channel protocol (FCP) identifier for the logical unit.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_FcpScsiEntry**](hba-fcpscsientry.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_FCPTargetMapping%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






