---
title: HINTERNET Handles
description: This section contains information about the handles that are used by the WinINet functions and the hierarchy in which they work.
ms.assetid: 8a9788ed-eb25-42cb-b912-8dffa3df1850
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HINTERNET Handles

This section contains information about the handles that are used by the WinINet functions and the hierarchy in which they work.

-   [About HINTERNET Handles](#about-hinternet-handles)
-   [Handle Hierarchy](#handle-hierarchy)
-   [FTP Hierarchy](#ftp-hierarchy)
-   [HTTP Hierarchy](#http-hierarchy)

## About HINTERNET Handles

The handles that are created and used by the WinINet functions are of type **HINTERNET**. The WinINet functions return **HINTERNET** handles that are not interchangeable with other handle types. Therefore, they cannot be used with functions such as [**ReadFile**](https://msdn.microsoft.com/library/windows/desktop/aa365467) or [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211). Similarly, other handle types cannot be used with the WinINet functions. For example, a handle returned by [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) cannot be passed to [**InternetReadFile**](/windows/win32/Wininet/nf-wininet-internetreadfile?branch=master).

The [**InternetCloseHandle**](/windows/win32/Wininet/nf-wininet-internetclosehandle?branch=master) function closes handles of type **HINTERNET**. Note that handle values are recycled quickly; therefore, if a handle is closed and a new handle is generated immediately, there is a good chance that the new handle has the same value as the handle just closed.

## Handle Hierarchy

The **HINTERNET** handles are maintained in a tree hierarchy. The handle returned by the [**InternetOpen**](/windows/win32/Wininet/nf-wininet-internetopena?branch=master) function is the root node. Handles returned by the [**InternetConnect**](/windows/win32/Wininet/nf-wininet-internetconnecta?branch=master) function occupy the next level. Handles returned by the [**FtpOpenFile**](/windows/win32/Wininet/nf-wininet-ftpopenfilea?branch=master), [**FtpFindFirstFile**](/windows/win32/Wininet/nf-wininet-ftpfindfirstfilea?branch=master), and [**HttpOpenRequest**](/windows/win32/Wininet/nf-wininet-httpopenrequesta?branch=master) functions are the leaf nodes.

**Windows XP and Windows Server 2003 R2 and earlier:** Handles returned by , [**GopherOpenFile**](/windows/win32/Wininet/nf-wininet-gopheropenfilea?branch=master), and [**GopherFindFirstFile**](/windows/win32/Wininet/nf-wininet-gopherfindfirstfilea?branch=master) are also leaf nodes.

The following diagram illustrates the hierarchy of the **HINTERNET** handles. Each box in the diagram represents a function that returns an **HINTERNET** handle.

![functions that create handles](images/ax-wnt01.png)

At the top level is the [**InternetOpen**](/windows/win32/Wininet/nf-wininet-internetopena?branch=master) function, which creates the root handle. The next level contains the [**InternetOpenUrl**](/windows/win32/Wininet/nf-wininet-internetopenurla?branch=master) and [**InternetConnect**](/windows/win32/Wininet/nf-wininet-internetconnecta?branch=master) functions. The functions that use the handle returned by [**InternetConnect**](/windows/win32/Wininet/nf-wininet-internetconnecta?branch=master) make up the last level.

The following diagram shows the functions that are dependent on the handle created by [**InternetOpenUrl**](/windows/win32/Wininet/nf-wininet-internetopenurla?branch=master). The shaded boxes represent functions that return **HINTERNET** handles, while the plain boxes represent functions that use the **HINTERNET** handle created by the associated function.

![functions that use the internetopenurl handle](images/ax-wnt02.png)

The [**InternetQueryDataAvailable**](/windows/win32/Wininet/nf-wininet-internetquerydataavailable?branch=master), [**InternetReadFile**](/windows/win32/Wininet/nf-wininet-internetreadfile?branch=master), and [**InternetSetFilePointer**](/windows/win32/Wininet/nf-wininet-internetsetfilepointer?branch=master) functions use the **HINTERNET** handle created by [**InternetOpenUrl**](/windows/win32/Wininet/nf-wininet-internetopenurla?branch=master).

## FTP Hierarchy

The following diagram shows the FTP functions that are dependent on the FTP session handle returned by [**InternetConnect**](/windows/win32/Wininet/nf-wininet-internetconnecta?branch=master). The shaded boxes represent functions that return **HINTERNET** handles, while the plain boxes represent functions that use the **HINTERNET** handle created by the function on which they depend.

![functions that use the ftp session handle](images/ax-wnt06.png)

The [**FtpCreateDirectory**](/windows/win32/Wininet/nf-wininet-ftpcreatedirectorya?branch=master), [**FtpDeleteFile**](/windows/win32/Wininet/nf-wininet-ftpdeletefilea?branch=master), [**FtpGetCurrentDirectory**](/windows/win32/Wininet/nf-wininet-ftpgetcurrentdirectorya?branch=master), [**FtpGetFile**](/windows/win32/Wininet/nf-wininet-ftpgetfilea?branch=master), [**FtpPutFile**](/windows/win32/Wininet/nf-wininet-ftpputfilea?branch=master), [**FtpRemoveDirectory**](/windows/win32/Wininet/nf-wininet-ftpremovedirectorya?branch=master), [**FtpRenameFile**](/windows/win32/Wininet/nf-wininet-ftprenamefilea?branch=master), and [**FtpSetCurrentDirectory**](/windows/win32/Wininet/nf-wininet-ftpsetcurrentdirectorya?branch=master) functions all use the **HINTERNET** handle created by [**InternetConnect**](/windows/win32/Wininet/nf-wininet-internetconnecta?branch=master).

The following diagram shows the two FTP functions that return handles and the functions that are dependent on them. The shaded boxes represent functions that return **HINTERNET** handles, while the plain boxes represent functions that use the **HINTERNET** handle created by the function on which they depend.

![functions that use the handle from ftpopen and ftpfindfirstfile](images/ax-wnt03.png)

The [**InternetFindNextFile**](/windows/win32/Wininet/nf-wininet-internetfindnextfilea?branch=master) function is dependent on the handle created by [**FtpFindFirstFile**](/windows/win32/Wininet/nf-wininet-ftpfindfirstfilea?branch=master), while [**InternetReadFile**](/windows/win32/Wininet/nf-wininet-internetreadfile?branch=master) and [**InternetWriteFile**](/windows/win32/Wininet/nf-wininet-internetwritefile?branch=master) use the handle created by [**FtpOpenFile**](/windows/win32/Wininet/nf-wininet-ftpopenfilea?branch=master).

## HTTP Hierarchy

The following diagram shows the relationships of the functions that are used for the HTTP protocol. The shaded boxes represent functions that return **HINTERNET** handles, while the plain boxes represent functions that use the **HINTERNET** handle created by the function on which they depend.

![functions that use the handle from httpopenrequest](images/ax-wnt05.png)

The [**HttpAddRequestHeaders**](/windows/win32/Wininet/nf-wininet-httpaddrequestheadersa?branch=master), [**HttpQueryInfo**](/windows/win32/Wininet/nf-wininet-httpqueryinfoa?branch=master), [**HttpSendRequest**](/windows/win32/Wininet/nf-wininet-httpsendrequesta?branch=master), [**HttpSendRequestEx**](/windows/win32/Wininet/nf-wininet-httpsendrequestexa?branch=master), and [**InternetErrorDlg**](/windows/win32/Wininet/nf-wininet-interneterrordlg?branch=master) functions are dependent on the handle created by [**HttpOpenRequest**](/windows/win32/Wininet/nf-wininet-httpopenrequesta?branch=master).

The following diagram shows the functions that use the **HINTERNET** handle created by [**HttpOpenRequest**](/windows/win32/Wininet/nf-wininet-httpopenrequesta?branch=master) after it is sent by [**HttpSendRequest**](/windows/win32/Wininet/nf-wininet-httpsendrequesta?branch=master). The shaded boxes represent functions that return **HINTERNET** handles, while the plain boxes represent functions that use the **HINTERNET** handle created by the function on which they depend.

![functions that use the handle after httpsendrequest](images/ax-wnt07.png)

After [**HttpSendRequest**](/windows/win32/Wininet/nf-wininet-httpsendrequesta?branch=master) has used the handle returned by [**HttpOpenRequest**](/windows/win32/Wininet/nf-wininet-httpopenrequesta?branch=master), it can be used by [**InternetQueryDataAvailable**](/windows/win32/Wininet/nf-wininet-internetquerydataavailable?branch=master), [**InternetReadFile**](/windows/win32/Wininet/nf-wininet-internetreadfile?branch=master), and [**InternetSetFilePointer**](/windows/win32/Wininet/nf-wininet-internetsetfilepointer?branch=master).

![functions that use the handle after httpsendrequestex](images/ax-wnt08.png)

After [**HttpSendRequestEx**](/windows/win32/Wininet/nf-wininet-httpsendrequestexa?branch=master) has used the handle returned by [**HttpOpenRequest**](/windows/win32/Wininet/nf-wininet-httpopenrequesta?branch=master), the handle can be used by [**HttpEndRequest**](/windows/win32/Wininet/nf-wininet-httpendrequesta?branch=master), [**InternetReadFileEx**](/windows/win32/Wininet/nf-wininet-internetreadfileexa?branch=master), and [**InternetWriteFile**](/windows/win32/Wininet/nf-wininet-internetwritefile?branch=master). After [**HttpEndRequest**](/windows/win32/Wininet/nf-wininet-httpendrequesta?branch=master) has been called, the handle can be used by [**InternetReadFile**](/windows/win32/Wininet/nf-wininet-internetreadfile?branch=master), [**InternetSetFilePointer**](/windows/win32/Wininet/nf-wininet-internetsetfilepointer?branch=master), and [**InternetQueryDataAvailable**](/windows/win32/Wininet/nf-wininet-internetquerydataavailable?branch=master).

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](https://msdn.microsoft.com/library/windows/desktop/aa384273).

 

 

 




