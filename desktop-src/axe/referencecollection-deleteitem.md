---
title: ReferenceCollection DeleteItem method
description: Deletes an IssueReference from the ReferenceCollection.
ms.assetid: '7B61CD05-03D8-4B0A-9DC8-A8A38951399C'
keywords: ["DeleteItem method Access Execution Engine", "DeleteItem method Access Execution Engine , ReferenceCollection interface", "ReferenceCollection interface Access Execution Engine , DeleteItem method"]
topic_type:
- apiref
api_name:
- ReferenceCollection.DeleteItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# ReferenceCollection::DeleteItem method

Deletes an [**IssueReference**](issuereference-struct.md) from the **ReferenceCollection**.

## Syntax


```C++
virtual HRESULT DeleteItem(
  [in] INT index
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **IssueReference** identifier.

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

 

 





