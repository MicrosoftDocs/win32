---
title: Support GetErrorText method
description: Retrieves an Axe error message given the Axe error code.
ms.assetid: AA09D692-C5D1-4E77-978F-0EECECE7F2F8
keywords:
- GetErrorText method Access Execution Engine
- GetErrorText method Access Execution Engine , Support interface
- Support interface Access Execution Engine , GetErrorText method
topic_type:
- apiref
api_name:
- Support.GetErrorText
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

# Support::GetErrorText method

Retrieves an Axe error message given the Axe error code. This method allows an assessment to get a human-readable string explaining what an error code means.

## Syntax


```C++
virtual HRESULT GetErrorText(
  [in]  HRESULT   axeError,
  [out] ErrorList **errorList
) = 0;
```



## Parameters

<dl> <dt>

*axeError* \[in\]
</dt> <dd>

The **HRESULT** representing an Axe error code.

</dd> <dt>

*errorList* \[out\]
</dt> <dd>

A double pointer to an [**ErrorList**](errorlist.md) object that is populated with an [**AxeErrorInfo**](axeerrorinfo.md) structure that contains the error string.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

This method enables an assessment to get a human-readable string explaining the meaning of an error code.

Managed code uses [**Support.GetErrorText \| getErrorText**](axe-support_geterrortext_om) method.

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
</dt> </dl>

 

 





