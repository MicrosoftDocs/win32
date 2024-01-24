---
description: The GetFileCapabilities method retrieves a list of file capabilities from the current file.
ms.assetid: 0d24efd2-d411-4fb3-95c2-4742a58aeb5e
title: ISCardFileAccess::GetFileCapabilities method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardFileAccess.GetFileCapabilities
api_type: 
- COM
api_location: 
---

# ISCardFileAccess::GetFileCapabilities method

\[The **GetFileCapabilities** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **GetFileCapabilities** method retrieves a list of file capabilities from the current file.

## Syntax


```C++
HRESULT GetFileCapabilities(
  [in, out] LPTLV_TABLE *ppProperties,
  [in, out] LONG        *plProperties,
  [in]      SCARD_FLAGS Flags
);
```



## Parameters

<dl> <dt>

*ppProperties* \[in, out\]
</dt> <dd>

Pointer to TLV (tag, length, value) structures. On input, this parameter indicates the files for which to get properties; on output, this parameter contains the properties. The following example is a definition of the TLV structure.


```C++
#include <windows.h>

typedef struct
{
  DWORD  Tag;
  DWORD  Length;
  BYTE[]  Value;
  BOOL  Valid;
} TLV;
```



For more information on TLV structures, see [https://pcscworkgroup.com/](https://pcscworkgroup.com/).

</dd> <dt>

*plProperties* \[in, out\]
</dt> <dd>

Pointer to the number of TLV entries in *ppProperties*.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Specifies whether secure messaging has to be used and data preallocated.

<dl><span id="SC_FL_SECURE_MESSAGING"></span><span id="sc_fl_secure_messaging"></span><dt>

**SC\_FL\_SECURE\_MESSAGING**
</dt><span id="SC_FL_PREALLOCATED"></span><span id="sc_fl_preallocated"></span><dt>

**SC\_FL\_PREALLOCATED**
</dt> </dl> </dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation was completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                        |



 

## Remarks

For a list of all the methods defined by this interface, see [**ISCardFileAccess**](iscardfileaccess.md).

In addition to the COM error codes listed above, this interface may return a [*smart card*](../secgloss/s-gly.md) error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows XP<br/>                                |
| End of server support<br/>    | Windows Server 2003<br/>                       |



## See also

<dl> <dt>

[**ISCardFileAccess**](iscardfileaccess.md)
</dt> </dl>

 

 
