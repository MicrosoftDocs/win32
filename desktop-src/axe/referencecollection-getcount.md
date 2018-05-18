---
title: ReferenceCollection GetCount method
description: Returns the count of IssueReference objects in the ReferenceCollection.
ms.assetid: '6A260EFA-3583-4FF8-B76C-1065A0B4CCBE'
keywords: ["GetCount method Access Execution Engine", "GetCount method Access Execution Engine , ReferenceCollection interface", "ReferenceCollection interface Access Execution Engine , GetCount method"]
topic_type:
- apiref
api_name:
- ReferenceCollection.GetCount
api_location:
- AxeCore.dll
api_type:
- COM
---

# ReferenceCollection::GetCount method

Returns the count of [**IssueReference**](issuereference-struct.md) objects in the **ReferenceCollection**.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
) const = 0;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

The count.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **ReferenceCollection** holds data from an **Activity/References** element.

An **IssueReference** holds data from a **References/IssueReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ReferenceCollection**](referencecollection.md)
</dt> </dl>

 

 





