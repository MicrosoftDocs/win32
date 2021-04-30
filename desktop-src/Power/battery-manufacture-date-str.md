---
description: Contains the date of manufacture of a battery.
ms.assetid: 0cda66fc-bf4a-4a38-b43c-6eecde46c414
title: BATTERY_MANUFACTURE_DATE structure (Poclass.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BATTERY_MANUFACTURE_DATE
api_type: 
- HeaderDef
api_location: 
- Poclass.h
- Batclass.h
---

# BATTERY\_MANUFACTURE\_DATE structure

Contains the date of manufacture of a battery. This structure is used by the [**BATTERY\_QUERY\_INFORMATION**](battery-query-information-str.md) structure when the BatteryManufactureDate information level is requested.

## Syntax


```C++
typedef struct _BATTERY_MANUFACTURE_DATE {
  UCHAR  Day;
  UCHAR  Month;
  USHORT Year;
} BATTERY_MANUFACTURE_DATE, *PBATTERY_MANUFACTURE_DATE;
```



## Members

<dl> <dt>

**Day**
</dt> <dd>

The day of the month of manufacture, in the range 1 to 31. In spite of the data type, this is not an ASCII encoded value. It is an unsigned byte.

</dd> <dt>

**Month**
</dt> <dd>

The month of manufacture, in the range 1 (January) to 12 (December). In spite of the data type, this is not an ASCII encoded value. It is an unsigned byte.

</dd> <dt>

**Year**
</dt> <dd>

The year of manufacture. This will typically be in the range 1900-2100.

</dd> </dl>

## Remarks

The date is encoded in the Gregorian or western calendar format.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                                                                                                                                                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                                                                                                                                                                                |
| Header<br/>                   | <dl> <dt>Poclass.h; </dt> <dt>Batclass.h on Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP</dt> </dl> |



## See also

<dl> <dt>

[**BATTERY\_QUERY\_INFORMATION**](battery-query-information-str.md)
</dt> <dt>

[**IOCTL\_BATTERY\_QUERY\_INFORMATION**](ioctl-battery-query-information.md)
</dt> </dl>

 

 




