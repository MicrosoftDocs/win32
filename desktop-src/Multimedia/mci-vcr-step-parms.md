---
title: MCI_VCR_STEP_PARMS structure
description: The MCI\_VCR\_STEP\_PARMS structure contains parameters for the MCI\_STEP command for video-cassette recorders.
ms.assetid: 57751de6-d174-418f-8167-402d3ead4e24
keywords:
- MCI_VCR_STEP_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_VCR_STEP_PARMS
api_location:
- Vcr.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MCI\_VCR\_STEP\_PARMS structure

The **MCI\_VCR\_STEP\_PARMS** structure contains parameters for the [**MCI\_STEP**](mci-step.md) command for video-cassette recorders.

## Syntax


```C++
typedef struct tagMCI_VCR_STEP_PARMS {
  DWORD_PTR dwCallback;
  DWORD     dwFrames;
} MCI_VCR_STEP_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwFrames**
</dt> <dd>

Number of frames to jump (the length of a single step) as the [**MCI\_STEP**](mci-step.md) command steps forward or backward through the content.

</dd> </dl>

## Remarks

When assigning data to the members in this structure, set the corresponding flags in the *fdwCommand* parameter of [**mciSendCommand**](https://msdn.microsoft.com/en-us/library/Dd757160(v=VS.85).aspx) to validate the members.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vcr.h</dt> </dl> |



## See also

<dl> <dt>

[**MCI**](mci.md)
</dt> <dt>

[**MCI Structures**](mci-structures.md)
</dt> <dt>

[**MCI\_STEP**](mci-step.md)
</dt> <dt>

[**mciSendCommand**](https://msdn.microsoft.com/en-us/library/Dd757160(v=VS.85).aspx)
</dt> </dl>

 

 





