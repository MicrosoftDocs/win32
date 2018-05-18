---
title: ConsentResult class
description: Used for managing the user's consent information.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'T:Microsoft.RightsManagement.ConsentResult'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ConsentResult class"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ConsentResult
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# ConsentResult class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Used for managing the user's consent information.

In operation, users can accept the consent or reject it. Users can also choose to show the consent again or not. You can save a user’s decision about whether to see the consent prompt again by using the [**ShowAgain**](consentresult-showagain.md) property.

## Syntax


```C++
public ref class ConsentResult sealed 
```



## Members

The **ConsentResult** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **ConsentResult** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ConsentResult** class has these methods. It also inherits methods from the **Object** class.



| Method                                               | Description                                                    |
|:-----------------------------------------------------|:---------------------------------------------------------------|
| [**ConsentResult**](consentresult-consentresult.md) | Creates and initializes an instance of a ConsentResult object. |



 

### Properties

The **ConsentResult** class has these properties.



| Property                                                | Access type          | Description                                                                                      |
|:--------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------|
| [**Accepted**](consentresult-accepted.md)<br/>   | Read-only<br/> | Gets the Accepted flag indicating the user has consented or not.                                 |
| [**ShowAgain**](consentresult-showagain.md)<br/> | Read-only<br/> | Gets the ShowAgain flag indicating whether the user consent prompt should be shown again or not. |
| [**UserId**](consentresult-userid.md)<br/>       | Read-only<br/> | Gets the email ID of the user giving consent.                                                    |



 

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

 

 





