---
description: Options for enumerating display modes.
ms.assetid: 7e0f5629-f8e2-478b-b8eb-00780a3dcf1f
title: DXGI_ENUM_MODES (DXGI.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DXGI\_ENUM\_MODES

Options for enumerating display modes.



| Constant/value                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                     |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DXGI_ENUM_MODES_INTERLACED"></span><span id="dxgi_enum_modes_interlaced"></span><dl> <dt>**DXGI\_ENUM\_MODES\_INTERLACED**</dt> <dt>1UL</dt> </dl>                 | Include interlaced modes.<br/>                                                                                                                                                                                                                                                                                                            |
| <span id="DXGI_ENUM_MODES_SCALING"></span><span id="dxgi_enum_modes_scaling"></span><dl> <dt>**DXGI\_ENUM\_MODES\_SCALING**</dt> <dt>2UL</dt> </dl>                          | Include stretched-scaling modes.<br/>                                                                                                                                                                                                                                                                                                     |
| <span id="DXGI_ENUM_MODES_STEREO"></span><span id="dxgi_enum_modes_stereo"></span><dl> <dt>**DXGI\_ENUM\_MODES\_STEREO**</dt> <dt>4UL</dt> </dl>                             | Include stereo modes.<br/> **Direct3D 11:** This enumeration value is supported starting with Windows 8.<br/>                                                                                                                                                                                                                       |
| <span id="DXGI_ENUM_MODES_DISABLED_STEREO"></span><span id="dxgi_enum_modes_disabled_stereo"></span><dl> <dt>**DXGI\_ENUM\_MODES\_DISABLED\_STEREO**</dt> <dt>8UL</dt> </dl> | Include stereo modes that are hidden because the user has disabled stereo. Control panel applications can use this option to show stereo capabilities that have been disabled as part of a user interface that enables and disables stereo.<br/> **Direct3D 11:** This enumeration value is supported starting with Windows 8.<br/> |



## Remarks

These flag options are used in [**IDXGIOutput::GetDisplayModeList**](/windows/desktop/api/DXGI/nf-dxgi-idxgioutput-getdisplaymodelist) to enumerate display modes.

These flag options are also used in [**IDXGIOutput1::GetDisplayModeList1**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutput1-getdisplaymodelist1) to enumerate display modes.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>DXGI.h</dt> </dl> |



## See also

<dl> <dt>

[DXGI Constants](d3d10-graphics-reference-dxgi-constants.md)
</dt> </dl>

 

 




