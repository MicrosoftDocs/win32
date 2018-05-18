---
title: Logging LogFileVersion method
description: Writes the four-part version number of an executable to Axe’s pre-configured ETW file.
ms.assetid: '1d07d13e-cc49-40d3-a323-803d56ab2fb7'
keywords: ["LogFileVersion method Access Execution Engine", "LogFileVersion method Access Execution Engine , Logging interface", "Logging interface Access Execution Engine , LogFileVersion method"]
topic_type:
- apiref
api_name:
- Logging.LogFileVersion
api_location:
- AxeCore.dll
api_type:
- COM
---

# Logging::LogFileVersion method

Writes the four-part version number of an executable to Axe’s pre-configured ETW file.

## Syntax


```C++
virtual HRESULT LogFileVersion(
  [in, optional] LPCWSTR message,
  [in]           LPCWSTR fileName,
  [in, optional] LPCWSTR extraInformation
) = 0;
```



## Parameters

<dl> <dt>

*message* \[in, optional\]
</dt> <dd>

A custom message to display at the beginning of the log message.

</dd> <dt>

*fileName* \[in\]
</dt> <dd>

The name of the executable from which to retrieve the version number.

</dd> <dt>

*extraInformation* \[in, optional\]
</dt> <dd>

A custom message that is appended to the end of the log message.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The file version is written out using the following format:

<dl> *message fileName version messageTimestamp extraInformation*  
</dl>

where the *messageTimestamp* is the time the message is logged.

Managed code uses the [**Logging.LogFileVersion**](axe-logging_logfileversion_om) method.

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
</dt> </dl>

 

 





