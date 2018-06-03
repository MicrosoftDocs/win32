---
title: Assessment GetToolTip method
description: Retrieve the short description of the assessment.
ms.assetid: AFDB69EB-B978-4592-ADD3-433AB5892610
keywords:
- GetToolTip method Access Execution Engine
- GetToolTip method Access Execution Engine , Assessment interface
- Assessment interface Access Execution Engine , GetToolTip method
topic_type:
- apiref
api_name:
- Assessment.GetToolTip
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

# Assessment::GetToolTip method

Retrieve the short description of the assessment.

## Syntax


```C++
virtual HRESULT GetToolTip(
  [out, optional] LPCWSTR *toolTip
) const = 0;
```



## Parameters

<dl> <dt>

*toolTip* \[out, optional\]
</dt> <dd>

A pointer to receive the tooltip string.

</dd> </dl>

## Return value

If the tooltip is successfully retrieved, the method returns **S\_OK**.

If the *tooltip* is null, the method returns **E\_POINTER**.

## Remarks

Managed code uses the [**Assessment.ToolTip \| toolTip property**](https://www.bing.com/search?q=**Assessment.ToolTip \| toolTip property**).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Assessment**](assessment-inf.md)
</dt> </dl>

 

 





