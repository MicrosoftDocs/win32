---
title: Link GetLinkValue method
description: Returns the link value from the Link.
ms.assetid: 'FD8D1A9C-80B8-4A9A-9E26-652CE92A4F2C'
keywords: ["GetLinkValue method Access Execution Engine", "GetLinkValue method Access Execution Engine , Link interface", "Link interface Access Execution Engine , GetLinkValue method"]
topic_type:
- apiref
api_name:
- Link.GetLinkValue
api_location:
- AxeCore.dll
api_type:
- COM
---

# Link::GetLinkValue method

Returns the link value from the **Link**.

## Syntax


```C++
virtual HRESULT GetLinkValue(
  [out] LPCWSTR *linkValue
) const = 0;
```



## Parameters

<dl> <dt>

*linkValue* \[out\]
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
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Link**](link-struct.md)
</dt> </dl>

 

 





