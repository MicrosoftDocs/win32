---
title: BG\_ERROR\_CONTEXT enumeration
description: The BG\_ERROR\_CONTEXT enumeration defines the constant values that specify the context in which the error occurred.
ms.assetid: '86202343-5B5B-4A2E-A58D-7634BCB41E1C'
keywords: ["BG_ERROR_CONTEXT enumeration"]
topic_type:
- apiref
api_name:
- BG_ERROR_CONTEXT
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
---

# BG\_ERROR\_CONTEXT enumeration

The **BG\_ERROR\_CONTEXT** enumeration defines the constant values that specify the context in which the error occurred.

## Syntax


```C++
typedef enum  { 
  BG_ERROR_CONTEXT_NONE                        = 0,
  BG_ERROR_CONTEXT_UNKNOWN                     = 1,
  BG_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER       = 2,
  BG_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION  = 3,
  BG_ERROR_CONTEXT_LOCAL_FILE                  = 4,
  BG_ERROR_CONTEXT_REMOTE_FILE                 = 5,
  BG_ERROR_CONTEXT_GENERAL_TRANSPORT           = 6,
  BG_ERROR_CONTEXT_REMOTE_APPLICATION          = 7
} BG_ERROR_CONTEXT;
```



## Constants

<dl> <dt>

<span id="BG_ERROR_CONTEXT_NONE"></span><span id="bg_error_context_none"></span>**BG\_ERROR\_CONTEXT\_NONE**
</dt> <dd>

An error has not occurred.

</dd> <dt>

<span id="BG_ERROR_CONTEXT_UNKNOWN"></span><span id="bg_error_context_unknown"></span>**BG\_ERROR\_CONTEXT\_UNKNOWN**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BG_ERROR_CONTEXT_GENERAL_QUEUE_MANAGER"></span><span id="bg_error_context_general_queue_manager"></span>**BG\_ERROR\_CONTEXT\_GENERAL\_QUEUE\_MANAGER**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BG_ERROR_CONTEXT_QUEUE_MANAGER_NOTIFICATION"></span><span id="bg_error_context_queue_manager_notification"></span>**BG\_ERROR\_CONTEXT\_QUEUE\_MANAGER\_NOTIFICATION**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BG_ERROR_CONTEXT_LOCAL_FILE"></span><span id="bg_error_context_local_file"></span>**BG\_ERROR\_CONTEXT\_LOCAL\_FILE**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BG_ERROR_CONTEXT_REMOTE_FILE"></span><span id="bg_error_context_remote_file"></span>**BG\_ERROR\_CONTEXT\_REMOTE\_FILE**
</dt> <dd>

The error was related to the specified remote file. For example, the URL was not accessible.

</dd> <dt>

<span id="BG_ERROR_CONTEXT_GENERAL_TRANSPORT"></span><span id="bg_error_context_general_transport"></span>**BG\_ERROR\_CONTEXT\_GENERAL\_TRANSPORT**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="BG_ERROR_CONTEXT_REMOTE_APPLICATION"></span><span id="bg_error_context_remote_application"></span>**BG\_ERROR\_CONTEXT\_REMOTE\_APPLICATION**
</dt> <dd>

Not supported.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



## See also

<dl> <dt>

[**IBackgroundCopyError::GetError**](ibackgroundcopyerror-geterror-method.md)
</dt> </dl>

 

 





