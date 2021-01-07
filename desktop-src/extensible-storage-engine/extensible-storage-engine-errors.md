---
description: "Learn more about: Extensible Storage Engine Errors"
title: Extensible Storage Engine Errors
TOCTitle: Extensible Storage Engine Errors
ms:assetid: 0c071ed6-0ea2-448b-9f9f-e606c5abf3db
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269184(v=EXCHG.10)
ms:contentKeyID: 32765487
ms.date: 04/11/2016
ms.topic: article
---

# Extensible Storage Engine Errors


_**Applies to:** Windows | Windows Server_

## Extensible Storage Engine Errors

All possible errors returned by the Extensible Storage Engine (ESE) API are defined by the [JET_ERR](./jet-err.md) data type. For a list of the error flags that are defined for this API, see [Extensible Storage Engine Error Codes](./extensible-storage-engine-error-codes.md).

Throughout the ESE API documentation, only the most important errors are documented. These errors typically represent API usage errors or very important error conditions. Be aware that any of these ESE APIs can also return other errors that are not documented for each API. In these cases, the caller should simply handle the error as they would any other error that is returned by the API. The specific error value may then be used for diagnostic purposes such as tracing.

In general, a value that is greater than zero should be interpreted as a warning, a value of zero should be interpreted as success, and a value that is less than zero should be interpreted as an error. No other patterns in these values (for example, ranges of values) should be relied upon by an application.

When ESE encounters some of the more serious errors, it creates an event log entry that contains details about the errors. The level of logging can be controlled by [Event Log Parameters](./event-log-parameters.md).

Some applications require the ability to return [JET_ERR](./jet-err.md)s as HRESULTs. The following C++ example shows how to make that conversion:

```cpp
    #ifndef FACILITY_JET_ERR
    #define FACILITY_JET_ERR 0xE5E
    #endif
    #ifndef HRESULT_FROM_JET_ERR
    #define HRESULT_FROM_JET_ERR( __err )
    (
      ( __err ) == JET_errSuccess ?
      S_OK :
      (
        ( __err ) == JET_errOutOfMemory ?
        E_OUTOFMEMORY :
        MAKE_HRESULT
        (
          (
            ( __err ) < 0 ?
            SEVERITY_ERROR :
            SEVERITY_SUCCESS
          ),
          FACILITY_JET_ERR,
          (
            ( __err ) < 0 ?
            -( __err ) :
            ( __err )
          )
          & 0xFFFF
        )
      )
    )
    
    #endif
```

For information about configuring system parameters for error handling, see [Error Handling Parameters](./error-handling-parameters.md).

### See Also

[Error Handling Parameters](./error-handling-parameters.md)

[Extensible Storage Engine Error Codes](./extensible-storage-engine-error-codes.md)

[JET_ERR](./jet-err.md)
