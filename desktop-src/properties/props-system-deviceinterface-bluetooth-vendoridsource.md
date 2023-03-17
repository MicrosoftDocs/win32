---
description: Bluetooth device vendor identifier source.
ms.assetid: 1e46f850-5f10-4de2-90fb-f9fe6e88c4d8
title: System.DeviceInterface.Bluetooth.VendorIdSource
ms.topic: article
ms.date: 05/31/2018
---

# System.DeviceInterface.Bluetooth.VendorIdSource

Bluetooth device vendor identifier source.

| Value | Description |
|:-:|-|
| 0x01 | Bluetooth SIG-assigned Device ID Vendor ID value from the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/) |
| 0x02 | [USB Implementer’s Forum](https://www.usb.org/developers) assigned Vendor ID value |
| 0x00<br>0x03-0xFF | Reserved for future use |

See [Device Information Service](https://www.bluetooth.com/specifications/specs/device-information-service-1-1/) spec for more info.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511

```
propertyDescription
   name = System.DeviceInterface.Bluetooth.VendorIdSource
   shellPKey = PKEY_DeviceInterface_Bluetooth_VendorIdSource
   formatID = 2BD67D8B-8BEB-48D5-87E0-6CDA3428040A
   propID = 6
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Byte
      IsInnate = true
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

 

 
