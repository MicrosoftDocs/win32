---
title: IixssoQuery OutOfDate property
description: Determines whether the content index is no longer current.
ms.assetid: 2d0664ab-8511-40d6-86b9-b3ce99ac4268
keywords:
- OutOfDate property Indexing Service
- OutOfDate property Indexing Service , IixssoQuery interface
- IixssoQuery interface Indexing Service , OutOfDate property
topic_type:
- apiref
api_name:
- IixssoQuery.OutOfDate
- IixssoQuery.get_OutOfDate
api_location:
- Ixsso.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoQuery::OutOfDate property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Determines whether the content index is no longer current.

This property is read-only.

## Syntax


```C++
HRESULT get_OutOfDate(
  [out, retval] VARIANT_BOOL *val
);
```



## Property value

**VARIANT\_TRUE** if the content index is out of date, otherwise **VARIANT\_FALSE**.

## Remarks

You must call the [**CreateRecordset**](iixssoquery-createrecordset.md) method before using this property. The **OutOfDate** property value comes from detecting how many documents remain to be indexed for a catalog. Because different operating systems support different notification systems, this value is only as accurate as is allowed by the change notification system or by the interval between directory scans.

Documents that are temporarily inaccessible to the filtering process because of sharing violations or other reasons are placed on a separate queue for later retry and can prevent the count of files to index from decreasing to zero. Use the [**GetLongProperty**](iadminindexserver-getlongproperty.md) or [**SetLongProperty**](iadminindexserver-setlongproperty.md) for the **[DelayedFilterRetries](delayedfilterretries.md)** registry value to adjust this value for such a situation.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoQuery**](iixssoquery.md)
</dt> </dl>

 

 





