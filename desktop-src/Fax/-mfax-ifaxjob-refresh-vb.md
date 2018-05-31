---
Description: The Refresh method updates FaxJob object information for the associated fax job.
ms.assetid: 655acc35-304e-4e40-97c4-dd201fbad219
title: FaxJob.Refresh method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJob.Refresh method

The **Refresh** method updates [FaxJob](-mfax-faxjob.md) object information for the associated fax job.

## Syntax


```VB
FaxJob.Refresh() As Long
```



## Parameters

This method has no parameters.

## Remarks

Call the **Refresh** method to poll the fax service for new information about a specified fax job. After you successfully call **Refresh**, you must call the appropriate [**IFaxJob**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxjob) interface method to retrieve new attribute values that are valid.

It is recommended that you limit calls to this method because frequent calls to **Refresh** can degrade system performance.

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
</dt> </dl>

 

 




