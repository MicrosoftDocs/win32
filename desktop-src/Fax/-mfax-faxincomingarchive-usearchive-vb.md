---
Description: The UseArchive property is a Boolean value that indicates whether the fax service archives inbound fax messages.
ms.assetid: c454022a-353f-4df7-8d24-17fc8ad4ec63
title: FaxIncomingArchive.UseArchive property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingArchive.UseArchive property

The **UseArchive** property is a Boolean value that indicates whether the fax service archives inbound fax messages. If this property is equal to **True**, the fax service archives inbound fax messages. If this property is equal to **False**, the fax service does not archive inbound faxes.

This property is read/write.

## Syntax


```VB
Property UseArchive As Boolean
```



## Property value

A value of type **Boolean** that indicates whether the fax service archives inbound fax messages.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.UseArchive**](-mfax-faxconfiguration-usearchive-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

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

 

 




