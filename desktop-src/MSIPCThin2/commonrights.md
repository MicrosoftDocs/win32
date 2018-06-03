---
title: CommonRights class
description: Rights that are supported by all apps.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: T:Microsoft.RightsManagement.CommonRights
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CommonRights class
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CommonRights
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CommonRights class

Rights that are supported by all apps.

## Syntax


```C++
public ref class CommonRights sealed 
```



## Members

The **CommonRights** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **CommonRights** also has these types of members:

-   [Properties](#properties)

### Properties

The **CommonRights** class has these properties.



| Property                                       | Description                                                       |
|:-----------------------------------------------|:------------------------------------------------------------------|
| [**All**](commonrights-all.md)<br/>     | Gets a set of all **CommonRights**.<br/>                    |
| [**Owner**](commonrights-owner.md)<br/> | Gets a right that represents content ownership.<br/>        |
| [**View**](commonrights-view.md)<br/>   | Gets a right that allows viewing of protected content.<br/> |



 

## Remarks

For more information about the built-in rights and the usage restrictions associated with them that apps should observe, see [Built-in Rights Usage Restriction Reference](built-in-rights-usage-restriction-reference.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

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

 

 





