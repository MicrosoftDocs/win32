---
title: Logging LogEndOperation method
description: This method logs an end event to the AXE engine s pre-configured ETW session.
ms.assetid: 11f533d1-2186-4a6b-8644-b7ab23fcfe3d
keywords:
- LogEndOperation method Access Execution Engine
- LogEndOperation method Access Execution Engine , Logging interface
- Logging interface Access Execution Engine , LogEndOperation method
topic_type:
- apiref
api_name:
- Logging.LogEndOperation
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

# Logging::LogEndOperation method

This method logs an end event to the AXE engine s pre-configured ETW session.

## Syntax


```C++
virtual HRESULT LogEndOperation(
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

If the function succeeds, the return is **S\_OK**. If *blob* is **NULL** when *blobByteSize* is not zero, the return is **E\_POINTER**.

## Remarks

Calling this API logs the *operationId*, *message* and the blob to AXE s pre-configured ETW session as the session s **ASSESSMENT\_END\_OPERATION** event. Assessments should begin the session with a call to [**LogBeginOperation**](logging-logbeginoperation.md).

It is strongly recommended that the Begin and End operation events be logged as pairs matched by Id. If they are not matched, ETW trace processing tools and data viewers will not be able to analyze paired events.

Managed code uses [**Logging.LogEndOperation**](https://www.bing.com/search?q=**Logging.LogEndOperation**) method .

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

 

 





