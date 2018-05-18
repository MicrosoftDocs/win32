---
title: PrerequisiteCollection GetItem method
description: Returns an issue from the collection.
ms.assetid: '32FFD2BF-FCA4-41DE-B21B-C380F2BEEF40'
keywords: ["GetItem method Access Execution Engine", "GetItem method Access Execution Engine , PrerequisiteCollection interface", "PrerequisiteCollection interface Access Execution Engine , GetItem method"]
topic_type:
- apiref
api_name:
- PrerequisiteCollection.GetItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# PrerequisiteCollection::GetItem method

Returns an issue from the collection.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]        INT               index,
  [out] const PrerequisiteIssue **item
) const = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The zero-based index of the issue in the collection.

</dd> <dt>

*item* \[out\]
</dt> <dd>

A pointer to receive the issue. This parameter will be **NULL** if the method returns an error.

</dd> </dl>

## Return value

*index* ranges from 0 to one less than the count of items in the collection.

If the **PrerequisiteIssue** object was successfully retrieved, the method returns **S\_OK**.

If there is any error, the method returns **NULL**.

If *index* is less than zero or specifies a non-existent issue, the method returns **E\_BOUNDS**.

If item is **NULL**, the method returns **E\_POINTER**.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl> |



## See also

<dl> <dt>

[**PrerequisiteCollection**](prerequisitecollection.md)
</dt> </dl>

 

 





