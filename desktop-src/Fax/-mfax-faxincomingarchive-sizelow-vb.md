---
Description: The SizeLow property is a value that specifies the low 32-bit value (in bytes) for the size of the archive of inbound fax messages.
ms.assetid: 6ad44cc1-7068-42f2-a7a7-563470e58ae5
title: FaxIncomingArchive.SizeLow property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxIncomingArchive.SizeLow property

The **SizeLow** property is a value that specifies the low 32-bit value (in bytes) for the size of the archive of inbound fax messages.

This property is read-only.

## Syntax


```VB
Property SizeLow As Integer
```



## Property value

A value of type **Integer** that receives the low 32-bit value of the size of the archive of inbound fax messages.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows.

 

Because the archive may exceed 4 GB in size, the archive's size is described using two long values. SizeLow is the low 32-bit value of the archive size. SizeHigh is the high 32-bit value of the archive size. The size of the archive is: SizeLow + 4 GB \* SizeHigh.

If both the **SizeLow** and [**SizeHigh**](-mfax-faxincomingarchive-sizehigh-vb.md) properties have the value 0xffffffff, they specify an invalid archive size, and you should ignore both property values.

To read this property, a user must have the [****farQUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

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

 

 




