---
title: MSFC\_TM structure
description: The MSFC\_TM structure is used by WMI providers to timestamp events.
ms.assetid: '7e27f53f-350e-4315-9de6-60835bddcbfb'
keywords: ["MSFC_TM structure Storage Devices", "PMSFC_TM structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MSFC_TM
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# MSFC\_TM structure

The MSFC\_TM structure is used by WMI providers to timestamp events.

## Syntax


```C++
typedef struct _MSFC_TM {
  ULONG tm_sec;
  ULONG tm_min;
  ULONG tm_hour;
  ULONG tm_mday;
  ULONG tm_mon;
  ULONG tm_year;
  ULONG tm_wday;
  ULONG tm_yday;
  ULONG tm_isdst;
} MSFC_TM, *PMSFC_TM;
```



## Members

<dl> <dt>

**tm\_sec**
</dt> <dd>

Indicates the number of seconds past the minute. This member must have a value between 0 and 59.

</dd> <dt>

**tm\_min**
</dt> <dd>

Indicates the number of minutes after the hour. This member must have a value between 0 and 59.

</dd> <dt>

**tm\_hour**
</dt> <dd>

Indicates the number of hours since midnight. This member must have a value between 0 and 23.

</dd> <dt>

**tm\_mday**
</dt> <dd>

Indicates the day of the month. This member must have a value between 1 and 31.

</dd> <dt>

**tm\_mon**
</dt> <dd>

Indicates the number of months since January. This member must have a value between 0 and 11.

</dd> <dt>

**tm\_year**
</dt> <dd>

Indicates the number of years since 1900.

</dd> <dt>

**tm\_wday**
</dt> <dd>

Indicates the number of days since Sunday. This member must have a value between 0 and 6.

</dd> <dt>

**tm\_yday**
</dt> <dd>

Indicates the number of days since January 1. This member must have a value between 0 and 365.

</dd> <dt>

**tm\_isdst**
</dt> <dd>

Indicates when **TRUE** that the time stamp complies with daylight savings time. When **FALSE**, indicates that the timestamp does not comply with daylight savings time.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[MSFC\_TM WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562965)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_TM%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






