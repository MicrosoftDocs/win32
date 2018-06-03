---
Description: The canonical type of the item.
ms.assetid: 530ba98a-09fd-438b-8872-9eee47f0cf54
title: System.ItemType
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

If there is no canonical type, the value is VT\_EMPTY. If the item is a file ([System.FileName](https://www.bing.com/search?q=System.FileName) is not VT\_EMPTY), the value is the same as [System.FileExtension](https://www.bing.com/search?q=System.FileExtension). Use [System.ItemTypeText](https://www.bing.com/search?q=System.ItemTypeText) when you want to display the type to end users in a view.

> [!Note]  
> If the item is a file, passing the [System.ItemType](https://www.bing.com/search?q=System.ItemType) value to [**PSFormatForDisplay**](https://www.bing.com/search?q=**PSFormatForDisplay**) results in the same value as [System.ItemTypeText](https://www.bing.com/search?q=System.ItemTypeText).

 

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
</dt> <dt>

[Programmatic Identifiers](https://msdn.microsoft.com/windows/desktop/f2b666d6-bf22-47b5-87e1-8de5ff51c152)
</dt> </dl>

 

 



