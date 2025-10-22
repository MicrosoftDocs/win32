---
title: Registry Keys Affected by WOW64
description: Under WOW64, certain registry keys are redirected.
ms.assetid: 7b3f4f11-24bc-44f7-837e-d61d853c7291
keywords:
- registry keys 64-bit Windows Programming
- WOW64 64-bit Windows Programming , registry keys
- redirected registry keys 64-bit Windows Programming
- reflected registry keys 64-bit Windows Programming
- shared registry keys 64-bit Windows Programming
ms.topic: concept-article
ms.date: 01/23/2021
---

# Registry Keys Affected by Windows Installations That Include Windows on Windows (WOW) Support For Multiple Processor Architectures

In 64-bit Windows installations beginning with Windows XP and Windows Server 2003, and in 32-bit ARM processor architecture Windows installations beginning with Windows RT (Windows 8) (hereafter referenced as **affected Windows installations**), certain registry keys are *redirected*.

On affected Windows installations, when a process with a processor architecture different from the operating system's processor architecture (referred to hereafter as a **WOW application**) makes a registry call for a redirected key, the registry redirector intercepts the call and maps it to the key's corresponding physical registry location. For example, a 32-bit Intel IA-32 [**x86**] application running on an **AMD64** / Intel x86-x64 Windows installation would be affected by a redirected registry key; when this x86 application calls a redirected key, the registry redirector intercepts the application's call and redirects it to the key's corresponding physical registry location. For more information, see [Registry Redirector](registry-redirector.md).

Other registry keys are *shared* by applications of differing processor architectures on affected Windows installations. WOW application registry calls to shared keys are not redirected. Instead, one physical copy of the key is mapped into each logical view of the registry.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** A subset of redirected registry keys are also *reflected* to keep the keys and their values synchronized between 32-bit and 64-bit views of the registry. Registry reflection was removed starting with Windows 7 and Windows Server 2008 R2. For more information, see [Registry Reflection](registry-reflection.md).

This topic lists registry keys that are redirected, shared, or redirected and reflected under WOW. It also lists symbolic links that provide compatibility for existing applications that may use hardcoded registry key paths containing **Wow6432Node**, the redirected registry location for x86 processes running on AMD64 Windows installations. For more information, see the following:

- [Redirected, Shared, and Reflected Keys Under WOW](#redirected-shared-and-reflected-keys-under-wow)
- [Windows on Windows 64 (WOW64) Symbolic Links](#windows-on-windows-64-wow64-symbolic-links)

## Redirected, Shared, and Reflected Keys Under WOW

For WOW applications on affected Windows installations, the following table lists registry keys that are redirected, shared, or redirected and reflected. Subkeys of the keys in this table inherit the parent key's behavior unless otherwise specified. If a key has no parent listed in this table, the key is shared.

| Key | Windows Server 2008 R2, Windows 7, and Newer | Windows Server 2008, Windows Vista, Windows Server 2003, and Windows XP |
|-|-|-|
| **:::no-loc text="HKEY_LOCAL_MACHINE":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE":::** | Redirected | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes":::** | Shared | Redirected and reflected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Appid":::** | Shared | Redirected and reflected with one exception: the [DllSurrogate](../com/dllsurrogate.md) and [DllSurrogateExecutable]( ../com/dllsurrogateexecutable.md) registry values are not reflected if their value is an empty string. |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\CLSID":::** | Redirected | Redirected and reflected only for CLSIDs that do not specify InprocServer32 or InprocHandler32. |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\DirectShow":::** | Redirected | Redirected and reflected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\HCP":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Interface":::** | Redirected | Redirected and reflected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Media Type":::** | Redirected | Redirected and reflected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\MediaFoundation":::** | Redirected | Redirected and reflected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Clients":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\COM3":::** | Shared | Redirected and reflected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\Calais\\Current":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\Calais\\Readers":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\Services":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\CTF\\SystemShared":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\CTF\\TIP":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\DFS":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Driver Signing":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EnterpriseCertificates":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\EventSystem":::** | Shared | Redirected and reflected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\MSMQ":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Non-Driver Signing":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Notepad\\DefaultFonts":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\OLE":::** | Shared | Redirected and reflected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\RAS":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\RPC":::** | Shared | Redirected and reflected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\SOFTWARE\\Microsoft\\Shared Tools\\MSInfo":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\SystemCertificates":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\TermServLicensing":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\TransactionServer":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Control Panel\\Cursors\\Schemes":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AutoplayHandlers":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\DriveIcons":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\KindMap":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Group Policy":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\PreviewHandlers":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Setup":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Telephony\\Locations":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Console":::**| Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontDpi":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontLink":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontMapper":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\FontSubstitutes":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Gre_Initialize":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Language Pack":::** | Shared | Redirected |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkCards":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Perflib":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Ports":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Print":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Time Zones":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies":::** | Shared | Shared |
| **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\RegisteredApplications":::** | Shared | Shared; **Windows Server 2003 and Windows XP:** This key was added in Windows Vista. |
| **:::no-loc text="HKEY_CURRENT_USER":::** | Shared | Shared |
| **:::no-loc text="HKEY_CURRENT_USER\\SOFTWARE":::** | Shared | Shared |
| **:::no-loc text="HKEY_CURRENT_USER\\SOFTWARE\\Classes":::** | Shared | Redirected and reflected |
| **:::no-loc text="HKEY_CURRENT_USER\\SOFTWARE\\Classes\\Appid":::** | Shared | Redirected and reflected with one exception: the [DllSurrogate](../com/dllsurrogate.md) and [DllSurrogateExecutable]( ../com/dllsurrogateexecutable.md) registry values are not reflected if their value is an empty string. |
| **:::no-loc text="HKEY_CURRENT_USER\\SOFTWARE\\Classes\\CLSID":::** | Redirected | Redirected and reflected |
| **:::no-loc text="HKEY_CURRENT_USER\\SOFTWARE\\Classes\\DirectShow":::** | Redirected | Redirected and reflected |
| **:::no-loc text="HKEY_CURRENT_USER\\SOFTWARE\\Classes\\Interface":::** | Redirected | Redirected and reflected |
| **:::no-loc text="HKEY_CURRENT_USER\\SOFTWARE\\Classes\\Media Type":::** | Redirected | Redirected and reflected |
| **:::no-loc text="HKEY_CURRENT_USER\\SOFTWARE\\Classes\\MediaFoundation":::** | Redirected | Redirected and reflected |

**:::no-loc text="HKEY_CURRENT_USER":::** is a symbolic link to **:::no-loc text="HKEY_USERS\\[SID]":::** where [SID] indicates a match for the current user's security ID (SID). **:::no-loc text="HKEY_USERS\\[SID]\\SOFTWARE\\Classes":::** is a symbolic link to **:::no-loc text="HKEY_USERS\\[SID]_Classes":::**.

**:::no-loc text="HKEY_CLASSES_ROOT":::** is a merged view of **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes":::** and **:::no-loc text="HKEY_CURRENT_USER\\SOFTWARE\\Classes":::**. Redirected keys in these registry paths are effectively redirected for **:::no-loc text="HKEY_CLASSES_ROOT":::** also. This is also true for reflected keys on systems that support them.

## Windows on Windows 64 (WOW64) Symbolic Links

WOW64 defines the following symbolic links only for compatibility with existing applications that may use hardcoded registry key paths containing Wow6432Node. New applications should avoid using Wow6432Node in registry key paths.

- **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Classes":::** is linked to **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Wow6432Node":::**
- **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Wow6432Node\\AppId":::** is linked to **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppId":::**
- **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Wow6432Node\\PROTOCOLS":::** is linked to **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\PROTOCOLS":::**
- **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Wow6432Node\\Typelib":::** is linked to **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Typelib":::**

**Windows Server 2008, Windows Vista, Windows Server 2003, and Windows XP:  :::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Classes":::** is linked to **:::no-loc text="HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\Wow6432Node":::**. Other symbolic links were added in Windows 7 and Windows Server 2008 R2.
