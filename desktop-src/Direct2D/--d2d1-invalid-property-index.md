---
title: D2D1\_INVALID\_PROPERTY\_INDEX
description: Defines an invalid property index.
ms.assetid: 912207f4-90fc-47f6-851a-6537cfe80d49
topic_type:
- apiref
api_name:
- D2D1_INVALID_PROPERTY_INDEX
api_location:
- D2D1.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D2D1\_INVALID\_PROPERTY\_INDEX

Defines an invalid property index.

## Remarks

When the invalid property index is provided to [**GetValue**](/windows/win32/D2d1_1/?branch=master) or [**GetValueByName**](/windows/win32/D2d1_1/?branch=master), the call fails and the output buffer is zero-filled.

This value is returned by [**ID2D1Properties::GetPropertyIndex**](/windows/win32/D2d1_1/?branch=master) to indicate that the named property does not have an index in the property interface.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 and Platform Update for Windows 7 \[desktop apps \| UWP apps\]<br/>                        |
| Minimum supported server<br/> | Windows Server 2012 and Platform Update for Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/>                    |
| Header<br/>                   | <dl> <dt>D2D1.h</dt> </dl>                          |



## See also

<dl> <dt>

[**ID2D1Properties::GetPropertyIndex**](/windows/win32/D2d1_1/?branch=master)
</dt> </dl>

 

 





