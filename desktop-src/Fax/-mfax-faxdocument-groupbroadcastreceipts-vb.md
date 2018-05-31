---
Description: The GroupBroadcastReceipts property is a Boolean value that indicates whether to send an individual delivery receipt for each recipient of the broadcast, or to send a summary receipt for all the recipients.
ms.assetid: faf24ed7-094d-4b44-9c57-82d378bffda7
title: FaxDocument.GroupBroadcastReceipts property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.GroupBroadcastReceipts property

The **GroupBroadcastReceipts** property is a Boolean value that indicates whether to send an individual delivery receipt for each recipient of the broadcast, or to send a summary receipt for all the recipients.

This property is read/write.

## Syntax


```VB
Property GroupBroadcastReceipts As Boolean
```



## Property value

A **Boolean** that specifies or receives a value indicating whether to send an individual delivery receipt for each recipient of the broadcast or to send a summary receipt for all the recipients.

<dt>



 (True)


</dt> <dd>

A summary receipt will be sent.

</dd> <dt>



 (False)


</dt> <dd>

Default. An individual delivery receipt will be sent to each recipient of the broadcast.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-broadcasting-a-fax.md)
</dt> <dt>

[**FaxDocument**](-mfax-faxdocument.md)
</dt> <dt>

[**IFaxDocument**](-mfax-faxdocument-cpp.md)
</dt> </dl>

 

 




