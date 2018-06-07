---
Description: Indicates the average data rate in Hertz (Hz) for the audio file in bits per second.
ms.assetid: 570711c2-ef9b-4b3a-9b5f-94a6601fa3d4
title: System.Audio.EncodingBitrate
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Audio.EncodingBitrate

Indicates the average data rate in Hertz (Hz) for the audio file in bits per second.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Audio.EncodingBitrate
   shellPKey = PKEY_Audio_EncodingBitrate
   formatID = 64440490-4C8B-11D1-8B70-080036B11A03
   propID = 4
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            name = AMBroadcast
            minValue = 0
            setValue = 0
            text = Voice and AM Broadcast (0 - 32 Kbps)
            defineToken = ENCODINGBITRATE_AM_BROADCAST
         enumRange
            name = FMBroadcast
            minValue = 32769
            setValue = 32769
            text = FM Broadcast (32 - 64 Kbps)
            defineToken = ENCODINGBITRATE_FM_BROADCAST
         enumRange
            name = HighQuality
            minValue = 65537
            setValue = 65537
            text = High Quality (64 - 128 Kbps)
            defineToken = ENCODINGBITRATE_HIGH_QUALITY
         enumRange
            name = NearCDQuality
            minValue = 131073
            setValue = 131073
            text = Near CD Quality (over 128 Kbps)
            defineToken = ENCODINGBITRATE_NEAR_CD_QUALITY
         enumRange
            name
            minValue = 4294967295
```

## Windows Vista

```
propertyDescription
   name = System.Audio.EncodingBitrate
   shellPKey = PKEY_Audio_EncodingBitrate
   formatID = 64440490-4C8B-11D1-8B70-080036B11A03
   propID = 4
   SearchInfo
      IsColumn = true
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enumRange
            minValue = 0
            setValue = 0
            text = Voice and AM Broadcast (0 - 32 Kbps)
         enumRange
            minValue = 32769
            setValue = 32769
            text = FM Broadcast (32 - 64 Kbps)
         enumRange
            minValue = 65537
            setValue = 65537
            text = High Quality (64 - 128 Kbps)
         enumRange
            minValue = 131073
            setValue = 131073
            text = Near CD Quality (over 128 Kbps)
         enumRange
            minValue = 4294967295
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

 

 



