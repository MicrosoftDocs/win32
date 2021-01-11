---
description: The scripting sample in this topic shows you how to use the Windows Update Agent (WUA) to scan, download, and install a specific update. The update can be specified by its title.
ms.assetid: 4a5bb920-fc51-48a0-8f66-bb2fcc72589f
title: Searching, Downloading, and Installing Specific Updates
ms.topic: article
ms.date: 05/31/2018
---

# Searching, Downloading, and Installing Specific Updates

The scripting sample in this topic shows you how to use the Windows Update Agent (WUA) to scan, download, and install a specific update. The update can be specified by its title.

The sample searches for a specific software update, downloads the update, and then installs the update. For example, a user can use this method to determine if a critical security update is installed on a computer. If the update isn't installed, the user can ensure that the update is downloaded and installed. The user can also ensure that they are notified about the status of the installation.

The sample update is identified by the update title in [**Title Property of IUpdate**](/windows/desktop/api/Wuapi/nf-wuapi-iupdate-get_title). The title of the update that is suggested in this sample is "Update for Windows Rights Management client 1.0."

> [!Note]  
> For info about how to search, download, and install all the updates that apply to a specific application, see [Searching, Downloading, and Installing Updates](searching--downloading--and-installing-updates.md).

 

Before you attempt to run this sample, note the following:

-   WUA must be installed on the computer. For more info about how to determine the version of WUA that is installed, see [Determining the Current Version of WUA](determining-the-current-version-of-wua.md).
-   The sample doesn't provide its own user interface. WUA prompts the user to restart the computer if an update requires a restart.
-   The sample can download updates only from WUA. It can't download updates from a Software Update Services (SUS) 1.0 server.
-   Running this sample requires Windows Script Host (WSH). For more info about WSH, see the WSH section of the Platform Software Development Kit (SDK). If the sample is copied to a file named WUA\_SpecificUpdate.vbs, you can run it by opening a Command Prompt window and by typing this command: **cscript WUA\_SpecificUpdate.vbs**  
    

## Example

> [!IMPORTANT]
> This script is intended to demonstrate the use of the Windows Update Agent APIs, and provide an example of how developers can use these APIs to solve problems. This script is not intended as production code, and the script itself is not supported by Microsoft (though the underlying Windows Update Agent APIs are supported).

 


```VB
Set updateSession = CreateObject("Microsoft.Update.Session")
updateSession.ClientApplicationID = "MSDN Sample Script"

'Get update title to search for
WScript.Echo "Enter the title of the update: " & _
"(for example, Update for Windows Rights Management client 1.0)"
updateTitle = WScript.StdIn.Readline

WScript.Echo vbCRLF & "Searching for: " & updateTitle & "..."

Set updateSearcher = updateSession.CreateupdateSearcher()

'Search for all software updates, already installed and not installed
Set searchResult = _
updateSearcher.Search("Type='Software'")

Set updateToInstall = CreateObject("Microsoft.Update.UpdateColl")

updateIsApplicable = False

'Cycle through search results to look for the update title
For i = 0 To searchResult.Updates.Count-1
   Set update = searchResult.Updates.Item(i)
   If UCase(update.Title) = UCase(updateTitle) Then
   'Update in list of applicable updates 
   'Determine if it is already installed or not
      If update.IsInstalled = False Then
         WScript.Echo vbCRLF & _
         "Result: Update applicable, not installed."
         updateIsApplicable = True
         updateToInstall.Add(update)
      Else 
         'Update is installed so notify user and quit
         WScript.Echo vbCRLF & _
         "Result: Update applicable, already installed."
         updateIsApplicable = True
         WScript.Quit 
      End If
   End If 
Next

If updateIsApplicable = False Then
   WScript.Echo "Result: Update is not applicable to this machine."
   WScript.Quit
End If

WScript.Echo vbCRLF & "Would you like to install now? (Y/N)"
stdInput = WScript.StdIn.Readline
 
If (strInput = "N" or strInput = "n") Then 
   WScript.Quit
ElseIf  (stdInput = "Y" OR stdInput = "y") Then
   'Download update
   Set downloader = updateSession.CreateUpdateDownloader() 
   downloader.Updates = updateToInstall
   WScript.Echo vbCRLF & "Downloading..."
   Set downloadResult = downloader.Download()
   WScript.Echo "Download Result: " & downloadResult.ResultCode
  
   'Install Update
   Set installer = updateSession.CreateUpdateInstaller()
   WScript.Echo vbCRLF & "Installing..."
   installer.Updates = updateToInstall
   Set installationResult = installer.Install()
  
   'Output the result of the installation
   WScript.Echo "Installation Result: " & _
   installationResult.ResultCode
   WScript.Echo "Reboot Required: " & _
   installationResult.RebootRequired 
End If
```



 

 



