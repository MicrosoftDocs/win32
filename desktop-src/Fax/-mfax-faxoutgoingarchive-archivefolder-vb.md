---
Description: 'The ArchiveFolder property is a null-terminated string that specifies the folder location on the fax server for archived outbound faxes.'
ms.assetid: '8352f192-a485-4864-a12c-8e7c02263a63'
title: 'FaxOutgoingArchive.ArchiveFolder property'
---

# FaxOutgoingArchive.ArchiveFolder property

The **ArchiveFolder** property is a null-terminated string that specifies the folder location on the fax server for archived outbound faxes.

This property is read-only.

## Syntax


```VB
Property ArchiveFolder As String
```



## Property value

A **String** that receives Null-terminated string that specifies the fully qualified path and file name of the location in which the fax service archives outbound faxes.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.ArchiveLocation**](-mfax-faxconfiguration-archivelocation-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

To read or to write to this property, a user must have the [**farQUERY\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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
</dt> <dt>

[**FaxConfiguration**](-mfax-faxconfiguration.md)
</dt> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> </dl>

 

 




