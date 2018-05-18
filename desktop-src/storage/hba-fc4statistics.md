---
title: HBA\_FC4Statistics structure
description: The HBA\_FC4Statistics structure contains port statistics.
ms.assetid: 'e1e37d2c-5688-4528-9cc5-62e70a7561fe'
keywords: ["HBA_FC4Statistics structure Storage Devices", "HBA_FC4STATISTICS structure Storage Devices", "PHBA_FC4STATISTICS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_FC4STATISTICS
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_FC4Statistics structure

The **HBA\_FC4Statistics** structure contains port statistics.

## Syntax


```C++
typedef struct HBA_FC4Statistics {
  HBA_INT64 InputRequests;
  HBA_INT64 OutputRequests;
  HBA_INT64 ControlRequests;
  HBA_INT64 InputMegabytes;
  HBA_INT64 OutputMegabytes;
} HBA_FC4STATISTICS, *PHBA_FC4STATISTICS;
```



## Members

<dl> <dt>

**InputRequests**
</dt> <dd>

Contains the number of input requests that a port has received.

</dd> <dt>

**OutputRequests**
</dt> <dd>

Contains the number of output requests that a port has received.

</dd> <dt>

**ControlRequests**
</dt> <dd>

Contains the number of control requests that a port has received.

</dd> <dt>

**InputMegabytes**
</dt> <dd>

Contains the number of megabytes of input data that a port has received.

</dd> <dt>

**OutputMegabytes**
</dt> <dd>

Contains the number of megabytes of output data that a port has transmitted.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_GetFC4Statistics**](hba-getfc4statistics.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_FC4Statistics%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






