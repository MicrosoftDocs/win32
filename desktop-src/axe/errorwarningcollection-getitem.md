---
title: ErrorWarningCollection GetItem method
description: Gets an item from the collection.
ms.assetid: 'A543CE88-A7C8-482B-BAA3-59C66BE14542'
keywords: ["GetItem method Access Execution Engine", "GetItem method Access Execution Engine , ErrorWarningCollection interface", "ErrorWarningCollection interface Access Execution Engine , GetItem method"]
topic_type:
- apiref
api_name:
- ErrorWarningCollection.GetItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# ErrorWarningCollection::GetItem method

Gets an item from the collection.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT          index,
  [out] ErrorWarning **errorWarning
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The item identifier.

</dd> <dt>

*errorWarning* \[out\]
</dt> <dd>

A double pointer to receive a pointer to the item.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ErrorWarningCollection**](errorwarningcollection.md)
</dt> </dl>

 

 





