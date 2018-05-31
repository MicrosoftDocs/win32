---
Description: The LowQuotaWaterMark property is a value that specifies the lower threshold for the archive of outbound fax messages, in megabytes.
ms.assetid: 24b28cf9-54ef-4458-bef4-8d985ffc80fc
title: FaxOutgoingArchive.LowQuotaWaterMark property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingArchive.LowQuotaWaterMark property

The **LowQuotaWaterMark** property is a value that specifies the lower threshold for the archive of outbound fax messages, in megabytes. If the fax service has issued a warning in the event log, the service does not issue additional warnings until the size of the outbound archive drops below this value.

This property is read/write.

## Syntax


```VB
Property LowQuotaWaterMark As Long
```



## Property value

A **Long** value that receives the lower threshold for the archive of outbound fax messages.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.LowQuotaWaterMark**](-mfax-faxconfiguration-lowquotawatermark-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

To read this property, a user must have the [**farQUERY\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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

 

 




