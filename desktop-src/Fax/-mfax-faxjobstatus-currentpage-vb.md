---
Description: The CurrentPage property is a number that identifies the page that the fax service is actively processing.
ms.assetid: f93699bb-3391-4d64-8d54-4213abe5357e
title: FaxJobStatus.CurrentPage property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxJobStatus.CurrentPage property

The **CurrentPage** property is a number that identifies the page that the fax service is actively processing.

This property is read-only.

## Syntax


```VB
Property CurrentPage As Long
```



## Property value

A **Long** that receives the number of the page in the fax transmission that the fax service is currently processing.

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

 

 




