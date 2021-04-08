---
Description: Specifies information about a document that is associated with an endpoint DLP operation.
title: DLP_DOCUMENT_INFO structure (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DLP_DOCUMENT_INFO
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# DLP_DOCUMENT_INFO structure

Specifies information about a document that is associated with an endpoint DLP operation.

## Syntax


```C++
typedef struct _DLP_DOCUMENT_INFO {

    DWORD Version;    
    LPCWSTR PersistentFileName;
    LPCWSTR LocalFileName;

}DLP_DOCUMENT_INFO, *PDLP_DOCUMENT_INFO;
```


## Members

<dl> <dt>

*Version* \[in\]
</dt> <dd>

A DWORD specifying the API version. This value should always be **DLP_DOCUMENT_INFO_V_LATEST**. This constant is defined in the endpointdlp.h sample header file listing in the article [Endpoint data loss prevention](endpointdlp-endpoint-data-loss-prevention.md).

</dd> </dl>

<dl> <dt>

*PersistentFileName* \[in\]
</dt> <dd>

A LPCWSTR specifying the original path of the document.

</dd> </dl>

<dl> <dt>

*LocalFileName* \[in\]
</dt> <dd>

A LPCWSTR specifying the path to the real backing file of the document.

</dd> </dl>



## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |

