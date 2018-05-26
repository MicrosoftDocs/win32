---
title: HBA\_FCPBinding2 structure
description: The HBA\_FCPBinding2 structure contains an array of bindings between operating system identifiers, SCSI logical unit ID descriptors (LUIDs) and fibre channel protocol (FCP) identifiers for a set of logical units.
ms.assetid: f715d45c-30e1-414f-907c-9ad1203ca604
keywords:
- HBA_FCPBinding2 structure Storage Devices
- HBA_FCPBINDING2 structure Storage Devices
- PHBA_FCPBINDING2 structure pointer Storage Devices
topic_type:
- apiref
api_name:
- HBA_FCPBINDING2
api_location:
- hbaapi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HBA\_FCPBinding2 structure

The HBA\_FCPBinding2 structure contains an array of bindings between operating system identifiers, SCSI logical unit ID descriptors (LUIDs) and fibre channel protocol (FCP) identifiers for a set of logical units.

## Syntax


```C++
typedef struct HBA_FCPBinding2 {
  HBA_UINT32           NumberOfEntries;
  HBA_FCPBINDINGENTRY2 entry[1];
} HBA_FCPBINDING2, *PHBA_FCPBINDING2;
```



## Members

<dl> <dt>

**NumberOfEntries**
</dt> <dd>

Indicates, on input, the number of bindings that can fit in the array at **entry**. On output, this member holds the number of entries actually returned, which will be equal to the number specified on input or the full set of available bindings, whichever is smaller. The value in **NumberOfEntries** will contain the number of persistent bindings returned even when an error occurred because of insufficient buffer space.

</dd> <dt>

**entry**
</dt> <dd>

Variable length array of elements of type [**HBA\_FCPBindingEntry2**](hba-fcpbindingentry2.md), each of which holds a persistent binding between operating system identifiers, a SCSI logical unit ID descriptor (LUID) and a fibre channel protocol (FCP) identifier for a logical unit.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_GetPersistentBindingV2**](hba-getpersistentbindingv2.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_FCPBinding2%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






