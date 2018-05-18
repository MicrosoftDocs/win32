---
title: GetPathConfiguration\_OUT structure
description: The GetPathConfiguration\_OUT structure is used to report the output parameters that are associated with the GetPathConfiguration method.
ms.assetid: '055db46e-59fc-4eb9-93d7-16d680495220'
keywords: ["GetPathConfiguration_OUT structure Storage Devices", "PGetPathConfiguration_OUT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- GetPathConfiguration_OUT
api_location:
- mpiowmi.h
api_type:
- HeaderDef
---

# GetPathConfiguration\_OUT structure

The GetPathConfiguration\_OUT structure is used to report the output parameters that are associated with the GetPathConfiguration method.

## Syntax


```C++
typedef struct _GetPathConfiguration_OUT {
  ULONG     EntryCount;
  SCSI_ADDR Address[1];
} GetPathConfiguration_OUT, *PGetPathConfiguration_OUT;
```



## Members

<dl> <dt>

**EntryCount**
</dt> <dd>

A 32-bitfield that indicates the number of entries contained in the array of SCSI addresses.

</dd> <dt>

**Address**
</dt> <dd>

An array that returns information about the SCSI addresses. The number of elements in the array is given by EntryCount and each element of the array represents an instance of an SCSI\_ADDR structure.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GetPathConfiguration_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





