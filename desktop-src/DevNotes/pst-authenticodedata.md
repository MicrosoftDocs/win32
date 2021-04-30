---
description: Defines data to be used in Microsoft Authenticode verification of item data.
ms.assetid: 73c0e84f-7d59-4efa-927d-af8d7305bc9d
title: PST_AUTHENTICODEDATA structure (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PST_AUTHENTICODEDATA
api_type: 
- HeaderDef
api_location: 
- Pstore.h
---

# PST\_AUTHENTICODEDATA structure

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

Defines data to be used in Microsoft Authenticode verification of item data.

## Syntax


```C++
typedef struct {
  DWORD    cbSize;
  DWORD    dwModifiers;
  LPCWSTR  szRootCA;
  LPCWSTR  szIssuer;
  LPCWSTR  szPublisher;
  LPCWSTR  szProgramName;
} PST_AUTHENTICODEDATA, *PPST_AUTHENTICODE_DATA;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size of this structure.

</dd> <dt>

**dwModifiers**
</dt> <dd>

A value that identifies the modifier that one of a chain of callers must verify.



| Value                                                                                                                                                                                                                                                 | Meaning                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PST_AC_SINGLE_CALLER"></span><span id="pst_ac_single_caller"></span><dl> <dt>**PST\_AC\_SINGLE\_CALLER**</dt> <dt>0</dt> </dl>           | Only a single level in the call chain to PStore. The caller passes the verification check. The specified image is the immediate caller, and is an application (.exe).<br/>              |
| <span id="PST_AC_TOP_LEVEL_CALLER"></span><span id="pst_ac_top_level_caller"></span><dl> <dt>**PST\_AC\_TOP\_LEVEL\_CALLER**</dt> <dt>1</dt> </dl> | The top-level caller must pass the check, but there may be intermediate DLLs. The specified image is not necessarily the immediate caller, and is an application (.exe).<br/>           |
| <span id="PST_AC_IMMEDIATE_CALLER"></span><span id="pst_ac_immediate_caller"></span><dl> <dt>**PST\_AC\_IMMEDIATE\_CALLER**</dt> <dt>2</dt> </dl>  | The immediate caller must pass the check, but need not be the top-level process. The specified image is the immediate caller, and the image can be an application (.exe) or a DLL.<br/> |



 

</dd> <dt>

**szRootCA**
</dt> <dd>

A pointer to a wide character string that represents the root certification authority (CA) for the certificate; use **NULL** to use any available CA.

</dd> <dt>

**szIssuer**
</dt> <dd>

A pointer to a wide character string that represents the CA that issued the certificate; use **NULL** to use any available CA.

</dd> <dt>

**szPublisher**
</dt> <dd>

A pointer to a wide character string that represents the software publisher; use **NULL** to use any available CA.

</dd> <dt>

**szProgramName**
</dt> <dd>

A pointer to a wide character string that represents the program name; use **NULL** to use any available CA.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl> |



 

 
