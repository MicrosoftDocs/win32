---
Description: 'The Count property returns the number of queued fax jobs associated with the connected fax server.'
ms.assetid: 'a6760eb2-f98c-41f5-84c5-698a512038e2'
title: 'FaxJobs.Count property'
---

# FaxJobs.Count property

The **Count** property returns the number of queued fax jobs associated with the connected fax server.

This property is read-only.

## Syntax


```VB
Property Count As Long
```



## Property value

A **Long** that receives the number of fax jobs associated with the connected fax server.

## Remarks

After calling the **Count** property, a fax client application can call the [**Item**](-mfax-ifaxjobs-get-item-vb.md) property to retrieve one or more [FaxJob](-mfax-faxjob.md) objects.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxJobs**](-mfax-faxjobs-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[FaxJobs](-mfax-faxjobs.md)
</dt> <dt>

[**Item**](-mfax-ifaxjobs-get-item-vb.md)
</dt> <dt>

[FaxJob](-mfax-faxjob.md)
</dt> <dt>

[**GetJobs**](-mfax-ifaxserver-getjobs-vb.md)
</dt> </dl>

 

 




