---
title: DirectStorage constants
description: The following constants are declared in dstorageerr.h for DirectStorage-based programming.
ms.date: 08/25/2022
keywords:
- Constants
topic_type:
- apiref
api_name:
- Constants
api_location:
- dstorageerr.h
api_type:
- HeaderDef
ms.topic: reference
---

# DirectStorage constants

The following constants are declared in `dstorage.h` and `dstorageerr.h` for DirectStorage-based programming.

| Constant & value | Description |
|-|-|
| DSTORAGE_MIN_QUEUE_CAPACITY (0x80) | The minimum valid queue capacity. |
| DSTORAGE_MAX_QUEUE_CAPACITY (0x2000) | The maximum valid queue capacity. |
| DSTORAGE_REQUEST_MAX_NAME (64) | The maximum number of characters that will be stored for a request's name. |
| DSTORAGE_SDK_VERSION ([release-dependent]) | The major version number of DirectStorage. |
| E_DSTORAGE_ACCESS_VIOLATION ((HRESULT)0x89240009L) | The destination buffer for the DirectStorage request is not accessible. |
| E_DSTORAGE_ALREADY_RUNNING ((HRESULT)0x89240001L) | DirectStorage is already running exclusively. |
| E_DSTORAGE_COMPRESSED_DATA_TOO_LARGE ((HRESULT)0x89240039L) | The size of the resulting compressed data is too large for DirectStorage to decompress successfully on the GPU. |
| E_DSTORAGE_DECOMPRESSION_ERROR ((HRESULT)0x89240030L) | A generic error has happened during decompression. |
| E_DSTORAGE_END_OF_FILE ((HRESULT)0x89240007L) | The specified offset and length exceeds the size of the file. |
| E_DSTORAGE_FILE_NOT_OPEN ((HRESULT)0x8924000BL) | The file is not open. |
| E_DSTORAGE_INDEX_BOUND ((HRESULT)0x89240015L) | The index parameter is out of bound. |
| E_DSTORAGE_INVALID_DESTINATION_SIZE ((HRESULT)0x8924000FL) | The request's destination size is invalid. If no decompression is used, it must be equal to the request's length; If decompression is used, it must be larger than the request's length. |
| E_DSTORAGE_INVALID_FENCE ((HRESULT)0x89240022L) | The fence is not valid or has been released. |
| E_DSTORAGE_INVALID_FILE_HANDLE ((HRESULT)0x89240017L) | The specified file has not been opened. |
| E_DSTORAGE_INVALID_FILE_OFFSET ((HRESULT)0x8924001AL) | The request has invalid file offset for the specified decompression mode. |
| E_DSTORAGE_INVALID_MEMORY_QUEUE_PRIORITY ((HRESULT)0x89240024L) | Invalid priority is specified for the queue. Only DSTORAGE_PRIORITY_REALTIME is a valid priority for a memory queue. |
| E_DSTORAGE_INVALID_QUEUE_CAPACITY ((HRESULT)0x89240003L) | Invalid queue capacity parameter. |
| E_DSTORAGE_INVALID_QUEUE_PRIORITY ((HRESULT)0x89240013L) | Invalid priority is specified for the queue. |
| E_DSTORAGE_INVALID_SOURCE_TYPE ((HRESULT)0x8924001BL) | A memory source request was enqueued into a file source queue, or a file source request was enqueued into a memory source queue. |
| E_DSTORAGE_INVALID_STAGING_BUFFER_SIZE ((HRESULT)0x89240020L) | The specified staging buffer size is not valid. |
| E_DSTORAGE_INVALID_STATUS_ARRAY ((HRESULT)0x89240023L) | The status array is not valid or has been released. |
| E_DSTORAGE_IO_TIMEOUT ((HRESULT)0x89240016L) | The IO operation has timed out. |
| E_DSTORAGE_NOT_RUNNING ((HRESULT)0x89240002L) | DirectStorage is not running. |
| E_DSTORAGE_QUEUE_CLOSED ((HRESULT)0x89240010L) | The request targets a queue that is closed. |
| E_DSTORAGE_REQUEST_TOO_LARGE ((HRESULT)0x89240008L) | The IO request is too large. |
| E_DSTORAGE_RESERVED_FIELDS ((HRESULT)0x8924000CL) | A reserved field is not set to 0. |
| E_DSTORAGE_STAGING_BUFFER_LOCKED ((HRESULT)0x8924001FL) | Staging buffer size can be changed only when no queue is created and no file is open. |
| E_DSTORAGE_STAGING_BUFFER_TOO_SMALL ((HRESULT)0x89240021L) | The staging buffer isn't large enough to perform this operation. |
| E_DSTORAGE_TOO_MANY_FILES ((HRESULT)0x89240014L) | The number of files has reached the maximum limit. |
| E_DSTORAGE_TOO_MANY_QUEUES ((HRESULT)0x89240012L) | The number of queues has reached the maximum limit. |

## Requirements

| Requirement | Value |
|-|-|
| Header | dstorage.h<br/>dstorageerr.h |

## See also

* [DirectStorage API reference](./dstorage-api-reference.md)
