---
title: Link GetLinkTitle method
description: Returns the link title from the Link.
ms.assetid: 1ED1CE4E-B3AF-495F-A389-322BA12BA47E
keywords:
- GetLinkTitle method Access Execution Engine
- GetLinkTitle method Access Execution Engine , Link interface
- Link interface Access Execution Engine , GetLinkTitle method
topic_type:
- apiref
api_name:
- Link.GetLinkTitle
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

# Link::GetLinkTitle method

Returns the link title from the **Link**.

## Syntax


```C++
virtual HRESULT GetLinkTitle(
  [out] LPCWSTR *linkTitle
) const = 0;
```



## Parameters

<dl> <dt>

*linkTitle* \[out\]
</dt> <dd>

The link title.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **Link** holds data from an **Issue/Solution/Links/Link** or **Issue/AnalysisLinks/Link** element.

The link title is the value of element **Link/LinkTitle**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Link**](link-struct.md)
</dt> </dl>

 

 





