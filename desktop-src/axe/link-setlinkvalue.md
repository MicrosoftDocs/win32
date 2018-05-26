---
title: Link SetLinkValue method
description: Sets the link value of the Link.
ms.assetid: 90E9D200-D6E4-4906-9BE5-2FDCF2BF1CCC
keywords:
- SetLinkValue method Access Execution Engine
- SetLinkValue method Access Execution Engine , Link interface
- Link interface Access Execution Engine , SetLinkValue method
topic_type:
- apiref
api_name:
- Link.SetLinkValue
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

# Link::SetLinkValue method

Sets the link value of the **Link**.

## Syntax


```C++
virtual HRESULT SetLinkValue(
  [in] LPCWSTR linkValue
) = 0;
```



## Parameters

<dl> <dt>

*linkValue* \[in\]
</dt> <dd>

The link value, a URI.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **Link** holds data from an **Issue/Solution/Links/Link** or **Issue/AnalysisLinks/Link** element.

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

[**Link**](link-struct.md)
</dt> </dl>

 

 





