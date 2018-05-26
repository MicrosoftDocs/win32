---
Description: Specifies the low-order 32-bit value of the size (in bytes) of the archive of outbound fax messages for a particular fax account.
ms.assetid: 70456818-6079-42c0-8c90-4a67239cf654
title: FaxAccountOutgoingArchive.SizeLow property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxAccountOutgoingArchive.SizeLow property

Specifies the low-order 32-bit value of the size (in bytes) of the archive of outbound fax messages for a particular fax account.

This property is read-only.

## Syntax


```VB
Property SizeLow As Long
```



## Property value

A **Long** that receives the low-order 32-bit value of the size (in bytes) of the archive of outbound fax messages for the account.

## Remarks

Because the archive size can exceed 4 GB in size, its size is described as a 64-bit integer whose value is returned as two 32-bit integer values. SizeLow contains the low-order 32-bit value of the archive size. SizeHigh contains the high-order 32-bit value of the archive size. The 64-bit value of the archive size can be computed as: Size64 = (SizeHigh &lt;&lt; 32) + SizeLow.

If both the **SizeLow** and [**SizeHigh**](-mfax-faxaccountoutgoingarchive-sizehigh-vb.md) properties have the value 0xffffffff, they specify an invalid archive size, and you should ignore both property values.

To read this property, a user must have the [****far2QUERY\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum_2?branch=master) access right.

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

[**IFaxAccountOutgoingArchive**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccountoutgoingarchive?branch=master)
</dt> </dl>

 

 




