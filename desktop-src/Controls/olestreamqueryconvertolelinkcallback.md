---
description: Points to a function that queries the application if linked object in OLESTREAM should be disabled or not while converting OLESTREAM to IStorage.
title: OLESTREAMQUERYCONVERTOLELINKCALLBACK callback function
ms.topic: reference
ms.date: 08/30/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OLESTREAMQUERYCONVERTOLELINKCALLBACK
api_type: 
- DllExport
api_location: 
- Ole32.dll
---

# OLESTREAMQUERYCONVERTOLELINKCALLBACK callback function

Points to a function that queries the application if linked object in OLESTREAM should be disabled or not while converting OLESTREAM to IStorage.

## Syntax


```C++
typedef HRESULT(STDAPICALLTYPE* OLESTREAMQUERYCONVERTOLELINKCALLBACK)
    (_In_ LPCLSID       pClsid,
    _In_ LPOLESTR       szClass,
    _In_opt_ LPOLESTR   szTopicName,
    _In_opt_ LPOLESTR   szItemName,
    _In_opt_ LPOLESTR   szUNCName,
    _In_opt_ ULONG      linkUpdatingOption,
    _In_opt_ PVOID      pvContext);
```

## Parameters

### pClsid [in]

The CLSID for the linked object. If the ProgID(specified in szClass) is "OLE2Link", it's CLSID_StdOleLink; Otherwise it's the CLSID mapped to the ProgID in the registry.

### szClass [in]

The ProgID of the linked object.

### szTopicName [in, optional]

Path name of the linked file. May be NULL.

### szItemName [in, optional]

The name of item within the linked file to which is being linked. May be NULL.

### szUNCName [in, optional]

The network path name of the linked file in UNC format. May be NULL.

### linkUpdatingOption [in, optional]

Implementation-specific hint supplied by the application or higher-level protocol.

### pvContext [in, optional]

The context of the user passed to this callback function. May be NULL.


## Return value

| Value | Description |
|-------|-------------|
| S_OK | Success. |


## Remarks


## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client| TBD |
| Minimum supported server| TBD |





 
