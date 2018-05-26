---
Description: The SenderCompany property is a null-terminated string that contains the company name for the sender of the fax job. The SenderCompany property applies only to outgoing fax transmissions.
ms.assetid: abb984dc-d6f6-4aa0-be40-33066ce19b19
title: FaxJob.SenderCompany property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxJob.SenderCompany property

The **SenderCompany** property is a null-terminated string that contains the company name for the sender of the fax job. The **SenderCompany** property applies only to outgoing fax transmissions.

This property is read-only.

## Syntax


```VB
Property SenderCompany As String
```



## Property value

A **String** that receives the company name of the sender of the fax transmission.

## Remarks

If the sender's company is not available, the **SenderCompany** property contains an empty string.

**SenderCompany** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxJob**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxjob?branch=master)
</dt> <dt>

[**IFaxJobs**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxjobs?branch=master)
</dt> </dl>

 

 




