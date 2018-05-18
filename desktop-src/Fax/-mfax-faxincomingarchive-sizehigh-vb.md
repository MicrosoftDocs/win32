---
Description: 'The SizeHigh property is a value that specifies the high 32-bit value (in bytes) for the size of the archive of inbound fax messages.'
ms.assetid: '65b02e5f-45c1-48e7-8e9b-ce669e393c99'
title: 'FaxIncomingArchive.SizeHigh property'
---

# FaxIncomingArchive.SizeHigh property

The **SizeHigh** property is a value that specifies the high 32-bit value (in bytes) for the size of the archive of inbound fax messages.

This property is read-only.

## Syntax


```VB
Property SizeHigh As Integer
```



## Property value

A value of type **Integer** that receives the high 32-bit value of the size of the archive of inbound fax messages.

## Remarks

> [!Note]  
> This property is not supported in Windows Vista, Windows Server 2008, and later versions of Windows.

 

Because the archive may exceed 4 GB in size, the archive's size is described using two long values. SizeLow is the low 32-bit value of the archive size. SizeHigh is the high 32-bit value of the archive size. The size of the archive is: SizeLow + 4 GB \* SizeHigh.

If both the [**SizeLow**](-mfax-faxincomingarchive-sizelow-vb.md) and **SizeHigh** properties have the value 0xffffffff, they specify an invalid archive size, and you should ignore both property values.

To read or to write to this property, a user must have the [****farQUERY\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

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

[**IFaxIncomingArchive**](-mfax-faxincomingarchive-cpp.md)
</dt> </dl>

 

 




