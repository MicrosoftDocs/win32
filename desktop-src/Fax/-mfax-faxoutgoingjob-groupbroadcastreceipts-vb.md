---
Description: 'The GroupBroadcastReceipts property is a Boolean value that indicates whether to send an individual delivery receipt for each recipient of the broadcast or to send a summary receipt for all recipients.'
ms.assetid: 'f2627ec8-791e-4405-aa75-3355a8f8fa09'
title: 'FaxOutgoingJob.GroupBroadcastReceipts property'
---

# FaxOutgoingJob.GroupBroadcastReceipts property

The **GroupBroadcastReceipts** property is a Boolean value that indicates whether to send an individual delivery receipt for each recipient of the broadcast or to send a summary receipt for all recipients.

This property is read-only.

## Syntax


```VB
Property GroupBroadcastReceipts As Boolean
```



## Property value

A **Boolean** that receives whether to send an individual delivery receipt for each recipient of the broadcast or to send a summary receipt for all recipients.

<dt>

<span id="False"></span><span id="false"></span><span id="FALSE"></span>

<span id="False"></span><span id="false"></span><span id="FALSE"></span>**False** (False)


</dt> <dd>

Default. An individual delivery receipt will be sent to each recipient of the broadcast.

</dd> <dt>

<span id="True"></span><span id="true"></span><span id="TRUE"></span>

<span id="True"></span><span id="true"></span><span id="TRUE"></span>**True** (True)


</dt> <dd>

Only a summary receipt will be sent.

</dd> </dl>

## Remarks

Set the **GroupBroadcastReceipts** property for a document using the [**GroupBroadcastReceipts**](-mfax-faxdocument-groupbroadcastreceipts-vb.md) property.

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

[**IFaxOutgoingJob**](-mfax-faxoutgoingjob-cpp.md)
</dt> </dl>

 

 




