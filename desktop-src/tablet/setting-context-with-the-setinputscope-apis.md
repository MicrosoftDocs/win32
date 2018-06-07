---
Description: The recommended programmatic technique for setting contexts in an application that is not ink enabled is to use the SetInputScope functions to associate context with the fields in the application.
ms.assetid: 95b93804-8079-4b97-b1b0-dfc0138c94e8
title: Setting Context with the SetInputScope APIs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting Context with the SetInputScope APIs

The recommended programmatic technique for setting contexts in an application that is not ink enabled is to use the [**SetInputScope**](https://msdn.microsoft.com/4098525c-8d29-419a-9484-9e70420416bc) functions to associate context with the fields in the application.

The Microsoft Windows XP Tablet PC Edition Development Kit 1.7 was the first version of Microsoft Windows to offer [**SetInputScope**](https://msdn.microsoft.com/4098525c-8d29-419a-9484-9e70420416bc). Windows Vista also provides support for these functions. The **SetInputScope** definitions are declared in InputScope.idl and InputScope.h. For more details, see [Text Services Framework](https://msdn.microsoft.com/ecc34b2e-89e8-48a8-8a8e-442d2145fe24).

The [**SetInputScope**](https://msdn.microsoft.com/4098525c-8d29-419a-9484-9e70420416bc) functions are the recommended way to set context for controls and applications that are not ink enabled.

## Common Input Scopes

Using the [**SetInputScope**](https://msdn.microsoft.com/4098525c-8d29-419a-9484-9e70420416bc) functions and the defined set of common input scopes described in the [**InputScope**](https://www.bing.com/search?q=**InputScope**) enumeration, you can improve the recognition accuracy of the Microsoft handwriting recognizers.

> [!Note]  
> The recognizers for English (United States), English (United Kingdom), German, French, Italian, Spanish, Dutch, and Portuguese currently support using the common input scopes with [**SetInputScope**](https://msdn.microsoft.com/4098525c-8d29-419a-9484-9e70420416bc).

 

 

 



