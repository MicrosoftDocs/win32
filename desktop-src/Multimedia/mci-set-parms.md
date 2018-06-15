---
title: MCI\_SET\_PARMS structure
description: The MCI\_SET\_PARMS structure contains information for the MCI\_SET command.
ms.assetid: 58811a0f-dc89-4303-b2b2-c98933ebab80
keywords:
- MCI_SET_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_SET_PARMS
api_location:
- mciapi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MCI\_SET\_PARMS structure

The **MCI\_SET\_PARMS** structure contains information for the [**MCI\_SET**](mci-set.md) command.

## Syntax


```C++
typedef struct {
  DWORD_PTR dwCallback;
  DWORD     dwTimeFormat;
  DWORD     dwAudio;
} MCI_SET_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwTimeFormat**
</dt> <dd>

Time format for device.

</dd> <dt>

**dwAudio**
</dt> <dd>

Audio output channel.

</dd> </dl>

## Remarks

When assigning data to the members of this structure, set the corresponding flags in the *fdwCommand* parameter of the [**mciSendCommand**](https://msdn.microsoft.com/en-us/library/Dd757160(v=VS.85).aspx) function to validate the members.

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

[**MCI\_SET**](mci-set.md)
</dt> <dt>

[**mciSendCommand**](https://msdn.microsoft.com/en-us/library/Dd757160(v=VS.85).aspx)
</dt> </dl>

 

 





