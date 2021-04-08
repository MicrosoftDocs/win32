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

A DWORD specifying the API version. This value should always be **DLP_POSTOP_STATUS_V_LATEST**. This constant is defined in the endpointdlp.h sample header file listing in the article [Endpoint data loss prevention](endpointdlp-endpoint-data-loss-prevention.md)

</dd> </dl>

<dl> <dt>

*OperationSuccess* \[in\]
</dt> <dd>

A BOOL indicating whether the open operation was successful.

</dd> </dl>





## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |
