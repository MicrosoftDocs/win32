---
title: ResultSnippet GetXmlText method
description: Gets the XML text.
ms.assetid: 51B054D3-15AB-4EA8-B03E-0C2524F4E61F
keywords:
- GetXmlText method Access Execution Engine
- GetXmlText method Access Execution Engine , ResultSnippet interface
- ResultSnippet interface Access Execution Engine , GetXmlText method
topic_type:
- apiref
api_name:
- ResultSnippet.GetXmlText
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

# ResultSnippet::GetXmlText method

Gets the XML text.

## Syntax


```C++
virtual HRESULT GetXmlText(
  [out] BSTR *xmlText
) = 0;
```



## Parameters

<dl> <dt>

*xmlText* \[out\]
</dt> <dd>

The returned text.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ResultSnippet**](resultsnippet.md)
</dt> </dl>

 

 





