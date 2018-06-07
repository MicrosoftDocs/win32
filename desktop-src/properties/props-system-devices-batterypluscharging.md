---
Description: Remaining battery life of the device and its charging state.
ms.assetid: 9c6800ed-ca55-4202-8dfb-6e430121d6b7
title: System.Devices.BatteryPlusCharging
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Devices.BatteryPlusCharging

Remaining battery life of the device and its charging state.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Devices.BatteryPlusCharging
   shellPKey = PKEY_Devices_BatteryPlusCharging
   formatID = 49CD1F76-5626-4B17-A4E8-18B4AA1A2213
   propID = 22
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Byte
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            name = CriticallyLow
            minValue = 0
            setValue = 5
            text = Critically low battery
            defineToken = BATTERYPLUSCHARGING_CRITICALLY_LOW
         enumRange
            name = Low
            minValue = 11
            setValue = 18
            text = Low battery
            defineToken = BATTERYPLUSCHARGING_LOW
         enumRange
            name = Average
            minValue = 26
            setValue = 60
            text = Average battery
            defineToken = BATTERYPLUSCHARGING_AVERAGE
         enumRange
            name = Full
            minValue = 90
            setValue = 95
            text = Full battery
            defineToken = BATTERYPLUSCHARGING_FULL
         enumRange
            name = CriticallyLow
            minValue = 101
            setValue = 5
            text = Critically low battery (charging)
            defineToken = BATTERYPLUSCHARGING_CHARGING_CRITICALLY_LOW
         enumRange
            name = Low
            minValue = 111
            setValue = 18
            text = Low battery (charging)
            defineToken = BATTERYPLUSCHARGING_CHARGING_LOW
         enumRange
            name = Average
            minValue = 126
            setValue = 60
            text = Average battery (charging)
            defineToken = BATTERYPLUSCHARGING_CHARGING_AVERAGE
         enumRange
            name = Full
            minValue = 190
            setValue = 95
            text = Full battery (charging)
            defineToken = BATTERYPLUSCHARGING_CHARGING_FULL
         enumRange
            name = UnknownStatus
            minValue = 201
            setValue = 201
            text = Unknown battery and charging status
            defineToken = BATTERYPLUSCHARGING_UNKNOWN_STATUS
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[propertyDescription](https://www.bing.com/search?q=propertyDescription)
</dt> <dt>

[searchInfo](https://www.bing.com/search?q=searchInfo)
</dt> <dt>

[labelInfo](https://www.bing.com/search?q=labelInfo)
</dt> <dt>

[typeInfo](https://www.bing.com/search?q=typeInfo)
</dt> <dt>

[displayInfo](https://www.bing.com/search?q=displayInfo)
</dt> <dt>

[stringFormat](https://www.bing.com/search?q=stringFormat)
</dt> <dt>

[booleanFormat](https://www.bing.com/search?q=booleanFormat)
</dt> <dt>

[numberFormat](https://www.bing.com/search?q=numberFormat)
</dt> <dt>

[dateTimeFormat](https://www.bing.com/search?q=dateTimeFormat)
</dt> <dt>

[enumeratedList](https://www.bing.com/search?q=enumeratedList)
</dt> <dt>

[drawControl](https://www.bing.com/search?q=drawControl)
</dt> <dt>

[editControl](https://www.bing.com/search?q=editControl)
</dt> <dt>

[filterControl](https://www.bing.com/search?q=filterControl)
</dt> <dt>

[queryControl](https://www.bing.com/search?q=queryControl)
</dt> </dl>

 

 



