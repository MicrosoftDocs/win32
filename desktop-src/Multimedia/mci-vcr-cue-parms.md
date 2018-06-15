---
title: MCI\_VCR\_CUE\_PARMS structure
description: The MCI\_VCR\_CUE\_PARMS structure contains parameters for the MCI\_CUE command for video-cassette recorders.
ms.assetid: b2ac0c43-93ea-41c9-b886-542bda57b59e
keywords:
- MCI_VCR_CUE_PARMS structure Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_VCR_CUE_PARMS
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

# MCI\_VCR\_CUE\_PARMS structure

The **MCI\_VCR\_CUE\_PARMS** structure contains parameters for the [**MCI\_CUE**](mci-cue.md) command for video-cassette recorders.

## Syntax


```C++
typedef struct tagMCI_VCR_CUE_PARMS {
  DWORD_PTR dwCallback;
  DWORD     dwFrom;
  DWORD     dwTo;
} MCI_VCR_CUE_PARMS;
```



## Members

<dl> <dt>

**dwCallback**
</dt> <dd>

The low-order word specifies a window handle used for the MCI\_NOTIFY flag.

</dd> <dt>

**dwFrom**
</dt> <dd>

Position to cue from.

</dd> <dt>

**dwTo**
</dt> <dd>

Position to cue to.

</dd> </dl>

## Remarks

When assigning data to the members of this structure, set the corresponding flags in the *fdwCommand* parameter of the [**mciSendCommand**](https://msdn.microsoft.com/en-us/library/Dd757160(v=VS.85).aspx) function to validate the members.

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

[**MCI\_CUE**](mci-cue.md)
</dt> <dt>

[**mciSendCommand**](https://msdn.microsoft.com/en-us/library/Dd757160(v=VS.85).aspx)
</dt> </dl>

 

 





