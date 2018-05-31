---
Description: The UseDeviceTSID property is a Boolean value that indicates whether the fax service uses the device transmitting station identifier (TSID) instead of a sender TSID.
ms.assetid: 1ca178fd-6740-449a-842d-cabfc4f47a54
title: FaxOutgoingQueue.UseDeviceTSID property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingQueue.UseDeviceTSID property

The **UseDeviceTSID** property is a Boolean value that indicates whether the fax service uses the device transmitting station identifier (TSID) instead of a sender TSID.

This property is read/write.

## Syntax


```VB
Property UseDeviceTSID As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the fax service uses the device TSID instead of a user-specified TSID when submitting new jobs.

## Remarks

If this property is equal to **True**, the fax service uses the device TSID rather than a user-specified TSID. If this property is equal to **False**, the fax service uses a user-specified TSID.

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

[**IFaxOutgoingQueue**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingqueue)
</dt> <dt>

[Setting the Outgoing Queue Properties](-mfax-setting-the-outgoing-queue-properties.md)
</dt> </dl>

 

 




