---
Description: The NMCOLUMNINFO structure defines one column in the top pane of the Event Viewer.
ms.assetid: 21e0a129-464b-45b3-9c6b-6594e62fbce9
title: NMCOLUMNINFO structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# NMCOLUMNINFO structure

The **NMCOLUMNINFO** structure defines one column in the top pane of the Event Viewer.

## Syntax


```C++
typedef struct {
  LPSTR           szColumnName;
  NMCOLUMNVARIANT VariantData;
} EVENTCOLUMNINFO;
```



## Members

<dl> <dt>

**szColumnName**
</dt> <dd>

Displayable name of a specific column. If the name is too long, it will not be completely visible in the default Event Viewer configuration.

</dd> <dt>

**VariantData**
</dt> <dd>

The data inserted into the column.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




