---
description: A list of some of the possible return codes for methods and functions.
ms.assetid: 391b56a1-d0aa-4d35-8dba-cf7de66513d8
title: S_PRESENT
ms.topic: article
ms.date: 05/31/2018
---

# S\_PRESENT

A list of some of the possible return codes for methods and functions.



| \#define                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| S\_OK                     | The device is running normally and can be used for rendering.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| S\_PRESENT\_OCCLUDED      | The presentation area is occluded. Occlusion means that the presentation window is minimized or another device entered the fullscreen mode on the same monitor as the presentation window and the presentation window is completely on that monitor. Occlusion will not occur if the client area is covered by another Window.<br/> Occluded applications can continue rendering and all calls will succeed, but the occluded presentation window will not be updated. Preferably the application should stop rendering to the presentation window using the device and keep calling [**CheckDeviceState**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9ex-checkdevicestate) until S\_OK or S\_PRESENT\_MODE\_CHANGED returns.<br/> |
| S\_PRESENT\_MODE\_CHANGED | The desktop display mode has been changed. The application can continue rendering, but there might be color conversion/stretching. Pick a back buffer format similar to the current display mode, and call Reset to recreate the swap chains. The device will leave this state after a Reset is called.                                                                                                                                                                                                                                                                                                                                                                                                                 |



 

Other error codes are contained in [D3DERR](d3derr.md).

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 




