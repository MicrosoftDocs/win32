---
Description: The Refresh method updates FaxJob object information for the associated fax job.
ms.assetid: 655acc35-304e-4e40-97c4-dd201fbad219
title: FaxJob.Refresh method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Call the **Refresh** method to poll the fax service for new information about a specified fax job. After you successfully call **Refresh**, you must call the appropriate [**IFaxJob**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxjob?branch=master) interface method to retrieve new attribute values that are valid.

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

[**IFaxJob**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxjob?branch=master)
</dt> <dt>

[**IFaxJobs**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxjobs?branch=master)
</dt> </dl>

 

 




