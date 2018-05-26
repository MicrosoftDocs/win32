---
title: MCI\_OVLY\_LOAD\_PARMS structure
description: The MCI\_OVLY\_LOAD\_PARMS structure contains information for the MCI\_LOAD command for video-overlay devices.
ms.assetid: 701c27da-72bf-493d-a679-9e0bd210215d
keywords:
- MCI_OVLY_LOAD_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_OVLY_LOAD_PARMS
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MCI\_OVLY\_LOAD\_PARMS structure

The **MCI\_OVLY\_LOAD\_PARMS** structure contains information for the [**MCI\_LOAD**](mci-load.md) command for video-overlay devices.

## Syntax


```C++
typedef struct {
  DWORD_PTR dwCallback;
  LPCTSTR   lpfilename;
  RECT      rc;
} MCI_OVLY_LOAD_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**lpfilename**
</dt> <dd>

Name of file to load.

</dd> <dt>

**rc**
</dt> <dd>

Identifies the area of the video buffer to update. [RECT](http://go.microsoft.com/fwlink/p/?linkid=16998) structures are handled differently in MCI than in other parts of Windows; in MCI, **rc.right** contains the width of the rectangle and **rc.bottom** contains its height.

</dd> </dl>

## Remarks

When assigning data to the members of this structure, set the corresponding flags in the *fdwCommand* parameter of the [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) function to validate the members.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Mmsystem.h</dt> </dl> |



## See also

<dl> <dt>

[**MCI**](mci.md)
</dt> <dt>

[**MCI Structures**](mci-structures.md)
</dt> <dt>

[**MCI\_LOAD**](mci-load.md)
</dt> <dt>

[**mciSendCommand**](/windows/win32/Mmsystem/?branch=master)
</dt> <dt>

[RECT](http://go.microsoft.com/fwlink/p/?linkid=16998)
</dt> </dl>

 

 





