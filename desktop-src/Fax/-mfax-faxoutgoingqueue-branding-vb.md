---
Description: The Branding property is a Boolean value that indicates whether the fax service generates a brand (banner) at the top of outgoing fax transmissions.
ms.assetid: 8c7223e6-603b-4411-b2c1-814bcec9eb6e
title: FaxOutgoingQueue.Branding property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingQueue.Branding property

The **Branding** property is a Boolean value that indicates whether the fax service generates a brand (banner) at the top of outgoing fax transmissions. A brand contains transmission-related information, such as the transmitting station identifier, date, time, and page count.

This property is read/write.

## Syntax


```VB
Property Branding As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the fax service generates a brand (banner) at the top of outgoing fax transmissions.

## Remarks

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingQueue**](-mfax-faxoutgoingqueue.md)
</dt> <dt>

[**IFaxOutgoingQueue**](-mfax-faxoutgoingqueue-cpp.md)
</dt> <dt>

[Setting the Outgoing Queue Properties](-mfax-setting-the-outgoing-queue-properties.md)
</dt> </dl>

 

 




