---
title: Custom Dialers
description: Windows 2000 and later operating systems enable developers to provide their own custom dialers that work with the Remote Access Service (RAS).
ms.assetid: ad94f38d-812f-4329-8055-6274a21a3242
keywords:
- Custom Dialers
ms.topic: article
ms.date: 05/31/2018
---

# Custom Dialers

Windows 2000 and later operating systems enable developers to provide their own custom dialers that work with the Remote Access Service (RAS). The custom dialer is implemented as a single dynamic-link library (DLL) that exports the following entry points:

-   [**RasCustomDial**](/windows/desktop/api/Ras/nc-ras-rascustomdialfn)
-   [**RasCustomDialDlg**](/windows/desktop/api/Rasdlg/nc-rasdlg-rascustomdialdlgfn)
-   [**RasCustomHangup**](/windows/desktop/api/Ras/nc-ras-rascustomhangupfn)
-   [**RasCustomEntryDlg**](/windows/desktop/api/Rasdlg/nc-rasdlg-rascustomentrydlgfn)
-   [**RasCustomDeleteEntryNotify**](/windows/desktop/api/Ras/nc-ras-rascustomdeleteentrynotifyfn)

The custom-dial DLL must export all of these entry points, and it must implement the entry points as Unicode functions. For more information about these functions, see the reference page for each function in the Windows SDK Remote Access Service Reference.

In order for a RAS connection to use the custom dialer, the phone-book entry for the connection must contain the path to the custom-dial DLL. Use the RAS API functions [**RasGetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rasgetentrypropertiesa) and [**RasSetEntryProperties**](/windows/desktop/api/Ras/nf-ras-rassetentrypropertiesa) to set this path in the **szCustomDialDll** member of the [**RASENTRY**](/previous-versions/windows/desktop/legacy/aa377274(v=vs.85)) structure for the phone-book entry.

## Updating the Registry for Custom Dialers

In order for the system to dial a connection that uses a custom dialer, the path to the custom-dial DLL must exist in the following registry value.

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Services
            Rasman
               Parameters
                  CustomDLL<dl>
<dt>

                  Data type
</dt>
<dd>                  REG_MULTI_SZ</dd>
</dl>
```

Because **CustomDLL** is of type **REG\_MULTI\_SZ**, it can hold paths to multiple custom-dial DLLs. You need to set the path to the custom-dial DLL in this registry value, in addition to the phone-book entry for the connection.

By default, this registry value is writeable only by a user with Administrator or System privileges. For security reasons, do not change the permissions on this registry key.

## Using Custom Dialers at System Logon

Windows 2000 and later operating systems allow a user to establish a RAS connection at the time of logon. To do so, the user checks **Logon using Dial-up Networking** in the **Logon Information** dialog box. After the user clicks the Okay button, the system displays the available connections.

## Security Considerations

In most cases, a custom dialer operates with the security privileges of the user that invokes it. However, if the custom dialer is invoked at logon, it operates with system privileges. Therefore, design the custom dialer so that it cannot be used to violate system security. For example, the dialer should not present a user interface that allows the user write access to the computer's file system. User interfaces that provide such access include the **Find-File** dialog, the **File-Open** common dialog, and Windows **Help**.

## Custom Dialer User Interface Must Support IDCANCEL

If the custom dialer displays a user interface, the user interface must support WM\_COMMAND messages where LOWORD(*wParam*) equals IDCANCEL.

 

 