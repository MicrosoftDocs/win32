---
Description: The BillingCode property is a null-terminated string that contains an optional billing code that applies to the fax job.
ms.assetid: 7772502c-623d-47f9-adbe-87d32bac8219
title: FaxJob.BillingCode property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxJob.BillingCode property

The **BillingCode** property is a null-terminated string that contains an optional billing code that applies to the fax job.

This property is read-only.

## Syntax


```VB
Property BillingCode As String
```



## Property value

A **String** that receives an application- or server-specific billing code that applies to the fax job. The fax server uses the string to generate an entry in the fax event log. Billing codes are optional.

## Remarks

If billing information is not available, the **BillingCode** property contains an empty string.

**BillingCode** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

 

 




