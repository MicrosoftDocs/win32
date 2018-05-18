---
title: ReferenceCollection GetItem method
description: Returns an IssueReference from the ReferenceCollection.
ms.assetid: 'B4F3244D-239E-46C6-AB58-639F4C94FDE7'
keywords: ["GetItem method Access Execution Engine", "GetItem method Access Execution Engine , ReferenceCollection interface", "ReferenceCollection interface Access Execution Engine , GetItem method"]
topic_type:
- apiref
api_name:
- ReferenceCollection.GetItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# ReferenceCollection::GetItem method

Returns an [**IssueReference**](issuereference-struct.md) from the **ReferenceCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT            index,
  [out] IssueReference **issueReference
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **IssueReference** identifier.

</dd> <dt>

*issueReference* \[out\]
</dt> <dd>

The **IssueReference**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

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

 

 





