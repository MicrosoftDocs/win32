---
Description: 'The CopyTiff method copies the Tagged Image File Format Class F (TIFF Class F) file associated with the outbound fax job, to a file on the local computer.'
ms.assetid: 'da262d27-342d-4a90-9581-e7dafaea6f5a'
title: 'FaxOutgoingJob.CopyTiff method'
---

# FaxOutgoingJob.CopyTiff method

The **CopyTiff** method copies the Tagged Image File Format Class F (TIFF Class F) file associated with the outbound fax job, to a file on the local computer.

## Syntax


```VB
FaxOutgoingJob.CopyTiff( _
  ByVal bstrTiffPath As String _
) As Long
```



## Parameters

<dl> <dt>

*bstrTiffPath* 
</dt> <dd>

Type: **String**

Null-terminated string that contains a fully qualified path and file name on the local computer. The fax service will copy the TIFF Class F file associated with the outbound fax to the specified file.

</dd> </dl>

## Remarks

To use this method, a user must have the [**farSUBMIT\_LOW**](-mfax-fax-access-rights-enum.md) or **farQUERY\_JOBS** access right.

With the [**farSUBMIT\_LOW**](-mfax-fax-access-rights-enum.md) access right, users will be able to use this method only for their own faxes. With the **farQUERY\_JOBS** access right, users will be able to use this method for all faxes on the server.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-outgoing-jobs.md)
</dt> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob**](-mfax-faxoutgoingjob-cpp.md)
</dt> </dl>

 

 




