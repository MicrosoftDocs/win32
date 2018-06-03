---
title: PolicyDescriptor.EncryptedAppData property
description: Gets or sets the encrypted app data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: P:Microsoft.RightsManagement.PolicyDescriptor.EncryptedAppData
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- EncryptedAppData property
- EncryptedAppData property, PolicyDescriptor class
- PolicyDescriptor class, EncryptedAppData property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.PolicyDescriptor.EncryptedAppData
- Microsoft.RightsManagement.PolicyDescriptor.
- Microsoft.RightsManagement.PolicyDescriptor.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PolicyDescriptor.EncryptedAppData property

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Gets or sets the encrypted app data.

## Syntax


```C++
public:
property IMapView<String^, String^>^ EncryptedAppData { 
   IMapView<String^, String^>^ get();
   void set (IMapView<String^, String^>^ value);
}
```



## Property value

Type: **IMapView&lt;String^, String^&gt;^**

Encrypted app data accessed via [IMapView](https://msdn.microsoft.com/library/windows/apps/br226037.aspx).

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

[**PolicyDescriptor**](policydescriptor.md)
</dt> </dl>

 

 





