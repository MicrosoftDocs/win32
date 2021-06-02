---
description: The Direct3D 9 API operates on either the Windows XP display driver model (XPDM) or the Windows Vista display driver model (WDDM), depending on the operating system installed.
ms.assetid: b552c822-aa01-4f1d-a0a6-1411ab006e7b
title: XPDM vs. WDDM
ms.topic: article
ms.date: 05/31/2018
---

# XPDM vs. WDDM

The Direct3D 9 API operates on either the Windows XP display driver model (XPDM) or the Windows Vista display driver model (WDDM), depending on the operating system installed. There are some differences in the way the Direct3D API behaves on the two driver models.

-   [Secure Desktop](#secure-desktop)
-   [Remote Desktop](#remote-desktop)
-   [Windows Service](#windows-service)
-   [Related topics](#related-topics)

## Secure Desktop

The secure desktop is active whenever any of the following occur: the user locks their desktop (Windows+L), the screen saver activates (when no user is logged in), or by default when User Account Control presents a prompt. When the secure desktop is active, the HAL device is not accessible.

Differences between XPDM and WDDM:

- Attempting to create a Direct3D9 HAL device will fail (with **D3DERR\_NOT\_AVAILABLE**), and any existing Direct3D 9 device will indicate a lost device return code on Present.

- Direct3D9Ex and Direct3D 10 APIs can successfully create a device while the secure desktop is active, and any calls to Present ([**IDirect3D9Ex**](/windows/desktop/api/d3d9/nn-d3d9-idirect3d9ex) or DXGI) will return a status code indicating the desktop is currently unavailable.



 

## Remote Desktop

When a remote desktop is active, the display is handled by the viewing machine with the hosting machine sending information via the network.

Differences between XPDM and WDDM:

- On XPDM, all attempts to create a Direct3D 9 device on a remote desktop will fail.

- On WDDM, remote desktop does support creating a HAL device over a remote desktop session.



 

## Windows Service

A Windows service is a process that runs in the background, controlled by the service-control manager (SCM). A service runs independent of the active desktop and therefore has limited ability to interact with users.

Differences between XPDM and WDDM:

- On WDDM, Session 0 Isolation ensures that a service does not have access to any user desktop as a security measure, therefore, a Direct3D 9 HAL device is never available from a Windows service.



 

> [!Note]  
> You cannot use Direct3D 9 in a Windows service. For more information, see [Microsoft support article 978635](https://support.microsoft.com/kb/978635).

 


The following table summarizes the differences listed here.



| Secure Desktop | XPDM | WDDM (Direct3D9) | WDDM(Direct3D9Ex/Direct3D10) |
|-----------------|------|------------------|------------------------------|
| NULLREF         | Yes  | Yes              | Yes                          |
| HAL             | No   | No               | Yes                          |
| REF             | Yes  | Yes              | Yes                          |
| Remote Desktop  |      |                  |                              |
| NULLREF         | No   | Yes              | Yes                          |
| HAL             | No   | Yes              | Yes                          |
| REF             | Yes  | Yes              | Yes                          |
| Windows Service |      |                  |                              |
| NULLREF         | No   | No               | No                           |
| HAL             | No   | No               | No                           |
| REF             | No   | No               | No                           |
| WARP10          | N/A  | N/A              | Yes                          |



 

For more information about XPDM, WDDM, Direct3D9Ex, and Direct3D 10, see [Graphics APIs in Windows](../direct3darticles/graphics-apis-in-windows-vista.md).

## Related topics

<dl> <dt>

[Direct3D Devices](direct3d-devices.md)
</dt> </dl>

 

 
