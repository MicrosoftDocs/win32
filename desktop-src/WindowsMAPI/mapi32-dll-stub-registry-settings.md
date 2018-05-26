---
Description: The stub library uses values under the default mail key to dispatch Simple MAPI and MAPI calls.
ms.assetid: 4CDD0CB1-81EE-458c-8B3B-82AC4FA49BD0
title: Mapi32.dll Stub Registry Settings
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Mapi32.dll Stub Registry Settings

The stub library uses values under the default mail key to dispatch Simple MAPI and MAPI calls.

The default mail client for Simple MAPI or MAPI calls is defined by the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail::(default)** registry value. This value identifies a subkey that contains information about the current default mail client as seen in the following example.

``` syntax
Mail::(Default) [="Microsoft Outlook"]
     \Microsoft Outlook::DLLPath  [="MAPI32.dll"]
     \Microsoft Outlook::MSIComponentID [="{GUID}"]
     \Microsoft Outlook::MSIApplicationLCID [=value]
     \Microsoft Outlook::MSIOfficeLCID [=value]
     \Outlook Express::DLLPath   [="c:\%SYSTEMDRIVE%\Program Files\Microsoft Outlook\msoe.dll."]
....
```

The registry values used under a particular mail client key are listed in the following table.



| Reg Key                       | Type               | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DLLPath**<br/>        | REG\_SZ<br/> | Full path to the Simple MAPI provider DLL.<br/>                                                                                                                                                                                                                                                                                                                                                       |
| **DLLPathEx**<br/>      | REG\_SZ<br/> | Full path to the MAPI provider DLL. Provider DLLs that support both Simple MAPI and MAPI must have both keys set.<br/>                                                                                                                                                                                                                                                                                |
| **MSIComponentID**<br/> | REG\_SZ<br/> | A Windows Installer, formerly the Microsoft Software installer (MSI), PublishComponent category id (GUID) that in turn identifies the DLL that exports Simple MAPI or MAPI calls. If set, this key takes precedence over **DLLPath** or **DLLPathEx**. For more information on configuring the installer, see [Setting Up the MSI Keys for Your MAPI DLL](d869c201-f126-4c8c-b842-258f8806b6bf).<br/> |



 

Depending on the type of MAPI call received, the stub library loads the appropriate DLL as defined by the registry keys and values for the default mail client and then dispatches the call. Simple MAPI calls are dispatched to the DLL pointed to by **DLLPath**, and MAPI calls are dispatched to the DLL pointed to by **DLLPathEx**. However, if the **MSIComponentID** registry key is listed under the mail client key, the stub library installs the component on demand using the Windows Installer, loads the DLL, and dispatches the calls.

If there is no default mail client or if none of the DLLs identified by the default mail client support the requested MAPI functionality, the stub library checks for the existence of Mapi32x.dll and Mapisvc.inf (indicating the presence of a MAPI mail client) in the system directory. If they are found, the stub library loads Mapi32x.dll and dispatches the call. This mechanism allows for the Microsoft Exchange client and earlier versions of Outlook to continue using the original (renamed to Mapi32x.dll) Mapi32.dll.

If the DLLs defined in the default mail client key cannot handle a MAPI call and if Mapi32x.dll and Mapisvc.inf files do not exist in the system directory, the stub library displays a first-time initialization message by using the strings in the **PreFirstRun** value of the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Clients**\\**Mail** key. The format of the string is &lt;messagebox text&gt;\* &lt;messagebox caption&gt;. This string allows applications to present a message if they need to prepare for handling particular MAPI calls upon first request. The stub library subsequently returns E\_FAIL to all MAPI calls that cannot be handled by the default mail client configuration after the initial message is displayed.

## Related topics

<dl> <dt>

[Mapi32 Stub Library](mapi32-stub-library.md)
</dt> </dl>

 

 




