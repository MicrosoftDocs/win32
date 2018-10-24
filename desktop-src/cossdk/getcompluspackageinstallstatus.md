---
Description: Indicates whether the 64-bit Common Language Runtime (CLR) is installed.
ms.assetid: c68af270-6a40-4026-9725-5fe657123fd5
title: GetComPlusPackageInstallStatus function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetComPlusPackageInstallStatus
api_type: 
- NA
api_location: 
---

# GetComPlusPackageInstallStatus function

Indicates whether the 64-bit Common Language Runtime (CLR) is installed.

## Syntax


```C++
ULONG WINAPI GetComPlusPackageInstallStatus(void);
```



## Parameters

This function has no parameters.

## Return value

This method can return the following values.



| Return value                                                                          | Description                                                       |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>          | The 32-bit Common Language Runtime (CLR) is installed.<br/> |
| <dl> <dt>0x00000001</dt> </dl> | The 64-bit Common Language Runtime (CLR) is installed.<br/> |



 

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




