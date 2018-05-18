---
Description: 'The AllowPersonalCoverPages property is a Boolean value that indicates whether fax client applications can include a user-designed cover page with fax transmissions.'
ms.assetid: '22942a11-e689-4b48-bed0-ac1f4bef706b'
title: 'FaxOutgoingQueue.AllowPersonalCoverPages property'
---

# FaxOutgoingQueue.AllowPersonalCoverPages property

The AllowPersonalCoverPages property is a Boolean value that indicates whether fax client applications can include a user-designed cover page with fax transmissions.

This property is read/write.

## Syntax


```VB
Property AllowPersonalCoverPages As Boolean
```



## Property value

A **Boolean** that specifies or receives whether fax client applications can include a user-designed cover page with fax transmissions.

## Remarks

If this property is equal to **True**, clients can include personal cover page files with fax transmissions. If this property is equal to **False**, clients must use a common cover page file stored on the fax server.

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

 

 




