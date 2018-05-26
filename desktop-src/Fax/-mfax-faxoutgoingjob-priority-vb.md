---
Description: The Priority property specifies the priority to use when sending the fax; for example, normal, low, or high priority.
ms.assetid: b4583bf9-ed29-45c1-a92a-5eabe629d721
title: FaxOutgoingJob.Priority property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingJob.Priority property

The **Priority** property specifies the priority to use when sending the fax; for example, normal, low, or high priority.

This property is read-only.

## Syntax


```VB
Property Priority As Integer
```



## Property value

A value from the [**FAX\_PRIORITY\_TYPE\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_priority_type_enum?branch=master) enumeration, specifying the fax job's priority.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-outgoing-jobs.md)
</dt> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingjob?branch=master)
</dt> </dl>

 

 




