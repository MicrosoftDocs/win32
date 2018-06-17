---
title: Establishing a Dial-Up Connection to the Internet
description: The following functions are used to handle modem connections.
ms.assetid: dd33ed4b-eb7c-449c-b309-8f5c290a5a93
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Establishing a Dial-Up Connection to the Internet

The following functions are used to handle modem connections.

-   [**InternetAutodial**](/windows/desktop/api)
-   [**InternetAutodialHangup**](/windows/desktop/api)
-   [**InternetDial**](/windows/desktop/api)
-   [**InternetGetConnectedState**](/windows/desktop/api)
-   [**InternetGetConnectedStateEx**](/windows/desktop/api)
-   [**InternetHangUp**](/windows/desktop/api)
-   [**InternetGoOnline**](/windows/desktop/api)

> [!Note]  
> WinINet dial-up functions do not support double-dial connections, SmartCard authentication, or connections that require registry-based certification.

 

> [!Note]  
> Starting on Windows Vista and Windows Server 2008, the WinINet dial-up functions use the [RAS functions](https://msdn.microsoft.com/library/windows/desktop/aa446739) to establish a dial-up connection. WinINet supports the functionality documented in the [**RasDialDlg**](https://msdn.microsoft.com/library/windows/desktop/aa377020) function.

 

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](https://msdn.microsoft.com/library/windows/desktop/aa384273).

 

 

 




