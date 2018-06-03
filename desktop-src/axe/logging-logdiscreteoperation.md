---
title: Logging LogDiscreteOperation method
description: This method logs a discrete event to the AXE engine s pre-configured ETW session.
ms.assetid: ee464a68-e707-4218-91ac-e3ab6bedbbf3
keywords:
- LogDiscreteOperation method Access Execution Engine
- LogDiscreteOperation method Access Execution Engine , Logging interface
- Logging interface Access Execution Engine , LogDiscreteOperation method
topic_type:
- apiref
api_name:
- Logging.LogDiscreteOperation
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

# Logging::LogDiscreteOperation method

This method logs a discrete event to the AXE engine s pre-configured ETW session.

## Syntax


```C++
virtual HRESULT LogDiscreteOperation(
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

A custom byte stream to log to the ETW session. If the *blobByteSize* is 0, this parameter must be NULL.

</dd> </dl>

## Return value

If the function succeeds, the return is **S\_OK**. If *blob* is not **NULL** when *blobByteSize* is zero, the return is **E\_INVALIDARG**. If *blob* is **NULL** when *blobByteSize* is not zero, the return is E\_POINTER.

## Remarks

Calling this API logs the *operationId*, *message* and the blob to AXE s pre-configured ETW session as the session s **ASSESSMENT\_DISCRETE\_OPERATION** event. Assessments should end the session with a call to [**LogEndOperation**](logging-logendoperation.md).

It is strongly recommended that the Begin and End operation events be logged as pairs matched by Id. If they are not matched, ETW trace processing tools and data viewers will not be able to analyze paired events.

Managed code uses the [**Logging.LogDiscreteOperation**](https://www.bing.com/search?q=**Logging.LogDiscreteOperation**) method.

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

 

 





