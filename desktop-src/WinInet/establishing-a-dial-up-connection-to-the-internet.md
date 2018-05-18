---
title: Establishing a Dial-Up Connection to the Internet
description: The following functions are used to handle modem connections.
ms.assetid: 'dd33ed4b-eb7c-449c-b309-8f5c290a5a93'
---

# Establishing a Dial-Up Connection to the Internet

The following functions are used to handle modem connections.

-   [**InternetAutodial**](internetautodial.md)
-   [**InternetAutodialHangup**](internetautodialhangup.md)
-   [**InternetDial**](internetdial.md)
-   [**InternetGetConnectedState**](internetgetconnectedstate.md)
-   [**InternetGetConnectedStateEx**](internetgetconnectedstateex.md)
-   [**InternetHangUp**](internethangup.md)
-   [**InternetGoOnline**](internetgoonline.md)

> [!Note]  
> WinINet dial-up functions do not support double-dial connections, SmartCard authentication, or connections that require registry-based certification.

 

> [!Note]  
> Starting on Windows Vista and Windows Server 2008, the WinINet dial-up functions use the [RAS functions](https://msdn.microsoft.com/library/windows/desktop/aa446739) to establish a dial-up connection. WinINet supports the functionality documented in the [**RasDialDlg**](https://msdn.microsoft.com/library/windows/desktop/aa377020) function.

 

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](https://msdn.microsoft.com/library/windows/desktop/aa384273).

 

 

 




