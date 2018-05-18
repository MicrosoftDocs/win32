---
title: Activity AddReference method
description: Creates an IssueReference and adds it to the Activity.
ms.assetid: 'C0AD2F0F-4BC6-4F94-BA97-4D782214840F'
keywords: ["AddReference method Access Execution Engine", "AddReference method Access Execution Engine , Activity interface", "Activity interface Access Execution Engine , AddReference method"]
topic_type:
- apiref
api_name:
- Activity.AddReference
api_location:
- AxeCore.dll
api_type:
- COM
---

# Activity::AddReference method

Creates an [**IssueReference**](issuereference-struct.md) and adds it to the **Activity**.

## Syntax


```C++
virtual HRESULT AddReference(
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

**Activity** objects hold data from **Iteration/Activities/Activity** elements.

**IssueReference** objects hold data from **Activity/References/IssueReference** elements.

The issue ID is the value of attribute **IssueID** of the **IssueReference**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Activity**](activity-struct.md)
</dt> </dl>

 

 





