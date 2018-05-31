---
Description: The RegisteredEvents property is a value from an enumeration that indicates the types of fax service events a client application is listening for.
ms.assetid: 8a5bed59-4c4d-43db-96e2-9d9312e05983
title: FaxServer.RegisteredEvents property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxServer.RegisteredEvents property

The **RegisteredEvents** property is a value from an enumeration that indicates the types of fax service events a client application is listening for.

This property is read-only.

## Syntax


```VB
Property RegisteredEvents As Integer
```



## Property value

Value from the [**FAX\_SERVER\_EVENTS\_TYPE\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_server_events_type_enum) enumeration that indicates the types of events the fax service sends to client applications that are listening for events.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxServer**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxserver)
</dt> </dl>

 

 




