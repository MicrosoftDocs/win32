---
Description: 'MAPI calls made from a particular DLL or executable file may have to be routed to the system MAPI DLL Mapi32x.dll or another custom MAPI DLL.'
ms.assetid: '9FE83CB4-69C6-4e61-8BED-1A93FA9A1A9F'
title: Explicitly Mapping MAPI Calls to MAPI DLLs
---

# Explicitly Mapping MAPI Calls to MAPI DLLs

MAPI calls made from a particular DLL or executable file may have to be routed to the system MAPI DLL Mapi32x.dll or another custom MAPI DLL. Routing must be done even though the default mail client supports the call. Such DLLs or executable files are listed as string registry values in the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows Messaging Subsystem**\\**MSMapiApps** key. The registry value for these keys can be empty or identify a mail client key that resides under **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail**.

## Handling the MAPI Call

When the stub library resolves a MAPI call, it first checks to see whether the DLL or executable file is currently in process. It does this by enumerating the DLL and executable files listed under the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows Messaging Subsystem**\\**MSMapiApps** key.

If there is a match, the stub library obtains the string value. If the value is the empty string, the stub library routes the call to the system MAPI DLL, Mapi32x.dll.

If the string is not empty, the stub uses the string value to find the key under **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail**. This key is where the stub can find the appropriate registry value to dispatch the call.

The appropriate registry value may be one of the following.

-   **DLLPath**

-   **DLLPathEx**

-   **MSIComponentID**

The following example illustrates this.

``` syntax
//Route call to Mapi32x.dll
HKLM\Software\Microsoft\Windows Messaging Subsystem\MSMapiApps::exchng32.exe = ""

//Route call using Microsoft Outlook key under HKLM\Software\Clients\Mail
HKLM\Software\Microsoft\Windows Messaging Subsystem\MSMapiApps::msspc32.dll = "Microsoft Outlook"
```

## Related topics

<dl> <dt>

[Mapi32 Stub Library](mapi32-stub-library.md)
</dt> <dt>

[Mapi32.dll Stub Registry Settings](mapi32-dll-stub-registry-settings.md)
</dt> <dt>

[Installing or Restoring the Mapi32.dll Stub](installing-or-restoring-the-mapi32-dll-stub.md)
</dt> </dl>

 

 



