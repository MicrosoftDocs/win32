---
Description: The SizeQuotaWarning property is a Boolean value that indicates whether the fax service issues a warning in the event log when the size of the outbound archive exceeds the limit defined by the HighQuotaWaterMark property.
ms.assetid: ec1e9f9e-b3b0-4535-899f-e96a5c59a504
title: FaxOutgoingArchive.SizeQuotaWarning property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingArchive.SizeQuotaWarning property

The **SizeQuotaWarning** property is a Boolean value that indicates whether the fax service issues a warning in the event log when the size of the outbound archive exceeds the limit defined by the [**HighQuotaWaterMark**](-mfax-faxoutgoingarchive-highquotawatermark-vb.md) property.

This property is read/write.

## Syntax


```VB
Property SizeQuotaWarning As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the fax service issues a warning in the event log when the size of the outbound archive exceeds the limit defined by the [**HighQuotaWaterMark**](-mfax-faxoutgoingarchive-highquotawatermark-vb.md) property.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.SizeQuotaWarning**](-mfax-faxconfiguration-sizequotawarning-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

If this property is equal to **True**, the fax service issues a warning when the number of fax messages in the archive exceeds the limit. If this property is equal to **False**, the fax service does not issue a warning.

To read or to write to this property, a user must have the [**farQUERY\_CONFIG**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md)
</dt> </dl>

 

 




