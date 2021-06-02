---
description: Sets an on-disk .NET CRL Dynamic Code trustable for .NET.
ms.assetid: 4C8C3EF5-5C3C-4710-8223-D7B5BA86EF47
title: WldpSetDynamicCodeTrust function (Wldp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WldpSetDynamicCodeTrust
api_type: 
- DllExport
api_location: 
- wldp.dll
---

# WldpSetDynamicCodeTrust function

Sets an on-disk .NET CRL Dynamic Code trustable for .NET.

## Syntax


```C++
HRESULT WINAPI WldpSetDynamicCodeTrust(
   HANDLE FileHandle
);
```



## Parameters

<dl> <dt>

*FileHandle* 
</dt> <dd>

Handle to a on-disk dynamic code file.

</dd> </dl>

## Return value

This method returns **S\_OK** if successful or a failure code otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1803 \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wldp.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Wldp.dll</dt> </dl> |



 

 




