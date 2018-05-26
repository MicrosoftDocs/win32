---
title: LinkCollection AddItem method
description: Creates a Link and adds it to the LinkCollection.
ms.assetid: 9D61575F-C960-4AB1-AD3F-695E9EBFB1D3
keywords:
- AddItem method Access Execution Engine
- AddItem method Access Execution Engine , LinkCollection interface
- LinkCollection interface Access Execution Engine , AddItem method
topic_type:
- apiref
api_name:
- LinkCollection.AddItem
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

# LinkCollection::AddItem method

Creates a [**Link**](link-struct.md) and adds it to the **LinkCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [in]            LPCWSTR linkTitle,
  [in]            LPCWSTR linkValue,
  [out, optional] Link    **link
) = 0;
```



## Parameters

<dl> <dt>

*linkTitle* \[in\]
</dt> <dd>

The link title.

</dd> <dt>

*linkValue* \[in\]
</dt> <dd>

The link value, a URI.

</dd> <dt>

*link* \[out, optional\]
</dt> <dd>

The link that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **LinkCollection** holds data from an **Issue/Solution/Links** or **Issue/AnalysisLinks** element.

A **Link** holds data from a **Links/Link** or **AnalysisLinks/Link** element.

The link title is the value of element **Link/LinkTitle**.

The link value is the value of element **Link/LinkURI**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**LinkCollection**](linkcollection.md)
</dt> </dl>

 

 





