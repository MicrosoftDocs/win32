---
description: Windows Update Agent (WUA) can be used to scan computers for security updates without connecting to Windows Update or to a Windows Server Update Services (WSUS) server, which enables computers that are not connected to the Internet to be scanned for security updates. Offline scanning for updates requires the download of a signed file, Wsusscn2.cab, from Windows Update.
ms.assetid: 452b53af-0f7b-435e-bf12-dd9d84cbd564
title: Using WUA to Scan for Updates Offline
ms.topic: article
ms.date: 07/23/2020
---

# Using WUA to Scan for Updates Offline

Windows Update Agent (WUA) can be used to scan computers for security updates without connecting to Windows Update or to a Windows Server Update Services (WSUS) server, which enables computers that are not connected to the Internet to be scanned for security updates.

Offline scanning for updates requires the download of a signed file, Wsusscn2.cab, from Windows Update.

The Wsusscn2.cab file is a cabinet file that is signed by Microsoft. This file contains info about security-related updates that are published by Microsoft. Computers that aren't connected to the Internet can be scanned to see whether these security-related updates are present or required. The Wsusscn2.cab file doesn't contain the security updates themselves so you must obtain and install any needed security-related updates through other means. New versions of the Wsusscn2.cab file are released periodically as security-related updates are released, removed, or revised on the Windows Update site. The latest Wsusscn2.cab file is available for download at the following location: [Download Wsusscn2.cab](http://download.windowsupdate.com/microsoftupdate/v6/wsusscan/wsusscn2.cab)

After you download the latest Wsusscn2.cab, the file can be provided to the [**AddScanPackageService**](/windows/desktop/api/Wuapi/nf-wuapi-iupdateservicemanager-addscanpackageservice) method, and the WUA API can be used to search the offline computer for security updates. WUA validates that the Wsusscn2.cab is signed by a valid Microsoft certificate before running an offline scan.

> [!NOTE]
> In accordance with our [SHA-1 deprecation initiative](https://aka.ms/sha1deprecation), the Wsusscn2.cab file is no longer dual-signed using both SHA-1 and the SHA-2 suite of hash algorithms (specifically SHA-256). This file is now signed using only SHA-256. Administrators who verify digital signatures on this file should now expect only single SHA-256 signatures.

## Example

The following example uses the Wsusscn2.cab file to scan a computer and displays updates that are missing.

> [!IMPORTANT]
> This script is intended to demonstrate the use of the Windows Update Agent APIs, and provide an example of how developers can use these APIs to solve problems. This script is not intended as production code, and the script itself is not supported by Microsoft (though the underlying Windows Update Agent APIs are supported).

 


```VB
Set UpdateSession = CreateObject("Microsoft.Update.Session")
Set UpdateServiceManager = CreateObject("Microsoft.Update.ServiceManager")
Set UpdateService = UpdateServiceManager.AddScanPackageService("Offline Sync Service", "c:\wsusscn2.cab")
Set UpdateSearcher = UpdateSession.CreateUpdateSearcher()

WScript.Echo "Searching for updates..." & vbCRLF

UpdateSearcher.ServerSelection = 3 ' ssOthers

UpdateSearcher.ServiceID = UpdateService.ServiceID

Set SearchResult = UpdateSearcher.Search("IsInstalled=0")

Set Updates = SearchResult.Updates

If searchResult.Updates.Count = 0 Then
    WScript.Echo "There are no applicable updates."
    WScript.Quit
End If

WScript.Echo "List of applicable items on the machine when using wssuscan.cab:" & vbCRLF

For I = 0 to searchResult.Updates.Count-1
    Set update = searchResult.Updates.Item(I)
    WScript.Echo I + 1 & "> " & update.Title
Next

WScript.Quit
```



 

 



