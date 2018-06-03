---
title: ErrorWarning GetMessage method
description: Gets the text message of this item.
ms.assetid: AF0053CF-9A1D-45D8-86C4-B857A1E20BB0
keywords:
- GetMessage method Access Execution Engine
- GetMessage method Access Execution Engine , ErrorWarning interface
- ErrorWarning interface Access Execution Engine , GetMessage method
topic_type:
- apiref
api_name:
- ErrorWarning.GetMessage
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

# ErrorWarning::GetMessage method

Gets the text message of this item.

## Syntax


```C++
virtual HRESULT GetMessage(
  [out] LPCWSTR *message
) const = 0;
```



## Parameters

<dl> <dt>

*message* \[out\]
</dt> <dd>

The text message.

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

[**ErrorWarning**](errorwarning.md)
</dt> </dl>

 

 





