---
title: ParameterSet GetParameter method
description: Returns a parameter object for the specified named parameter.
ms.assetid: C583AE52-77BF-4086-A68F-C743A0CBD02D
keywords:
- GetParameter method Access Execution Engine
- GetParameter method Access Execution Engine , ParameterSet interface
- ParameterSet interface Access Execution Engine , GetParameter method
topic_type:
- apiref
api_name:
- ParameterSet.GetParameter
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

# ParameterSet::GetParameter method

Returns a parameter object for the specified named parameter.

## Syntax


```C++
virtual HRESULT GetParameter(
  [in]  LPCWSTR   parameterName,
  [out] Parameter **parameter
) const = 0;
```



## Parameters

<dl> <dt>

*parameterName* \[in\]
</dt> <dd>

The name of the parameter for which to retrieve the value.

</dd> <dt>

*parameter* \[out\]
</dt> <dd>

A pointer to the [**Parameter**](parameter.md) object

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**.

If the parameter that was specified does not exist, the return value is **E\_INVALIDARG**.

If *parameter* is **NULL**, the return value is **E\_POINTER**.

## Remarks

An assessment can use this method to get the value of the parameter that was specified by the user when the job was created or when a solution called [**SetJobParameter**](job-setjobparameter.md).

The managed API implements a default indexer to access a [**Parameter**](parameter.md) object using the [**ParameterSet**](parameterset.md) as a collection.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ParameterSet**](parameterset.md)
</dt> </dl>

 

 





