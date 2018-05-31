---
Description: The ArchiveFolder property is a null-terminated string that specifies the folder location on the fax server for archived inbound faxes.
ms.assetid: 0ec3aa0d-6c45-450e-ae12-606d3b6e11ed
title: FaxIncomingArchive.ArchiveFolder property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingArchive.ArchiveFolder property

The **ArchiveFolder** property is a null-terminated string that specifies the folder location on the fax server for archived inbound faxes.

This property is read/write.

## Syntax


```VB
Property ArchiveFolder As String
```



## Property value

A **String** value that specifies or receives the fully qualified path and file name of the location in which the fax service archives inbound faxes.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.ArchiveLocation**](-mfax-faxconfiguration-archivelocation-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

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

[**IFaxIncomingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingarchive)
</dt> <dt>

[**FaxConfiguration**](-mfax-faxconfiguration.md)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> </dl>

 

 




