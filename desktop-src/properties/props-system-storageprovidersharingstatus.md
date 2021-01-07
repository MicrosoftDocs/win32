---
description: This property represents a the most permissive share status for the file/folder specified by the storage provider.The share statuses from most to least permissive are Owned > Co-owned > Public > Shared > Private.StorageProviderSharingStatus is a readonly property.
ms.assetid: c3b93159-4279-4b27-b006-ab73e0beee9c
title: System.StorageProviderSharingStatus
ms.topic: article
ms.date: 05/31/2018
---

# System.StorageProviderSharingStatus

This property represents a the most permissive share status for the file/folder specified by the storage provider.The share statuses from most to least permissive are Owned > Co-owned > Public > Shared > Private.StorageProviderSharingStatus is a readonly property.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1

```
propertyDescription
   name = System.StorageProviderSharingStatus
   shellPKey = PKEY_StorageProviderSharingStatus
   formatID = FCEFF153-E839-4CF3-A9E7-EA22832094B8
   propID = 117
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = NotShared
            value = 0
            text
            defineToken = STORAGE_PROVIDER_SHARINGSTATUS_NOTSHARED
         enum
            name = Shared
            value = 1
            text = Shared
            defineToken = STORAGE_PROVIDER_SHARINGSTATUS_SHARED
         enum
            name = Private
            value = 2
            text
            defineToken = STORAGE_PROVIDER_SHARINGSTATUS_PRIVATE
         enum
            name = Public
            value = 3
            text = Public
            defineToken = STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC
         enum
            name = SharedOwned
            value = 4
            text = Shared (co-owned, owner)
            defineToken = STORAGE_PROVIDER_SHARINGSTATUS_SHARED_OWNED
         enum
            name = SharedCoOwned
            value = 5
            text = Shared (co-owned)
            defineToken = STORAGE_PROVIDER_SHARINGSTATUS_SHARED_COOWNED
         enum
            name = PublicOwned
            value = 6
            text = Public (co-owned, owner)
            defineToken = STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_OWNED
         enum
            name = PublicCoOwned
            value = 7
            text = Public (co-owned)
            defineToken = STORAGE_PROVIDER_SHARINGSTATUS_PUBLIC_COOWNED
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

 

 
