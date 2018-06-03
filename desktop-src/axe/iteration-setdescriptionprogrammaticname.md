---
title: Iteration SetDescriptionProgrammaticName method
description: Sets the description programmatic name of the Iteration.
ms.assetid: 408BCBBC-0018-4CA3-978E-B23DC3B815E6
keywords:
- SetDescriptionProgrammaticName method Access Execution Engine
- SetDescriptionProgrammaticName method Access Execution Engine , Iteration interface
- Iteration interface Access Execution Engine , SetDescriptionProgrammaticName method
topic_type:
- apiref
api_name:
- Iteration.SetDescriptionProgrammaticName
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

# Iteration::SetDescriptionProgrammaticName method

Sets the description programmatic name of the **Iteration**.

## Syntax


```C++
virtual HRESULT SetDescriptionProgrammaticName(
  [in] LPCWSTR descriptionProgrammaticName
) = 0;
```



## Parameters

<dl> <dt>

*descriptionProgrammaticName* \[in\]
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

 

 





