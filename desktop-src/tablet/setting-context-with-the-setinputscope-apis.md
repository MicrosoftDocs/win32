---
Description: The recommended programmatic technique for setting contexts in an application that is not ink enabled is to use the SetInputScope functions to associate context with the fields in the application.
ms.assetid: 95b93804-8079-4b97-b1b0-dfc0138c94e8
title: Setting Context with the SetInputScope APIs
ms.topic: article
ms.date: 05/31/2018
---

# Setting Context with the SetInputScope APIs

The recommended programmatic technique for setting contexts in an application that is not ink enabled is to use the [**SetInputScope**](https://msdn.microsoft.com/en-us/library/ms629025(v=VS.85).aspx) functions to associate context with the fields in the application.

The Microsoft Windows XP Tablet PC Edition Development Kit 1.7 was the first version of Microsoft Windows to offer [**SetInputScope**](https://msdn.microsoft.com/en-us/library/ms629025(v=VS.85).aspx). Windows Vista also provides support for these functions. The **SetInputScope** definitions are declared in InputScope.idl and InputScope.h. For more details, see [Text Services Framework](https://msdn.microsoft.com/en-us/library/ms629032(v=VS.85).aspx).

The [**SetInputScope**](https://msdn.microsoft.com/en-us/library/ms629025(v=VS.85).aspx) functions are the recommended way to set context for controls and applications that are not ink enabled.

## Common Input Scopes

Using the [**SetInputScope**](https://msdn.microsoft.com/en-us/library/ms629025(v=VS.85).aspx) functions and the defined set of common input scopes described in the [**InputScope**](https://msdn.microsoft.com/library/ms538181(v=VS.85).aspx) enumeration, you can improve the recognition accuracy of the Microsoft handwriting recognizers.

> [!Note]  
> The recognizers for English (United States), English (United Kingdom), German, French, Italian, Spanish, Dutch, and Portuguese currently support using the common input scopes with [**SetInputScope**](https://msdn.microsoft.com/en-us/library/ms629025(v=VS.85).aspx).

 

 

 



