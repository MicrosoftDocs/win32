---
description: Device charging status.
ms.assetid: 33ef8ecb-29e3-4809-9d56-8d884f9c9ff6
title: System.Devices.ChargingState
ms.topic: article
ms.date: 05/31/2018
---

# System.Devices.ChargingState

Device charging status.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Devices.ChargingState
   shellPKey = PKEY_Devices_ChargingState
   formatID = 49CD1F76-5626-4B17-A4E8-18B4AA1A2213
   propID = 11
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Byte
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            name = NotCharging
            minValue = 0
            setValue = 0
            text = Not charging
            defineToken = CHARGINGSTATE_NOT_CHARGING
         enumRange
            name = Charging
            minValue = 1
            setValue = 1
            text = Charging
            defineToken = CHARGINGSTATE_CHARGING
         enumRange
            name = UnknownChargingState
            minValue = 2
            setValue = 2
            text = Unknown charging state
            defineToken = CHARGINGSTATE_UNKNOWN_STATE
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[propertyDescription](./propdesc-schema-propertydescription.md)
</dt> <dt>

[searchInfo](./propdesc-schema-searchinfo.md)
</dt> <dt>

[labelInfo](./propdesc-schema-labelinfo.md)
</dt> <dt>

[typeInfo](./propdesc-schema-typeinfo.md)
</dt> <dt>

[displayInfo](./propdesc-schema-displayinfo.md)
</dt> <dt>

[stringFormat](./propdesc-schema-stringformat.md)
</dt> <dt>

[booleanFormat](./propdesc-schema-booleanformat.md)
</dt> <dt>

[numberFormat](./propdesc-schema-numberformat.md)
</dt> <dt>

[dateTimeFormat](./propdesc-schema-datetimeformat.md)
</dt> <dt>

[enumeratedList](./propdesc-schema-enumeratedlist.md)
</dt> <dt>

[drawControl](./propdesc-schema-drawcontrol.md)
</dt> <dt>

[editControl](./propdesc-schema-editcontrol.md)
</dt> <dt>

[filterControl](./propdesc-schema-filtercontrol.md)
</dt> <dt>

[queryControl](./propdesc-schema-querycontrol.md)
</dt> </dl>

 

 
