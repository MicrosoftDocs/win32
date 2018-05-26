---
title: ErrorList GetError method
description: Retrieve a specific error from the error list.
ms.assetid: 9EC773A4-A8AB-414D-9C9E-B8664DD0EC5E
keywords:
- GetError method Access Execution Engine
- GetError method Access Execution Engine , ErrorList interface
- ErrorList interface Access Execution Engine , GetError method
topic_type:
- apiref
api_name:
- ErrorList.GetError
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

# ErrorList::GetError method

Retrieve a specific error from the error list.

## Syntax


```C++
virtual HRESULT GetError(
  [in]        UINT         errorIndex,
  [out] const AxeErrorInfo **error
) const = 0;
```



## Parameters

<dl> <dt>

*errorIndex* \[in\]
</dt> <dd>

The zero-based index of the error in the error list. If this value is ((unsigned int)-1), the most recent error is returned. If this value is less than zero, or specifies an index with no error, the return is **AXE\_E\_INVALID\_INDEX**.

</dd> <dt>

*error* \[out\]
</dt> <dd>

A reference to an [**AxeErrorInfo**](axeerrorinfo.md) structure to be populated with the requested error information.

</dd> </dl>

## Return value

If the method is successful, the return value is **S\_OK**.

If the *errorIndex* specifies an invalid index, the return value is **AXE\_E\_INVALID\_INDEX**.

## Remarks

When the solution is finished with the [**AxeErrorInfo**](axeerrorinfo.md) structure the solution is responsible for calling **Release**.

Managed code uses the [**AxeException**](https://msdn.microsoft.com/library/windows/desktop/hh802908) object.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorList**](errorlist.md)
</dt> </dl>

 

 





