---
Description: The AgeLimit property is a value that indicates the number of days that the fax service retains fax messages in the archive of outbound faxes.
ms.assetid: 33476d8a-981a-49b2-a52f-0c150b070859
title: FaxOutgoingArchive.AgeLimit property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingArchive.AgeLimit property

The **AgeLimit** property is a value that indicates the number of days that the fax service retains fax messages in the archive of outbound faxes. The fax service deletes messages from the outbound archive when they exceed the age limit. If the value of this property is zero, the fax service does not enforce an age limit.

This property is read/write.

## Syntax


```VB
Property AgeLimit As Long
```



## Property value

A **Long** value that receives the number of days that the fax service retains fax messages in the archive of outbound faxes.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.ArchiveAgeLimit**](-mfax-faxconfiguration-archiveagelimit-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

To read or to write to this property, a user must have the [**farQUERY\_CONFIG**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-outgoing-archive.md)
</dt> <dt>

[**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md)
</dt> <dt>

[**IFaxOutgoingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingarchive)
</dt> </dl>

 

 




