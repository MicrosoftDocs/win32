---
description: Converts the specified object from the OLE 1 storage model to an OLE 2 structured storage object including presentation data.
title: OleConvertOLESTREAMToIStorageEx2 function
ms.topic: reference
ms.date: 08/30/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OleConvertOLESTREAMToIStorageEx2
api_type: 
- DllExport
api_location: 
- Ole32.dll
---

# OleConvertOLESTREAMToIStorageEx2 function

Converts the specified object from the OLE 1 storage model to an OLE 2 structured storage object including presentation data.

> [!NOTE]  
> This is one of several compatibility functions.



## Syntax


```C++
HRESULT OleConvertOLESTREAMToIStorageEx2(
  [in]  LPOLESTREAM polestm,
  [out] LPSTORAGE   pstg,
  [out] CLIPFORMAT  *pcfFormat,
  [out] LONG        *plwWidth,
  [out] LONG        *plHeight,
  [out] DWORD       *pdwSize,
  [out] LPSTGMEDIUM pmedium,
  [in]  DWORD           opt,
  [in]  PVOID           pvCallbackContext,
  [in]  OLESTREAMQUERYCONVERTOLELINKCALLBACK pQueryConvertOLELinkCallback
);


```

## Parameters

### polestm [int]

A pointer to a stream that contains the persistent representation of the object in the OLE 1 storage format.

### pstg [out]

Pointer to the OLE 2 structured storage object.

### pcfFormat [out]

Pointer to where the format of the presentation data is returned. May be NULL, indicating the absence of presentation data.

### plwWidth [out]

Pointer to where the width value, in HIMETRIC, of the presentation data is returned.

### plHeight [out]

Pointer to where the height value, in HIMETRIC, of the presentation data is returned.

### pdwSize [out]

Pointer to where the size in bytes of the converted data is returned.

### pmedium [out]

Pointer to where the [STGMEDIUM](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure for the converted serialized data is returned.

### opt [in]

This value can be 0 or OLESTREAM_CONVERSION_DISABLEOLELINK(0x00000001). If the value is OLESTREAM_CONVERSION_DISABLEOLELINK, linked object will be disabled during conversion.

### pvCallbackContext [in]

The context of the user to be passed to the callback function *pQueryConvertOLELinkCallback*. May be NULL.

### pQueryConvertOLELinkCallback [in]

A pointer to an [OLESTREAMQUERYCONVERTOLELINKCALLBACK](/windows/win32/controls/olestreamqueryconvertolelinkcallback) callback function that queries the application if linked object should be converted or not. May be NULL.


## Return value

| Value | Description |
|-------|-------------|
| S_OK | Success. |
| E_INVALIDARG | Invalid argument. |

## Remarks

This function converts an OLE 1 object to an OLE 2 structured storage object. You can use this function to update OLE 1 objects to OLE 2 objects when a new version of the object application supports OLE 2.
This function differs from the [OleConvertOLESTREAMToIStorageEx](/windows/win32/api/ole2/nf-ole2-oleconvertolestreamtoistorageex) function in that the application can pass in an optional value to disable linked object during conversion or a callback function that queries the application if linked object should be converted or not.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from Ole32.dll.

## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client| Windows 10 RTM (with Oct 2023 security update or later) |
| Minimum supported server| Windows Server 2008 (with Oct 2023 security update or later) |
| Library | Ole32.lib | 
| DLL | Ole32.dll |





 
