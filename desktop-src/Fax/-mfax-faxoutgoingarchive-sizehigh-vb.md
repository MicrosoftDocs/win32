---
Description: The SizeHigh property is a value that specifies the high 32-bit value (in bytes) for the size of the archive of outgoing fax messages.
ms.assetid: 4284d609-416a-4207-bb2d-eb08a4764000
title: FaxOutgoingArchive.SizeHigh property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingArchive.SizeHigh property

The **SizeHigh** property is a value that specifies the high 32-bit value (in bytes) for the size of the archive of outgoing fax messages.

This property is read-only.

## Syntax


```VB
Property SizeHigh As Long
```



## Property value

A **Long** that receives the high 32-bit value of the size of the archive of outgoing fax messages.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.ArchiveSizeHigh**](-mfax-faxconfiguration-archivesizehigh-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

Because the archive may exceed 4 gigabytes (GB) in size, the archive size is described using two long values. [**SizeLow**](-mfax-faxoutgoingarchive-sizelow-vb.md) is the low 32-bit value of the archive size. **SizeHigh** is the high 32-bit value of the archive size. The size of the archive is: **SizeLow** + 4 GB \* **SizeHigh**. If both the **SizeLow** and **SizeHigh** properties have the value 0xffffffff, they specify an invalid archive size, and you should ignore both property values.

To read this property, a user must have the [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

[**IFaxOutgoingArchive**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingarchive?branch=master)
</dt> </dl>

 

 




