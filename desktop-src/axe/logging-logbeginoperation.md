---
title: Logging LogBeginOperation method
description: This method logs a begin event to the AXE engine s pre-configured ETW session.
ms.assetid: 3c44f6d9-8b0a-4fd6-9caf-b932e70fe152
keywords:
- LogBeginOperation method Access Execution Engine
- LogBeginOperation method Access Execution Engine , Logging interface
- Logging interface Access Execution Engine , LogBeginOperation method
topic_type:
- apiref
api_name:
- Logging.LogBeginOperation
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

# Logging::LogBeginOperation method

This method logs a begin event to the AXE engine s pre-configured ETW session.

## Syntax


```C++
virtual HRESULT LogBeginOperation(
  [in]           UINT    operationId,
  [in, optional] LPCWSTR message,
  [in]           UINT    blobSize,
  [in, optional] BYTE    *blob
) = 0;
```



## Parameters

<dl> <dt>

*operationId* \[in\]
</dt> <dd>

A custom numerical identifier that identifies some operation expressed by the assessment.

</dd> <dt>

*message* \[in, optional\]
</dt> <dd>

A **UNICODE** string to log with the begin operation event. This string may be empty. This string must not be longer than 1024 characters.

</dd> <dt>

*blobSize* \[in\]
</dt> <dd>

The number of bytes pointed to by the *blob* parameter. The *blobByteSize* may be 0. The blob size must not be greater than 32K bytes.

</dd> <dt>

*blob* \[in, optional\]
</dt> <dd>

A custom byte stream to log to the ETW session. If the *blobByteSize* is 0, this parameter must be **NULL**.

</dd> </dl>

## Return value

If the function succeeds, the return is **S\_OK**.

If *blob* is not **NULL** when *blobByteSize* is zero, the return is **E\_INVALIDARG**.

If *blob* is **NULL** when *blobByteSize* is not zero, the return is **E\_POINTER**.

## Remarks

Calling this API logs the *operationId*, *message* and the blob to AXE s ETW pre-configured session as the session s **ASSESSMENT\_BEGIN\_OPERATION** event. Assessments should end the session with a call to [**LogEndOperation**](logging-logendoperation.md).

It is strongly recommended that the begin and end operation events be logged as pairs matched by Id. If they are not matched, ETW trace processing tools and data viewers will not be able to analyze paired events.

Managed code uses [**Logging.LogBeginOperation**](https://www.bing.com/search?q=**Logging.LogBeginOperation**) method.

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
</dt> </dl>

 

 





