---
Description: 'The HighQuotaWaterMark property is a value that specifies the upper threshold for the size of the archive of inbound fax messages, in megabytes.'
ms.assetid: '4a3ee635-51c1-4638-aedf-af359ac9dbb8'
title: 'FaxOutgoingArchive.HighQuotaWaterMark property'
---

# FaxOutgoingArchive.HighQuotaWaterMark property

The **HighQuotaWaterMark** property is a value that specifies the upper threshold for the size of the archive of inbound fax messages, in megabytes. If the archived fax messages in the archive exceed this value, and the [**SizeQuotaWarning**](-mfax-faxoutgoingarchive-sizequotawarning-vb.md) property is equal to **True**, the fax service issues a warning in the event log.

This property is read/write.

## Syntax


```VB
Property HighQuotaWaterMark As Long
```



## Property value

A **Long** value that receives the upper threshold for the size of the archive of outbound fax messages.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.HighQuotaWaterMark**](-mfax-faxconfiguration-highquotawatermark-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

To read or to write to this property, a user must have the [**farQUERY\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-outgoing-archive.md)
</dt> <dt>

[**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md)
</dt> <dt>

[**IFaxOutgoingArchive**](-mfax-faxoutgoingarchive-cpp.md)
</dt> </dl>

 

 




