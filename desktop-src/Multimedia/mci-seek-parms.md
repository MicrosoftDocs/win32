---
title: MCI\_SEEK\_PARMS structure
description: The MCI\_SEEK\_PARMS structure contains positioning information for the MCI\_SEEK command.
ms.assetid: 2c199855-2134-4709-9313-5b8d66ce4f03
keywords:
- MCI_SEEK_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SEEK_PARMS
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MCI\_SEEK\_PARMS structure

The **MCI\_SEEK\_PARMS** structure contains positioning information for the [**MCI\_SEEK**](mci-seek.md) command.

## Syntax


```C++
typedef struct {
  DWORD_PTR dwCallback;
  DWORD     dwTo;
} MCI_SEEK_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwTo**
</dt> <dd>

Position to seek to.

</dd> </dl>

## Remarks

When assigning data to the members of this structure, set the corresponding flags in the *fdwCommand* parameter of the [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) function to validate the members.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mciapi.h</dt> </dl> |



## See also

<dl> <dt>

[**MCI**](mci.md)
</dt> <dt>

[**MCI Structures**](mci-structures.md)
</dt> <dt>

[**MCI\_SEEK**](mci-seek.md)
</dt> <dt>

[**mciSendCommand**](/windows/win32/Mmsystem/?branch=master)
</dt> </dl>

 

 





