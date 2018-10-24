---
Description: An indicator of the flash status when the photo was taken, as read from the Exchangeable Image File (EXIF) info.
ms.assetid: e21de610-9916-4b3f-8e50-f0141b476346
title: System.Photo.Flash
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Photo.Flash

An indicator of the flash status when the photo was taken, as read from the Exchangeable Image File (EXIF) info.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Photo.Flash
   shellPKey = PKEY_Photo_Flash
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 37385
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = Byte
      EnumeratedList
         UseValueForDefault = True
         enum
            name = NoFlash
            value = 0
            text = No flash
            defineToken = PHOTO_FLASH_NONE
         enum
            name = Flash
            value = 1
            text = Flash
            defineToken = PHOTO_FLASH_FLASH
         enum
            name = FlashNoReturnLight
            value = 5
            text = Flash, no strobe return
            defineToken = PHOTO_FLASH_WITHOUTSTROBE
         enum
            name = FlashReturnLight
            value = 7
            text = Flash, strobe return
            defineToken = PHOTO_FLASH_WITHSTROBE
         enum
            name = FlashCompulsory
            value = 9
            text = Flash, compulsory
            defineToken = PHOTO_FLASH_FLASH_COMPULSORY
         enum
            name = FlashCompulsoryNoReturnLight
            value = 13
            text = Flash, compulsory, no strobe return
            defineToken = PHOTO_FLASH_FLASH_COMPULSORY_NORETURNLIGHT
         enum
            name = FlashCompulsoryReturnLight
            value = 15
            text = Flash, compulsory, strobe return
            defineToken = PHOTO_FLASH_FLASH_COMPULSORY_RETURNLIGHT
         enum
            name = NoFlashCompulsory
            value = 16
            text = No flash, compulsory
            defineToken = PHOTO_FLASH_NONE_COMPULSORY
         enum
            name = NoFlashAuto
            value = 24
            text = No flash, auto
            defineToken = PHOTO_FLASH_NONE_AUTO
         enum
            name = FlashAuto
            value = 25
            text = Flash, auto
            defineToken = PHOTO_FLASH_FLASH_AUTO
         enum
            name = FlashAutoNoReturnLight
            value = 29
            text = Flash, auto, no strobe return
            defineToken = PHOTO_FLASH_FLASH_AUTO_NORETURNLIGHT
         enum
            name = FlashAutoReturnLight
            value = 31
            text = Flash, auto, strobe return
            defineToken = PHOTO_FLASH_FLASH_AUTO_RETURNLIGHT
         enum
            name = NoFlashFunction
            value = 32
            text = No flash function
            defineToken = PHOTO_FLASH_NOFUNCTION
         enum
            name = FlashRedEye
            value = 65
            text = Flash, red-eye
            defineToken = PHOTO_FLASH_FLASH_REDEYE
         enum
            name = FlashRedEyeNoReturnLight
            value = 69
            text = Flash, red-eye, no strobe return
            defineToken = PHOTO_FLASH_FLASH_REDEYE_NORETURNLIGHT
         enum
            name = FlashRedEyeReturnLight
            value = 71
            text = Flash, red-eye, strobe return
            defineToken = PHOTO_FLASH_FLASH_REDEYE_RETURNLIGHT
         enum
            name = FlashCompulsoryRedEye
            value = 73
            text = Flash, compulsory, red-eye
            defineToken = PHOTO_FLASH_FLASH_COMPULSORY_REDEYE
         enum
            name = FlashCompulsoryRedEyeNoReturnLight
            value = 77
            text = Flash, compulsory, red-eye, no strobe return
            defineToken = PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_NORETURNLIGHT
         enum
            name = FlashCompulsoryRedEyeReturnLight
            value = 79
            text = Flash, compulsory, red-eye, strobe return
            defineToken = PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_RETURNLIGHT
         enum
            name = FlashAutoRedEye
            value = 89
            text = Flash, auto, red-eye
            defineToken = PHOTO_FLASH_FLASH_AUTO_REDEYE
         enum
            name = FlashAutoRedEyeNoReturnLight
            value = 93
            text = Flash, auto, no strobe return, red-eye
            defineToken = PHOTO_FLASH_FLASH_AUTO_REDEYE_NORETURNLIGHT
         enum
            name = FlashAutoRedEyeReturnLight
            value = 95
            text = Flash, auto, strobe return, red-eye
            defineToken = PHOTO_FLASH_FLASH_AUTO_REDEYE_RETURNLIGHT
```

## Windows Vista

```
propertyDescription
   name = System.Photo.Flash
   shellPKey = PKEY_Photo_Flash
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 37385
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = Byte
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 0
            text = No Flash
            defineName = PHOTO_FLASH_NONE
         enum
            value = 1
            text = Flash
            defineName = PHOTO_FLASH_FLASH
         enum
            value = 5
            text = Flash without strobe return
            defineName = PHOTO_FLASH_WITHOUTSTROBE
         enum
            value = 7
            text = Flash with strobe return
            defineName = PHOTO_FLASH_WITHSTROBE
         enum
            value = 9
            text = @propsys.dll,-39680
            defineName = PHOTO_FLASH_FLASH_COMPULSORY
         enum
            value = 13
            text = @propsys.dll,-39681
            defineName = PHOTO_FLASH_FLASH_COMPULSORY_NORETURNLIGHT
         enum
            value = 15
            text = @propsys.dll,-39682
            defineName = PHOTO_FLASH_FLASH_COMPULSORY_RETURNLIGHT
         enum
            value = 16
            text = @propsys.dll,-39683
            defineName = PHOTO_FLASH_NONE_COMPULSORY
         enum
            value = 24
            text = @propsys.dll,-39684
            defineName = PHOTO_FLASH_NONE_AUTO
         enum
            value = 25
            text = @propsys.dll,-39685
            defineName = PHOTO_FLASH_FLASH_AUTO
         enum
            value = 29
            text = @propsys.dll,-39686
            defineName = PHOTO_FLASH_FLASH_AUTO_NORETURNLIGHT
         enum
            value = 31
            text = @propsys.dll,-39687
            defineName = PHOTO_FLASH_FLASH_AUTO_RETURNLIGHT
         enum
            value = 32
            text = @propsys.dll,-39688
            defineName = PHOTO_FLASH_NOFUNCTION
         enum
            value = 65
            text = @propsys.dll,-39689
            defineName = PHOTO_FLASH_FLASH_REDEYE
         enum
            value = 69
            text = @propsys.dll,-39690
            defineName = PHOTO_FLASH_FLASH_REDEYE_NORETURNLIGHT
         enum
            value = 71
            text = @propsys.dll,-39691
            defineName = PHOTO_FLASH_FLASH_REDEYE_RETURNLIGHT
         enum
            value = 73
            text = @propsys.dll,-39692
            defineName = PHOTO_FLASH_FLASH_COMPULSORY_REDEYE
         enum
            value = 77
            text = @propsys.dll,-39693
            defineName = PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_NORETURNLIGHT
         enum
            value = 79
            text = @propsys.dll,-39694
            defineName = PHOTO_FLASH_FLASH_COMPULSORY_REDEYE_RETURNLIGHT
         enum
            value = 89
            text = @propsys.dll,-39695
            defineName = PHOTO_FLASH_FLASH_AUTO_REDEYE
         enum
            value = 93
            text = @propsys.dll,-39696
            defineName = PHOTO_FLASH_FLASH_AUTO_REDEYE_NORETURNLIGHT
         enum
            value = 95
            text = @propsys.dll,-39697
            defineName = PHOTO_FLASH_FLASH_AUTO_REDEYE_RETURNLIGHT
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[Exchangeable Image File Format for Digital Still Cameras: Exif Version 2.2](http://www.exif.org/Exif2-2.PDF)
</dt> <dt>

[propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx)
</dt> <dt>

[searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx)
</dt> <dt>

[labelInfo](https://msdn.microsoft.com/library/Bb773876(v=VS.85).aspx)
</dt> <dt>

[typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx)
</dt> <dt>

[displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx)
</dt> <dt>

[stringFormat](https://msdn.microsoft.com/library/Bb773886(v=VS.85).aspx)
</dt> <dt>

[booleanFormat](https://msdn.microsoft.com/library/Bb773862(v=VS.85).aspx)
</dt> <dt>

[numberFormat](https://msdn.microsoft.com/library/Bb773877(v=VS.85).aspx)
</dt> <dt>

[dateTimeFormat](https://msdn.microsoft.com/library/Bb773863(v=VS.85).aspx)
</dt> <dt>

[enumeratedList](https://msdn.microsoft.com/library/Bb773871(v=VS.85).aspx)
</dt> <dt>

[drawControl](https://msdn.microsoft.com/library/Bb773866(v=VS.85).aspx)
</dt> <dt>

[editControl](https://msdn.microsoft.com/library/Bb773868(v=VS.85).aspx)
</dt> <dt>

[filterControl](https://msdn.microsoft.com/library/Bb773874(v=VS.85).aspx)
</dt> <dt>

[queryControl](https://msdn.microsoft.com/library/Bb773883(v=VS.85).aspx)
</dt> </dl>

 

 



