---
title: HINTERNET Handles
description: This section contains information about the handles that are used by the WinINet functions and the hierarchy in which they work.
ms.assetid: '8a9788ed-eb25-42cb-b912-8dffa3df1850'
---

# HINTERNET Handles

This section contains information about the handles that are used by the WinINet functions and the hierarchy in which they work.

-   [About HINTERNET Handles](#about-hinternet-handles)
-   [Handle Hierarchy](#handle-hierarchy)
-   [FTP Hierarchy](#ftp-hierarchy)
-   [HTTP Hierarchy](#http-hierarchy)

## About HINTERNET Handles

The handles that are created and used by the WinINet functions are of type **HINTERNET**. The WinINet functions return **HINTERNET** handles that are not interchangeable with other handle types. Therefore, they cannot be used with functions such as [**ReadFile**](https://msdn.microsoft.com/library/windows/desktop/aa365467) or [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211). Similarly, other handle types cannot be used with the WinINet functions. For example, a handle returned by [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) cannot be passed to [**InternetReadFile**](internetreadfile.md).

The [**InternetCloseHandle**](internetclosehandle.md) function closes handles of type **HINTERNET**. Note that handle values are recycled quickly; therefore, if a handle is closed and a new handle is generated immediately, there is a good chance that the new handle has the same value as the handle just closed.

## Handle Hierarchy

The **HINTERNET** handles are maintained in a tree hierarchy. The handle returned by the [**InternetOpen**](internetopen.md) function is the root node. Handles returned by the [**InternetConnect**](internetconnect.md) function occupy the next level. Handles returned by the [**FtpOpenFile**](ftpopenfile.md), [**FtpFindFirstFile**](ftpfindfirstfile.md), and [**HttpOpenRequest**](httpopenrequest.md) functions are the leaf nodes.

**Windows XP and Windows Server 2003 R2 and earlier:** Handles returned by , [**GopherOpenFile**](gopheropenfile.md), and [**GopherFindFirstFile**](gopherfindfirstfile.md) are also leaf nodes.

The following diagram illustrates the hierarchy of the **HINTERNET** handles. Each box in the diagram represents a function that returns an **HINTERNET** handle.

![functions that create handles](images/ax-wnt01.png)

At the top level is the [**InternetOpen**](internetopen.md) function, which creates the root handle. The next level contains the [**InternetOpenUrl**](internetopenurl.md) and [**InternetConnect**](internetconnect.md) functions. The functions that use the handle returned by [**InternetConnect**](internetconnect.md) make up the last level.

The following diagram shows the functions that are dependent on the handle created by [**InternetOpenUrl**](internetopenurl.md). The shaded boxes represent functions that return **HINTERNET** handles, while the plain boxes represent functions that use the **HINTERNET** handle created by the associated function.

![functions that use the internetopenurl handle](images/ax-wnt02.png)

The [**InternetQueryDataAvailable**](internetquerydataavailable.md), [**InternetReadFile**](internetreadfile.md), and [**InternetSetFilePointer**](internetsetfilepointer.md) functions use the **HINTERNET** handle created by [**InternetOpenUrl**](internetopenurl.md).

## FTP Hierarchy

The following diagram shows the FTP functions that are dependent on the FTP session handle returned by [**InternetConnect**](internetconnect.md). The shaded boxes represent functions that return **HINTERNET** handles, while the plain boxes represent functions that use the **HINTERNET** handle created by the function on which they depend.

![functions that use the ftp session handle](images/ax-wnt06.png)

The [**FtpCreateDirectory**](ftpcreatedirectory.md), [**FtpDeleteFile**](ftpdeletefile.md), [**FtpGetCurrentDirectory**](ftpgetcurrentdirectory.md), [**FtpGetFile**](ftpgetfile.md), [**FtpPutFile**](ftpputfile.md), [**FtpRemoveDirectory**](ftpremovedirectory.md), [**FtpRenameFile**](ftprenamefile.md), and [**FtpSetCurrentDirectory**](ftpsetcurrentdirectory.md) functions all use the **HINTERNET** handle created by [**InternetConnect**](internetconnect.md).

The following diagram shows the two FTP functions that return handles and the functions that are dependent on them. The shaded boxes represent functions that return **HINTERNET** handles, while the plain boxes represent functions that use the **HINTERNET** handle created by the function on which they depend.

![functions that use the handle from ftpopen and ftpfindfirstfile](images/ax-wnt03.png)

The [**InternetFindNextFile**](internetfindnextfile.md) function is dependent on the handle created by [**FtpFindFirstFile**](ftpfindfirstfile.md), while [**InternetReadFile**](internetreadfile.md) and [**InternetWriteFile**](internetwritefile.md) use the handle created by [**FtpOpenFile**](ftpopenfile.md).

## HTTP Hierarchy

The following diagram shows the relationships of the functions that are used for the HTTP protocol. The shaded boxes represent functions that return **HINTERNET** handles, while the plain boxes represent functions that use the **HINTERNET** handle created by the function on which they depend.

![functions that use the handle from httpopenrequest](images/ax-wnt05.png)

The [**HttpAddRequestHeaders**](httpaddrequestheaders.md), [**HttpQueryInfo**](httpqueryinfo.md), [**HttpSendRequest**](httpsendrequest.md), [**HttpSendRequestEx**](httpsendrequestex.md), and [**InternetErrorDlg**](interneterrordlg.md) functions are dependent on the handle created by [**HttpOpenRequest**](httpopenrequest.md).

The following diagram shows the functions that use the **HINTERNET** handle created by [**HttpOpenRequest**](httpopenrequest.md) after it is sent by [**HttpSendRequest**](httpsendrequest.md). The shaded boxes represent functions that return **HINTERNET** handles, while the plain boxes represent functions that use the **HINTERNET** handle created by the function on which they depend.

![functions that use the handle after httpsendrequest](images/ax-wnt07.png)

After [**HttpSendRequest**](httpsendrequest.md) has used the handle returned by [**HttpOpenRequest**](httpopenrequest.md), it can be used by [**InternetQueryDataAvailable**](internetquerydataavailable.md), [**InternetReadFile**](internetreadfile.md), and [**InternetSetFilePointer**](internetsetfilepointer.md).

![functions that use the handle after httpsendrequestex](images/ax-wnt08.png)

After [**HttpSendRequestEx**](httpsendrequestex.md) has used the handle returned by [**HttpOpenRequest**](httpopenrequest.md), the handle can be used by [**HttpEndRequest**](httpendrequest.md), [**InternetReadFileEx**](internetreadfileex.md), and [**InternetWriteFile**](internetwritefile.md). After [**HttpEndRequest**](httpendrequest.md) has been called, the handle can be used by [**InternetReadFile**](internetreadfile.md), [**InternetSetFilePointer**](internetsetfilepointer.md), and [**InternetQueryDataAvailable**](internetquerydataavailable.md).

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](https://msdn.microsoft.com/library/windows/desktop/aa384273).

 

 

 




