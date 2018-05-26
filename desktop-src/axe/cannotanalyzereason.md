---
title: CannotAnalyzeReason enumeration
description: The reason why execution results cannot be analyzed.
ms.assetid: BB8C6FC1-DC62-498F-A213-32144E131FC9
keywords:
- CannotAnalyzeReason enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- CannotAnalyzeReason
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CannotAnalyzeReason enumeration

The reason why execution results cannot be analyzed.

## Syntax


```C++
enum CannotAnalyzeReason {
  CannotAnalyzeReasonNone             = 0, 
  CannotAnalyzeReasonNotSupported, 
  CannotAnalyzeReasonExecutionFailed, 
  CannotAnalyzeReasonInvalid 

};
```



## Constants

<dl> <dt>

<span id="CannotAnalyzeReasonNone"></span><span id="cannotanalyzereasonnone"></span><span id="CANNOTANALYZEREASONNONE"></span>**CannotAnalyzeReasonNone**
</dt> <dd>

The results can be analyzed.

</dd> <dt>

<span id="CannotAnalyzeReasonNotSupported"></span><span id="cannotanalyzereasonnotsupported"></span><span id="CANNOTANALYZEREASONNOTSUPPORTED"></span>**CannotAnalyzeReasonNotSupported**
</dt> <dd>

The results cannot be analyzed because the assessment manifest does not support it.

</dd> <dt>

<span id="CannotAnalyzeReasonExecutionFailed"></span><span id="cannotanalyzereasonexecutionfailed"></span><span id="CANNOTANALYZEREASONEXECUTIONFAILED"></span>**CannotAnalyzeReasonExecutionFailed**
</dt> <dd>

The results cannot be analyzed because assessment execution failed.

</dd> <dt>

<span id="CannotAnalyzeReasonInvalid"></span><span id="cannotanalyzereasoninvalid"></span><span id="CANNOTANALYZEREASONINVALID"></span>**CannotAnalyzeReasonInvalid**
</dt> <dd>

Invalid reason.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





