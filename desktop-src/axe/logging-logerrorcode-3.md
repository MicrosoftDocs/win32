---
title: Logging LogErrorCode method
description: This method logs an error code and custom message to AXE’s pre-configured ETW session.
ms.assetid: '5200EF6A-922A-4927-9986-FD47F24D8017'
keywords: ["LogErrorCode method Access Execution Engine", "LogErrorCode method Access Execution Engine , Logging interface", "Logging interface Access Execution Engine , LogErrorCode method"]
topic_type:
- apiref
api_name:
- Logging.LogErrorCode
api_location:
- AxeCore.dll
api_type:
- COM
---

# Logging::LogErrorCode method

This method logs an error code and custom message to AXE’s pre-configured ETW session.

## Syntax


```C++
virtual HRESULT LogErrorCode(
  [in]           HRESULT errorCode,
  [in, optional] LPCWSTR messageFormat,
  [in, optional] va_list *messageArguments
) = 0;
```



## Parameters

<dl> <dt>

*errorCode* \[in\]
</dt> <dd>

The **HRESULT** error code to log.

</dd> <dt>

*messageFormat* \[in, optional\]
</dt> <dd>

An optional string value that can be a [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) format string used for formatting custom messages.

</dd> <dt>

*messageArguments* \[in, optional\]
</dt> <dd>

A variable argument list to be used with the *messageFormat* parameter.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

Managed code uses the [**Logging.LogErrorCode(Int32, IFormatProvider, String, Object\[\])**](axe-logging_logerrorcode_1046263256_om) method.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl> |



## See also

<dl> <dt>

[**Logging**](logging.md)
</dt> <dt>

[**LogErrorCode methods**](logging-logerrorcode-ovl.md)
</dt> </dl>

 

 





