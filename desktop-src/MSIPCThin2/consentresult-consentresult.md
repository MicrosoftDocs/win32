---
title: ConsentResult.ConsentResult method
description: Creates and initializes an instance of a ConsentResult object.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.ConsentResult.ConsentResult
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ConsentResult method
- ConsentResult method, ConsentResult class
- ConsentResult class, ConsentResult method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ConsentResult.ConsentResult
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ConsentResult.ConsentResult method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Creates and initializes an instance of a [**ConsentResult**](https://msdn.microsoft.com/library/windows/desktop/dn920694) object.

## Syntax


```C++
public:
ConsentResult(
  bool accepted, 
  bool showAgain, 
  String^ userId
)
```



## Parameters

<dl> <dt>

*accepted* 
</dt> <dd>

Type: **bool**

True or false; the user accepted

</dd> <dt>

*showAgain* 
</dt> <dd>

Type: **bool**

True or false; the consent prompt should be shown to the user again

</dd> <dt>

*userId* 
</dt> <dd>

Type: **String^**

The Id of the user; usually represented as an email address

</dd> </dl>

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

[**ConsentResult**](consentresult.md)
</dt> </dl>

 

 





