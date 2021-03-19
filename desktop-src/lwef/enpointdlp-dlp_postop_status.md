---
Description: Specifies status information about an endpoint DLP operation.
title: DLP_POSTOP_STATUS structure (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DLP_POSTOP_STATUS
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# DLP_POSTOP_STATUS structure

Specifies status information about an endpoint DLP operation.

## Syntax


```C++
typedef struct _DLP_POSTOP_STATUS {
    
    DWORD Version;    
    BOOL OperationSuccess;  

} DLP_POSTOP_STATUS, *PDLP_POSTOP_STATUS; 
```


## Members

<dl> <dt>

*Version* \[in\]
</dt> <dd>

A DWORD specifying the API version. In the current release, this value must be 0x1.

</dd> </dl>

<dl> <dt>

*PersistentFileName* \[in\]
</dt> <dd>

A BOOL indicating whether the open operation was successful.

</dd> </dl>





## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10                                             |
| Minimum supported server<br/> | Windows Server                                    |
