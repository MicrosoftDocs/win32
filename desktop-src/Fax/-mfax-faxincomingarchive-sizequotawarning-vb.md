---
Description: The SizeQuotaWarning property is a Boolean value that indicates whether the fax service issues a warning in the event log when the size of the inbound archive exceeds the limit defined by the HighQuotaWaterMark property.
ms.assetid: 5329c340-0e8c-478d-845b-7a8b748edc17
title: FaxIncomingArchive.SizeQuotaWarning property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingArchive.SizeQuotaWarning property

The **SizeQuotaWarning** property is a Boolean value that indicates whether the fax service issues a warning in the event log when the size of the inbound archive exceeds the limit defined by the [**HighQuotaWaterMark**](-mfax-faxincomingarchive-highquotawatermark-vb.md) property.

This property is read/write.

## Syntax


```VB
Property SizeQuotaWarning As Boolean
```



## Property value

A value of type **Boolean** that indicates whether the fax service issues a warning in the event log when the size of the inbound archive exceeds the limit defined by the [**HighQuotaWaterMark**](-mfax-faxincomingarchive-highquotawatermark-vb.md) property.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.SizeQuotaWarning**](-mfax-faxconfiguration-sizequotawarning-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

If this property is equal to **True**, the fax service will issue a warning when the number of fax messages exceeds the threshold. If this property is equal to **False**, the fax service does not issue a warning.

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-incoming-archive.md)
</dt> <dt>

[**FaxIncomingArchive**](-mfax-faxincomingarchive.md)
</dt> <dt>

[**IFaxIncomingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingarchive)
</dt> </dl>

 

 




