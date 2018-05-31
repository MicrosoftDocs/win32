---
Description: Specifies the high-order 32-bit value of the size (in bytes) of the archive of outbound fax messages for a particular fax account.
ms.assetid: 85c13a7e-0af6-4d47-97a0-bbe4ae1d87c5
title: FaxAccountOutgoingArchive.SizeHigh property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxAccountOutgoingArchive.SizeHigh property

Specifies the high-order 32-bit value of the size (in bytes) of the archive of outbound fax messages for a particular fax account.

This property is read-only.

## Syntax


```VB
Property SizeHigh As Long
```



## Property value

A **Long** that receives the high-order 32-bit value of the size (in bytes) of the archive of outbound fax messages for a particular account.

## Remarks

Because the archive size can exceed 4 GB in size, its size is described as a 64-bit integer whose value is returned as two 32-bit integer values. SizeLow contains the low-order 32-bit value of the archive size. SizeHigh contains the high-order 32-bit value of the archive size. The 64-bit value of the archive size can be computed as: Size64 = (SizeHigh &lt;&lt; 32) + SizeLow.

If both the [**SizeLow**](-mfax-faxaccountoutgoingarchive-sizelow-vb.md) and **SizeHigh** properties have the value 0xffffffff, they specify an invalid archive size, and you should ignore both property values.

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

[**FaxAccountOutgoingArchive**](-mfax-faxaccountoutgoingarchive.md)
</dt> <dt>

[**IFaxAccountOutgoingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountoutgoingarchive)
</dt> </dl>

 

 




