---
title: Logging LogErrorCode method
description: This method logs an error code and custom message to AXE s pre-configured ETW session.
ms.assetid: D067B7EE-1AFE-420F-A884-347E45829ED9
keywords:
- LogErrorCode method Access Execution Engine
- LogErrorCode method Access Execution Engine , Logging interface
- Logging interface Access Execution Engine , LogErrorCode method
topic_type:
- apiref
api_name:
- Logging.LogErrorCode
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

# Logging::LogErrorCode method

This method logs an error code and custom message to AXE s pre-configured ETW session.

## Syntax


```C++
virtual HRESULT LogErrorCode(
  [in]           HRESULT errorCode,
  [in, optional] LPCWSTR message
) = 0;
```



## Parameters

<dl> <dt>

*errorCode* \[in\]
</dt> <dd>

The **HRESULT** error code to log.

</dd> <dt>

*message* \[in, optional\]
</dt> <dd>

An optional string value that can be a message to add to the logged output.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

Managed code uses the [**Logging.LogErrorCode(Int32, String)**](axe-logging_logerrorcode_903209994_om) method.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl> |



## See also

<dl> <dt>

[**Logging**](logging.md)
</dt> <dt>

[**LogErrorCode methods**](logging-logerrorcode-ovl.md)
</dt> </dl>

 

 





