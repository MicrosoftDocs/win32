---
title: Logging LogErrorCode method
description: This method logs an error code and custom message to AXE s pre-configured ETW session.
ms.assetid: 1A62DAB2-BD0C-426B-A3C3-35E76099A5D2
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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Logging::LogErrorCode method

This method logs an error code and custom message to AXE s pre-configured ETW session.

## Syntax


```C++
virtual HRESULT LogErrorCode(
  [in] HRESULT errorCode
) = 0;
```



## Parameters

<dl> <dt>

*errorCode* \[in\]
</dt> <dd>

The **HRESULT** error code to log.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

Managed code uses the [**Logging.LogErrorCode(Int32)**](https://www.bing.com/search?q=**Logging.LogErrorCode(Int32)**) method.

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

 

 





