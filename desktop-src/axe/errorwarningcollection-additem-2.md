---
title: ErrorWarningCollection AddItem method
description: Adds an ErrorWarning item to the collection.
ms.assetid: '88EA6637-036E-444E-909B-1BAA99A5A860'
keywords: ["AddItem method Access Execution Engine", "AddItem method Access Execution Engine , ErrorWarningCollection interface", "ErrorWarningCollection interface Access Execution Engine , AddItem method"]
topic_type:
- apiref
api_name:
- ErrorWarningCollection.AddItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# ErrorWarningCollection::AddItem method

Adds an [**ErrorWarning**](errorwarning.md) item to the collection.

## Syntax


```C++
virtual HRESULT AddItem(
  [in]      IssueType    issueType,
  [in]      LPCWSTR      message,
  [in, out] ErrorWarning **errorWarning
) = 0;
```



## Parameters

<dl> <dt>

*issueType* \[in\]
</dt> <dd>

The type of the item being added.

</dd> <dt>

*message* \[in\]
</dt> <dd>

The message text for the item.

</dd> <dt>

*errorWarning* \[in, out\]
</dt> <dd>

A double pointer that receives a pointer to the new item.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

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

 

 





