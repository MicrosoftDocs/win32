---
title: Link GetLinkToolTip method
description: Returns the link tooltip from the Link.
ms.assetid: 1976FA00-173E-434F-9F22-CCB09CF91E32
keywords:
- GetLinkToolTip method Access Execution Engine
- GetLinkToolTip method Access Execution Engine , Link interface
- Link interface Access Execution Engine , GetLinkToolTip method
topic_type:
- apiref
api_name:
- Link.GetLinkToolTip
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

# Link::GetLinkToolTip method

Returns the link tooltip from the **Link**.

## Syntax


```C++
virtual HRESULT GetLinkToolTip(
  [out] LPCWSTR *linkToolTip
) const = 0;
```



## Parameters

<dl> <dt>

*linkToolTip* \[out\]
</dt> <dd>

The link tooltip.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **Link** holds data from an **Issue/Solution/Links/Link** or **Issue/AnalysisLinks/Link** element.

The link tooltip is the value of element **Link/LinkToolTip**.

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

 

 





