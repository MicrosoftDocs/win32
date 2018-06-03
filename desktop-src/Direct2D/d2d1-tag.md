---
title: D2D1\_TAG
description: An application-defined 64-bit value used to \ 160;mark a set of rendering operations.
ms.assetid: 4f363295-f140-4149-ba78-3abbc56eebe8
keywords:
- D2D1_TAG
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D2D1\_TAG

An application-defined 64-bit value used to mark a set of rendering operations.


```C++
typedef UINT64 D2D1_TAG;
```



## Remarks

To set a tag before a series of rendering operations, use the [**ID2D1RenderTarget::SetTags**](/windows/desktop/api/d2d1/) method. To retrieve the current tag, use the [**ID2D1RenderTarget::GetTags**](/windows/desktop/api/d2d1/) method.

## Requirements



|                                     |                                                                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7, Windows Vista with SP2 and Platform Update for Windows Vista \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2008 R2, Windows Server 2008 with SP2 and Platform Update for Windows Server 2008 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>D2d1.h</dt> </dl>                                                        |



## See also

<dl> <dt>

[**GetTags**](/windows/desktop/api/d2d1/)
</dt> <dt>

[**SetTags**](/windows/desktop/api/d2d1/)
</dt> </dl>

 

 





