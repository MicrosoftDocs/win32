---
Description: The RoutingInformation property is a null-terminated string that specifies routing information for the inbound fax job.
ms.assetid: 289787f4-7f00-4352-b20c-278712e8c3a1
title: FaxIncomingJob.RoutingInformation property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingJob.RoutingInformation property

The **RoutingInformation** property is a null-terminated string that specifies routing information for the inbound fax job.

This property is read-only.

## Syntax


```VB
Property RoutingInformation As String
```



## Property value

A **String** that receives the inbound routing information for the fax job.

## Remarks

For more information about routing information, see the [**RoutingInfo**](/windows/previous-versions/FaxDev/ns-faxdev-_fax_dev_status?branch=master) member of the [**FAX\_DEV\_STATUS**](/windows/previous-versions/FaxDev/ns-faxdev-_fax_dev_status?branch=master) structure.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-incoming-queue.md)
</dt> <dt>

[**FaxIncomingJob**](-mfax-faxincomingjob.md)
</dt> <dt>

[**IFaxIncomingJob**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingjob?branch=master)
</dt> </dl>

 

 




