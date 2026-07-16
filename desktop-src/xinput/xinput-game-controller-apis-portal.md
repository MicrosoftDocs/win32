---
title: XInput Game Controller APIs
description: XInput Game Controller APIs
ms.assetid: fbbc651b-9264-9b5d-01c6-efc58f50b19d
ms.topic: reference
ms.date: 07/14/2025
---

# XInput Game Controller APIs

> [!Important]
> **For new projects, use [GameInput](/gaming/gdk/_content/gc/input/overviews/input-overview) instead of XInput.** GameInput is the modern replacement that supports all controller types (not just Xbox-compatible gamepads), provides lower latency, and works across all Windows platforms. XInput is limited to 4 Xbox-compatible controllers and does not support newer input devices. Existing XInput code continues to work, but new development should target GameInput.

> [!NOTE]
> GameInput is a functional superset of all legacy input APIs—XInput, DirectInput, Raw Input, Human Interface Device (HID), and WinRT—with new features that expose input devices of all kinds through a single consistent interface. It's available on all Windows platforms (including PC, Xbox, HoloLens, IoT), previous versions of Windows (all the way back to Windows 7), and is callable from GDK, Win32, and Universal Windows Platform (UWP) applications.

## Purpose

XInput Game Controller API enables applications to receive input from a controller.

## In this section

| Topic                                                         | Description                                                                                                                                             |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Programming Guide](programming-guide.md)<br/>         | This guide contains information on how to use the XInput API to interact with a controller when it is connected to a Windows PC. <br/> |
| [Programming Reference](programming-reference.md)<br/> | XInput functions and structures.<br/>                                                                                                             |

## Developer audience

XInput Game Controller APIs is designed for use by developers who want to use a controller for their Windows applications.

