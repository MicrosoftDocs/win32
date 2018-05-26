---
title: Iteration GetDescriptionProgrammaticName method
description: Returns the description programmatic name of the Iteration.
ms.assetid: 84775A08-B159-4272-8AAA-E05E3A780254
keywords:
- GetDescriptionProgrammaticName method Access Execution Engine
- GetDescriptionProgrammaticName method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , GetDescriptionProgrammaticName method
topic_type:
- apiref
api_name:
- Iteration.GetDescriptionProgrammaticName
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

# Iteration::GetDescriptionProgrammaticName method

Returns the description programmatic name of the **Iteration**.

## Syntax


```C++
virtual HRESULT GetDescriptionProgrammaticName(
  [out] LPCWSTR *descriptionProgrammaticName
) const = 0;
```



## Parameters

<dl> <dt>

*descriptionProgrammaticName* \[out\]
</dt> <dd>

The description programmatic name.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The description programmatic name is the value of element **Iteration/Description/ProgrammaticName**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Iteration**](iteration-struct.md)
</dt> </dl>

 

 





