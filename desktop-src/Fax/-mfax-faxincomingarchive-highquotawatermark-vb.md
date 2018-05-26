---
Description: The HighQuotaWaterMark property is a value that specifies the upper warning threshold for the size of the archive of inbound fax messages, in megabytes.
ms.assetid: ce611bcf-5e9c-4f65-adc5-054a2f69b421
title: FaxIncomingArchive.HighQuotaWaterMark property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingArchive.HighQuotaWaterMark property

The **HighQuotaWaterMark** property is a value that specifies the upper warning threshold for the size of the archive of inbound fax messages, in megabytes. If the size of the archive exceeds this value, and the [**SizeQuotaWarning**](-mfax-faxincomingarchive-sizequotawarning-vb.md) property is equal to **True**, the fax service issues a warning in the event log.

This property is read/write.

## Syntax


```VB
Property HighQuotaWaterMark As Integer
```



## Property value

A value of type **Integer** that specifies or receives the upper threshold for the size of the archive of inbound fax messages.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.HighQuotaWaterMark**](-mfax-faxconfiguration-highquotawatermark-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

[**IFaxIncomingArchive**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxincomingarchive?branch=master)
</dt> </dl>

 

 




