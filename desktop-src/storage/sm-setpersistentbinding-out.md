---
title: SM\_SetPersistentBinding\_OUT structure
description: The SM\_SetPersistentBinding\_OUT structure is used to receive output parameters from the SM\_SetPersistentBinding method.
ms.assetid: '42d451ab-51dc-4b59-b6e9-42e02ec1b500'
keywords: ["SM_SetPersistentBinding_OUT structure Storage Devices", "PSM_SetPersistentBinding_OUT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SetPersistentBinding_OUT
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# SM\_SetPersistentBinding\_OUT structure

The SM\_SetPersistentBinding\_OUT structure is used to receive output parameters from the SM\_SetPersistentBinding method.

## Syntax


```C++
typedef struct _SM_SetPersistentBinding_OUT {
  ULONG HBAStatus;
  ULONG OutStatusCount;
  ULONG EntryStatus[1];
} SM_SetPersistentBinding_OUT, *PSM_SetPersistentBinding_OUT;
```



## Members

<dl> <dt>

**HBAStatus**
</dt> <dd>

The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233).

</dd> <dt>

**OutStatusCount**
</dt> <dd>

The number of entries.

</dd> <dt>

**EntryStatus**
</dt> <dd>

The status of each entry.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SM\_\_SetPersistentBinding\_OUT structure in *Hbapiwmi.h* when it compiles the MS\_SM\_TargetInformationMethods WMI class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SM_SetPersistentBinding_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





