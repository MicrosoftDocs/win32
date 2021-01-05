---
description: Retrieves a value that determines if the specified in-memory or on-disk .NET CRL dynamic code is trusted by Device Guard policy.
ms.assetid: 9C12894D-98AF-4408-A11A-865E4DA1DA68
title: WldpQueryDynamicCodeTrust function (Wldp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WldpQueryDynamicCodeTrust
api_type: 
- DllExport
api_location: 
- wldp.dll
---

# WldpQueryDynamicCodeTrust function

Retrieves a value that determines if the specified in-memory or on-disk .NET CRL dynamic code is trusted by Device Guard policy.

## Syntax


```C++
HRESULT WINAPI WldpQueryDynamicCodeTrust(
   _When_(baseImage != NULL, _In_opt_)
    _When_(baseImage == NULL, _In_)
    HANDLE                                                 fileHandle,
   _When_(fileHandle == NULL, _In_reads_bytes_opt_(imageSize))
    _When_(fileHandle != NULL, _In_reads_bytes_(imageSize))
    PVOID  baseImage,
   _In_ ULONG                                                                                                                         ImageSize
);
```



## Parameters

<dl> <dt>

*fileHandle* 
</dt> <dd>

Handle to the on-disk dynamic code file to check. If *fileHandle* is non-**NULL**, *baseImage* should be **NULL**.

</dd> <dt>

*baseImage* 
</dt> <dd>

Pointer to the in-memory PE file to check. If *baseImage* is non-**NULL**, *FileHandle* should be **NULL**.

</dd> <dt>

*ImageSize* 
</dt> <dd>

When *baseImage* is non-**NULL**, indicates the buffer size that *baseImage* points to.

</dd> </dl>

## Return value

This method returns **S\_OK** if successful or a failure code otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wldp.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Wldp.dll</dt> </dl> |



 

 




