---
description: The CABINETDLLVERSIONINFO contains the version information for Cabinet.dll.
ms.assetid: 1dc6962c-3087-4f56-8b65-fbf55e17eeb6
title: CABINETDLLVERSIONINFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CABINETDLLVERSIONINFO
api_type: 
- NA
api_location: 
---

# CABINETDLLVERSIONINFO structure

\[This structure contains information required only when using the **DllGetVersion** function, which is not supported. This documentation is provided for informational purposes only.\]

The **CABINETDLLVERSIONINFO** contains the version information for Cabinet.dll.

## Syntax


```C++
typedef struct {
  DWORD cbStruct;
  DWORD dwReserved1;
  DWORD dwReserved2;
  DWORD dwFileVersionMS;
  DWORD dwFileVersionLS;
} CABINETDLLVERSIONINFO, *PCABINETDLLVERSIONINFO;
```



## Members

<dl> <dt>

**cbStruct**
</dt> <dd>

The size of this structure, in bytes.

</dd> <dt>

**dwReserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**dwReserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**dwFileVersionMS**
</dt> <dd>

Contains the most significant bits of the version information. Bits 0-15 contain the minor version, and bits 16-31 contain the major version.

</dd> <dt>

**dwFileVersionLS**
</dt> <dd>

Contains the least significant bits of the version information. Bits 0-15 contain the revision number, and bits 16-31 contain the build number.

</dd> </dl>

## See also

<dl> <dt>

[**DllGetVersion**](dllgetversion.md)
</dt> </dl>

 

 



