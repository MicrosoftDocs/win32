---
Description: The SizeLow property is a value that specifies the low 32-bit value (in bytes) for the size of the archive of outgoing fax messages.
ms.assetid: 781341d3-652d-4f50-95df-ad14daac1798
title: FaxOutgoingArchive.SizeLow property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingArchive.SizeLow property

The **SizeLow** property is a value that specifies the low 32-bit value (in bytes) for the size of the archive of outgoing fax messages.

This property is read-only.

## Syntax


```VB
Property SizeLow As Long
```



## Property value

A **Long** that receives the low 32-bit value of the size of the archive of outgoing fax messages.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.ArchiveSizeLow**](-mfax-faxconfiguration-archivesizelow-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

Because the archive may exceed 4 gigabytes (GB) in size, the archive size is described using two long values. **SizeLow** is the low 32-bit value of the archive size. [**SizeHigh**](-mfax-faxoutgoingarchive-sizehigh-vb.md) is the high 32-bit value of the archive size. The size of the archive is: **SizeLow** + 4 GB \* **SizeHigh**. If both the **SizeLow** and **SizeHigh** properties have the value 0xffffffff, they specify an invalid archive size, and you should ignore both property values.

To read this property, a user must have the [**farQUERY\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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

[**IFaxOutgoingArchive**](-mfax-faxoutgoingarchive-cpp.md)
</dt> </dl>

 

 




