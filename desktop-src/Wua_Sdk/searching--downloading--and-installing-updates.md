---
Description: The scripting sample in this topic shows you how to use Windows Update Agent (WUA) to scan, download, and install updates.
ms.assetid: 4b2b1898-64f1-4908-98b7-ea87a6fcb71d
title: Searching, Downloading, and Installing Updates
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Searching, Downloading, and Installing Updates

The scripting sample in this topic shows you how to use Windows Update Agent (WUA) to scan, download, and install updates.

The sample searches for all the applicable software updates and then lists those updates. Next, it creates a collection of updates to download and then downloads them. Finally, it creates a collection of updates to install and then installs them.

If you want to search, download, and install a specific update that you identify by using the update title, see [Searching, Downloading, and Installing Specific Updates](searching--downloading--and-installing-specific-updates.md).

Before you attempt to run this sample, note the following:

-   WUA must be installed on the computer. For more information about how to determine the version of WUA that is installed, see [Determining the Current Version of WUA](determining-the-current-version-of-wua.md).
-   The sample can download updates only by using WUA. It cannot download updates from a Software Update Services (SUS) 1.0 server.
-   Running this sample requires Windows Script Host (WSH). For more information about WSH, see the WSH section of the Platform Software Development Kit (SDK). If the sample is copied to a file named WUA\_SearchDownloadInstall.vbs, you can run the sample by opening a Command Prompt window and typing the following command at the command prompt.

    **cscript WUA\_SearchDownloadInstall.vbs**

## Example

> \[!Important\]  
> This script is intended to demonstrate the use of the Windows Update Agent APIs, and provide an example of how developers can use these APIs to solve problems. This script is not intended as production code, and the script itself is not supported by Microsoft (though the underlying Windows Update Agent APIs are supported).

 


```VB
Set updateSession = CreateObject("Microsoft.Update.Session")
updateSession.ClientApplicationID = "MSDN Sample Script"

Set updateSearcher = updateSession.CreateUpdateSearcher()

WScript.Echo "Searching for updates..." & vbCRLF

Set searchResult = _
updateSearcher.Search("IsInstalled=0 and Type='Software' and IsHidden=0")

WScript.Echo "List of applicable items on the machine:"

For I = 0 To searchResult.Updates.Count-1
    Set update = searchResult.Updates.Item(I)
    WScript.Echo I + 1 & "> " & update.Title
Next

If searchResult.Updates.Count = 0 Then
    WScript.Echo "There are no applicable updates."
    WScript.Quit
End If

WScript.Echo vbCRLF & "Creating collection of updates to download:"

Set updatesToDownload = CreateObject("Microsoft.Update.UpdateColl")

For I = 0 to searchResult.Updates.Count-1
    Set update = searchResult.Updates.Item(I)
    addThisUpdate = false
    If update.InstallationBehavior.CanRequestUserInput = true Then
        WScript.Echo I + 1 & "> skipping: " & update.Title & _
        " because it requires user input"
    Else
        If update.EulaAccepted = false Then
            WScript.Echo I + 1 & "> note: " & update.Title & _
            " has a license agreement that must be accepted:"
            WScript.Echo update.EulaText
            WScript.Echo "Do you accept this license agreement? (Y/N)"
            strInput = WScript.StdIn.Readline
            WScript.Echo 
            If (strInput = "Y" or strInput = "y") Then
                update.AcceptEula()
                addThisUpdate = true
            Else
                WScript.Echo I + 1 & "> skipping: " & update.Title & _
                " because the license agreement was declined"
            End If
        Else
            addThisUpdate = true
        End If
    End If
    If addThisUpdate = true Then
        WScript.Echo I + 1 & "> adding: " & update.Title 
        updatesToDownload.Add(update)
    End If
Next

If updatesToDownload.Count = 0 Then
    WScript.Echo "All applicable updates were skipped."
    WScript.Quit
End If
    
WScript.Echo vbCRLF & "Downloading updates..."

Set downloader = updateSession.CreateUpdateDownloader() 
downloader.Updates = updatesToDownload
downloader.Download()

Set updatesToInstall = CreateObject("Microsoft.Update.UpdateColl")

rebootMayBeRequired = false

WScript.Echo vbCRLF & "Successfully downloaded updates:"

For I = 0 To searchResult.Updates.Count-1
    set update = searchResult.Updates.Item(I)
    If update.IsDownloaded = true Then
        WScript.Echo I + 1 & "> " & update.Title 
        updatesToInstall.Add(update) 
        If update.InstallationBehavior.RebootBehavior > 0 Then
            rebootMayBeRequired = true
        End If
    End If
Next

If updatesToInstall.Count = 0 Then
    WScript.Echo "No updates were successfully downloaded."
    WScript.Quit
End If

If rebootMayBeRequired = true Then
    WScript.Echo vbCRLF & "These updates may require a reboot."
End If

WScript.Echo  vbCRLF & "Would you like to install updates now? (Y/N)"
strInput = WScript.StdIn.Readline
WScript.Echo 

If (strInput = "Y" or strInput = "y") Then
    WScript.Echo "Installing updates..."
    Set installer = updateSession.CreateUpdateInstaller()
    installer.Updates = updatesToInstall
    Set installationResult = installer.Install()
 
    'Output results of install
    WScript.Echo "Installation Result: " & _
    installationResult.ResultCode 
    WScript.Echo "Reboot Required: " & _ 
    installationResult.RebootRequired & vbCRLF 
    WScript.Echo "Listing of updates installed " & _
    "and individual installation results:" 
 
    For I = 0 to updatesToInstall.Count - 1
        WScript.Echo I + 1 & "> " & _
        updatesToInstall.Item(i).Title & _
        ": " & installationResult.GetUpdateResult(i).ResultCode   
    Next
End If
```



 

 



