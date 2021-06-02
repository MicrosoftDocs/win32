---
description: You can hide the Cancel button that is used to cancel an installation by using a command-line option, the Windows Installer API, or a custom action. The Cancel button can be hidden for part or all of the installation depending on which method you use.
ms.assetid: de2bb788-0d19-4818-8038-cae6000b38c4
title: Hiding the Cancel Button During an Installation
ms.topic: article
ms.date: 05/31/2018
---

# Hiding the Cancel Button During an Installation

You can hide the **Cancel** button that is used to cancel an installation by using a command-line option, the Windows Installer API, or a custom action. The **Cancel** button can be hidden for part or all of the installation depending on which method you use.

## Hiding the Cancel Button from the Command Line

The **Cancel** button can be hidden during installation by using the (!) command-line option. This can only be done for a basic user interface level installation (/qb). The **Cancel** button is hidden for the entire installation. For more information, see [Command-Line Options](command-line-options.md) and [User Interface Levels](user-interface-levels.md). The following command line hides the **Cancel** button and installs Example.msi.

**msiexec /I example.msi /qb!**

## Hiding the Cancel Button from an Application or Script

You can write an application or script to hide the **Cancel** button. This can only be done for a basic UI level installation so that the **Cancel** button is hidden for the entire installation.

To hide the Cancel button from an application, set INSTALLUILEVEL\_HIDECANCEL when calling [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui). The following example hides the **Cancel** button and installs Example.msi.


```C++
#include <windows.h>
#include <stdio.h>
#include <Shellapi.h>
#include <msi.h>
#include <Msiquery.h>
#include <tchar.h>
#pragma comment(lib, "msi.lib")

int main()  
{

INSTALLUILEVEL uiPrevLevel = MsiSetInternalUI( INSTALLUILEVEL(INSTALLUILEVEL_BASIC | INSTALLUILEVEL_HIDECANCEL), 0); 
UINT uiStat = MsiInstallProduct(_T("example.msi"), NULL);

return 0;  
}
```



To hide the **Cancel** button from script, add msiUILevelHideCancel to the [**UILevel**](installer-uilevel.md) property of the [**Installer Object**](installer-object.md). The following VBScript sample hides the **Cancel** button and installs Example.msi.


```VB
Dim Installer As Object
Set Installer = CreateObject("WindowsInstaller.Installer")
Installer.UILevel = msiUILevelBasic + msiUILevelHideCancel
Installer.InstallProduct "example.msi"
```



## Hiding the Cancel Button for Parts of an Installation Using a Custom Action

Your installation can hide and unhide the **Cancel** button during parts of an installation by sending an INSTALLMESSAGE\_COMMONDATA message using a DLL custom action or scripts. For more information, see [Dynamic-Link Libraries](dynamic-link-libraries.md), [Scripts](scripts.md), [Custom Actions](custom-actions.md), and [Sending Messages to Windows Installer Using MsiProcessMessage](sending-messages-to-windows-installer-using-msiprocessmessage.md).

A call to a custom action must provide a record. Field 1 of this record must contain the value 2 (two) to specify the **Cancel** button. Field 2 must contain either the value 0 or 1. A value of 0 in Field 2 hides the button and a value of 1 in Field 2 unhides the button. Note that allocating a record of size 2 with [**MsiCreateRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msicreaterecord) provides fields 0, 1, and 2.

The following sample DLL custom action hides the **Cancel** button.


```C++
#include <windows.h>
#include <stdio.h>
#include <Shellapi.h>
#include <msi.h>
#include <Msiquery.h>

UINT __stdcall HideCancelButton(MSIHANDLE hInstall)
{
    PMSIHANDLE hRecord = MsiCreateRecord(2);
    if ( !hRecord)
        return ERROR_INSTALL_FAILURE;

    if (ERROR_SUCCESS != MsiRecordSetInteger(hRecord, 1, 2)
     || ERROR_SUCCESS != MsiRecordSetInteger(hRecord, 2, 0))
        return ERROR_INSTALL_FAILURE;

    MsiProcessMessage(hInstall, INSTALLMESSAGE_COMMONDATA, hRecord);

    return ERROR_SUCCESS;
}
```



The following VBScript Custom Action hides the **Cancel** button.


```VB
Function HideCancelButton()

    Dim Record
    Set Record = Installer.CreateRecord(2)

    Record.IntegerData(1) = 2
    Record.IntegerData(2) = 0

    Session.Message msiMessageTypeCommonData, Record
 
    ' return success
    HideCancelButton = 1
    Exit Function

End Function
```



 

 



