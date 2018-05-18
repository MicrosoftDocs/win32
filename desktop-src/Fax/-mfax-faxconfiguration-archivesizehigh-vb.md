---
Description: 'The value that specifies the high-order 32-bit value (in bytes) for the size of the fax message archive.'
ms.assetid: '599b0eee-83fa-46fd-9420-19f6b4ab9b6b'
title: 'FaxConfiguration.ArchiveSizeHigh property'
---

# FaxConfiguration.ArchiveSizeHigh property

The value that specifies the high-order 32-bit value (in bytes) for the size of the fax message archive.

This property is read-only.

## Syntax


```VB
Property ArchiveSizeHigh As Integer
```



## Property value

A value of type **Integer** that receives the high-order 32-bit value of the size of the fax message archive.

## Remarks

Because the archive may exceed 4 gigabytes (GB) in size, the archive size is described using two long values. [**ArchiveSizeLow**](-mfax-ifaxconfiguration-archivesizelow.md) is the low 32-bit value of the archive size. [**ArchiveSizeHigh**](-mfax-ifaxconfiguration-archivesizehigh.md) is the high 32-bit value of the archive size. The size of the archive is: **ArchiveSizeLow** + 4 GB \* **ArchiveSizeHigh**.

If both the [**ArchiveSizeLow**](-mfax-ifaxconfiguration-archivesizelow.md) and [**ArchiveSizeHigh**](-mfax-ifaxconfiguration-archivesizehigh.md) properties have the value 0xffffffff, they specify an invalid archive size, and you should ignore both property values.

To read this property, a user must have the [**farQUERY\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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

 

 




