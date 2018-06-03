---
title: GetProtectedFileStreamResult class
description: The result of the ProtectedFileStream AcquireAsync operation.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: T:Microsoft.RightsManagement.GetProtectedFileStreamResult
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- GetProtectedFileStreamResult class
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.GetProtectedFileStreamResult
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetProtectedFileStreamResult class

The result of the [**ProtectedFileStream::AcquireAsync**](protectedfilestream-acquireasync.md) operation.

## Syntax


```C++
public ref class GetProtectedFileStreamResult sealed 
```



## Members

The **GetProtectedFileStreamResult** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **GetProtectedFileStreamResult** also has these types of members:

-   [Properties](#properties)

### Properties

The **GetProtectedFileStreamResult** class has these properties.



| Property                                                             | Access type          | Description                                           |
|:---------------------------------------------------------------------|:---------------------|:------------------------------------------------------|
| [**Referrer**](getprotectedfilestreamresult-referrer.md)<br/> | Read-only<br/> | Gets the referral info.                               |
| [**Status**](getprotectedfilestreamresult-status.md)<br/>     | Read-only<br/> | Gets the return code.                                 |
| [**Stream**](getprotectedfilestreamresult-stream.md)<br/>     | Read-only<br/> | Gets the protected file stream if the call succeeded. |



 

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## See also

<dl> <dt>

[IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821)
</dt> </dl>

 

 





