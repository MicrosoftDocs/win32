---
Description: The Priority property specifies the priority used when sending the fax; for example, normal, low, or high priority.
ms.assetid: b1f20850-830f-4dd8-8427-2af80c094d06
title: FaxOutgoingMessage.Priority property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingMessage.Priority property

The **Priority** property specifies the priority used when sending the fax; for example, normal, low, or high priority.

This property is read-only.

## Syntax


```VB
Property Priority As Integer
```



## Property value

Value from the [**FAX\_PRIORITY\_TYPE\_ENUM**](-mfax-fax-priority-type-enum.md) enumeration that specifies the fax priority.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-outgoing-archive.md)
</dt> <dt>

[**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md)
</dt> <dt>

[**IFaxOutgoingMessage**](-mfax-faxoutgoingmessage-cpp.md)
</dt> </dl>

 

 




