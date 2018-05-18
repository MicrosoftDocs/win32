---
title: LinkCollection Clear method
description: Deletes all Link objects from the LinkCollection.
ms.assetid: 'D1E8C7CD-3CAE-4424-A08C-4A3B380EDDFD'
keywords: ["Clear method Access Execution Engine", "Clear method Access Execution Engine , LinkCollection interface", "LinkCollection interface Access Execution Engine , Clear method"]
topic_type:
- apiref
api_name:
- LinkCollection.Clear
api_location:
- AxeCore.dll
api_type:
- COM
---

# LinkCollection::Clear method

Deletes all [**Link**](link-struct.md) objects from the **LinkCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **LinkCollection** holds data from an **Issue/Solution/Links** or **Issue/AnalysisLinks** element.

A **Link** holds data from a **Links/Link** or **AnalysisLinks/Link** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**LinkCollection**](linkcollection.md)
</dt> </dl>

 

 





