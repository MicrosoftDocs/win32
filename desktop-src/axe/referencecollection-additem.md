---
title: ReferenceCollection AddItem method
description: Creates an IssueReference and adds it to the ReferenceCollection.
ms.assetid: 'F737C445-9386-4BAA-9D46-2571E91DCB97'
keywords: ["AddItem method Access Execution Engine", "AddItem method Access Execution Engine , ReferenceCollection interface", "ReferenceCollection interface Access Execution Engine , AddItem method"]
topic_type:
- apiref
api_name:
- ReferenceCollection.AddItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# ReferenceCollection::AddItem method

Creates an [**IssueReference**](issuereference-struct.md) and adds it to the **ReferenceCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [in, optional]  LPCWSTR        attributeIssueID,
  [out, optional] IssueReference **issueReference
) = 0;
```



## Parameters

<dl> <dt>

*attributeIssueID* \[in, optional\]
</dt> <dd>

The issue ID.

</dd> <dt>

*issueReference* \[out, optional\]
</dt> <dd>

The **IssueReference** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **ReferenceCollection** holds data from an **Activity/References** element.

An **IssueReference** holds data from a **References/IssueReference** element.

The issue ID is the value of attribute **IssueID** of element **IssueReference**.

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

 

 





