---
title: IConsentCallback interface
description: Interface for displaying consents.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: TMicrosoft.RightsManagement.IConsentCallback
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IConsentCallback interface
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.IConsentCallback
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IConsentCallback interface

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Interface for displaying consents. You provide the code for this callback to determine when and which consent notifications to display to the user.

## Syntax


```C++
public interface class IConsentCallback : IInspectable
```



## Members

The **IConsentCallback** interface inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **IConsentCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IConsentCallback** interface has these methods. It also inherits methods from the **Object** class.



| Method                                           | Description                                                                              |
|:-------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**ConsentAsync**](iconsent-iasyncoperation.md) | You, the app developer, will implement this method to prompt the user for their consent. |



 

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

 

 





