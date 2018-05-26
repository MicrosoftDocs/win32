---
title: Asynchronous Operation
description: In asynchronous mode, an application can execute any function that includes a context value as one of its parameters and can continue to execute other commands or functions while the application waits for the function to complete its task.
ms.assetid: 4b8ade00-deb3-4d9f-9ceb-5ba3296c8c68
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Asynchronous Operation

The amount of time it takes an application to access an Internet resource depends on a number of factors, such as the connection being used, the server on which the resource is located, and the number of users trying to access the resource. For applications that download multiple resources or handle multiple tasks (including one or more downloads), waiting for each download to complete before moving on to the next task can be extremely inefficient. To decrease the amount of time an application has to wait, many of the WinINet functions can operate asynchronously.

In asynchronous mode, an application can execute any function that includes a context value as one of its parameters and can continue to execute other commands or functions while the application waits for the function to complete its task. While the task is completing, a status callback function provided by the application is notified about the progress of the task and when it has completed. At this time, the status callback function can call other functions or perform any other required tasks that were dependent on the task's completion.

There is no callback thread afinity when you call WinINet asynchronously: a call might start from one thread, but any other thread can receive the callback.

-   [Benefits](#benefits)
-   [Scenarios](#scenarios)
-   [Related Topics](#related-topics)

## Benefits

There are several benefits to operating asynchronously. For example:

-   Downloading multiple Internet resources simultaneously.

    You can connect to multiple Internet resources at the same time and download them as they become available.

-   Increasing performance of your application.

    An application using the WinINet functions asynchronously does not have to wait until the request is completed, so the application is free to do other tasks that are not dependent on the request, thus improving the application's overall performance.

-   Monitor the progress of the download.

    The status callback function receives notifications while it is processing a request. If needed, your application can use the information provided by that status callback function to keep the user informed about the progress of the operation or to interrupt requests that are taking too long to complete.

## Scenarios

Let's say your application needs to download coffee prices from the Downfall Coffee & Tea and the Fourth Coffee sites and compare prices. The Fourth Coffee site usually has a slower response time, so your application should download the information from Downfall Coffee & Tea first.

Two versions of the application are developed. One works synchronously, first downloading the prices from the Downfall Coffee & Tea site and then the prices from the Fourth Coffee site. The second works asynchronously, sending requests to both sites and downloading the prices when they become available.

The following table illustrates what would happen if the Fourth Coffee site was faster on a particular day.



| Event                                                            | Synchronous version                        | Asynchronous version                                     |
|------------------------------------------------------------------|--------------------------------------------|----------------------------------------------------------|
| Start                                                            | Send request to Downfall Coffee & Tea      | Send requests to Downfall Coffee & Tea and Fourth Coffee |
| Request from the asynchronous version to Fourth Coffee completed | Waiting                                    | Download prices from Fourth Coffee                       |
| Request to Downfall Coffee & Tea completed                       | Download prices from Downfall Coffee & Tea | Download prices from Downfall Coffee & Tea               |
| After Downfall Coffee & Tea's prices are downloaded              | Send request to Fourth Coffee              | Compare prices                                           |
| Asynchronous version's comparison completed                      | Waiting                                    | Operation complete                                       |
| Request from the synchronous version to Fourth Coffee completed  | Download prices from Fourth Coffee         | n/a                                                      |
| After Fourth Coffee's prices are downloaded                      | Compare prices                             | n/a                                                      |
| Synchronous version's comparison completed                       | Operation complete                         | n/a                                                      |



 

Another example would be a web browser such as Microsoft Internet Explorer. When the browser downloads a page, it often needs to download other resources, such as images and sound files. In asynchronous mode, the page and its associated resources can be requested simultaneously and downloaded as they become available, instead of requesting and downloading the page and each resource one at a time.

## Related Topics

The following are related links.

Tutorials

-   [Creating Status Callback Functions](creating-status-callback-functions.md)

Functions needed to set up asynchronous operation

-   [**InternetOpen**](/windows/win32/Wininet/nf-wininet-internetopena?branch=master)
-   [**InternetSetStatusCallback**](/windows/win32/Wininet/nf-wininet-internetsetstatuscallback?branch=master)

Functions that can be used asynchronously

-   [**FtpCreateDirectory**](/windows/win32/Wininet/nf-wininet-ftpcreatedirectorya?branch=master)
-   [**FtpDeleteFile**](/windows/win32/Wininet/nf-wininet-ftpdeletefilea?branch=master)
-   [**FtpFindFirstFile**](/windows/win32/Wininet/nf-wininet-ftpfindfirstfilea?branch=master)
-   [**FtpGetCurrentDirectory**](/windows/win32/Wininet/nf-wininet-ftpgetcurrentdirectorya?branch=master)
-   [**FtpGetFile**](/windows/win32/Wininet/nf-wininet-ftpgetfilea?branch=master)
-   [**FtpOpenFile**](/windows/win32/Wininet/nf-wininet-ftpopenfilea?branch=master)
-   [**FtpPutFile**](/windows/win32/Wininet/nf-wininet-ftpputfilea?branch=master)
-   [**FtpRemoveDirectory**](/windows/win32/Wininet/nf-wininet-ftpremovedirectorya?branch=master)
-   [**FtpRenameFile**](/windows/win32/Wininet/nf-wininet-ftprenamefilea?branch=master)
-   [**FtpSetCurrentDirectory**](/windows/win32/Wininet/nf-wininet-ftpsetcurrentdirectorya?branch=master)
-   [**GopherFindFirstFile**](/windows/win32/Wininet/nf-wininet-gopherfindfirstfilea?branch=master)
-   [**GopherOpenFile**](/windows/win32/Wininet/nf-wininet-gopheropenfilea?branch=master)
-   [**HttpEndRequest**](/windows/win32/Wininet/nf-wininet-httpendrequesta?branch=master)
-   [**HttpOpenRequest**](/windows/win32/Wininet/nf-wininet-httpopenrequesta?branch=master)
-   [**HttpSendRequestEx**](/windows/win32/Wininet/nf-wininet-httpsendrequestexa?branch=master)
-   [**InternetConnect**](/windows/win32/Wininet/nf-wininet-internetconnecta?branch=master)
-   [**InternetOpenUrl**](/windows/win32/Wininet/nf-wininet-internetopenurla?branch=master)
-   [**InternetReadFileEx**](/windows/win32/Wininet/nf-wininet-internetreadfileexa?branch=master)

> [!Note]  
> The [**FtpCreateDirectory**](/windows/win32/Wininet/nf-wininet-ftpcreatedirectorya?branch=master), [**FtpRemoveDirectory**](/windows/win32/Wininet/nf-wininet-ftpremovedirectorya?branch=master), [**FtpSetCurrentDirectory**](/windows/win32/Wininet/nf-wininet-ftpsetcurrentdirectorya?branch=master), [**FtpGetCurrentDirectory**](/windows/win32/Wininet/nf-wininet-ftpgetcurrentdirectorya?branch=master), [**FtpDeleteFile**](/windows/win32/Wininet/nf-wininet-ftpdeletefilea?branch=master), and [**FtpRenameFile**](/windows/win32/Wininet/nf-wininet-ftprenamefilea?branch=master) functions use the context value provided in the call to the [**InternetConnect**](/windows/win32/Wininet/nf-wininet-internetconnecta?branch=master) function.

 

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](https://msdn.microsoft.com/library/windows/desktop/aa384273).

 

 

 




