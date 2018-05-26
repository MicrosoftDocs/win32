---
title: PrerequisiteCollection GetCount method
description: Returns the number of issues in the collection.
ms.assetid: 6E570BED-3E39-4C8C-9178-0754FFA2E005
keywords:
- GetCount method Access Execution Engine
- GetCount method Access Execution Engine , PrerequisiteCollection interface
- PrerequisiteCollection interface Access Execution Engine , GetCount method
topic_type:
- apiref
api_name:
- PrerequisiteCollection.GetCount
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

# PrerequisiteCollection::GetCount method

Returns the number of issues in the collection.

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

The number of issues in the collection.

</dd> </dl>

## Return value

If successful, the method returns **S\_OK**.

If issues parameter is **NULL**, the method returns **E\_POINTER**.

## Remarks

Manage code uses the [**PrerequisiteCollection.Count**](axe-prerequisitecollection_count_om) property.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl> |



## See also

<dl> <dt>

[**PrerequisiteCollection**](prerequisitecollection.md)
</dt> </dl>

 

 





