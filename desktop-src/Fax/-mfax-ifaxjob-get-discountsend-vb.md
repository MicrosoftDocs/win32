---
Description: The DiscountSend property is a Boolean value that indicates whether the fax server will transmit the fax job during the discount rate period. The discount period applies only to outgoing fax transmissions.
ms.assetid: 16d4fbe5-0328-403f-8685-3fd9d588d8b1
title: FaxJob.DiscountSend property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJob.DiscountSend property

The **DiscountSend** property is a Boolean value that indicates whether the fax server will transmit the fax job during the discount rate period. The discount period applies only to outgoing fax transmissions.

This property is read-only.

## Syntax


```VB
Property DiscountSend As Boolean
```



## Property value

A **Boolean** that receives a value that indicates whether the fax server will schedule the job during the transmission discount period. If this parameter is equal to TRUE, transmission will occur during the discount period. A value of FALSE indicates that the fax service will send the job immediately.

## Remarks

To determine the period during which the discount rate applies, you can use the following IFaxServer properties.

-   [**DiscountRateStartMinute**](-mfax-ifaxserver-get-discountratestartminute-vb.md)
-   [**DiscountRateEndMinute**](-mfax-ifaxserver-get-discountrateendminute-vb.md)
-   [**DiscountRateStartHour**](-mfax-ifaxserver-get-discountratestarthour-vb.md)
-   [**DiscountRateEndHour**](-mfax-ifaxserver-get-discountrateendhour-vb.md)

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

[Managing Fax Jobs](-mfax-managing-fax-jobs.md)
</dt> </dl>

 

 




