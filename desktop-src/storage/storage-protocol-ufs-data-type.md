---
title: STORAGE\_PROTOCOL\_UFS\_DATA\_TYPE enumeration
description: The UFS (Universal Flash Storage) data type. Describes the type of UFS specific data thats to be queried during an IOCTL\_STORAGE\_QUERY\_PROPERTY request.
ms.assetid: A4324FAD-A925-4D65-9697-9CC2878DBE0B
keywords:
- STORAGE_PROTOCOL_UFS_DATA_TYPE enumeration Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_PROTOCOL_UFS_DATA_TYPE
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_PROTOCOL\_UFS\_DATA\_TYPE enumeration

The UFS (Universal Flash Storage) data type. Describes the type of UFS specific data that's to be queried during an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590) request.

## Syntax


```C++
typedef enum _STORAGE_PROTOCOL_UFS_DATA_TYPE { 
  UfsDataTypeUnknown              = 0,
      UfsDataTypeQueryDescriptor,
          UfsDataTypeMax
} STORAGE_PROTOCOL_UFS_DATA_TYPE;
```



## Constants

<dl> <dt>

<span id="UfsDataTypeUnknown"></span><span id="ufsdatatypeunknown"></span><span id="UFSDATATYPEUNKNOWN"></span>**UfsDataTypeUnknown**
</dt> <dd>

Unknown data type.

</dd> <dt>

<span id="____UfsDataTypeQueryDescriptor"></span><span id="____ufsdatatypequerydescriptor"></span><span id="____UFSDATATYPEQUERYDESCRIPTOR"></span> **UfsDataTypeQueryDescriptor**
</dt> <dd>

Query Descriptor data type. Retrieved by command UfsSrbQueryProtocolQueryDescriptor.

</dd> <dt>

<span id="________UfsDataTypeMax"></span><span id="________ufsdatatypemax"></span><span id="________UFSDATATYPEMAX"></span> **UfsDataTypeMax**
</dt> <dd>

Max size of data type.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_PROTOCOL\_DATA\_DESCRIPTOR**](storage-protocol-data-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_PROTOCOL_UFS_DATA_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






