---
UID: 
title: UnicodeToBytes function
description: Converts Unicode characters to GB18030 bytes.
old-location: 
ms.assetid: na
ms.date: 04/10/2019
ms.keywords: WideCharToMultiByte, MultiByteToWideChar
ms.topic: reference
req.header: Gb18030.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP [desktop apps only]
req.target-min-winversvr: Windows Server 2003 [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: c_g18030.dll
req.irql: 
topic_type:
- APIRef
api_type: 
api_location:
- c_g18030.dll
api_name:
- UnicodeToBytes
targetos: Windows
req.typenames: 
req.redist: 
---

# UnicodeToBytes function

## Description

Deprecated. Converts Unicode characters to GB18030 bytes.

**Note**  When converting Unicode characters to GB18030 bytes, an application to run on Windows Vista and later should use the [WideCharToMultiByte](/windows/desktop/api/stringapiset/nf-stringapiset-widechartomultibyte) function.

```cpp
DWORD UnicodeToBytes(
  _In_ LPWSTR lpWideCharStr,
  _In_ UINT   cchWideChar,
  _In_ LPSTR  lpMultiByteStr,
  _In_ UINT   cchMultiByte
);
```

## Parameters

### lpWideCharStr [in]

Pointer to the Unicode string to convert.

### cchWideChar [in]

Character count of the Unicode string to convert.

### lpMultiByteStr [in]

Pointer to the target multibyte buffer.
If *lpMultiByteStr* is 0, the byte count of the GB18030 result is returned, and no conversion is done.

### cchMultiByte [in]

Byte count of the target multibyte buffer.
If *cchMultiByte* is 0, the byte count of the GB18030 result is returned, and no conversion is done.

## Returns

Returns the byte count of the multibyte characters that are generated, if successful.

## Remarks

## See also

[WideCharToMultiByte](/windows/desktop/api/stringapiset/nf-stringapiset-widechartomultibyte)

[MultiByteToWideChar](/windows/desktop/api/stringapiset/nf-stringapiset-multibytetowidechar)
