---
title: Link SetLinkTitle method
description: Sets the link title of the Link.
ms.assetid: 4FDC931B-CDCC-4236-91FC-C71FA27D0FC8
keywords:
- SetLinkTitle method Access Execution Engine
- SetLinkTitle method Access Execution Engine , Link interface
- Link interface Access Execution Engine , SetLinkTitle method
topic_type:
- apiref
api_name:
- Link.SetLinkTitle
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

# Link::SetLinkTitle method

Sets the link title of the **Link**.

## Syntax


```C++
virtual HRESULT SetLinkTitle(
  [in] LPCWSTR linkTitle
) = 0;
```



## Parameters

<dl> <dt>

*linkTitle* \[in\]
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

 

 





