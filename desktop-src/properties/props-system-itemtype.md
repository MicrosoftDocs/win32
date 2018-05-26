---
Description: The canonical type of the item.
ms.assetid: 530ba98a-09fd-438b-8872-9eee47f0cf54
title: System.ItemType
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.ItemType

The canonical type of the item.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ItemType
   shellPKey = PKEY_ItemType
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 11
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

The value for System.ItemType is intended to be programmatically parsed, and can be either:

-   A file extension that points to a ProgID value (HKEY\_CLASSES\_ROOT\\&lt;ProgID&gt;) holding the display name for the type.
-   A ProgID value (HKEY\_CLASSES\_RROOT\\&lt;ProgID&gt;), containing the display name for the type.

The FriendlyTypeName element of a ProgID should be a localized version of the application name (@winword.dll,-42), while the default value of the ProgID key is a non-localized name (Word.Document.12).

If there is no canonical type, the value is VT\_EMPTY. If the item is a file ([System.FileName](shell.props_System_FileName) is not VT\_EMPTY), the value is the same as [System.FileExtension](shell.props_System_FileExtension). Use [System.ItemTypeText](shell.props_System_ItemTypeText) when you want to display the type to end users in a view.

> [!Note]  
> If the item is a file, passing the [System.ItemType](shell.props_System_ItemType) value to [**PSFormatForDisplay**](shell.PSFormatForDisplay) results in the same value as [System.ItemTypeText](shell.props_System_ItemTypeText).

 

Example values:



| Path                                   | ItemType         |
|----------------------------------------|------------------|
| c:\\mydir\\bar\\hello.txt              | .txt             |
| \\\\server\\share\\mydir\\goodnews.doc | .doc             |
| \\\\server\\share\\folder              | Directory        |
| c:\\MyDir\\MyFolder                    | Directory        |
| \[desktop\]                            | Folder           |
| /Mailbox Account/Inbox/'Re: Hello!'    | MAPI/IPM.Message |



 

## Related topics

<dl> <dt>

[propertyDescription](shell.propdesc_schema_propertyDescription)
</dt> <dt>

[searchInfo](shell.propdesc_schema_searchInfo)
</dt> <dt>

[labelInfo](shell.propdesc_schema_labelInfo)
</dt> <dt>

[typeInfo](shell.propdesc_schema_typeInfo)
</dt> <dt>

[displayInfo](shell.propdesc_schema_displayInfo)
</dt> <dt>

[stringFormat](shell.propdesc_schema_stringFormat)
</dt> <dt>

[booleanFormat](shell.propdesc_schema_booleanFormat)
</dt> <dt>

[numberFormat](shell.propdesc_schema_numberFormat)
</dt> <dt>

[dateTimeFormat](shell.propdesc_schema_dateTimeFormat)
</dt> <dt>

[enumeratedList](shell.propdesc_schema_enumeratedList)
</dt> <dt>

[drawControl](shell.propdesc_schema_drawControl)
</dt> <dt>

[editControl](shell.propdesc_schema_editControl)
</dt> <dt>

[filterControl](shell.propdesc_schema_filterControl)
</dt> <dt>

[queryControl](shell.propdesc_schema_queryControl)
</dt> <dt>

[Programmatic Identifiers](shell.fa_progids)
</dt> </dl>

 

 



