---
title: Collect WinHTTP traces
description: On Windows 7 and later, you can collect WinHTTP traces by using netsh.exe.
ms.date: 11/02/2022
ms.topic: article
---

# Collect WinHTTP traces

The ability to monitor WinHTTP functions and their corresponding network traffic is important. On Windows 7 and later, you can collect [Microsoft Windows HTTP Services (WinHTTP)](about-winhttp.md) traces for debugging and packet-sniffing purposes by using the command `netsh trace start scenario=internetclient`.

For more info, see [Network tracing in Windows](/windows/win32/ndf/network-tracing-in-windows-7) and [Using netsh to manage traces](/windows/win32/ndf/using-netsh-to-manage-traces).

> [!NOTE]
> The trace configuration tool `WinHttpTraceCfg.exe` is now deprecated.
