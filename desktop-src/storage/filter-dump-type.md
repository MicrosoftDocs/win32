---
title: FILTER\_DUMP\_TYPE enumeration
description: The FILTER\_DUMP\_TYPE enumeration indicates the type of dump stack that this instance of the filter driver is loaded on.
ms.assetid: '396aec33-b4b4-4b4e-9890-b4aa829c3bbd'
keywords: ["FILTER_DUMP_TYPE enumeration Storage Devices", "PFILTER_DUMP_TYPE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- FILTER_DUMP_TYPE
api_location:
- ntdddump.h
api_type:
- HeaderDef
---

# FILTER\_DUMP\_TYPE enumeration

The FILTER\_DUMP\_TYPE enumeration indicates the type of dump stack that this instance of the filter driver is loaded on.

## Syntax


```C++
typedef enum _FILTER_DUMP_TYPE { 
  DumpTypeUndefined    = 0,
  DumpTypeCrashdump    = 1,
  DumpTypeHibernation  = 2
} FILTER_DUMP_TYPE, *PFILTER_DUMP_TYPE;
```



## Constants

<dl> <dt>

<span id="DumpTypeUndefined"></span><span id="dumptypeundefined"></span><span id="DUMPTYPEUNDEFINED"></span>**DumpTypeUndefined**
</dt> <dd>

This dump type is undefined.

</dd> <dt>

<span id="DumpTypeCrashdump"></span><span id="dumptypecrashdump"></span><span id="DUMPTYPECRASHDUMP"></span>**DumpTypeCrashdump**
</dt> <dd>

This dump type is for the crash dump stack.

</dd> <dt>

<span id="DumpTypeHibernation"></span><span id="dumptypehibernation"></span><span id="DUMPTYPEHIBERNATION"></span>**DumpTypeHibernation**
</dt> <dd>

This dump type is for hibernation.

</dd> </dl>

## Remarks

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows Vista and Windows Server 2008.<br/>                                  |
| Header<br/>  | <dl> <dt>Ntdddump.h (include Ntdddump.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FILTER_DUMP_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





