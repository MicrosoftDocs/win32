---
title: MCI\_STATUS\_PARMS structure
description: The MCI\_STATUS\_PARMS structure contains information for the MCI\_STATUS command.
ms.assetid: c4897b34-4184-46aa-af17-2127edfbf82d
keywords:
- MCI_STATUS_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_STATUS_PARMS
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

# MCI\_STATUS\_PARMS structure

The **MCI\_STATUS\_PARMS** structure contains information for the [**MCI\_STATUS**](mci-status.md) command.

## Syntax


```C++
typedef struct {
  DWORD_PTR dwCallback;
  DWORD_PTR dwReturn;
  DWORD     dwItem;
  DWORD     dwTrack;
} MCI_STATUS_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwReturn**
</dt> <dd>

Contains information on return.

</dd> <dt>

**dwItem**
</dt> <dd>

Capability being queried.

</dd> <dt>

**dwTrack**
</dt> <dd>

Length or number of tracks.

</dd> </dl>

## Remarks

The MCI\_STATUS\_ITEM flag must be set in the *fdwCommand* parameter of the [**mciSendCommand**](/windows/desktop/api/Mmsystem/) function to validate the **dwItem** member, which should contain one of the constants indicating what status information is being requested.

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

[**MCI\_STATUS**](mci-status.md)
</dt> <dt>

[**mciSendCommand**](/windows/desktop/api/Mmsystem/)
</dt> </dl>

 

 





