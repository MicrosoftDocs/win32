---
Description: The value that specifies the low-order 32-bit value (in bytes) for the size of the fax message archive.
ms.assetid: 0ab92bf2-cf0a-471c-8fa0-2148f24916b1
title: FaxConfiguration.ArchiveSizeLow property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxConfiguration.ArchiveSizeLow property

The value that specifies the low-order 32-bit value (in bytes) for the size of the fax message archive.

This property is read-only.

## Syntax


```VB
Property ArchiveSizeLow As Integer
```



## Property value

A value of type **Integer** that receives the low-order 32-bit value of the size of the fax message archive.

## Remarks

Because the archive may exceed 4 gigabytes (GB) in size, the archive size is described using two long values. [**ArchiveSizeLow**](/windows/previous-versions/Faxcomex/nf-faxcomex-ifaxconfiguration-get_archivesizelow?branch=master) is the low 32-bit value of the archive size. [**ArchiveSizeHigh**](/windows/previous-versions/Faxcomex/nf-faxcomex-ifaxconfiguration-get_archivesizehigh?branch=master) is the high 32-bit value of the archive size. The size of the archive is: **ArchiveSizeLow** + 4 GB \* **ArchiveSizeHigh**.

If both the [**ArchiveSizeLow**](/windows/previous-versions/Faxcomex/nf-faxcomex-ifaxconfiguration-get_archivesizelow?branch=master) and [**ArchiveSizeHigh**](/windows/previous-versions/Faxcomex/nf-faxcomex-ifaxconfiguration-get_archivesizehigh?branch=master) properties have the value 0xffffffff, they specify an invalid archive size, and you should ignore both property values.

To read this property, a user must have the [**farQUERY\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxConfiguration**](-mfax-faxconfiguration.md)
</dt> <dt>

[**FaxConfiguration**](fax._mfax_ifaxconfiguration)
</dt> </dl>

 

 




