---
title: CustomProtectedStream.CanWrite property
description: Gets a value that indicates whether the file can be written to.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'P:Microsoft.RightsManagement.CustomProtection.CustomProtectedStream.CanWrite'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["CanWrite property", "CanWrite property, CustomProtectedStream class", "CustomProtectedStream class, CanWrite property"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CustomProtectedStream.CanWrite
- Microsoft.RightsManagement.CustomProtectedStream.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# CustomProtectedStream.CanWrite property

Gets a value that indicates whether the file can be written to. Implements the [IRandomAccessStream.CanWrite](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.canwrite.aspx) property.

## Syntax


```C++
public:
virtual property bool CanWrite { 
   bool get();
}
```



## Property value

Type: [Boolean](https://msdn.microsoft.com/library/system.boolean.aspx)

**True** if the file can be written to; otherwise **false**.

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

[**CustomProtectedStream**](customprotectedstream.md)
</dt> </dl>

 

 





