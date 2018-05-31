---
Description: The CopyTiff method copies the Tagged Image File Format Class F (TIFF Class F) file associated with the inbound fax job to a file on the local computer.
ms.assetid: 3c9bef01-2a86-48b1-b2db-20d0dcc18f51
title: FaxIncomingJob.CopyTiff method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJob.CopyTiff method

The **CopyTiff** method copies the Tagged Image File Format Class F (TIFF Class F) file associated with the inbound fax job to a file on the local computer.

## Syntax


```VB
FaxIncomingJob.CopyTiff( _
  ByVal bstrTiffPath As String _
) As Long
```



## Parameters

<dl> <dt>

*bstrTiffPath* \[in\]
</dt> <dd>

Type: **String**

Null-terminated string that specifies a fully qualified path and file name on the local computer.

</dd> </dl>

## Remarks

To use this method, a user must have the [**farQUERY\_JOBS**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-incoming-queue.md)
</dt> <dt>

[**FaxIncomingJob**](-mfax-faxincomingjob.md)
</dt> <dt>

[**IFaxIncomingJob**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingjob)
</dt> </dl>

 

 




