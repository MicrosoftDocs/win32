---
title: Establishing a Dial-Up Connection to the Internet
description: The following functions are used to handle modem connections.
ms.assetid: dd33ed4b-eb7c-449c-b309-8f5c290a5a93
ms.topic: article
ms.date: 05/31/2018
---

# Establishing a Dial-Up Connection to the Internet

The following functions are used to handle modem connections.

-   [**InternetAutodial**](https://msdn.microsoft.com/en-us/library/Aa384336(v=VS.85).aspx)
-   [**InternetAutodialHangup**](https://msdn.microsoft.com/en-us/library/Aa384340(v=VS.85).aspx)
-   [**InternetDial**](https://msdn.microsoft.com/en-us/library/Aa384587(v=VS.85).aspx)
-   [**InternetGetConnectedState**](https://msdn.microsoft.com/en-us/library/Aa384702(v=VS.85).aspx)
-   [**InternetGetConnectedStateEx**](https://msdn.microsoft.com/en-us/library/Aa384705(v=VS.85).aspx)
-   [**InternetHangUp**](https://msdn.microsoft.com/en-us/library/Aa384737(v=VS.85).aspx)
-   [**InternetGoOnline**](https://msdn.microsoft.com/en-us/library/Aa384734(v=VS.85).aspx)

> [!Note]  
> WinINet dial-up functions do not support double-dial connections, SmartCard authentication, or connections that require registry-based certification.

 

> [!Note]  
> Starting on Windows Vista and Windows Server 2008, the WinINet dial-up functions use the [RAS functions](https://docs.microsoft.com/windows/desktop/RRAS/remote-access-service-functions) to establish a dial-up connection. WinINet supports the functionality documented in the [**RasDialDlg**](https://docs.microsoft.com/windows/desktop/api/rasdlg/nf-rasdlg-rasdialdlga) function.

 

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](https://docs.microsoft.com/windows/desktop/WinHttp/winhttp-start-page).

 

 

 




