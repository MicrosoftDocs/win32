---
description: Retrieves a value that describes the Device Guard policy enforcement status for .NET dynamic code.
ms.assetid: 11E6C631-0FF8-4DB2-931A-1012B3CA4357
title: WldpIsDynamicCodePolicyEnabled function (Wldp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WldpIsDynamicCodePolicyEnabled
api_type: 
- DllExport
api_location: 
- wldp.dll
---

# WldpIsDynamicCodePolicyEnabled function

Retrieves a value that describes the Device Guard policy enforcement status for .NET dynamic code.

## Syntax


```C++
HRESULT WINAPI WldpIsDynamicCodePolicyEnabled(
  _Out_ PBOOL  isEnabled
);
```



## Parameters

<dl> <dt>

*isEnabled* \[out\]
</dt> <dd>

On success, returns **true** if the Device Guard policy enforces .NET Dynamic Code policy; otherwise, returns **false**.

</dd> </dl>

## Return value

This method returns **S\_OK** if successful or a failure code otherwise.

## Remarks

Dynamic code refers to .NET CRL dynamically-generated code.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1803 \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wldp.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Wldp.dll</dt> </dl> |



 

 




