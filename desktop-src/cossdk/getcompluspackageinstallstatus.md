---
description: Gets a value indicating whether the 64-bit Common Language Runtime (CLR) is installed.
title: GetComPlusPackageInstallStatus function
ms.topic: reference
ms.date: 03/02/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetComPlusPackageInstallStatus
api_type: 
- DllExport
api_location: 
- kernel32.dll
---

# GetComPlusPackageInstallStatus function

Gets a value indicating whether the 64-bit Common Language Runtime (CLR) is installed.

## Syntax


```C++
ULONG GetComPlusPackageInstallStatus(
    VOID
    );
```



## Parameters

None.

## Return value

This method can return the following values.

| Value | Description |
|-------|-------------|
| 0 | The 32-bit Common Language Runtime (CLR) is installed. |
| 0x00000001 | The 64-bit Common Language Runtime (CLR) is installed. |
    

## Remarks

This function is not defined in an SDK header and must be declared by the caller. This function is exported from kernel32.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows 10 |
| DLL | wldp.dll |



## See also



 

 


