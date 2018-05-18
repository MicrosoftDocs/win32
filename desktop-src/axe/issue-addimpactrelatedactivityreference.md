---
title: Issue AddImpactRelatedActivityReference method
description: Creates and adds an impact-related ActivityReference to the Issue.
ms.assetid: '32FF1638-426A-4BA0-A52B-BFA83A7053DB'
keywords: ["AddImpactRelatedActivityReference method Access Execution Engine", "AddImpactRelatedActivityReference method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , AddImpactRelatedActivityReference method"]
topic_type:
- apiref
api_name:
- Issue.AddImpactRelatedActivityReference
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::AddImpactRelatedActivityReference method

Creates and adds an impact-related [**ActivityReference**](activityreference-struct.md) to the **Issue**.

## Syntax


```C++
virtual HRESULT AddImpactRelatedActivityReference(
  [in]            LPCWSTR           attributeActivityId,
  [out, optional] ActivityReference **activityReference
) = 0;
```



## Parameters

<dl> <dt>

*attributeActivityId* \[in\]
</dt> <dd>

The activity ID.

</dd> <dt>

*activityReference* \[out, optional\]
</dt> <dd>

The **ActivityReference** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The impact-related **ActivityReference** objects hold data from the **Issue/Impact/RelatedActivities/ActivityReference** elements.

The activity ID is the value of attribute **ActivityID** of the **Issue/Impact/RelatedActivities/ActivityReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





