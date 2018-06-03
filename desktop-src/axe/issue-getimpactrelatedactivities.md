---
title: Issue GetImpactRelatedActivities method
description: Returns the impact RelatedActivityCollection of the Issue.
ms.assetid: 2E226927-EEBE-4AD9-88C0-A4B1A7B222CD
keywords:
- GetImpactRelatedActivities method Access Execution Engine
- GetImpactRelatedActivities method Access Execution Engine , Issue interface
- Issue interface Access Execution Engine , GetImpactRelatedActivities method
topic_type:
- apiref
api_name:
- Issue.GetImpactRelatedActivities
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

# Issue::GetImpactRelatedActivities method

Returns the impact [**RelatedActivityCollection**](relatedactivitycollection.md) of the **Issue**.

## Syntax


```C++
virtual HRESULT GetImpactRelatedActivities(
  [out] RelatedActivityCollection **impactRelatedActivities
) = 0;
```



## Parameters

<dl> <dt>

*impactRelatedActivities* \[out\]
</dt> <dd>

The impact **RelatedActivityCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The impact **RelatedActivityCollection** holds data from the **Issue/Impact/RelatedActivities** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 





