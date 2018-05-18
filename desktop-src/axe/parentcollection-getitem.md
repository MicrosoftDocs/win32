---
title: ParentCollection GetItem method
description: Returns a parent from the ParentCollection.
ms.assetid: '60AAE54D-D235-4327-945B-F3D87623A438'
keywords: ["GetItem method Access Execution Engine", "GetItem method Access Execution Engine , ParentCollection interface", "ParentCollection interface Access Execution Engine , GetItem method"]
topic_type:
- apiref
api_name:
- ParentCollection.GetItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# ParentCollection::GetItem method

Returns a parent from the **ParentCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT     index,
  [out] LPCWSTR *parent
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The parent identifier.

</dd> <dt>

*parent* \[out\]
</dt> <dd>

The parent.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

A **ParentCollection** holds data from a **TestCase/Parents** element.

The parent is the value of element **Parents/Parent**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ParentCollection**](parentcollection.md)
</dt> </dl>

 

 





