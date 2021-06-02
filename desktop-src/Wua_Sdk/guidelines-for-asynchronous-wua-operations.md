---
description: This topic identifies guidelines for you to the follow when you perform asynchronous Windows Update Agent (WUA) operations.
ms.assetid: 1fb16904-732d-4341-8267-ab8896fc0f7c
title: Guidelines for Asynchronous WUA Operations
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Asynchronous WUA Operations

This topic identifies guidelines for you to the follow when you perform asynchronous Windows Update Agent (WUA) operations.

-   The asynchronous WUA operations do not guarantee any particular completion speed. The completion time for an asynchronous WUA operation can vary widely depending on computer hardware, version of the operating system, and network configuration. As with other Windows APIs that have network dependencies and that do not contain a time-out parameter or a documented time-out duration, we recommend that you consider implementing your own time-out mechanisms if you need guaranteed response times. For example, you can create a worker thread that calls an asynchronous WUA method and that sets an event or other synchronization object when the asynchronous WUA operation completes; the main thread can then use the [**WaitForSingleObject**](/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobject) or [**WaitForMultipleObjects**](/windows/desktop/api/synchapi/nf-synchapi-waitformultipleobjects) function, which allows you to specify a time-out value.
-   When you end a search, download, installation, or uninstallation of updates, you can use [**IUpdateSearcher::EndSearch**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesearcher-endsearch), [**IUpdateDowloader::EndDownload**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatedownloader), [**IUpdateInstaller::EndInstall**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-endinstall) and [**IUpdateInstaller::EndUninstall**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-enduninstall) from any thread.
-   When you start a search, download, installation, or uninstallation of updates by using [**IUpdateSearcher::BeginSearch**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesearcher-beginsearch), [**IUpdateDownloader::BeginDownload**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatedownloader-begindownload), [**IUpdateInstaller::BeginInstall**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-begininstall), and [**IUpdateInstaller::BeginUninstall**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-beginuninstall), ensure that you maintain sufficient access permisssions when you release references to WUA API objects.
    -   Make sure any callback objects that are used in the asynchronous operation are unreferenced before you destroy them. Wait for the reference count of a callback object to return to the initial value before you destroy it.
    -   The reference to the job object that is returned from the corresponding **Begin** method should be controlled by an object that differs from the callback objects. Use an object that differs from the callback objects to avoid circular references.
    -   If you attempt to control the reference to the job object by using a callback object, you must call the [**IDownloadJob::CleanUp**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadjob-cleanup), [**IInstallationJob::CleanUp**](/windows/desktop/api/Wuapi/nf-wuapi-iinstallationjob-cleanup), or [**ISearchJob::CleanUp**](/windows/desktop/api/Wuapi/nf-wuapi-isearchjob-cleanup) method outside the callback function to disconnect the job object from the callback object. You must do this before you release the reference to the job object that is returned by the **Begin** method.
-   Make sure that asynchronous WUA operations are complete. Windows Script Host can terminate a script when all the commands outside of any function are complete, even if the WUA API still has references to the callback object.
    -   Use one of the **CleanUp** methods or have the callback function set a shared global variable upon completion.
    -   Never call [**IDownloadJob::CleanUp**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadjob-cleanup), [**IInstallationJob::CleanUp**](/windows/desktop/api/Wuapi/nf-wuapi-iinstallationjob-cleanup), or [**ISearchJob::CleanUp**](/windows/desktop/api/Wuapi/nf-wuapi-isearchjob-cleanup) on a job object in its callback function.
    -   To ensure the correct clean-up sequence in a script that is running on Windows Internet Explorer, call the **CleanUp** method on all the job objects when processing window.onbeforeunload.
-   Do not use user-defined data types (UDT) for asynchronous WUA operations. The type is not supported by [**IUpdateSearcher::BeginSearch**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatesearcher-beginsearch), [**IUpdateDownloader::BeginDownload**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatedownloader-begindownload), [**IUpdateInstaller::BeginInstall**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-begininstall), or [**IUpdateInstaller::BeginUninstall**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateinstaller-beginuninstall).

 

 
