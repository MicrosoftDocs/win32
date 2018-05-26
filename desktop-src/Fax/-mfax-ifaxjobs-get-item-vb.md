---
Description: The Item property creates a FaxJob object for a specified fax job. The object allows enumeration of the fax jobs associated with a connected fax server.
ms.assetid: 2e9c8e57-6d2e-49fd-8879-1213c505f51a
title: FaxJobs.Item property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxJobs.Item property

The **Item** property creates a [FaxJob](-mfax-faxjob.md) object for a specified fax job. The object allows enumeration of the fax jobs associated with a connected fax server.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal lCount As Long _
) As Object
```



## Property value

An **Object** that receives a [FaxJob](-mfax-faxjob.md) object.

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

[FaxJob](-mfax-faxjob.md)
</dt> </dl>

 

 




