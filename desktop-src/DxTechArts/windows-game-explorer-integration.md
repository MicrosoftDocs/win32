---
title: Windows Games Explorer for Game Developers
description: This article outlines the process of registering a game with Games Explorer and parental controls on Windows Vista and Windows 7 by using the new GDF schema.
ms.assetid: 628f14bf-2714-0d68-8267-4f7f48c2774a
ms.topic: article
ms.date: 05/31/2018
---

# Windows Games Explorer for Game Developers

Windows Vista improves the user experience of gaming on Windows by including Games Explorer. Games Explorer is exposed in the Windows Vista Start Menu as the Games folder and provides a central location for accessing games.

Starting with the March 2009 release of the DirectX SDK, a new game definition file (GDF) schema is used to support features in Windows 7, Game Provider and RSS feed, and IGameExplorer2. IGameExplorer2 is a new interface on Windows 7 that simplifies the process of integrating a game with Games Explorer.

This article outlines the process of registering a game with Games Explorer and parental controls on Windows Vista and Windows 7 by using the new GDF schema.

Contents:

-   [Prerequisites](#prerequisites)
-   [Integrating with an Installer](#integrating-with-an-installer)
-   [Integration Process](#integration-process)
-   [Games Explorer Tasks](#games-explorer-tasks)
-   [Integrating into InstallScript](#integrating-into-installscript)
-   [Integrating into an MSI Package](#integrating-into-an-msi-package)
-   [Debugging Tips](#debugging-tips)
    -   [Test with sample code](#test-with-sample-code)
    -   [Make sure that your game was removed properly](#make-sure-that-your-game-was-removed-properly)
    -   [Be sure to sign using Authenticode](#be-sure-to-sign-using-authenticode)
    -   [Be sure that parental controls are available](#be-sure-that-parental-controls-are-available)
    -   [Verify that tasks are of the correct type](#verify-that-tasks-are-of-the-correct-type)
    -   [Verify the data in GDF binary](#verify-the-data-in-gdf-binary)
-   [Summary](#summary)

## Prerequisites

Before you can integrate a game into Games Explorer, you must create a game definition file (GDF). A GDF is an XML file that contains metadata that describes the game. In the March 2009 release of the DirectX SDK, a section for game provider, RSS feed, and game task has been added to the GDF schema. To use the instructions in this article, you must use this new GDF format to create your GDF file.

Microsoft provides a tool for authoring GDFs in the DirectX SDK, Game Definition File Editor, to make this creation process easier. This tool also helps you create localized versions of a GDF.

Once a GDF has been authored and localized, it must be encapsulated within a resource section of a binary file (either an executable or DLL), along with the game's thumbnail and icon. The GDF contains all of the metadata associated with the game, including the game's rating. Windows Parental Controls use the game's rating to allow parents to control access to the game. The binary file which contains the GDF must be digitally signed with a valid Authenticode certificate; otherwise, Games Explorer and the parental control system ignores the game's rating, because the rating information cannot be trusted without certification. For more details about signing code with Authenticode, see [Authenticode Signing for Game Developers](/windows/desktop/DxTechArts/authenticode-signing-for-game-developers).

## Integrating with an Installer

To simplify Games Explorer integration, the GameUXInstallHelper sample provides a common API that can be called on Windows XP, Windows Vista, and Windows 7. It is designed to work with scripts for InstallShield and Wise Installation System, as well as MSI custom actions and custom installation tools. Detection of the operating system is handled inside this sample DLL, so the caller does not need to worry whether the client is running Windows XP, Windows Vista, or Windows 7.

The functions exported by this DLL are the following:

<dl> <dt>

<span id="GameExplorerInstallW"></span><span id="gameexplorerinstallw"></span><span id="GAMEEXPLORERINSTALLW"></span>**GameExplorerInstallW**
</dt> <dd>

Registers a game with Games Explorer, given a path to the GDF binary, a full path to the folder where the game is installed, and the installation scope.

</dd> <dt>

<span id="GameExplorerInstallA"></span><span id="gameexplorerinstalla"></span><span id="GAMEEXPLORERINSTALLA"></span>**GameExplorerInstallA**
</dt> <dd>

Registers a game with Games Explorer; ANSI version of **GameExplorerInstallW**.

</dd> <dt>

<span id="GameExplorerUninstallW"></span><span id="gameexploreruninstallw"></span><span id="GAMEEXPLORERUNINSTALLW"></span>**GameExplorerUninstallW**
</dt> <dd>

Removes a game from registration with Games Explorer, given a path to the GDF binary.

</dd> <dt>

<span id="GameExplorerUninstallA"></span><span id="gameexploreruninstalla"></span><span id="GAMEEXPLORERUNINSTALLA"></span>**GameExplorerUninstallA**
</dt> <dd>

Removes a game from registration with Games Explorer; ANSI version of **GameExplorerUninstallW**.

</dd> <dt>

<span id="GameExplorerSetMSIProperties"></span><span id="gameexplorersetmsiproperties"></span><span id="GAMEEXPLORERSETMSIPROPERTIES"></span>**GameExplorerSetMSIProperties**
</dt> <dd>

Configures the CustomActionData properties for the actions of an MSI deferred custom installation. Usage of this function is described in detail later in this article.

</dd> <dt>

<span id="GameExplorerInstallUsingMSI"></span><span id="gameexplorerinstallusingmsi"></span><span id="GAMEEXPLORERINSTALLUSINGMSI"></span>**GameExplorerInstallUsingMSI**
</dt> <dd>

Adds a game to Games Explorer; for use during an MSI custom action installation.

</dd> <dt>

<span id="GameExplorerUninstallUsingMSI"></span><span id="gameexploreruninstallusingmsi"></span><span id="GAMEEXPLORERUNINSTALLUSINGMSI"></span>**GameExplorerUninstallUsingMSI**
</dt> <dd>

Remove a game from Games Explorer; for use during an MSI custom action installation.

</dd> </dl>

These functions are further explained in the GameUXInstallHelper.h header.

## Integration Process

Once the GDF and related files have been added to a binary resource, it is then possible to integrate the game with Games Explorer. Using **GameUXInstallHelper** will simplify the integration process. To register the game with Games Explorer, call the **GameExplorerInstall** with a path to the GDF binary, a full path to the folder where the game is installed, and the installation scope. To remove the game's registration, call **GameExplorerUninstall** with a path to the GDF binary.

Note that the removal process only removes one unique installation. If a game has been installed multiple times, this process must be repeated for each unique installation.

## Games Explorer Tasks

Games Explorer tasks will appear in the context menu of an item in Games Explorer. Tasks are divided into play tasks and support tasks. Play tasks launch a game into a particular mode, while support tasks serve any other purpose, including linking to web sites.

In Windows Vista, tasks are simply shortcuts that are located in specific folders. Play tasks and support tasks are stored in folders with the corresponding names PlayTasks and SupportTasks. GameUXInstallHelper can read the game's task information from the GDF binary file and create all of the shortcuts automatically.

In Windows 7, the shortcuts to the tasks are not needed, because Games Explorer obtains all of the task information directly from the GDF binary file.

## Integrating into InstallScript

Calling Games Explorer APIs from InstallShield's InstallScript is made easy by using the GameUXInstallHelper sample. The steps required to integrate with InstallShield are as follows:

1.  Open an InstallScript project in the InstallShield editor.
2.  Add GameUXInstallHelper.dll to the project to be installed to the target directory.

    **To add GameUXInstallHelper.dll to an InstallScript project:**

    1.  On the **Installation Designer** tab, click **Application Data** in the navigation pane on the left.
    2.  Click **Files and Folders** and browse in **Source computer's folders** to locate GameUXInstallerHelper.dll in **Source computer's files**.

        The default location for GameUXInstallerHelper.dll is DirectX SDK root\\Samples\\C++\\Misc\\Bin\\x86.

    3.  Under **Destination computer's folders**, click **Application Target Folder**.
    4.  Drag GameUXInstallerHelper.dll from **Source computer's files** to **Destination computer's files**.

3.  In the InstallScript explorer, click the InstallScript file (usually setup.rul) that calls the DLL function.
4.  Paste the following InstallScript into the file:

    ``` syntax
    typedef GUID
    begin
    LONG  Data1;
    SHORT Data2;
    SHORT Data3;
    CHAR  Data4(8);
    end;

    prototype LONG GameUXInstallHelper.GameExplorerInstallW(WSTRING, WSTRING, NUMBER);
    prototype LONG GameUXInstallHelper.GameExplorerUninstallW(WSTRING);

    function OnMoved()

    WSTRING gdfbin[256];
    WSTRING path[256];
    NUMBER scope;

    begin

    if !MAINTENANCE then

    UseDLL( TARGETDIR ^ "GameUXInstallHelper.dll" );
    UseDLL( WINSYSDIR ^ "OLE32.dll" );

    path = TARGETDIR;
    gdfbin = TARGETDIR ^ "bin\\ExampleGame.exe";  // TODO: Change this to point to binary containing the GDF

    if ALLUSERS == 1 then
    scope = 3;
    else
    scope = 2;
    endif;

    GameUXInstallHelper.GameExplorerInstallW( gdfbin, path, scope);

    UnUseDLL( TARGETDIR ^ "GameUXInstallHelper.dll" );
    UnUseDLL( WINSYSDIR ^ "OLE32.dll" );

    endif;

    end;

    function OnMoving()

    WSTRING gdfbin[256];

    begin

    if MAINTENANCE && UNINST != "" then

    UseDLL( TARGETDIR ^ "GameUXInstallHelper.dll" );
    UseDLL( WINSYSDIR ^ "OLE32.dll" );

    gdfbin = path ^ "bin\\ExampleGame.exe";  // TODO: Change this to point to binary containing the GDF

    GameUXInstallHelper.GameExplorerUninstallW(gdfbin);
    UnUseDLL( TARGETDIR ^ "GameUXInstallHelper.dll" );
    UnUseDLL( WINSYSDIR ^ "OLE32.dll" );

    endif;

    end;
    ```

## Integrating into an MSI Package

The following is a high-level description of the steps required to call the Games Explorer APIs using MSI custom actions:

1.  Add a property to the MSI Property table called "RelativePathToGDF" containing the relative path to the GDF binary.
2.  After the CostFinalize action, call the GameUXInstallHelper DLL function **SetMSIGameExplorerProperties** in an immediate custom action to set the appropriate MSI properties for the other custom actions.
3.  Upon installation, trigger a deferred custom action after the InstallFiles action that calls the GameUXInstallHelper DLL function **AddToGameExplorerUsingMSI**. If the installation is for all users, then the custom action must set the flag msidbCustomActionTypeNoImpersonate; otherwise, it must not set this flag. Therefore, two nearly identical custom actions are defined: GameUXAddAsAdmin and GameUXAddAsCurUser.
4.  Upon removal of the installation, trigger a deferred custom action before the RemoveFiles action that calls the GameUXInstallHelper DLL function **RemoveFromGameExplorerUsingMSI**. If the installation was for all users, then the custom action must set the flag msidbCustomActionTypeNoImpersonate; otherwise, it must not set this flag. Therefore, two nearly identical custom actions are defined: GameUXRemoveAsAdmin and GameUXRemoveAsCurUser.
5.  Define rollback custom actions to handle the case where the user cancels installing or removing after one of the these custom actions has already happened. This results in an additional 4 custom actions: GameUXRollBackAddAsAdmin, GameUXRollBackAddAsCurUser, GameUXRollBackRemoveAsAdmin, and GameUXRollBackRemoveAsCurUser.

This procedure is described in detail in the following instructions, which describe a process that can be done using an MSI editor, such as the Orca editor found in the Platform SDK. Some MSI editors have wizards which simplify some of these configuration steps.

**To configure an MSI package for integration with Games Explorer**

1.  Open the MSI package in Orca.
2.  Add the row shown in the following table to the **Binary** table in the MSI package. 

    | Name   | Data                                          |
    |--------|-----------------------------------------------|
    | GAMEUX | file path to the DLL\\GameUXInstallHelper.dll |

    

     

    > [!Note]  
    > This file will be embedded in the MSI package, so you must do this step every time you recompile GameUXInstallHelper.dll.

     

3.  Add the rows shown in the following table to the **CustomAction** table in the MSI package.

    | Action                        | Type                                                                                                                                                                                                   | Source | Target                         |
    |-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------|
    | GameUXSetMSIProperties        | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue = 65                                                                                                        | GAMEUX | SetMSIGameExplorerProperties   |
    | GameUXAddAsAdmin              | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue + msidbCustomActionTypeInScript + msidbCustomActionTypeNoImpersonate = 3137                                 | GAMEUX | AddToGameExplorerUsingMSI      |
    | GameUXAddAsCurUser            | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue + msidbCustomActionTypeInScript = 1089                                                                      | GAMEUX | AddToGameExplorerUsingMSI      |
    | GameUXRollBackAddAsAdmin      | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue + msidbCustomActionTypeRollback + msidbCustomActionTypeInScript + msidbCustomActionTypeNoImpersonate = 3393 | GAMEUX | RemoveFromGameExplorerUsingMSI |
    | GameUXRollBackAddAsCurUser    | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue + msidbCustomActionTypeRollback + msidbCustomActionTypeInScript = 1345                                      | GAMEUX | RemoveFromGameExplorerUsingMSI |
    | GameUXRemoveAsAdmin           | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue + msidbCustomActionTypeInScript + msidbCustomActionTypeNoImpersonate = 3137                                 | GAMEUX | RemoveFromGameExplorerUsingMSI |
    | GameUXRemoveAsCurUser         | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue + msidbCustomActionTypeInScript = 1089                                                                      | GAMEUX | RemoveFromGameExplorerUsingMSI |
    | GameUXRollBackRemoveAsAdmin   | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue + msidbCustomActionTypeRollback + msidbCustomActionTypeInScript + msidbCustomActionTypeNoImpersonate = 3393 | GAMEUX | AddToGameExplorerUsingMSI      |
    | GameUXRollBackRemoveAsCurUser | msidbCustomActionTypeDll + msidbCustomActionTypeBinaryData + msidbCustomActionTypeContinue + msidbCustomActionTypeRollback + msidbCustomActionTypeInScript = 1345                                      | GAMEUX | AddToGameExplorerUsingMSI      |

    

     

4.  Add the values shown for Action, Condition, and Sequence in the following table to the **InstallExecuteSequence** table in the MSI package.

    | Action                        | Condition                      | Sequence | Notes                                                                                                                                                                                            |
    |-------------------------------|--------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | GameUXSetMSIProperties        |                                | 1015     | The sequence number places the action soon after CostFinalize.                                                                                                                                   |
    | GameUXAddAsAdmin              | NOT Installed AND ALLUSERS     | 4003     | This custom action will only happen during a fresh installation for all users. The sequence number places the action after InstallFiles and after the rollbacks.                                 |
    | GameUXAddAsCurUser            | NOT Installed AND NOT ALLUSERS | 4004     | This custom action will only happen during a fresh installation for the current user only. The sequence number places the action after InstallFiles and after the rollbacks.                     |
    | GameUXRollBackAddAsAdmin      | NOT Installed AND ALLUSERS     | 4001     | This custom action will only happen when a fresh installation for all users is cancelled. The sequence number places the action after InstallFiles and before the Add custom action.             |
    | GameUXRollBackAddAsCurUser    | NOT Installed AND NOT ALLUSERS | 4002     | This custom action will only happen when a fresh installation for the current user only is cancelled. The sequence number places the action after InstallFiles and before the Add custom action. |
    | GameUXRemoveAsAdmin           | REMOVE~="ALL" AND ALLUSERS     | 3452     | This custom action will only happen during removal for all users. The sequence number places the action directly before RemoveFiles and after the rollbacks.                                     |
    | GameUXRemoveAsCurUser         | REMOVE~="ALL" AND NOT ALLUSERS | 3453     | This custom action will only happen during removal for the current user. The sequence number places the action directly before RemoveFiles and after the rollbacks.                              |
    | GameUXRollBackRemoveAsAdmin   | REMOVE~="ALL" AND ALLUSERS     | 3450     | This custom action will only happen when removal for all users is cancelled. The sequence number places the action directly before RemoveFiles and before the Remove custom action.              |
    | GameUXRollBackRemoveAsCurUser | REMOVE~="ALL" AND NOT ALLUSERS | 3451     | This custom action will only happen when removal for the current user is cancelled. The sequence number places the action directly before RemoveFiles and before the Remove custom action.       |

    

     

5.  Add the row shown in the following table to the Property table in the MSI package.

    | Property          | Value                                                         |
    |-------------------|---------------------------------------------------------------|
    | RelativePathToGDF | relative file path\\name of binary file that contains the GDF |

    

     

    > [!Note]  
    > The location specified by the path is relative to the location specified by the installation path. For example, bin\\GDF.dll.

     

6.  Save the MSI package.

For more detailed information about MSI packages and Windows Installer, see [Windows Installer](/windows/desktop/Msi/windows-installer-portal).

## Debugging Tips

The following are some tips to help debug issues when calling Games Explorer APIs:

### Test with sample code

Building the GameUXInstallHelper sample solution will create a GameUXInstallHelper.dll and a GDFInstall.exe. The GDFInstall.exe is a sample application that uses GameUXInstallHelper.dll. Running GDFInstall.exe will prompt if you want install or remove a GDF binary from game explorer. You can test your GDF binary file by passing it in as the first command line arg to GDFInstall.exe.

If you don't have a GDF binary or yours fails to install, try using the sample GDF in the DirectX SDK. The GDFExampleBinary sample is found in the DirectX SDK and is just a DLL that only contains a GDF file. Also included in the source is its GDFMaker project. You can build it and test it using GDFInstall.exe. You can also compare the its XML to yours to pinpoint exactly where the issue is.

### Make sure that your game was removed properly

If the game is already installed in Games Explorer, then subsequent calls to **IGameExplorer::AddGame** will return E\_FAIL so make sure your game isn't installed before testing. This also applies if you install the GDF for only the current user and then try to install the GDF for all users. You must first remove the game from the current users before **IGameExplorer::AddGame** will succeed.

If you run **GDFInstall.exe enum**, the sample application will enter a different mode which will enumerate all of the installed Games Explorer games and prompt you to remove them. You can also browse and search the registry in HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\GameUX to make sure that your game isn't installed for another user on the system. However, do not alter these registry settings for any other purpose, as they are not guaranteed to remain compatible in future versions of the operating system.

### Be sure to sign using Authenticode

If you have provided a rating, but are not seeing it in Games Explorer, make sure that you have used Authenticode to sign the executable or DLL file that contains the rating. Games Explorer ignores ratings information in unsigned files. For more information about Authenticode, see [Authenticode Signing for Game Developers](/windows/desktop/DxTechArts/authenticode-signing-for-game-developers).

### Be sure that parental controls are available

Ensure that you are testing parental controls on an edition of Windows Vista that provides parental controls: Home Basic, Home Premium, or Ultimate. Windows Vista Business and Windows Vista Enterprise do not provide parental controls however if you are testing on Windows Vista Ultimate, and the test computer is joined to a domain, you must change a group policy setting make parental controls visible. To do this, see [Getting Started with Games Explorer](/previous-versions/windows/desktop/legacy/ee417682(v=vs.85)).

### Verify that tasks are of the correct type

If you have specified support tasks that do not appear in Games Explorer, verify that they are all Web links. Any other shortcut tasks must be created as play tasks. Tasks are covered earlier in this article in [Games Explorer Tasks](#games-explorer-tasks).

### Verify the data in GDF binary

GDFTrace.exe is a tool found in the DirectX SDK. You can run GDFTrace.exe on your GDF binary and it will output all the GDF metadata contained in the binary for every supported language for quick validation. It also displays any warnings about missing or outdated information.

## Summary

Games Explorer in Windows Vista provides an easy, customizable way to present your game to users of Windows Vista, but it also requires you to register the game with the system during the installation process. The GameUXInstallHelper sample greatly simplifies this process for developers.

 

 