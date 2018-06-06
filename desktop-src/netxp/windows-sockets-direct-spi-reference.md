---
Description: Windows Sockets Direct SPI Reference
ms.assetid: 6bb2df4e-4e72-4fc3-aca1-690294d71b61
title: Windows Sockets Direct SPI Reference
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Sockets Direct SPI Reference

## 

This reference section documents the subset of the Windows Sockets service provider interface (SPI) functions that are exported by a SAN service provider.

> [!Note]  
> These SPI functions are defined in *Ws2spi.h* and require Windows Sockets version 2.0, except for the **WSPStartupEx** function, which is defined in *Ws2san.h* and requires Windows Sockets version 2.2.

 

The complete set of Windows SPI functions is documented in the Microsoft Windows SDK documentation. However, it does not include SAN-specific information. Writers of SAN service providers should refer to the *Windows Sockets Direct SPI Reference* instead.

A SAN service provider must export all the Windows Sockets Direct SPI functions described in the *Windows Sockets Direct SPI Reference*. If a SAN service provider does not support quality of service (QoS), its **WSPGetQOSByName**function must return the error WSAEOPNOTSUPP.

The following topics provide more information about the Windows Sockets Direct SPI functions:

<dl>

[**WSPAccept**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspaccept)  
[**WSPBind**](/windows/desktop/api/Ws2spi/)  
[**WSPCleanup**](/windows/desktop/api/Ws2spi/)  
[**WSPCloseSocket**](/windows/desktop/api/Ws2spi/)  
[**WSPConnect**](/windows/desktop/api/Ws2spi/)  
[**WSPDuplicateSocket**](/windows/desktop/api/Ws2spi/)  
[**WSPEnumNetworkEvents**](/windows/desktop/api/Ws2spi/)  
[**WSPEventSelect**](/windows/desktop/api/Ws2spi/)  
[**WSPGetOverlappedResult**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspgetoverlappedresult)  
[**WSPGetQOSByName**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspgetqosbyname)  
[**WSPGetSockOpt**](/windows/desktop/api/Ws2spi/)  
[**WSPIoctl**](/windows/desktop/api/Ws2spi/)  
[**WSPListen**](/windows/desktop/api/Ws2spi/)  
[**WSPRecv**](/windows/desktop/api/Ws2spi/)  
[**WSPSend**](/windows/desktop/api/Ws2spi/)  
[**WSPSetSockOpt**](/windows/desktop/api/Ws2spi/)  
[**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket)  
[**WSPStartupEx**](https://www.bing.com/search?q=**WSPStartupEx**)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetxp\netxp%5D:%20Windows%20Sockets%20Direct%20SPI%20Reference%20%20RELEASE:%20%283/30/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



