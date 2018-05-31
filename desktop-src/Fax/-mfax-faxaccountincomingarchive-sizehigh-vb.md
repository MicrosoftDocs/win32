---
Description: Specifies the high 32-bit value (in bytes) for the size of the archive of inbound fax messages for a particular fax account.
ms.assetid: df15d3c7-885d-4cda-bbd8-53a40e37b987
title: FaxAccountIncomingArchive.SizeHigh property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxAccountIncomingArchive.SizeHigh property

Specifies the high 32-bit value (in bytes) for the size of the archive of inbound fax messages for a particular fax account.

This property is read-only.

## Syntax


```VB
Property SizeHigh As Long
```



## Property value

A **Long** that receives the high 32-bit value of the size of the archive of inbound fax messages for a particular account.

## Remarks

Because the archive may exceed 4 GB in size, its size is described using two long values. SizeLow is the low 32-bit value of the archive size. SizeHigh is the high 32-bit value of the archive size. The size of the archive is: SizeLow + 4 GB \* SizeHigh.

If both the [**SizeLow**](-mfax-faxaccountincomingarchive-sizelow-vb.md) and **SizeHigh** properties have the value 0xffffffff, they specify an invalid archive size, and you should ignore both property values.

The property is read-only.

To read this property, a user must have the [****far2QUERY\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum_2) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxAccountIncomingArchive**](-mfax-faxaccountincomingarchive.md)
</dt> <dt>

[**IFaxAccountIncomingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountincomingarchive)
</dt> </dl>

 

 




