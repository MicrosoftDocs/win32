---
description: If VARIANT\_TRUE, the device installer is currently installing software.
ms.assetid: 7C62C1E3-D3F3-49ce-A19D-B3A1C14E24D6
title: System.Devices.IsSoftwareInstalling
ms.topic: article
ms.date: 05/31/2018
---

# System.Devices.IsSoftwareInstalling

If VARIANT\_TRUE, the device installer is currently installing software.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8

```
propertyDescription
   name = System.Devices.IsSoftwareInstalling
   shellPKey = PKEY_Devices_IsSoftwareInstalling
   formatID = 83DA6326-97A6-4088-9453-A1923F573B29
   propID = 9
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Boolean
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = SoftwareInstalling
            value = #TRUE#
            text = Device setup in progress
            defineToken = ISSOFTWAREINSTALLING_INSTALLING
```

## Windows 7

```
propertyDescription
   name = System.Devices.IsSoftwareInstalling
   shellPKey = PKEY_Devices_IsSoftwareInstalling
   formatID = 83DA6326-97A6-4088-9453-A1923F573B29
   propID = 9
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Boolean
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = SoftwareInstalling
            value = #TRUE#
            text = Software is installing for this device
            defineToken = ISSOFTWAREINSTALLING_INSTALLING
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

 

 
