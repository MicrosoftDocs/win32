---
title: MMC\_COOKIE
description: Represents a cookie that uniquely identifies a data object in MMC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'A57E9457-4947-4FE5-9856-06E35005DEA9'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMC_COOKIE"]
---

# MMC\_COOKIE

Represents a cookie that uniquely identifies a data object in MMC. For more information, see [Cookies](cookies.md).


```C++
typedef LONG_PTR MMC_COOKIE;
```



## Remarks

An **MMC\_COOKIE** value is provided by a snap-in, and is passed by MMC to methods such as [**IComponent::QueryDataObject**](icomponent-querydataobject.md).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                     |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mmc.idl</dt> </dl> |



## See also

<dl> <dt>

[MMC 2.0 Datatypes](mmc-2-0-datatypes.md)
</dt> <dt>

[Cookies](cookies.md)
</dt> <dt>

[**IS\_SPECIAL\_COOKIE**](is-special-cookie.md)
</dt> </dl>

 

 





