---
title: AssessmentResultsCollection GetCount method
description: Returns the count of AssessmentResults objects in the AssessmentResultsCollection.
ms.assetid: 9F9FE2AF-80A8-4837-B7F6-0C9477F4AA9C
keywords:
- GetCount method Access Execution Engine
- GetCount method Access Execution Engine , AssessmentResultsCollection interface
- AssessmentResultsCollection interface Access Execution Engine , GetCount method
topic_type:
- apiref
api_name:
- AssessmentResultsCollection.GetCount
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

# AssessmentResultsCollection::GetCount method

Returns the count of [**AssessmentResults**](assessmentresults-struct.md) objects in the **AssessmentResultsCollection**.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
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

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**AssessmentResultsCollection**](assessmentresultscollection.md)
</dt> </dl>

 

 





