---
Description: The DisplayName property is a null-terminated string that contains the user-friendly name to associate with the fax job.
ms.assetid: f8dd3a5a-9f3d-4c3e-b023-ee9f9aef2930
title: FaxJob.DisplayName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJob.DisplayName property

The **DisplayName** property is a null-terminated string that contains the user-friendly name to associate with the fax job.

This property is read-only.

## Syntax


```VB
Property DisplayName As String
```



## Property value

A **String** that receives the user-friendly name to associate with the fax job. This is the name that appears in the job queue.

## Remarks

You can use the [**JobId**](-mfax-ifaxjob-get-jobid-vb.md) property to uniquely identify a fax job because it is possible for multiple fax jobs to have the same **DisplayName** property.

**DisplayName** method allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**JobId**](-mfax-ifaxjob-get-jobid-vb.md)
</dt> </dl>

 

 




