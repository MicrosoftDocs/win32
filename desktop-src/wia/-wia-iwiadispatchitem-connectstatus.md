---
description: Retrieves the connection status of the device. This property applies only to items of type device (root items). Possible values are &\#0034;connected&\#0034;, &\#0034;disconnected&\#0034;, or NULL (if this property does not apply to the item). Read-only.
ms.assetid: 44b1713a-5859-4973-8495-e8a67f2344b2
title: Item.ConnectStatus property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Item.ConnectStatus
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# Item.ConnectStatus property

Retrieves the connection status of the device. This property applies only to items of type device (root items). Possible values are "connected", "disconnected", or **NULL** (if this property does not apply to the item). Read-only.

This property is read-only.

## Syntax


```JScript
propVal = Item.ConnectStatus
```



## Property value

String that receives the connection status.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 




