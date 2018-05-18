---
Description: 'The Refresh method refreshes FaxOutgoingJob object information from the fax server.'
ms.assetid: '191c6e5e-4c51-4963-a335-0375f936c52a'
title: 'FaxOutgoingJob.Refresh method'
---

# FaxOutgoingJob.Refresh method

The Refresh method refreshes [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md) object information from the fax server.

## Syntax


```VB
FaxOutgoingJob.Refresh() As Long
```



## Parameters

This method has no parameters.

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

 

 




