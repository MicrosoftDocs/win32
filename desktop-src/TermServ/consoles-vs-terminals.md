---
title: Remote and console terminal differences
description: The differences between consoles and remote sessions.
ms.tgt_platform: multiple
ms.topic: article
ms.date: 10/26/2021
---

# Remote and console terminal differences

## What is a terminal?

A `terminal` is a concept that describes a group of input/output devices (keyboard, mouse, monitor, etc.) and configurations (settings on the devices). Consider the device you are using to read this document; are you on a desktop computer with a mouse, keyboard, and monitor? Or a mobile device with an LCD screen with touch capability and a Bluetooth keyboard? All these could be considered a terminal; they are group devices that communicate with each other.

A terminal’s purpose in life is to be attached to a session.

A `session` is active communication between the terminal and other devices. It’s the element that holds the user’s processes, data identity and runs its own win32k instance under csrss.exe (Client-server run-time subsystem).  If a terminal is not attached to a session, it will be attached shortly, or it’s in the process of being destroyed.

There are different types of terminals, but the two most common ones are console and remote.

## Console vs. remote terminal

A `console` is a terminal session connected to a remote host, which is always active with few exceptions. There’s only one active console terminal on a given machine, and all the local input/output devices are attached to the terminal.

The other common terminal is the `remote` terminal. A remote terminal is when a console terminal ‘connects’ into another and manipulates it remotely. This terminal is created by protocol providers (RDP, Citrix, VMware, etc.) that integrate with the [Remote Desktop Services](/windows/win32/api/wtsprotocol/nf-wtsprotocol-iwrdsprotocolconnection-getusercredentials) Interface. The input/output devices associated with this are considered “remote.”

Win32k and other programs can use WTS APIs like [WTSQuerySessionInformation](/windows/win32/api/wtsapi32/nf-wtsapi32-wtsquerysessioninformationa) to be aware that the user is connected to the machine remotely. This is useful when devices are redirected; certain features need to be disabled, consider extra latency or take different paths.

## What happens when I remote into a machine?

Below is a walkthrough of what typically happens when you Remote Desktop Protocol (RDP) into a machine.

### Remote terminal lifetime

The lifetime of a Remote Terminal is generally close to the lifetime of the connection from the RDP Client to the RDP Server. If the RDP connection gets broken due to network issues, the Remote Terminal is disconnected and needs to be established.

### Multiple terminals and sessions

On operating systems like Windows 10 Multisession and Windows Server with the Remote Desktop Session Host (RDSH) role installed, multiple users can be logged in and have a connected terminal similar to the setup below.

### WDDM graphics adapters and terminals

To get graphics out of a remote terminal, you need a [Windows Display Driver Model](/windows-hardware/drivers/display/windows-vista-display-driver-model-design-guide) (WDDM) driver to configure your virtual monitor settings.

WDDM drivers can duplicate either or both render capabilities (WDDM Render Only Driver)  and display capabilities (WDDM Display Only Driver/[WDDM Indirect Display Driver](/windows-hardware/drivers/display/indirect-display-driver-model-overview)) of the remote terminal in your session window. For example, if the remote monitor supports 1080p at 60Hz, the session window can render its graphics at that specification despite the local monitor having different capabilities.

In WDDM remote sessions, the SKU’s default policy (with Group policy override) decides if  either WARP (CPU rasterizer) or a render GPU paired with the remote WDDM Indirect Display adapter will render the desktop and application for that remote session.
