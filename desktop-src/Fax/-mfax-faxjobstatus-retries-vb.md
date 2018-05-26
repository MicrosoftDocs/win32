---
Description: The Retries property is a value that indicates the number of times that the fax service attempted to transmit a fax job when the initial attempt failed.
ms.assetid: d1eb3b30-5a02-482a-b781-51afc9818590
title: FaxJobStatus.Retries property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxJobStatus.Retries property

The **Retries** property is a value that indicates the number of times that the fax service attempted to transmit a fax job when the initial attempt failed.

This property is read-only.

## Syntax


```VB
Property Retries As Long
```



## Property value

A **Long** that receives the number of times that the fax service attempted to transmit a fax job when the initial attempt failed.

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

[**IFaxJobStatus**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxjobstatus?branch=master)
</dt> </dl>

 

 




