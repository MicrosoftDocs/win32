---
title: Support CreateLogger method
description: Retrieves an instance of the Logging interface.
ms.assetid: FFC6BFA6-252B-4158-990B-098924EA4A52
keywords:
- CreateLogger method Access Execution Engine
- CreateLogger method Access Execution Engine , Support interface
- Support interface Access Execution Engine , CreateLogger method
topic_type:
- apiref
api_name:
- Support.CreateLogger
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

# Support::CreateLogger method

Retrieves an instance of the [**Logging**](logging.md) interface.

## Syntax


```C++
virtual HRESULT CreateLogger(
  [out] Logging **log
) = 0;
```



## Parameters

<dl> <dt>

*log* \[out\]
</dt> <dd>

A double pointer to receive the [**Logging**](logging.md) interface.

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**.

If *log* is **NULL**, the return value is **E\_POINTER**.

## Remarks

This method creates an instance of the [**Logging**](logging.md) interface. When the assessment is finished with the object, the assessment is responsible for calling **Release** on the interface.

Managed code uses the [**Support.CreateLogger**](axe-support_createlogger_om) method.

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

 

 





