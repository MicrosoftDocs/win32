---
title: Logging LogMessage method
description: Write custom messages to Axe’s pre-configured ETW file.
ms.assetid: '9EACB20D-FC4E-4038-9584-864BC53E8C19'
keywords: ["LogMessage method Access Execution Engine", "LogMessage method Access Execution Engine , Logging interface", "Logging interface Access Execution Engine , LogMessage method"]
topic_type:
- apiref
api_name:
- Logging.LogMessage
api_location:
- AxeCore.dll
api_type:
- COM
---

# Logging::LogMessage method

Write custom messages to Axe’s pre-configured ETW file.

## Syntax


```C++
virtual HRESULT LogMessage(
  [in, optional] LPCWSTR messageFormat,
  [in, optional] va_list *messageArguments
) = 0;
```



## Parameters

<dl> <dt>

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

[**LogMessage methods**](logging-logmessage-ovl.md)
</dt> </dl>

 

 





