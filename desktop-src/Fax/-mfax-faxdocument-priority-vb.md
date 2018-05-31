---
Description: The Priority property specifies the priority to use when sending the fax; for example, normal, low, or high priority.
ms.assetid: e3dc385d-51e6-4174-b1a5-ff48bde19995
title: FaxDocument.Priority property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.Priority property

The **Priority** property specifies the priority to use when sending the fax; for example, normal, low, or high priority.

This property is read/write.

## Syntax


```VB
Property Priority As Integer
```



## Property value

A variable of type [**FAX\_PRIORITY\_TYPE\_ENUM**](-mfax-fax-priority-type-enum.md) that specifies or receives the transmission priority. For possible values, see **FAX\_PRIORITY\_TYPE\_ENUM**.

## Remarks

By default, **Priority** is set to 0, which indicates low priority.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-sending-a-fax.md)
</dt> <dt>

[**FaxDocument**](-mfax-faxdocument.md)
</dt> <dt>

[**IFaxDocument**](-mfax-faxdocument-cpp.md)
</dt> </dl>

 

 




