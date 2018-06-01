---
Description: The UserName property is a null-terminated string that contains the name of the user who submitted the fax job to the job queue. The UserName property applies only to outgoing fax transmissions.
ms.assetid: 725bef60-dfe8-443b-a8ee-268944bd6569
title: FaxJob.UserName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJob.UserName property

The **UserName** property is a null-terminated string that contains the name of the user who submitted the fax job to the job queue. The **UserName** property applies only to outgoing fax transmissions.

This property is read-only.

## Syntax


```VB
Property UserName As String
```



## Property value

A **String** that receives the name of the account that queued the fax job.

## Remarks

You can use the **UserName** property to retrieve the name of the person who initiated the fax job.

**UserName** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxJob**](-mfax-faxjob-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxJob**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjob)
</dt> <dt>

[**IFaxJobs**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjobs)
</dt> <dt>

[**SenderName**](-mfax-ifaxjob-get-sendername-vb.md)
</dt> </dl>

 

 




