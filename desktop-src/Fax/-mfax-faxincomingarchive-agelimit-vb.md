---
Description: The AgeLimit property is a value that indicates the number of days that the fax service retains fax messages in the archive of inbound faxes.
ms.assetid: 6005a197-de27-4846-8d95-c8fa28e4a38a
title: FaxIncomingArchive.AgeLimit property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingArchive.AgeLimit property

The **AgeLimit** property is a value that indicates the number of days that the fax service retains fax messages in the archive of inbound faxes. The fax service deletes messages from the inbound archive when they exceed the age limit. If the value of this property is zero, the fax service does not enforce an age limit.

This property is read/write.

## Syntax


```VB
Property AgeLimit As Integer
```



## Property value

A value of type **Integer** that specifies or receives the number of days that the fax service retains fax messages in the archive of inbound faxes.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.ArchiveAgeLimit**](-mfax-faxconfiguration-archiveagelimit-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-incoming-archive.md)
</dt> <dt>

[**FaxIncomingArchive**](-mfax-faxincomingarchive.md)
</dt> <dt>

[**IFaxIncomingArchive**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingarchive?branch=master)
</dt> </dl>

 

 




