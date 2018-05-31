---
Description: The RoutingInformation property is a null-terminated string that specifies the routing information for the fax job.
ms.assetid: ecd730cd-09b1-45d8-9f6b-69d5adeadb77
title: FaxJobStatus.RoutingInformation property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJobStatus.RoutingInformation property

The **RoutingInformation** property is a null-terminated string that specifies the routing information for the fax job.

This property is read-only.

## Syntax


```VB
Property RoutingInformation As String
```



## Property value

A **String** that receives the routing information for the fax job.

## Remarks

For more information about routing information, see the [**RoutingInfo**](/previous-versions/windows/desktop/api/FaxDev/ns-faxdev-_fax_dev_status) member of the [**FAX\_DEV\_STATUS**](/previous-versions/windows/desktop/api/FaxDev/ns-faxdev-_fax_dev_status) structure.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-registering-for-fax-events.md)
</dt> <dt>

[**FaxJobStatus**](-mfax-faxjobstatus.md)
</dt> <dt>

[**IFaxJobStatus**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxjobstatus)
</dt> </dl>

 

 




