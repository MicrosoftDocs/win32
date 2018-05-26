---
Description: The LowQuotaWaterMark property is a value that specifies the lower warning threshold for the archive of inbound fax messages, in megabytes.
ms.assetid: 7880a723-1cc8-4bdf-98c7-fcb3013130ce
title: FaxIncomingArchive.LowQuotaWaterMark property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingArchive.LowQuotaWaterMark property

The **LowQuotaWaterMark** property is a value that specifies the lower warning threshold for the archive of inbound fax messages, in megabytes. If the fax service has issued a warning in the event log, the service does not issue additional warnings until the size of the inbound archive drops below this value.

This property is read/write.

## Syntax


```VB
Property LowQuotaWaterMark As Integer
```



## Property value

A value of type **Integer** that specifies or receives the lower threshold for the archive of inbound fax messages.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.LowQuotaWaterMark**](-mfax-faxconfiguration-lowquotawatermark-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxIncomingArchive**](-mfax-faxincomingarchive.md)
</dt> </dl>

 

 




