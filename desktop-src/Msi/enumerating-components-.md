---
Description: Windows Installer 5.0 running on Windows Server 2008 R2 or Windows 7 can enumerate all components installed on the computer and obtain the key path for the component.
ms.assetid: a6676340-1695-48c7-a1e4-7a02a7bc3fef
title: Enumerating Components
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Components

Windows Installer 5.0 running on Windows Server 2008 R2 or Windows 7 can enumerate all components installed on the computer and obtain the key path for the component. A package authored for Windows Installer 5.0 can use the [**MsiEnumComponentsEx**](/windows/win32/Msi/nf-msi-msienumcomponentsexa?branch=master), [**MsiEnumClientsEx**](/windows/win32/Msi/nf-msi-msienumclientsexa?branch=master), and [**MsiGetComponentPathEx**](/windows/win32/Msi/nf-msi-msigetcomponentpathexa?branch=master) functions to search for components and products across user accounts and installation contexts. The [**MsiEnumComponents**](/windows/win32/Msi/nf-msi-msienumcomponentsa?branch=master), [**MsiEnumClients**](/windows/win32/Msi/nf-msi-msienumclientsa?branch=master), and [**MsiGetComponentPath**](/windows/win32/Msi/nf-msi-msigetcomponentpatha?branch=master) functions only return information for components and products installed for the user account that called the function. Multiple calls to these functions, at least once for each user account, are required to collect information for the entire computer.

The [**MsiEnumComponentsEx**](/windows/win32/Msi/nf-msi-msienumcomponentsexa?branch=master) function enumerates installed components. The function retrieves one component code each time it is called. The [**Component Object**](components.md) receives information about an installed component by this function.

The [**MsiEnumClientsEx**](/windows/win32/Msi/nf-msi-msienumclientsexa?branch=master) function enumerates products that are clients of a specified installed component. The [**Client Object**](client.md) receives information about a client by this function.

The [**MsiGetComponentPathEx**](/windows/win32/Msi/nf-msi-msigetcomponentpathexa?branch=master) function returns the full path to an installed component. The function returns the registry key if the key path for the component is a registry key. The [**ComponentInfo Object**](componentinfo.md) receives information about an installed component by this function.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This functionality is available beginning with Windows Installer 5.0 running on Windows 7 or Windows Server 2008 R2.

 

 



