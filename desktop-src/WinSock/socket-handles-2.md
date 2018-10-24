---
Description: A socket handle can optionally be a file handle in Windows Sockets 2. A socket handle from a Winsock provider can be used with other non-Winsock functions such as ReadFile, WriteFile, ReadFileEx, and WriteFileEx.
ms.assetid: 986dd9d8-52be-47aa-92b2-6cd40b83f5de
title: Socket Handles
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Socket Handles

A socket handle can optionally be a file handle in Windows Sockets 2. A socket handle from a Winsock provider can be used with other non-Winsock functions such as [**ReadFile**](https://msdn.microsoft.com/library/Aa365467(v=VS.85).aspx), [**WriteFile**](https://msdn.microsoft.com/library/Aa365747(v=VS.85).aspx), [**ReadFileEx**](https://msdn.microsoft.com/library/Aa365468(v=VS.85).aspx), and [**WriteFileEx**](https://msdn.microsoft.com/library/Aa365748(v=VS.85).aspx).

The **XP1\_IFS\_HANDLES** member in the protocol information structure for a provider determines whether a socket handle from a provider is an Installable File System (IFS) handle. Socket handles that are IFS handles can be used without a performance penalty with other non-Winsock functions ([**ReadFile**](https://msdn.microsoft.com/library/Aa365467(v=VS.85).aspx) and [**WriteFile**](https://msdn.microsoft.com/library/Aa365747(v=VS.85).aspx), for example). Any non-IFS socket handles when used with non-Winsock functions (**ReadFile** and **WriteFile**, for example) result in interactions between the provider and the file system where extra processing overhead is involved that can result in a significant performance penalty. When using socket handles with non-Winsock functions, the error codes propagated from the base file system are not always mapped to Winsock error codes. Consequently, it is recommended that socket handles be used only with Winsock functions.

A socket handle should not be used with the [**DuplicateHandle**](https://msdn.microsoft.com/en-us/library/ms724251(v=VS.85).aspx) function. The presence of layered service providers (LSPs) can cause this to fail and there is no way for the destination process to import the socket handle.

> [!Note]  
> Layered Service Providers are deprecated. Starting with Windows 8 and Windows Server 2012, use [Windows Filtering Platform](https://msdn.microsoft.com/en-us/library/Aa366510(v=VS.85).aspx).

 

Windows Sockets 2 has expanded certain functions that transfer data between sockets using handles. The functions offer advantages specific to sockets for transferring data and include [**WSARecv**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecv), [**WSASend**](/windows/desktop/api/Winsock2/nf-winsock2-wsasend), and [**WSADuplicateSocket**](/windows/desktop/api/Winsock2/nf-winsock2-wsaduplicatesocketa).

 

 



