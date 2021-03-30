---
Description: Specifies information about a document that is associated with an endpoint DLP print operation.
title: DLP_PRINT_INFO structure (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DLP_PRINT_INFO
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# DLP_PRINT_INFO structure

Specifies information about a document that is associated with an endpoint DLP print operation.

## Syntax


```C++
typedef struct _DLP_PRINT_INFO {
    DWORD Version;
    LPCWSTR PrinterName;
    LPCWSTR JobName;
    LPCWSTR OutputFileName;
    
}DLP_PRINT_INFO, *PDLP_PRINT_INFO;
```


## Members

<dl> <dt>

*Version* \[in\]
</dt> <dd>

A DWORD specifying the API version. This value should always be **DLP_PRINT_INFO_V_LATEST**. This constant is defined in the endpointdlp.h sample header file listing in the article [Endpoint data loss prevention](endpointdlp-endpoint-data-loss-prevention.md).

</dd> </dl>

<dl> <dt>

*PrinterName* \[in\]
</dt> <dd>

A LPCWSTR identifying the destination printer.

</dd> </dl>

<dl> <dt>

*JobName* \[in\]
</dt> <dd>

A LPCWSTR specifying print job name.

</dd> </dl>

<dl> <dt>

*OutputFileName* \[in\]
</dt> <dd>

A LPCWSTR specifying the path to the output file, when printing to a file.

</dd> </dl>



## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10                                             |

