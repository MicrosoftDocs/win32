---
title: Logging LogMessage method
description: Write custom messages to Axe s pre-configured ETW file.
ms.assetid: B12FCDEC-25CB-483F-8A6F-C9531F6E9B57
keywords:
- LogMessage method Access Execution Engine
- LogMessage method Access Execution Engine , Logging interface
- Logging interface Access Execution Engine , LogMessage method
topic_type:
- apiref
api_name:
- Logging.LogMessage
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

# Logging::LogMessage method

Write custom messages to Axe s pre-configured ETW file.

## Syntax


```C++
virtual HRESULT LogMessage(
  [in, optional] LPCWSTR message
) = 0;
```



## Parameters

<dl> <dt>

*message* \[in, optional\]
</dt> <dd>

An optional string value that can be a message to add to the logged output.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

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

[**LogMessage methods**](logging-logmessage-ovl.md)
</dt> </dl>

 

 





