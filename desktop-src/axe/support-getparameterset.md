---
title: Support GetParameterSet method
description: Retrieves the specified set of parameters.
ms.assetid: 5822F467-887B-4DF2-8DFA-7F2E7CC1568E
keywords:
- GetParameterSet method Access Execution Engine
- GetParameterSet method Access Execution Engine , Support interface
- Support interface Access Execution Engine , GetParameterSet method
topic_type:
- apiref
api_name:
- Support.GetParameterSet
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

# Support::GetParameterSet method

Retrieves the specified set of parameters.

## Syntax


```C++
virtual HRESULT GetParameterSet(
  [in]  ParameterNamespace namespace,
  [out] ParameterSet       **params
) = 0;
```



## Parameters

<dl> <dt>

*namespace* \[in\]
</dt> <dd>

Specifies which collection of parameters to retrieve.

</dd> <dt>

*params* \[out\]
</dt> <dd>

A double pointer to receive the [**ParameterSet**](parameterset.md) interface.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**.

If an invalid namespace was specified, the return value is **E\_INVALIDARG**.

If *params* is **NULL**, the return value is **E\_POINTER**.

## Remarks

Managed code uses [**Support.GetParameterSet \| getParameterSet**](axe-support_getparameterset_om) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> <dt>

[**ParameterSet**](parameterset.md)
</dt> <dt>

[**Parameter**](parameter.md)
</dt> <dt>

[**ParameterNamespace**](parameternamespace.md)
</dt> </dl>

 

 





