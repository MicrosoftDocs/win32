---
description: This property represents a list of share statuses for the file/folder specified by the storage provider.Each share status must be one of the known value specified by the enumerations belowStorageProviderShareStatuses is a readonly property, it should only be updated by the storage provider.
ms.assetid: 131bf48a-0ab9-4b1f-9625-6fca5d15219f
title: System.StorageProviderShareStatuses
ms.topic: article
ms.date: 05/31/2018
---

# System.StorageProviderShareStatuses

This property represents a list of share statuses for the file/folder specified by the storage provider.Each share status must be one of the known value specified by the enumerations belowStorageProviderShareStatuses is a readonly property, it should only be updated by the storage provider.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1

```
propertyDescription
   name = System.StorageProviderShareStatuses
   shellPKey = PKEY_StorageProviderShareStatuses
   formatID = FCEFF153-E839-4CF3-A9E7-EA22832094B8
   propID = 111
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = Multivalue String
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Private
            value = Private
            text = Private
            defineToken = STORAGE_PROVIDER_SHARE_STATUS_PRIVATE
            mnemonics = private
         enum
            name = Shared
            value = Shared
            text = Shared
            defineToken = STORAGE_PROVIDER_SHARE_STATUS_SHARED
            mnemonics = shared
         enum
            name = Public
            value = Public
            text = Public
            defineToken = STORAGE_PROVIDER_SHARE_STATUS_PUBLIC
            mnemonics = public
         enum
            name = Group
            value = Group
            text = Group
            defineToken = STORAGE_PROVIDER_SHARE_STATUS_GROUP
            mnemonics = group
         enum
            name = Owner
            value = Owner
            text = Owner
            defineToken = STORAGE_PROVIDER_SHARE_STATUS_OWNER
            mnemonics = owner
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

 

 
