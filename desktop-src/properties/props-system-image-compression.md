---
description: The algorithm used to compress the image.
ms.assetid: b355351d-b0b4-4f5d-a440-fc408a29e700
title: System.Image.Compression
ms.topic: article
ms.date: 05/31/2018
---

# System.Image.Compression

The algorithm used to compress the image.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Image.Compression
   shellPKey = PKEY_Image_Compression
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 259
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt16
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Uncompressed
            value = 1
            text = Uncompressed
            defineToken = IMAGE_COMPRESSION_UNCOMPRESSED
         enum
            name = CCITT.T3
            value = 2
            text = CCITT T.3
            defineToken = IMAGE_COMPRESSION_CCITT_T3
         enum
            name = CCITT.T4
            value = 3
            text = CCITT T.4
            defineToken = IMAGE_COMPRESSION_CCITT_T4
         enum
            name = CCITT.T6
            value = 4
            text = CCITT T.6
            defineToken = IMAGE_COMPRESSION_CCITT_T6
         enum
            name = LZW
            value = 5
            text = LZW
            defineToken = IMAGE_COMPRESSION_LZW
         enum
            name = JPEG
            value = 6
            text = JPEG
            defineToken = IMAGE_COMPRESSION_JPEG
         enum
            name = PackBits
            value = 32773
            text = PackBits
            defineToken = IMAGE_COMPRESSION_PACKBITS
```

## Windows Vista

```
propertyDescription
   name = System.Image.Compression
   shellPKey = PKEY_Image_Compression
   formatID = 14B81DA1-0135-4D31-96D9-6CBFC9671A99
   propID = 259
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt16
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 1
            text = Uncompressed
            defineName = IMAGE_COMPRESSION_UNCOMPRESSED
         enum
            value = 2
            text = CCITT T.3
            defineName = IMAGE_COMPRESSION_CCITT_T3
         enum
            value = 3
            text = CCITT T.4
            defineName = IMAGE_COMPRESSION_CCITT_T4
         enum
            value = 4
            text = CCITT T.6
            defineName = IMAGE_COMPRESSION_CCITT_T6
         enum
            value = 5
            text = LZW
            defineName = IMAGE_COMPRESSION_LZW
         enum
            value = 6
            text = JPEG
            defineName = IMAGE_COMPRESSION_JPEG
         enum
            value = 32773
            text = PackBits
            defineName = IMAGE_COMPRESSION_PACKBITS
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

 

 
