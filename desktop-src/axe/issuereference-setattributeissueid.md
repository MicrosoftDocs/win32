---
title: IssueReference SetAttributeIssueID method
description: Sets the issue ID of the IssueReference.
ms.assetid: AEB9B39A-3CF5-4B81-AA9A-219F64EA9854
keywords:
- SetAttributeIssueID method Access Execution Engine
- SetAttributeIssueID method Access Execution Engine , IssueReference interface
- IssueReference interface Access Execution Engine , SetAttributeIssueID method
topic_type:
- apiref
api_name:
- IssueReference.SetAttributeIssueID
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IssueReference::SetAttributeIssueID method

Sets the issue ID of the **IssueReference**.

## Syntax


```C++
virtual HRESULT SetAttributeIssueID(
  [in] LPCWSTR attributeIssueID
) = 0;
```



## Parameters

<dl> <dt>

*attributeIssueID* \[in\]
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

 

 





