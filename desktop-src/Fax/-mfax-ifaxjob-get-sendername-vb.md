---
Description: The SenderName property is a null-terminated string that contains the name of the sender who initiated the fax job. The SenderName property applies only to outgoing fax transmissions.
ms.assetid: c0fc5c5a-8451-4c5b-9b11-b3dcb45e5f80
title: FaxJob.SenderName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJob.SenderName property

The **SenderName** property is a null-terminated string that contains the name of the sender who initiated the fax job. The **SenderName** property applies only to outgoing fax transmissions.

This property is read-only.

## Syntax


```VB
Property SenderName As String
```



## Property value

A **String** that receives the name of the sender of the fax transmission. The string can be in first name, last name format.

## Remarks

If the sender's name is not available, the **SenderName** property contains an empty string.

You can call the [**UserName**](-mfax-ifaxjob-get-username-vb.md) method to retrieve the name of the account that queued the fax job.

**SenderName** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**UserName**](-mfax-ifaxjob-get-username-vb.md)
</dt> </dl>

 

 




