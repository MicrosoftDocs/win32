---
title: MCI\_VD\_STEP\_PARMS structure
description: The MCI\_VD\_STEP\_PARMS structure contains information for the MCI\_STEP command for videodisc devices.
ms.assetid: 5345468c-b195-485a-8101-4a076410f26a
keywords:
- MCI_VD_STEP_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_VD_STEP_PARMS
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

# MCI\_VD\_STEP\_PARMS structure

The **MCI\_VD\_STEP\_PARMS** structure contains information for the [**MCI\_STEP**](mci-step.md) command for videodisc devices.

## Syntax


```C++
typedef struct {
  DWORD_PTR dwCallback;
  DWORD     dwFrames;
} MCI_VD_STEP_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwFrames**
</dt> <dd>

Number of frames to step.

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

[**MCI\_STEP**](mci-step.md)
</dt> <dt>

[**mciSendCommand**](/windows/win32/Mmsystem/?branch=master)
</dt> </dl>

 

 





