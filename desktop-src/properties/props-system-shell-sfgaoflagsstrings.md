---
description: Expresses the SFGAO flags as string values, and is used as a query optimization.
ms.assetid: b4ae5ec8-191b-4623-8968-1fbf69cc2eb3
title: System.Shell.SFGAOFlagsStrings
ms.topic: article
ms.date: 05/31/2018
---

# System.Shell.SFGAOFlagsStrings

Expresses the SFGAO flags as string values, and is used as a query optimization.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8

```
propertyDescription
   name = System.Shell.SFGAOFlagsStrings
   shellPKey = PKEY_Shell_SFGAOFlagsStrings
   formatID = D6942081-D53B-443D-AD47-5E059D9CD27A
   propID = 2
   SearchInfo
      InInvertedIndex = true
      IsColumn = false
   typeInfo
      type = Multivalue String
      EnumeratedList
         UseValueForDefault = True
         enum
            name = FileSys
            value = filesys
            text = filesys
            defineToken = SFGAOSTR_FILESYS
            defineComment = SFGAO_FILESYSTEM
         enum
            name = FileSysAncestor
            value = fileanc
            text = fileanc
            defineToken = SFGAOSTR_FILEANC
            defineComment = SFGAO_FILESYSANCESTOR
         enum
            name = StorageAncestor
            value = storageanc
            text = storageanc
            defineToken = SFGAOSTR_STORAGEANC
            defineComment = SFGAO_STORAGEANCESTOR
         enum
            name = Stream
            value = stream
            text = stream
            defineToken = SFGAOSTR_STREAM
            defineComment = SFGAO_STREAM
         enum
            name = Link
            value = link
            text = link
            defineToken = SFGAOSTR_LINK
            defineComment = SFGAO_LINK
         enum
            name = Hidden
            value = hidden
            text = hidden
            defineToken = SFGAOSTR_HIDDEN
            defineComment = SFGAO_HIDDEN
         enum
            name = Superhidden
            value = superhidden
            text = superhidden
            defineToken = SFGAOSTR_SUPERHIDDEN
            defineComment = SFGAO_SUPERHIDDEN
         enum
            name = Folder
            value = folder
            text = folder
            defineToken = SFGAOSTR_FOLDER
            defineComment = SFGAO_FOLDER
         enum
            name = NonEnumerated
            value = nonenum
            text = nonenum
            defineToken = SFGAOSTR_NONENUM
            defineComment = SFGAO_NONENUMERATED
         enum
            name = Browsable
            value = browsable
            text = browsable
            defineToken = SFGAOSTR_BROWSABLE
            defineComment = SFGAO_BROWSABLE
         enum
            name = System
            value = system
            text = system
            defineToken = SFGAOSTR_SYSTEM
            defineComment = SFGAO_SYSTEM
```

## Windows 7

```
propertyDescription
   name = System.Shell.SFGAOFlagsStrings
   shellPKey = PKEY_Shell_SFGAOFlagsStrings
   formatID = D6942081-D53B-443D-AD47-5E059D9CD27A
   propID = 2
   SearchInfo
      InInvertedIndex = true
      IsColumn = false
   typeInfo
      type = Multivalue String
      EnumeratedList
         UseValueForDefault = True
         enum
            name = FileSys
            value = filesys
            text = filesys
            defineToken = SFGAOSTR_FILESYS
            defineComment = SFGAO_FILESYSTEM
         enum
            name = FileSysAncestor
            value = fileanc
            text = fileanc
            defineToken = SFGAOSTR_FILEANC
            defineComment = SFGAO_FILESYSANCESTOR
         enum
            name = StorageAncestor
            value = storageanc
            text = storageanc
            defineToken = SFGAOSTR_STORAGEANC
            defineComment = SFGAO_STORAGEANCESTOR
         enum
            name = Stream
            value = stream
            text = stream
            defineToken = SFGAOSTR_STREAM
            defineComment = SFGAO_STREAM
         enum
            name = Link
            value = link
            text = link
            defineToken = SFGAOSTR_LINK
            defineComment = SFGAO_LINK
         enum
            name = Hidden
            value = hidden
            text = hidden
            defineToken = SFGAOSTR_HIDDEN
            defineComment = SFGAO_HIDDEN
         enum
            name = Superhidden
            value = superhidden
            text = superhidden
            defineToken = SFGAOSTR_SUPERHIDDEN
            defineComment = SFGAO_SUPERHIDDEN
         enum
            name = Folder
            value = folder
            text = folder
            defineToken = SFGAOSTR_FOLDER
            defineComment = SFGAO_FOLDER
         enum
            name = NonEnumerated
            value = nonenum
            text = nonenum
            defineToken = SFGAOSTR_NONENUM
            defineComment = SFGAO_NONENUMERATED
         enum
            name = Browsable
            value = browsable
            text = browsable
            defineToken = SFGAOSTR_BROWSABLE
            defineComment = SFGAO_BROWSABLE
```

## Windows Vista

```
propertyDescription
   name = System.Shell.SFGAOFlagsStrings
   shellPKey = PKEY_Shell_SFGAOFlagsStrings
   formatID = D6942081-D53B-443D-AD47-5E059D9CD27A
   propID = 2
   SearchInfo
      InInvertedIndex = true
      IsColumn = false
   typeInfo
      type = Multivalue String
      EnumeratedList
         UseValueForDefault = True
         enum
            value = filesys
            text = filesys
            defineName = SFGAOSTR_FILESYS
            defineComment = SFGAO_FILESYSTEM
         enum
            value = fileanc
            text = fileanc
            defineName = SFGAOSTR_FILEANC
            defineComment = SFGAO_FILESYSANCESTOR
         enum
            value = storageanc
            text = storageanc
            defineName = SFGAOSTR_STORAGEANC
            defineComment = SFGAO_STORAGEANCESTOR
         enum
            value = stream
            text = stream
            defineName = SFGAOSTR_STREAM
            defineComment = SFGAO_STREAM
         enum
            value = link
            text = link
            defineName = SFGAOSTR_LINK
            defineComment = SFGAO_LINK
         enum
            value = hidden
            text = hidden
            defineName = SFGAOSTR_HIDDEN
            defineComment = SFGAO_HIDDEN
         enum
            value = folder
            text = folder
            defineName = SFGAOSTR_FOLDER
            defineComment = SFGAO_FOLDER
         enum
            value = nonenum
            text = nonenum
            defineName = SFGAOSTR_NONENUM
            defineComment = SFGAO_NONENUMERATED
         enum
            value = browsable
            text = browsable
            defineName = SFGAOSTR_BROWSABLE
            defineComment = SFGAO_BROWSABLE
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

 

 
