---
title: AssessmentResultsCollection GetItem method
description: Returns an AssessmentResults object from the AssessmentResultsCollection.
ms.assetid: C6AB4E72-527F-4004-9F83-C943C0277B6A
keywords:
- GetItem method Access Execution Engine
- GetItem method Access Execution Engine , AssessmentResultsCollection interface
- AssessmentResultsCollection interface Access Execution Engine , GetItem method
topic_type:
- apiref
api_name:
- AssessmentResultsCollection.GetItem
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

# AssessmentResultsCollection::GetItem method

Returns an [**AssessmentResults**](assessmentresults-struct.md) object from the **AssessmentResultsCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]            INT               resultIndex,
  [out, optional] AssessmentResults **result
) const = 0;
```



## Parameters

<dl> <dt>

*resultIndex* \[in\]
</dt> <dd>

The item identifier.

</dd> <dt>

*result* \[out, optional\]
</dt> <dd>

The **AssessmentResults** object.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

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

 

 





