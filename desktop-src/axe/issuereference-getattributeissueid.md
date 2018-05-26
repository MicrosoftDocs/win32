---
title: IssueReference GetAttributeIssueID method
description: Returns the issue ID of the IssueReference.
ms.assetid: B617DCDF-82B6-4891-8C09-9C98DB31C74B
keywords:
- GetAttributeIssueID method Access Execution Engine
- GetAttributeIssueID method Access Execution Engine , IssueReference interface
- IssueReference interface Access Execution Engine , GetAttributeIssueID method
topic_type:
- apiref
api_name:
- IssueReference.GetAttributeIssueID
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IssueReference::GetAttributeIssueID method

Returns the issue ID of the **IssueReference**.

## Syntax


```C++
virtual HRESULT GetAttributeIssueID(
  [out] LPCWSTR *attributeIssueID
) const = 0;
```



## Parameters

<dl> <dt>

*attributeIssueID* \[out\]
</dt> <dd>

The issue ID.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

An **IssueReference** holds data from an **Activity/References/IssueReference** element.

The issue ID is the value of attribute **IssueID** of element **IssueReference**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IssueReference**](issuereference-struct.md)
</dt> </dl>

 

 





