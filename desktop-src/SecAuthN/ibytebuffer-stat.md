---
description: The Stat method retrieves statistical information from the stream object.
ms.assetid: 7dfb59e9-143a-402e-990a-a2b35e6443dd
title: IByteBuffer::Stat method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer.Stat
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer::Stat method

\[The **Stat** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **Stat** method retrieves statistical information from the stream object.

## Syntax


```C++
HRESULT Stat(
  [out] LPSTATSTRUCT pstatstg,
  [in]  LONG         grfStatFlag
);
```



## Parameters

<dl> <dt>

*pstatstg* \[out\]
</dt> <dd>

Points to a **STATSTRUCT** structure where this method places information about this stream object. This pointer is **NULL** if an error occurs.

</dd> <dt>

*grfStatFlag* \[in\]
</dt> <dd>

Specifies that this method does not return some of the fields in the **STATSTRUCT** structure, thus saving a memory allocation operation. Values are taken from the [**STATFLAG**](/windows/win32/api/wtypes/ne-wtypes-statflag) enumeration

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates the call was successful.

## Remarks

The **IByteBuffer::Stat** method retrieves a pointer to the **STATSTRUCT** structure that contains information about this open stream.

## Examples

The following example shows retrieving statistical information from the stream.


```C++
STATSTRUCT  statstr;
HRESULT     hr;

// Retrieve the statistical information.
hr = pIByteBuff->Stat(&statstr,
                      STATFLAG_DEFAULT);
if (FAILED(hr))
  printf("Failed IByteBuffer::Stat\n");
else
  // Use statstr as needed.
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardssp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardssp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_IByteBuffer is defined as E126F8FE-A7AF-11D0-B88A-00C04FD424B9<br/>          |



 

