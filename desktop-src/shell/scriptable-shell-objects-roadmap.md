---
description: The Windows Shell provides a powerful set of automation objects that enable you to program the Shell with Microsoft Visual Basic and scripting languages such as Microsoft JScript (compatible with ECMA 262 language specification) and Microsoft Visual Basic Scripting Edition (VBScript). You can use these objects to access many of the Shell's features and dialog boxes. For example, you can access the file system, launch programs, and change system settings.
title: Scriptable Shell Objects
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 09455fad-a769-42ef-83ba-b745ac819bf3
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Scriptable Shell Objects

The Windows Shell provides a powerful set of automation objects that enable you to program the Shell with Microsoft Visual Basic and scripting languages such as Microsoft JScript (compatible with ECMA 262 language specification) and Microsoft Visual Basic Scripting Edition (VBScript). You can use these objects to access many of the Shell's features and dialog boxes. For example, you can access the file system, launch programs, and change system settings.

This section introduces the scriptable Shell objects.

- [Shell Versions](#shell-versions)
- [Instantiating Shell Objects](#instantiating-shell-objects)
    - [Late Binding](#late-binding)
    - [HTML OBJECT Element](#html-object-element)
- [Shell Object](#shell-object)
    - [Security](#security)
- [Folder Objects](#folder-objects)

## Shell Versions

Many of the Shell objects became available in [version 4.71](versions.md) of the Shell. Others are available in version 5.00 and later. Version 5.00 became available with Windows 2000. The following table lists each Shell object under the version of the Shell in which the object became available.



| Version 4.71                                            | Version 5.00                                          |
|---------------------------------------------------------|-------------------------------------------------------|
| [**Folder**](folder.md)                                | [**DIDiskQuotaUser**](didiskquotauser-object.md)     |
| [**FolderItemVerb**](folderitemverb.md)                | [**DiskQuotaControl**](diskquotacontrol-object.md)   |
| [**FolderItemVerbs**](folderitemverbs.md)              | [**Folder2**](folder2-object.md)                     |
| [**Shell**](shell.md)                                  | [**FolderItem**](folderitem.md)                      |
| [**ShellFolderView**](shellfolderview.md)              | [**FolderItems**](folderitems.md)                    |
| [**ShellUIHelper**](shelluihelper.md)                  | [**FolderItems2**](folderitems2-object.md)           |
| [**ShellWindows**](shellwindows.md)                    | [**IShellDispatch2**](ishelldispatch2-object.md)     |
| [**WebViewFolderContents**](../lwef/webviewfoldercontents.md) | [**IShellLinkDual2**](ishelllinkdual2-object.md)     |
|                                                         | [**ShellFolderItem**](shellfolderitem-object.md)     |
|                                                         | [**ShellFolderViewOC**](shellfolderviewoc-object.md) |
|                                                         | [**ShellLinkObject**](shelllinkobject-object.md)     |



 

## Instantiating Shell Objects

To instantiate the Shell objects in Visual Basic applications with early binding, add references to the following libraries in your project:

-   Microsoft Internet Controls (SHDocVw)
-   Microsoft Shell Controls and Automation (Shell32)

### Late Binding

You can also instantiate many of the Shell objects with late binding. This approach works in Visual Basic applications and in script. The following example shows how to instantiate the [**Shell**](shell.md) object in JScript.


```
<SCRIPT LANGUAGE="JScript">
<!--
    function fnCreateShell()    
    {
        // Instantiate the Shell object and invoke its FileRun method.
        var oShell = new ActiveXObject("shell.application");
        oshell.FileRun;
    }
-->
</SCRIPT>
```



The following example shows how to instantiate the [**Folder**](folder.md) object in VBScript.


```
<SCRIPT LANGUAGE="VBScript">
<!--
    function fnCreateFolder()
        dim oShell    
        dim oFolder
        dim sDir

        sDir = "C:\SomePath" 
        set oShell = CreateObject("shell.application")
        set oFolder = oShell.NameSpace(sDir)  
    end function
-->  
</SCRIPT>
```



In the preceding example, *sDir* is the path to the [**Folder**](folder.md) object. Note that the [**ShellSpecialFolderConstants**](/windows/desktop/api/Shldisp/ne-shldisp-shellspecialfolderconstants) enumeration values are not available in script.

The ProgID for each of the Shell objects is shown in the following table.



| Object                                                  | ProgID                                                                                  |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**DIDiskQuotaUser**](didiskquotauser-object.md)       | Microsoft.DiskQuota.1                                                                   |
| [**DiskQuotaControl**](diskquotacontrol-object.md)     | Cannot late bind                                                                        |
| [**Folder**](folder.md)                                | shell.Shell\_Application.NameSpace("...")                                               |
| [**Folder2**](folder2-object.md)                       | shell.Shell\_Application.NameSpace("...")                                               |
| [**FolderItem**](folderitem.md)                        | shell.Shell\_Application.NameSpace("...").Self or Folder.Items.Item or Folder.ParseName |
| [**FolderItems**](folderitems.md)                      | Folder.Items                                                                            |
| [**FolderItems2**](folderitems2-object.md)             | Folder.Items                                                                            |
| [**FolderItemVerb**](folderitemverb.md)                | Shell.NameSpace("...").Self.Verbs.Item()                                                |
| [**FolderItemVerbs**](folderitemverbs.md)              | FolderItem.Verbs or Shell.NameSpace("...").Self.Verbs                                   |
| [**IShellDispatch2**](ishelldispatch2-object.md)       | shell.Shell\_Application                                                                |
| [**IShellLinkDual2**](ishelllinkdual2-object.md)       | Shell.NameSpace("...").Self.GetLink or Shell.NameSpace("...").Items().GetLink           |
| [**Shell**](shell.md)                                  | shell.Shell\_Application                                                                |
| [**ShellFolderItem**](shellfolderitem-object.md)       | Shell.NameSpace("...").Self or Shell.NameSpace("...").Items()                           |
| [**ShellFolderView**](shellfolderview.md)              | Cannot late bind                                                                        |
| [**ShellFolderViewOC**](shellfolderviewoc-object.md)   | Cannot late bind                                                                        |
| [**ShellLinkObject**](shelllinkobject-object.md)       | Shell.NameSpace("...").Self.GetLink or Shell.NameSpace("...").Items().GetLink           |
| [**ShellUIHelper**](shelluihelper.md)                  | Cannot late bind                                                                        |
| [**ShellWindows**](shellwindows.md)                    | shell.Shell\_Windows or ShellWindows.\_NewEnum                                          |
| [**WebViewFolderContents**](../lwef/webviewfoldercontents.md) | Cannot late bind                                                                        |



 

### HTML OBJECT Element

You can also use the [**OBJECT**](https://msdn.microsoft.com/library/ms535859(v=VS.85).aspx) element to instantiate Shell objects on an HTML page. To do this, set the **OBJECT** element's **ID** attribute to the variable name you will use in your scripts, and identify the object using its registered number (CLASSID). The following HTML creates an instance of the [**ShellFolderItem**](shellfolderitem-object.md) object using the **OBJECT** element.


```
<OBJECT ID="oShFolderItem" 
    NAME="Shell Folder Item Object"
    CLASSID="clsid:2fe352ea-fd1f-11d2-b1f4-00c04f8eeb3e">
</OBJECT>
```



The following table lists each Shell object and its respective CLASSID.



| Shell object                                           | CLASSID                              |
|--------------------------------------------------------|--------------------------------------|
| [**DIDiskQuotaUser**](didiskquotauser-object.md)       | 7988B571-EC89-11cf-9C00-00AA00A14F56 |
| [**DiskQuotaControl**](diskquotacontrol-object.md)     | 7988B571-EC89-11cf-9C00-00AA00A14F56 |
| [**Folder**](folder.md)                                | BBCBDE60-C3FF-11CE-8350-444553540000 |
| [**Folder2**](folder2-object.md)                       | f0d2d8ef-3890-11d2-bf8b-00c04fb93661 |
| [**FolderItem**](folderitem.md)                        | 744129E0-CBE5-11CE-8350-444553540000 |
| [**FolderItems**](folderitems.md)                      | 744129E0-CBE5-11CE-8350-444553540000 |
| [**FolderItems2**](folderitems2-object.md)             | C94F0AD0-F363-11d2-A327-00C04F8EEC7F |
| [**FolderItemVerb**](folderitemverb.md)                | 08EC3E00-50B0-11CF-960C-0080C7F4EE85 |
| [**FolderItemVerbs**](folderitemverbs.md)              | 1F8352C0-50B0-11CF-960C-0080C7F4EE85 |
| [**IShellDispatch2**](ishelldispatch2-object.md)       | A4C6892C-3BA9-11d2-9DEA-00C04FB16162 |
| [**IShellLinkDual2**](ishelllinkdual2-object.md)       | 317EE249-F12E-11d2-B1E4-00C04F8EEB3E |
| [**Shell**](shell.md)                                  | 13709620-C279-11CE-A49E-444553540000 |
| [**ShellFolderItem**](shellfolderitem-object.md)       | 2fe352ea-fd1f-11d2-b1f4-00c04f8eeb3e |
| [**ShellFolderView**](shellfolderview.md)              | 62112AA1-EBE4-11cf-A5FB-0020AFE7292D |
| [**ShellFolderViewOC**](shellfolderviewoc-object.md)   | 4a3df050-23bd-11d2-939f-00a0c91eedba |
| [**ShellLinkObject**](shelllinkobject-object.md)       | 11219420-1768-11d1-95BE-00609797EA4F |
| [**ShellUIHelper**](shelluihelper.md)                  | 64AB4BB7-111E-11D1-8F79-00C04FC2FBE1 |
| [**ShellWindows**](shellwindows.md)                    | 9BA05972-F6A8-11CF-A442-00A0C90A8F39 |
| [**WebViewFolderContents**](../lwef/webviewfoldercontents.md) | 1820FED0-473E-11D0-A96C-00C04FD705A2 |



 

## Shell Object

The [**Shell**](shell.md) object represents the objects in the Shell. You can use the methods exposed by the Shell object to:

-   Open, explore, and browse for folders.
-   Minimize, restore, cascade, or tile open windows.
-   Launch Control Panel applications.
-   Display system dialog boxes.

Users are perhaps most familiar with the commands they access from the **Start** menu and the taskbar's shortcut menu. The taskbar's shortcut menu appears when users right-click the taskbar. The following HTML Application (HTA) produces a start page with buttons that implement many of the [**Shell**](shell.md) object's methods. Some of these methods implement features on the **Start** menu and the taskbar's shortcut menu.


```
<HTML>
<HEAD>
    <TITLE>Start Page</TITLE>
    
    <OBJECT ID="oShell"
        CLASSID="clsid:13709620-C279-11CE-A49E-444553540000">
    </OBJECT>
    
    <STYLE>
        INPUT {width: 200} 
    </STYLE>  
    
    <SCRIPT LANGUAGE="VBScript">
    <!--
        function fnStart(sMethod)
            select case sMethod
              case 0    
                  'Minimizes all windows on the desktop
                oshell.Shell_MinimizeAll
              case 1  
                  'Displays the Run dialog box
                oshell.FileRun
              case 2  
                  'Displays the Shut Down Windows dialog box
                oshell.Shell_ShutdownWindows
              case 3  
                  'Displays the Find dialog box
                oshell.Shell_FindFilesr
              case 4  
                  'Displays the Date/Time dialog box
                oshell.Shell_SetTime 
              case 5  
                  'Displays the Internet Properties dialog box
                oshell.Shell_ControlPanelItem "INETCPL.cpl"
              case 6  
                  'Explores the My Documents folder
                oshell.Shell_Explore "C:\My Documents"
              case 7  
                  'Enables user to select folder from Program Files
                oshell.Shell_BrowseForFolder 0, "My Programs", 0, "C:\Program Files" 
              case 8  
                  'Opens the Favorites folder
                oshell.Shell_Open "C:\WINDOWS\Favorites"
              case 9  
                  'Displays the Taskbar Properties dialog box
                oshell.Shell_TrayProperties
            end select  
        end function      
    -->
    </SCRIPT>
</HEAD>

<BODY>
    <H1>Start...</H1>
    <INPUT type="button" value="Edit Taskbar Properties" onclick="fnStart(9)"><br>
    <INPUT type="button" value="Open Favorites Folder" onclick="fnStart(8)"><br>
    <INPUT type="button" value="Browse Program Files" onclick="fnStart(7)"><br>
    <INPUT type="button" value="Explore My Documents" onclick="fnStart(6)"><br>
    <INPUT type="button" value="Modify Internet Properties" onclick="fnStart(5)"><br>
    <INPUT type="button" value="Set System Time" onclick="fnStart(4)"><br>
    <INPUT type="button" value="Find a File or Folder" onclick="fnStart(3)"><br>
    <INPUT type="button" value="Shut Down Windows" onclick="fnStart(2)"><br>
    <INPUT type="button" value="Run" onclick="fnStart(1)">     
    <INPUT type="button" value="Minimize All Windows" onclick="fnStart(0)">     
</BODY>
</HTML>
```



### Security

As an application, an HTA runs under a different security model than a webpage. To interact with a webpage that implements the functionality of the Shell objects, users must enable the **Initialize and script ActiveX Controls not marked as safe** option for the security zone in which they are viewing the page.

## Folder Objects

The [**Folder**](folder.md) object represents a Shell folder. You can use the methods exposed by the Folder object to:

-   Get information about a folder.
-   Create subfolders.
-   Copy and move file objects into the folder.

The [**FolderItem**](folderitem.md) object represents an item in a Shell folder. Its properties enable you to retrieve information about the item. You can use the methods exposed by this object to run an item's verbs, or to retrieve information about an item's [**FolderItemVerbs**](folderitemverbs.md) object.

The [**FolderItems**](folderitems.md) object represents a collection of items in a Shell folder. Its methods and properties enable you to retrieve information about the collection.

The following Visual Basic example shows the relationship between several of the folder objects and how they can be used together. When the user clicks the command button called **cmdGetPath**, the program displays a dialog box that enables the user to select a folder from **My Computer**, where ssfDRIVES is the [**ShellSpecialFolderConstants**](/windows/desktop/api/Shldisp/ne-shldisp-shellspecialfolderconstants) enumeration value for **My Computer**. When the user chooses a folder, the folder's path is displayed in the text box called **txtPath**.


```
Private Sub cmdGetPath_Click()
    Dim oShell As New Shell
    Dim oFolder As Folder
    Dim oFolderItem As FolderItem
 
    Set oFolder = oshell.Shell_BrowseForFolder(Me.hWnd, "Select a Folder", 0, ssfDrives)
   
    Set oFolderItem = oFolderItems.Item

    txtPath.Text = oFolderItem.Path
End Sub
```



In VBScript, this function is slightly different because the [**ShellSpecialFolderConstants**](/windows/desktop/api/Shldisp/ne-shldisp-shellspecialfolderconstants) enumeration values are not available in script. The following example shows the VBScript equivalent of the previous example.


```
<SCRIPT LANGUAGE="VBScript">
<!--
    function fnGetMyPathVB() 
        dim oShell
        dim oFolder
        dim oFolderItem
        
        set oShell = CreateObject("shell.application")      
        set oFolder = oshell.Shell_BrowseForFolder(0, "Choose a Folder", 0)             
        set oFolderItem = oFolder.Items.Item         
        
        document.all.item("myPath").innerText = oFolderItem.Path                                
    end function
-->
</SCRIPT>
```



In the following JScript example, which is a direct translation of the preceding VBScript example, note how the empty parentheses '()' are used to invoke the [**Items**](folder-items.md) and [**Item**](folderitems-item.md) methods.


```
<SCRIPT LANGUAGE="JavaScript">
<!--
    function fnGetMyPathJ() 
    {       
        var oShell = new ActiveXObject("shell.application");
                    
        var oFolder = new Object;                   
        oFolder = oshell.Shell_BrowseForFolder(0, "Choose a folder", 0);
                                
        var oFolderItem = new Object;       
        oFolderItem = oFolder.Items().Item();                               
        
        document.all.item("myPath").innerText = oFolderItem.Path;
    }    
-->
</SCRIPT>
```



 

 
