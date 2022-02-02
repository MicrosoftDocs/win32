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

A `session` is an active communication between the terminal and other devices. It is the element that holds the user’s processes, data identity and runs its own win32k instance under csrss.exe (Client-server run-time subsystem).  If a terminal is not attached to a session, it will be attached shortly, or it is in the process of being destroyed.

There are different types of terminals, but the two most common ones are console and remote.

## Console vs. remote terminal

A `console` terminal is a terminal session connected to a console host, which is always active with few exceptions. There is only one active console terminal on a given machine, and all the local input/output devices are attached to that terminal.

The other common terminal is the `remote` terminal. A remote terminal is a terminal where all the input/output is on a remote system and not directly connected. For example, the keyboard, mouse, and monitor associated with the remote session are physically located on another system with a Remote Desktop Protocol (RDP) remote terminal. This terminal is created by protocol providers (RDP, Citrix, VMware, etc.) that integrate with the [Remote Desktop Services](/windows/win32/api/wtsprotocol/nf-wtsprotocol-iwrdsprotocolconnection-getusercredentials) Interface. The input/output devices associated with this are considered “remote.”

Win32k and other programs can use WTS APIs like [WTSQuerySessionInformation](/windows/win32/api/wtsapi32/nf-wtsapi32-wtsquerysessioninformationa) to be aware that the user is connected to the machine remotely. This is useful when devices are redirected; certain features need to be disabled, consider extra latency or take different paths.

## What happens when I remote into a machine?

Below is a walkthrough of what typically happens when you Remote Desktop Protocol into a machine.

### Remote terminal lifetime

The Remote Terminal lifetime is similar to the lifetime of the connection from the RDP Client to the RDP Server. If the RDP connection gets broken due to network issues, the Remote Terminal gets disconnected and needs to be established.

### Multiple terminals and sessions

On operating systems like Windows 10 Multisession and Windows Server with the Remote Desktop Session Host (RDSH) role installed, multiple users can be logged in and have a connected terminal like the setup below. In this case, there is still only a single console terminal/session but multiple remote terminals/sessions.

### WDDM graphics adapters and terminals

To get graphics out of a remote terminal, you need a remote [Windows Display Driver Model](/windows-hardware/drivers/display/windows-vista-display-driver-model-design-guide) (WDDM) indirect driver to configure your virtual monitor settings and process the desktop image to the client. There is a single instance of the WDDM remote Indirect Display driver for each remote terminal that the WDDM remote driver can expose up to 16 monitors to the remote session.

[WDDM remote Indirect Display drivers](/windows-hardware/drivers/display/indirect-display-driver-model-overview) can duplicate the display capabilities of the remote system. For example, if the monitor on the remote system is 1080p at 60Hz, the WDDM remote Indirect Display driver can expose a 1080p 60Hz monitor into the remote session; or if a remote client is running on an iPad, the WDDM remote Indirect Display driver for that remote terminal will expose a monitor matching the iPad display capabilities.

The display capacities of a WDDM GPU are always associated with the console terminal. This means a local monitor exposed through full WDDM driver, console WDDM Indirect Display Driver, or WDDM Display Only driver will only display the console terminal, hence the current console session. For example, a full WDDM GPU with two local monitors attached will be exposed in the console session. Still, that adapter is enumerated in a remote session without any monitors attached.

In WDDM remote sessions, the SKU’s default policy (with Group policy override) decides if either WARP (CPU rasterizer) or a render GPU paired with the remote WDDM Indirect Display adapter will render the desktop and application for that remote session.