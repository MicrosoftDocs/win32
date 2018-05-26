---
Description: The UseArchive property is a Boolean value that indicates whether the fax service archives outbound fax messages.
ms.assetid: a7e48e8e-0364-4aaf-9fff-e2778b66d1c7
title: FaxOutgoingArchive.UseArchive property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingArchive.UseArchive property

The **UseArchive** property is a Boolean value that indicates whether the fax service archives outbound fax messages. If this parameter is equal to **True**, the fax service archives outbound fax messages. If this parameter is equal to **False**, the fax service does not archive outbound faxes.

This property is read/write.

## Syntax


```VB
Property UseArchive As Boolean
```



## Property value

A **Boolean** that specifies or receives whether the fax service archives outbound fax messages.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows. To access this property in Windows Vista, Windows Server 2008, and later versions of Windows, get the [**FaxConfiguration.UseArchive**](-mfax-faxconfiguration-usearchive-vb.md) property from the [**FaxServer**](-mfax-faxserver.md) object.

 

To read or to write to this property, a user must have the [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

[**IFaxOutgoingArchive**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingarchive?branch=master)
</dt> </dl>

 

 




