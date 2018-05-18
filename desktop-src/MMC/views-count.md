---
title: Views Count property
description: The Count property returns the number of View objects that are in the Views collection. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '92dac3b7-c766-4d7e-8835-427b026f5c60'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Count property MMC", "Count property MMC , Views object", "Views object MMC , Count property", "Count property MMC , Views interface", "Views interface MMC , Count property"]
topic_type:
- apiref
api_name:
- Views.Count
- Views.Count
api_location:
- Mmc.exe
api_type:
- COM
---

# Views::Count property

The **Count** property returns the number of [**View**](view-object.md) objects that are in the [**Views**](views-collection.md) collection. This property is read-only.

## Syntax


```VB
Property Count As Long
```



## Property value

The number of [**View**](view-object.md) objects contained in this collection.

## Examples


```VB
' Retrieve the number of View objects.
Dim nCount As Long
nCount = objViews.Count
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Views is defined as D6B8C29D-A1FF-4D72-AAB0-E381E9B9338D<br/>              |



## See also

<dl> <dt>

[**Views.Add**](views-add.md)
</dt> <dt>

[**Views.Item**](views-item.md)
</dt> </dl>

 

 





