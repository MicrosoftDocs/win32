---
title: Games for Windows Test Cases Best Practices for Games on Windows XP, Windows Vista, Windows 7, and Windows 8
description: This article provides test cases for games for Windows.
ms.assetid: bbe84d3f-e7ff-f14f-ec25-ae1c980749fe
ms.topic: article
ms.date: 05/31/2018
---

# Games for Windows Test Cases: Best Practices for Games on Windows XP, Windows Vista, Windows 7, and Windows 8

This article provides test cases for games for Windows.

## How to Use This Article

There are three main sections to this article:

<dl> <dt>

<span id="Test_Requirements"></span><span id="test_requirements"></span><span id="TEST_REQUIREMENTS"></span>**Test Requirements**
</dt> <dd>

Each test requirement in this document has four main sections: a title and a table with three notable sections (left column, right top, right bottom).

<dl> <dt>

<span id="Title"></span><span id="title"></span><span id="TITLE"></span>Title
</dt> <dd>

Name of the test case.

</dd> <dt>

<span id="Box__far_left_column"></span><span id="box__far_left_column"></span><span id="BOX__FAR_LEFT_COLUMN"></span>Box, far left column
</dt> <dd>

Names of the operating systems to which the test case applies.

</dd> <dt>

<span id="Box__right_top"></span><span id="box__right_top"></span><span id="BOX__RIGHT_TOP"></span>Box, right top
</dt> <dd>

Brief summary of the test case.

</dd> <dt>

<span id="Box__right_bottom"></span><span id="box__right_bottom"></span><span id="BOX__RIGHT_BOTTOM"></span>Box, right bottom
</dt> <dd>

Details of the actual test case.

</dd> </dl> </dd> <dt>

<span id="Sample_Test_Script"></span><span id="sample_test_script"></span><span id="SAMPLE_TEST_SCRIPT"></span>**Sample Test Script**
</dt> <dd>

This section is a sample of the sequence that a typical test pass would follow if using the test requirements as a guide.

</dd> <dt>

<span id="Test_Tool_Notes"></span><span id="test_tool_notes"></span><span id="TEST_TOOL_NOTES"></span>**Test Tool Notes**
</dt> <dd>

This section contains detailed notes on each of the test tools used to verify pass or fail conditions in the test requirements.

</dd> </dl>

## Test Requirements

### 1. Game Requirements

### 1.1 Windows Games Explorer



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/></td>
<td>The game must be visible within the Games Explorer on Windows Vista and Windows 7. When selected, the game must also display correct metadata. The installation must not create a shortcut to launch the game on the desktop, in the Start menu, or in any other location. Tasks and shortcuts for removal must not be created.</td>
</tr>
<tr class="even">

<td><ol>
<li>After installing the game, open Games Explorer.</li>
<li>Verify that the game icon displays in Games Explorer.</li>
<li>Right-click the icon and test each application-defined play & support task.</li>
<li>Click the icon and verify that the metadata (publisher, developer, genre, release date, version) at the bottom displays and is correct.</li>
<li>Verify that the game icon displays Windows Experience Index (WEI) information in Games Explorer.</li>
<li>Verify that game hyperlinks for metadata work correctly in Games Explorer. (If hyperlinks don't show up, then this is a possible sign that the exe isn't signed; see <a href="#23-sign-files">section 2.3</a>.)</li>
<li>Verify that the game displays accurate parental control rating in Games Explorer. (If it says unrated, then verify that this is an unrated game; otherwise, this is an indicator that the exe isn't signed; see <a href="#23-sign-files">section 2.3</a>.)</li>
<li>Verify that the game does not place launch shortcuts on user desktop.</li>
<li>Click Start -> All Programs.</li>
<li>Verify that the game does not place launch shortcuts in the Start Menu.</li>
<li>Verify that the game does not place uninstall shortcuts in Start Menu outside of Control Panel.</li>
<li>If the game is distributed digitally, verify that the service provider appears in Windows Games Explorer.</li>
</ol>
<br/></td>
</tr>
</tbody>
</table>



 

### 1.2 Windows Family Safety / Parental Controls



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/></td>
<td>Game must execute within the context of a &quot;Standard User&quot;. Parental Controls must be able to block the game. Verify that the GDF has EXE names.</td>
</tr>
<tr class="even">

<td><ol>
<li>Create a Standard User account in Windows Vista or Windows 7 called Toby. Start -> Control Panel -> Add or Remove User Accounts -> Create New Account</li>
<li>As Jane, from Administrator account set up Parental Controls for the game. Start -> Control Panel -> Set Up Parental Controls for Any User -> Toby
<ol>
<li>Verify that the game launches from the Games Explorer icon.</li>
<li>Verify that the game displays accurate Parental Control Rating below the game title in the Parental Controls Control Panel.</li>
<li>Before applying Parental Controls, verify that the game does not prompt for Administrator Credentials on launch.</li>
<li>Set Parental Controls to &quot;On&quot;.</li>
<li>In the Windows Settings section, click Games.</li>
<li>Click OK (setting should now be &quot;AO / all games&quot;).</li>
<li>Verify that the game runs with these settings as User Jane.</li>
<li>Log off as Jane and log on as Toby.</li>
<li>Verify that the game runs with these settings as User Toby.</li>
<li>Log off as Toby and log on as Jane.</li>
<li>Go back to the previous screen and select &quot;Set Game Ratings&quot;.</li>
<li><p>Select a rating lower than the game's ESRB Rating.</p>
<blockquote>
[!Note]<br />
If the game is not rated, then skip this step and move onto the next part of this test. It may be necessary to choose a different rating system to find a game rating, depending on the language locale of the SKU being tested.
</blockquote>
<p><br/></p></li>
<li>Log off as Jane and log on as Toby.</li>
<li>Verify that the game does not launch for User Toby when ESRB is blocked by User Jane.</li>
<li>Log off as Toby and log on as Jane.</li>
<li>If changed previously, restore the ESRB settings.</li>
<li>If there are no ESRB settings, then select &quot;Block or Allow Specific Games&quot; and select the game by name.</li>
<li>Log off as Jane and log on as Toby.</li>
<li>Verify that the game does not launch for User Toby when EXE/Name is blocked by User Jane.</li>
<li>Log off as Toby and back on as Jane.</li>
<li>As Jane, open User Controls -> Application Restrictions.</li>
<li>Click &quot;Toby can only use the programs I allow&quot; and click OK (that is, allow no exes).</li>
<li>Go to User Controls | Games Controls and allow the specific game using the ESRB rating.</li>
<li>Log off as Jane, and log on as Toby and try to play the game.</li>
<li>Verify that the game is NOT blocked and that Toby can play it when &quot;allow no exes&quot; is set.</li>
</ol></li>
</ol>
<br/></td>
</tr>
</tbody>
</table>



 

### 1.3 Windows Vista Rich Saved Games

This requirement has been retired.

### 1.4 Xbox 360 Common Controller for Windows \[Conditional Requirement\]



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>Games that support gamepad controllers must support the Xbox 360 Controller for Windows using the XInput API. All references to common controller triggers and buttons must use the Xbox 360 names.</td>
</tr>
<tr class="even">

<td><ol>
<li>Launch the game.</li>
<li>Go into the controller options. **</li>
<li>Verify that the game recognizes Xbox 360 Controller for Windows as an input device.</li>
<li>Play the game and verify that the game and menu system are controllable with Xbox 360 Controller for Windows.</li>
<li>Verify that the Xbox 360 Controller for Windows behaves according to accepted standards. (B for back, A for accept, Start for in game menu/pause or accept, etc.)</li>
<li>Verify that the game refers to the controller buttons and triggers using Xbox 360 names.</li>
</ol>
<br/>
<blockquote>
[!Note]<br />
If the game does not support a game controller and/or only supports keyboard/mouse, then skip this test case.
</blockquote>
<br/> ** Settings for the controller might be located outside of the game. <br/></td>
</tr>
</tbody>
</table>



 

### 1.5 Multiple Aspect Ratios and Resolutions



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>The game must support at least the following aspect ratios and associated screen resolutions: <br/>
<ul>
<li>4:3 &quot;normal&quot; (800 600 or 1024 768)</li>
<li>16:9 &quot;widescreen&quot; (1280 720)</li>
<li>16:10 &quot;widescreen&quot; (1152 720, 1680 1050, or 800 480)</li>
</ul></td>
</tr>
<tr class="even">

<td>Locate the Video Options for the game (this may be in our out of game).<br/>
<blockquote>
[!Note]<br />
The following tests must be done on a widescreen monitor.
</blockquote>
<br/>
<ol>
<li>In the video resolution section, select 800 600 or 1024 768.</li>
<li>Verify that the game runs at a 4:3 Aspect Ratio resolution.</li>
<li>In the video resolution section, select 1280 720.</li>
<li>Verify that the game runs at a 16:9 Aspect Ratio resolution.</li>
<li>In the video resolution section, select 1680 1050, 800 480, or 1152 720.</li>
<li>Verify that the game runs at a 16:10 Aspect Ratio resolution.</li>
<li>Verify that the game does not stretch the picture and in turn presents a wider area of view.</li>
<li>Verify that the game prompts the user when a change is made to the resolution.</li>
<li>If the user does not accept within 15 seconds, verify that the display reverts to the previous setting.</li>
<li>Verify that the game does not add black bars to the left and right of the game play area. (In this case, you will see the game area still in a 4:3 ratio in the middle of the screen.)</li>
</ol>
<br/></td>
</tr>
</tbody>
</table>



 

### 1.6 Windows Media Center

This requirement has been retired.

### 1.7 Direct3D \[Conditional Requirement\]



| OS                                                                    | Requirement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows 7<br/> Windows Vista<br/> Windows XP<br/> | If the game uses Direct3D, the minimum version supported must be Direct3D 9, and Direct3D must be the default for any display configuration option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|     <dl> <dt><span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>Manual</dt> <dd> Launch the game. In the video options, check to see if there are render options, D3D and/or OpenGL. If there are, verify that the game render options default to Direct3D. If you are unable to verify that D3D9 is the version of DirectX that is being used, then proceed to Automated Test. <br/> </dd> <dt><span id="Automated_Test"></span><span id="automated_test"></span><span id="AUTOMATED_TEST"></span>Automated Test</dt> <dd> Use tool: Depends.exe <br/> </dd> </dl> |



 

### 1.8 Enable High-DPI Aware



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/></td>
<td>Games and their installers must run correctly without visual problems when DPI scaling is enabled.</td>
</tr>
<tr class="even">

<td><dl> <dt><span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>Manual</dt> <dd>
<ol>
<li>Set the system to DPI 150%: <br/> Windows Vista: Control Panel: Personalization, Adjust font size (DPI), Custom DPI. Set to 150%.<br/> Windows 7: Control Panel: Display, Set to Larger - 150%.<br/></li>
<li>Run the installation process and game to verify there are no problems with clipped screens or dialog boxes.</li>
</ol>
</dd> <dt><span id="Automated_Test"></span><span id="automated_test"></span><span id="AUTOMATED_TEST"></span>Automated Test</dt> <dd> Verify that element <dpiAware>true</dpiAware> is contained in the embedded manifest.<br/> Use tool: Mt.exe <br/> </dd> </dl></td>
</tr>
</tbody>
</table>



 

### 2. Security and Compatibility

### 2.1 Follow User Account Control Guidelines



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/></td>
<td>Every executable file (.EXE extension) included with an application must have an embedded manifest that defines its execution level:
<pre class="syntax" data-space="preserve"><code><requestedExecutionLevel level=&quot;asInvoker|highestAvailable|requireAdministrator&quot; 
              uiAccess=&quot;true|false&quot;/></code></pre>
<br/>
<blockquote>
[!Note]<br />
For games and game installers, uiAccess should always be set to &quot;false&quot;.
</blockquote>
<br/></td>
</tr>
<tr class="even">

<td><ol>
<li>Verify game executable files contain manifests.</li>
<li>Verify game executable file manifest requestedExecutionLevel is &quot;AsInvoker&quot;.</li>
</ol>
Use tool: Mt.exe <br/></td>
</tr>
</tbody>
</table>



 

### 2.2 Support x64 Versions of Windows



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/></td>
<td>To maintain compatibility with x64 versions of Windows: <br/>
<ul>
<li>Titles and title installers must not contain any 16-bit code or rely on any 16-bit component.</li>
<li>If the game is dependent on kernel-mode drivers for operation, x64 versions of these drivers must be available. The game setup must detect and install the proper drivers and components for 64-bit editions of Windows.</li>
</ul>
<blockquote>
[!Note]<br />
Support for the 64-bit Edition of Windows XP Professional is optional.
</blockquote>
<br/></td>
</tr>
<tr class="even">

<td>Manual Test<br/>
<ol>
<li>Run the game on 64-bit editions of Windows. Verify that the game installation process runs normally on 64-bit editions of Windows Vista or Windows 7.</li>
<li>Verify that the game does not encounter an error as a result of 16-bit executables on 64-bit editions of Windows Vista or Windows 7. The error will mention the 16-bit application in the error window.</li>
<li>If the game has a native 64-bit executable, then use that as well.</li>
</ol></td>
</tr>
</tbody>
</table>



 

### 2.3 Sign Files



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>All executable code files (for example, .exe and .dll extensions) must be signed with an Authenticode certificate. <br/> If you are using Windows Installer, the installer's package files (.msi files) must be signed. <br/></td>
</tr>
<tr class="even">

<td>Manual Test<br/>
<ol>
<li>Navigate to the game directory.</li>
<li>Locate all of the .exe and .dll files.</li>
<li>Right-click Properties on each file.</li>
<li>Verify that the game executable files contain a digital signature.</li>
</ol></td>
</tr>
</tbody>
</table>



 

### 2.4 Sign Drivers



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>Any kernel-mode driver that is installed by the game must be signed with a publicly valid Authenticode certificate. <br/> Any kernel-mode hardware device driver that is installed by the game must have a Microsoft signature obtained through the Windows Hardware Quality Labs (WHQL) or Driver Reliability Signature (DRS) program. <br/></td>
</tr>
<tr class="even">

<td>Manual Test<br/>
<ol>
<li>Install the game.</li>
<li>Verify that the game install process does not display unsigned driver dialog(s).</li>
</ol></td>
</tr>
</tbody>
</table>



 

### 2.5 Perform Version Checking Properly



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>Games must not fail to run on future operating systems as indicated by changes in the Windows version number, unless the End User License Agreement prohibits use on future operating systems. If the game is supposed to fail, it must do so gracefully by displaying a message to the user.</td>
</tr>
<tr class="even">

<td><dl> <dt><span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>Manual</dt> <dd>
<ol>
<li>Install the game on Windows XP, on 32-bit editions of Windows Vista and Windows 7, and on 64-bit editions of Windows Vista and Windows 7.</li>
<li>Verify that the game installation process does not encounter an error regarding OS version.</li>
</ol>
</dd> <dt><span id="Automated_Test"></span><span id="automated_test"></span><span id="AUTOMATED_TEST"></span>Automated Test</dt> <dd> Use tool: Application Verifier<br/>
<ol>
<li>Launch Application Verifier.</li>
<li>Enable the Compatibility:HighVersionLie test after selecting the INSTALL.EXE.</li>
<li>Install the game and ensure that it does not block installation based on the OS version.</li>
<li>Enable the Compatibility:HighVersionLie test after selecting the GAME.EXE.</li>
<li>Run the game and ensure it does not block execution based on the OS version.</li>
</ol>
</dd> </dl></td>
</tr>
</tbody>
</table>



 

### 2.6 Support Concurrent User Sessions



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>Games must support standard Windows multitasking scenarios.</td>
</tr>
<tr class="even">

<td>Create a Standard User account in Windows Vista or Windows 7 called Toby. Start -> Control Panel -> Add or Remove User Accounts -> Create New Account <br/>
<ol>
<li>Launch the game as User Jane.</li>
<li>ALT+TAB back to the desktop.</li>
<li>Verify that the game properly ALT+TABs to the Windows desktop.</li>
<li>Click Start -> [arrow to the right of Lock] -> Switch User.</li>
<li>Log on as User Toby.</li>
<li>Verify that the game launches as User Toby while still running as User Jane.</li>
<li>Verify that the game does not encounter errors for User Toby or User Jane during User Switch process.</li>
<li>If you can launch another game session, verify that you cannot hear audio from the original game session.</li>
<li>Close the game and switch back to the original user and game.</li>
</ol></td>
</tr>
</tbody>
</table>



 

### 2.7 Support Long Names



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>If a game supports saving files, it must be able to save files that have long names and paths. The game must properly handle special file system characters, such as \ / : * ? &quot; < or > in any user input fields used to create file names or paths.</td>
</tr>
<tr class="even">

<td><ol>
<li>Launch the game.</li>
<li>Start a new game.</li>
<li>Save the game. During the save process, verify that the game saves using the save name: My First Save Game.</li>
<li>Exit back to the main menu.</li>
<li>Attempt to load the newly saved game.</li>
<li>Verify that the game does not encounter errors when handling unsupported file system characters, such as \ / : * ? &quot; < or > If the game allows you, name the saved game.</li>
<li>If the user is allowed to name their profile and/or character or save games, verify that the game does not encounter errors when using long file names here as well.</li>
</ol></td>
</tr>
</tbody>
</table>



 

### 3. Installation

### 3.1 Easy Install



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>Games with a traditional installation must provide a simplified path in their setup user interface.</td>
</tr>
<tr class="even">

<td><ol>
<li>Insert the game disc.</li>
<li>Verify that the game does not display more than one End-User License Agreement (EULA).</li>
<li>If the game supports a custom or advanced installation option, verify that this option is accessible during the installation process.</li>
<li>Verify that the Default installation option bypasses all user input selections for the installation process (selection of installation folder, components selection, and so on).</li>
<li>Verify that the game installation process does not prompt for OS component setup (DirectX setup, Visual C Runtimes, and so on).</li>
<li>Verify that the game installation process does not prompt for firewall interaction.</li>
<li>Verify that the game automatically runs or that a launcher menu is present at the end of the install process.</li>
<li>Verify that the game uninstallation process removes all installed, non-redistributed OS component files and clears all settings. Cleaning up all per-user settings and data (such as saved games) is not required.</li>
</ol></td>
</tr>
</tbody>
</table>



 

### 3.2 Support User Account Control for Installation



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/></td>
<td>The game installer must not assume it is running in the same context as the user. Games must therefore perform per-user tasks on first-run separately from the installation.</td>
</tr>
<tr class="even">

<td><ol>
<li>Verify that you can install the game as User Jane. (This will require elevated rights during the setup/installation process.)</li>
<li>Verify that the game installation process prompts User Jane to elevate through Administrator Credentials. (The prompt to elevate will come up when the user attempts to install.)</li>
<li>Opt to Autorun the game at the end of installation, if it does not already do so, or launch it from the menu that appears.</li>
<li>Once in-game, create a new profile, play and save a game.</li>
<li>Exit the game.</li>
<li>Restart the game and verify that User Profiles and Saved Games can be accessed by the User Jane account.</li>
</ol></td>
</tr>
</tbody>
</table>



 

### 3.3 Install to Correct Folders



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>Games must be installed to the Program Files folder by default. User data must be written at first run and not during the installation.</td>
</tr>
<tr class="even">

<td><ol>
<li>Install the game using the Default install type.</li>
<li>Verify that the game was installed to Program Files.</li>
</ol>
<blockquote>
[!Note]<br />
If this test fails, verify that the game is intended to install for All Users. If so, this is a failure.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### 3.4 Install Windows Resources Properly



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>Applications must not attempt to install files or registry keys that are protected by Windows Resource Protection (WRP).</td>
</tr>
<tr class="even">

<td><ul>
<li>Verify that no Windows Resource Protection WRP dialog boxes appear during the installation process.</li>
</ul></td>
</tr>
</tbody>
</table>



 

### 3.5 Avoid Reboots During Installation



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>The game installer should not assume that installation of Windows components from redistribution packages requires a reboot, unless the reboot is indicated by a return result or by Microsoft documentation.</td>
</tr>
<tr class="even">

<td><ol>
<li>Install the game.</li>
<li>Verify that the game does not require the system to be rebooted after installation.</li>
</ol>
<blockquote>
[!Note]<br />
If a Microsoft system update REDIST requires a reboot, then do the following: Complete the game installation, uninstall the game, and reinstall the game a second time. The game installation process should not require a reboot on this second installation.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### 3.6 Use File Versioning Correctly



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>The game installation program must properly check to ensure that the latest file versions are installed. Installing a game must never regress any files that you do not produce or that are shared by applications that you do not produce.</td>
</tr>
<tr class="even">

<td><ol>
<li>Prior to installing the game, create a pre-install snapshot of System32.<br/>
<ol>
<li>Make a directory called G4Wtest.</li>
<li>Bring up a command Window (Start -> Run -> cmd).</li>
<li>Navigate to c:\windows\system32.</li>
<li>Type dir /o:-g /o:-d >> c:\G4Wtest\pregame.txt.</li>
</ol></li>
<li>Create a post-install snapshot of System32. <br/>
<ol>
<li>Bring up a command Window (Start -> Run -> cmd).</li>
<li>Navigate to c:\windows\system32.</li>
<li>Type dir /o:-g /o:-d >> c:\G4Wtest\postgame.txt.</li>
<li>Verify that the game does not regress any file versions of files that the game did not produce (...of the files listed in the two documents by comparing pregame.txt to postgame.txt).</li>
</ol></li>
</ol></td>
</tr>
</tbody>
</table>



 

### 3.7 Support Autorun \[Conditional Requirement\]



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>For games distributed on CD, DVD, or other removable media that support Autorun, when the disc is inserted for the first time, the application must automatically run or prompt the user to install the game. <br/>
<blockquote>
[!Note]<br />
Autorun programs that were written for use on versions of Windows prior to Windows Vista should not use the .NET runtime, because this technology is not included with Windows XP or older versions of Windows.
</blockquote>
<br/> For further guidance, please refer to <a href="/windows/win32/DxTechArts/games-for-windows-technical-requirements-1-1-0006">Games for Windows Technical Requirements</a> 3.7, Support Autorun. <br/></td>
</tr>
<tr class="even">

<td><ol>
<li>Insert the game disc or media.</li>
<li>Verify that the install / run dialog box comes up automatically.</li>
<li>Windows Vista or Windows 7: Verify that the game Autorun program itself does not prompt User Jane to elevate through Administrator Credentials.</li>
<li>Verify that the Autorun executable doesn't need out-of-box REDIST components, such as .NET 3.5, C Run-Time libraries, and so on.</li>
<li>Verify that re-inserting the disc in the drive after installation does not cause installation to automatically begin again.</li>
</ol></td>
</tr>
</tbody>
</table>



 

### 4. Reliability

### 4.1 Eliminate Unnecessary Reboots



| OS                                              | Requirement                                                                                                                                                                   |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows 7<br/> Windows Vista<br/> | All application installers must take advantage of the Restart Manager APIs to avoid system reboots (see [requirement 3.5](#35-avoid-reboots-during-installation)). |



 

### 4.2 Eliminate Application Verifier Failures



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>The game must generate no failures running under Microsoft Application Verifier (AppVerifier), version 4.0 or later, in the following tests: <br/>
<ul>
<li>Basics: Handles, Heaps, Locks, Memory, TLS</li>
<li>Miscellaneous: DangerousAPIs, DirtyStacks</li>
</ul></td>
</tr>
<tr class="even">

<td>Use Tool: AppVerifier 4.0 (or later)<br/>
<ol>
<li>Install AppVerifier.</li>
<li>Launch AppVerifier and select File -> Add Application.</li>
<li>Locate the game executable, select it, and click the &quot;Open&quot; button.</li>
<li>In the &quot;Applications&quot; section, select the game executable.</li>
<li>In the &quot;Tests&quot; section, select the tests listed above under the categories &quot;Basics&quot; and &quot;Miscellaneous&quot; (uncheck ThreadPool and TimeRollOver), and ensure all other tests are not selected.</li>
<li>Launch the game.</li>
<li>Verify that the game does not generate failures when run under Application Verifier.</li>
</ol>
<blockquote>
[!Note]<br />
Some tests require a debugger to be fully run. This may require an unprotected release version of the game executable, since anti-cheat/anti-piracy technology may interfere with AppVerifer.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

### 4.3 Support Windows Error Reporting



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>Games must handle only exceptions that are known and expected, and Windows Error Reporting must not be disabled. If a fault (such as an Access Violation) is injected into a game, it must allow Windows Error Reporting to report the crash.</td>
</tr>
<tr class="even">

<td>Use Tool: Thread Hijacker <br/>
<ul>
<li>If the application crashes while testing, verify that the game displays Windows Error Reporting properly and collects crash data.</li>
</ul></td>
</tr>
</tbody>
</table>



 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>All executable files (for example, .exe or .dll files) must contain an accurate Product Name, Company Name, and File Version.</td>
</tr>
<tr class="even">

<td><dl> <dt><span id="Manual_test_"></span><span id="manual_test_"></span><span id="MANUAL_TEST_"></span>Manual test:</dt> <dd>
<ol>
<li>Right-click the game's executable file(s) on both the installation media and those installed to the computer hard drive.</li>
<li>Select Properties.</li>
<li>Windows XP: Click the <strong>Version</strong> tab. Verify that the Product Name, Company Name, and File Version fields are properly populated.</li>
<li>Windows Vista or Windows 7: Click the <strong>Details</strong> tab. Verify that the Product name and File Version fields are properly populated. Company Name is not visible in the Windows Vista or Windows 7 properties page.</li>
</ol>
</dd> <dt><span id="Automated_test_"></span><span id="automated_test_"></span><span id="AUTOMATED_TEST_"></span>Automated test:</dt> <dd>
<ul>
<li>Use the Microsoft Games for Windows Test Tool; see <a href="#64-microsoft-games-for-windows-test-tool">section 6.4</a>.</li>
</ul>
</dd> </dl></td>
</tr>
</tbody>
</table>



 



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Windows 7<br/> Windows Vista<br/> Windows XP<br/></td>
<td>Normal exit of the game must not result in an unknown exception fault.</td>
</tr>
<tr class="even">

<td><ul>
<li>After playing the game for a normal gaming session, verify that the game does not generate errors on exit.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## 5. Sample Test Script

This is an example of a typical test pass using the preceding test requirements as a guide.

### 5.1 Tools

-   32-bit edition of Windows Vista SP1 and/or Windows 7 on an AMD CPU
-   32-bit edition of Windows Vista SP1 and/or Windows 7 on an Intel CPU
-   64-bit edition of Windows Vista SP1 and/or Windows 7 on an AMD CPU
-   64-bit edition of Windows Vista SP1 and/or Windows 7 on an Intel CPU
-   32-bit edition Windows XP SP2 on an AMD CPU
-   32-bit edition Windows XP SP2 on an Intel CPU
-   Wide Screen Monitor that supports 1680 1050
-   Xbox 360 Controller for Windows

### 5.2 Pre-Install

1.  Windows Vista and Windows 7: Create two Standard Users: Jane and Toby
2.  Windows Vista and Windows 7: Ensure User Account Control is enabled
3.  Create a pre-install snapshot of System32

    1.  Make a directory called G4Wtest
    2.  Bring up a command Window (Start -> Run -> cmd)
    3.  Navigate to c:\\windows\\system32
    4.  Type dir /o:-g /o:-d >> c:\\G4Wtest\\pregame.txt

4.  Windows Vista and Windows 7: Set to 150% DPI \[1.8\]
5.  Proceed to [Install](#3-installation)

### 5.3 Install

1.  Log on as User Jane
2.  Insert the game disc into the CD/DVD drive, verify that the install / run dialog box comes up automatically \[3.7\]
3.  Verify that the game installation process prompts User Jane to elevate Administrator Credentials \[3.2\]
4.  Verify that the game Autorun program itself does not prompt User Jane to elevate through Administrator Credentials \[3.7\]
5.  Verify that the game does not display more than one End-User License Agreement (EULA) \[3.1\]
6.  Verify that the game displays Default/Easy and Custom/Advanced installation options \[3.1\]
7.  Verify that the Default/Easy installation option bypasses all user input selections for the install process (selection of installation folder, components selection, and so on.) \[3.1\]
8.  Verify that the game installation process does not prompt for OS component setup (DirectX setup, C Run-Time libraries, and so on.) \[3.1\]
9.  Verify that the game installation process does not prompt for firewall interaction \[3.1\]
10. Verify that the game installation process does not encounter an error regarding OS Version \[2.5\] \[4.2\]
11. Verify that the game installation process does not display unsigned driver dialog(s) \[2.4\]
12. Verify that no Windows Resource Protection (WRP) dialogs appear during the install process \[3.4\]
13. Verify that re-inserting the disc in the drive after installation does not cause installation to automatically begin again
14. Verify that the game does not require the system to be rebooted after installation \[3.5\]
15. Verify that you can install the game as User Jane \[3.2\]
16. Verify that the game automatically runs or that a launcher menu is present at the end of the installation process \[3.1\]
17. If the game does auto-run after installation, skip to [Runtime](#55-runtime)
18. If the game left a launch menu up, or failed to uninstall see section [Post-Install](#54-post-install)

### 5.4 Post-Install

1.  Verify that the game does not place launch shortcuts on user desktop \[1.1\]
2.  Verify that the game does not place launch shortcuts in the Start Menu \[1.1\]
3.  Verify that the game icon displays in Windows Games Explorer \[1.1\]
4.  Verify that the metadata (publisher, developer, genre, release date, version) at the bottom displays and is correct \[1.1\]
5.  Verify that the game icon displays Windows Experience Index (WEI) information in Windows Games Explorer \[1.1\]
6.  Verify that game hyperlinks for metadata work correctly in Windows Games Explorer \[1.1\]
7.  Verify that the game displays accurate parental control rating in Windows Games Explorer \[1.1\]
8.  Create a post-install snapshot of System32

    1.  Bring up a command Window (Start -> Run -> cmd)
    2.  Navigate to c:\\windows\\system32
    3.  Type dir /o:-g /o:-d >> c:\\G4Wtest\\postgame.txt
    4.  Verify that the game does not regress any file versions of files listed in the two documents by comparing pregame.txt to postgame.txt \[3.6\]

9.  Proceed to [Runtime](#55-runtime)

### 5.5 Runtime

1.  RUNTIME 1: If the launch menu is present, launch the game from there. If the game auto-ran or was launched from the game launcher menu after install, perform the following; if not, skip to RUNTIME 2:

    1.  Create a profile (if the game allows)
    2.  Start a new game
    3.  Save the game
    4.  Exit the game
    5.  Launch the game from Games Explorer
    6.  Verify that the game launches from the Games Explorer icon \[1.2\]
    7.  Verify that the game does not prompt for Administrator Credentials on launch \[1.2\]
    8.  Verify that User Profiles and Save Games can be accessed by User Jane account \[3.2\]
    9.  Proceed to RUNTIME 3

2.  RUNTIME 2: If the game did not auto-run or display a launch from the game launcher menu, this is a failure of \[3.1\]; however, testing can continue normally:

    1.  Launch the game from Games Explorer
    2.  Verify that the game launches from the Games Explorer icon \[1.2\]
    3.  Verify that the game does not prompt for Administrator Credentials on launch \[1.2\]
    4.  Proceed to RUNTIME 3

3.  RUNTIME 3: If the game supports a game pad, verify that the game recognizes Xbox 360 Controller for Windows as an input device \[1.4\]

    1.  If needed, enable the controller via the options menu
    2.  Verify that the game refers to the controller buttons and triggers using Xbox 360 names
    3.  Verify that the game and menu system are controllable with the Xbox 360 Controller for Windows
    4.  Verify that the Xbox 360 Controller for Windows behaves according to accepted standards

4.  Set the video to \[1.5\]:

    1.  Verify that the game runs at a 4:3 Aspect Ratio resolution (800 600 or 1024 768)
    2.  Verify that the game runs at a 16:9 Aspect Ratio resolution (1280 720)
    3.  Verify that the game runs at a 16:10 Aspect Ratio resolution (1680 1050, 800 480, or 1152 720)
    4.  Verify that the game prompts the user when a change is made to the resolution
    5.  Verify that the display reverts to the previous setting if you do not accept within 15 seconds
    6.  Verify that the game does not stretch the picture and in turn presents a wider area of view
    7.  Verify that the game does not add black bars to the left and right of the game play area

5.  If available in the video settings, verify that the game render options default to Direct3D \[1.7\]; otherwise, proceed to [Automated Tests](#58-automated-tests)
6.  If prompted or if the option is available, create a user profile. Verify that the game does not encounter errors when using long file names \[2.7\]
7.  Start a new game, create a game save, and verify that the game does not encounter errors when handling unsupported file system characters \[2.7\]
8.  Verify that the game properly ALT+TABs to the Windows desktop \[2.6\]

    1.  Switch users with the game running by clicking Start -> Switch User
    2.  Log on as Toby
    3.  Verify that the game launches as User Toby while still running as User Jane \[2.6\]
    4.  Verify that the game does not encounter errors for User Toby or User Jane during User Switch process \[2.6\]
    5.  Verify that you cannot hear audio from the original game session \[2.6\]
    6.  Exit the game
    7.  Log off Toby
    8.  Switch back to the original user where the game is running
    9.  ALT+TAB back into the game

9.  Exit the game
10. Proceed to [Post-Runtime](#56-post-runtime)

### 5.6 Post-Runtime

1.  Verify that the game does not generate errors on exit \[4.3\]
2.  Verify that the game installed to Program Files \[3.3\]
3.  Proceed to [Parental Controls](/windows)

### 5.7 Parental Controls

1.  Open Parental Controls in Control Panel
2.  Verify that the game displays accurate Parental Control Rating below the game title in Parental Controls Control Panel \[1.2\]
3.  See Test Case \[1.2\] for the following tests:

    1.  After setting Parental Controls to "On", verify that the game runs with these settings as User Jane \[1.2\]
    2.  Log off and log on as Toby
    3.  Verify that the game runs with these settings as User Toby \[1.2\]
    4.  Log off and log on as Jane
    5.  In the Parental Control section, block User Toby from seeing games one ESRB level up and higher from the game that you just installed

        Example: If the game is rated E, set it so Toby can only play games that are rated C

    6.  Verify that the game runs with these settings as User Jane \[1.2\]
    7.  Log off and log on as user Toby
    8.  Verify that the game does not launch on User Toby when ESRB is blocked by User Jane \[1.2\]
    9.  Log off as user Toby and back on as user Jane
    10. If changed previously, restore the ESRB settings
    11. If there are no ESRB settings, then select "Block or Allow Specific Games" and select the game by name
    12. Log off as Jane and on as Toby
    13. Verify that the game does not launch on User Toby when EXE/Name is blocked by User Jane \[1.2\]
    14. Log off as Toby and back on as Jane
    15. As Jane, open User Controls -> Application Restrictions
    16. Click "Toby can only use the programs I allow", and then click OK (i.e. allow no exes)
    17. Click the Uncheck All box, and then click OK
    18. Go to User Controls \| Games Controls and allow the specific game using the ESRB rating
    19. Log off as Jane and log on as Toby and try to play the game
    20. Verify that the game is NOT blocked and that Toby can play it when "allow no exes" is set \[1.2\]
    21. Log off as user Toby and back on as user Jane
    22. Go to Parental Controls in Control Panel and remove the restrictions
    23. Verify that both users can now play the game

4.  Proceed to [Automated Tests](#58-automated-tests)

### 5.8 Automated Tests

1.  Verify that the game does not generate failures when run under Application Verifier - See Branding Test Tool Documentation \[4.2\]
2.  Verify that the game executable files contain manifests - see Branding Test Tool Documentation \[2.1\]
3.  Verify that the game executable file manifest requestedExecutionLevel is "AsInvoker" - see Branding Test Tool Documentation \[2.1\]
4.  Proceed to [Other Tests](#59-other-tests)

### 5.9 Other Tests

1.  Verify that the game executable files contain a digital signature \[2.3\]
2.  Verify that the game installation process runs normally on 64-bit editions of Windows Vista and/or Windows 7 \[2.3\]
3.  Verify that the game does not encounter an error as a result of 16-bit executables on 64-bit editions of Windows Vista and/or Windows 7 \[2.3\]
4.  Force the application to crash while testing, and verify that the game displays Windows Error Reporting properly and collects crash data \[4.3\]
5.  Ensure proper file summaries \[4.3\]

    1.  Click Start -> Computer
    2.  Navigate to the game directory
    3.  In the search window, type \*.dll
    4.  For each file: Right-click the file and click Properties

        -   In Windows XP: Click the Version tab. Verify that the Product Name, Company Name, and File Version fields are properly populated. \[4.3\]
        -   In Windows Vista and Windows 7: Click the Details tab. Verify that the Product name and File Version fields are properly populated. Company Name is not visible in the Windows Vista or Windows 7 properties page \[4.3\]

    5.  Repeat this check for .exe files

6.  Launch the game.

    1.  Press CTRL+ALT+DEL
    2.  Click the "Shutdown Options" arrow
    3.  Click Restart
    4.  Verify game does not block shutdown \[3.1\]

7.  Proceed to [Uninstall](#510-uninstall)

### 5.10 Uninstall

-   Verify that the game uninstallation process removes all installed, non-redistributed operating system component files and clears all settings \[3.1\]

    -   Verify in Windows Vista or Windows 7 that Control Panel is the only way to remove the program \[1.1\]

## Test Tool Notes

These are notes for each of the test tools listed in the above test requirements.

### 6.1 Appverifier 4.0 (or higher)

**Test Case: 2.5, 4.2**

> [!Note]  
> Some applications fail to run with AppVerifier running, because of copy protection. This can be resolved by running with an unprotected release version of the game executable.

 

1.  Install AppVerifier 4.0 (or higher) on a computer running Windows XP
2.  Launch AppVerifier and click File -> Add Application
3.  Locate the game executable, select it and click Open
4.  In the "Applications" section, select the game executable
5.  Select the following tests in the "Basics" section:

    -   Handles
    -   Heaps
    -   Locks
    -   Memory
    -   TLS

6.  Select the following tests in the "Miscellaneous" section:

    -   DangerousAPIs
    -   DirtyStacks

7.  Ensure all other tests are not selected
8.  Launch the game
9.  Play the game
10. Close the game
11. In AppVerifier select View -> Logs
12. In the "Applications" section select the app .exe file
13. In the "Logs" section, select the log file and observe the error count. If there are no errors, then end AppVerifier tests. If there are errors, click the View button
14. Search the document (CTRL+F) for Severity="Error
15. Create bugs based on the LayerName= portion of the failure

### 6.2 Manifest Test - mt.exe

**Test Case: 1.8, 2.1**

This tool is run from a command prompt where MT.exe is located.

Example:

``` syntax
mt.exe -inputresource:"c:\yourdir\YourGame.exe";#1 -out:yourgame.manifest
```

1.  Click Start -> Run -> type cmd and click the OK button
2.  Run the mt.exe tool to generate a .manifest file for each .exe file that installs with the game
3.  Open the generated .manifest file
4.  Ensure that each .exe file contains the following (requested:

    ``` syntax
    <description>Example Game Name</description>
    <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
      <security>
        <requestedPrivileges>
          <requestedExecutionLevel level="asInvoker"></requestedExecutionLevel>
        </requestedPrivileges>
      </security>
    </trustInfo>
      <asmv3:windowsSettings xmlns=http://schemas.microsoft.com/SMI/2005/WindowsSettings>
        <dpiAware>true<dpiAware>
      </asmv3:windowsSettings>
    </asmv3:application>
    ```

> [!Note]  
> Requested execution level should be present for every file, and dpiAware should be present for at least the game s executable file.

 

### 6.3 Thread Hijacker - threadhijacker.exe

This tool is run from a command prompt where threadhijacker.exe is located.

Example:

``` syntax
threadhijacker.exe /process:str
```

Where str is the name\_of\_program.exe

1.  Bring up Task Manager, click the Processes tab, and locate the name of the game executable.
2.  Open a command prompt in Admin mode
3.  Navigate to the directory where threadhijacker.exe is
4.  Type: **threadhijacker.exe /process:**str, where str is the name of the executable that you want to hit

### 6.4 Microsoft Games for Windows Test Tool

This tool is located in the DirectX SDK. Once the SDK is installed on a computer, the installer for the Games for Windows Test Tool can be placed on the test computer and installed.

Locate the Microsoft Games for Windows Test Tool installer on the development computer where the DirectX SDK is installed. By default, it is placed in the following location:

``` syntax
%SystemDrive%\Program Files (x86)\Microsoft DirectX SDK (Date)\Utilities\bin\x86\Microsoft Games for Windows Test Tools\
```

1.  Copy the installer (MicrosoftGFWTestTool.msi / setup.exe) to the test computer.
2.  Run the installer.
3.  Launch the Microsoft Games for Windows Test Tool.
4.  In the **Project List** field replace **Create New Project** with your title name and click **Create New**.

    Wait for the Baseline to complete.

5.  Fill in any information that you may have in the **Game Information** section, and click **Update Game Information**.
6.  Click on **Test Cases** tab.
7.  Starting at the top, proceed through the test cases, clicking **Pass** or **Fail** as appropriate.

    See "Writing a Bug", later in this section, for details on including a bug in the report.

8.  Return to the **Projects** tab after reviewing the report (by checking the **Report** and **Bug Edit** tabs).
9.  Click **Compile Report**.

    A window will open when the report is finished compiling. Here you will find a .ZIP file names *ProjectName*\_report.zip. This file contains all of the logs and results collected during the test pass.

### Writing a Bug

There are two ways to write a bug report: you can go through the test cases and click **Fail** when the title fails a test case, or you can click the **Bug Edit** tab and manually add a bug report.

### Clicking Fail on a test case

1.  When you click **Fail** on a test case, the **Issue Type** drop-down list will automatically be set to the test case type.
2.  Add a short description to the **Title** field that briefly describes the issue.
3.  Add a detailed description of the issue to the **Observed Behavior** field.
4.  As appropriate, add what was expected (as opposed to a description of the issue) to the **Expected Behavior** field.
5.  Add a detailed description of how to reproduce the issue to the **Repro-Steps** field.
6.  When done, click the **Save** button.

### Manually Adding a Bug

This process is the same as clicking **Fail**, with the exception of the auto-populated drop-down list. In this case, either select the appropriate TCR failure type or select **\*\* Non-TR Issue \*\*** for bugs that fall outside of the TR range but should still be reported.

## Resources

<dl> <dt>

<span id="Games_for_Windows__Technical_Requirements"></span><span id="games_for_windows__technical_requirements"></span><span id="GAMES_FOR_WINDOWS__TECHNICAL_REQUIREMENTS"></span>Games for Windows: Technical Requirements
</dt> <dd>

[Games for Windows Technical Requirements: Best Practices for Games on Windows XP, Windows Vista, and Windows 7](./games-for-windows-technical-requirements-1-1-0006.md)

</dd> <dt>

<span id="Windows_SDK"></span><span id="windows_sdk"></span><span id="WINDOWS_SDK"></span>Windows SDK
</dt> <dd>

[Windows SDKs](https://msdn.microsoft.com/bb980924.aspx)

</dd> <dt>

<span id="User_Account_Control_Guidelines"></span><span id="user_account_control_guidelines"></span><span id="USER_ACCOUNT_CONTROL_GUIDELINES"></span>User Account Control Guidelines
</dt> <dd>

[Windows Vista Application Development Requirements for User Account Control Compatibility](/previous-versions/dotnet/articles/bb530410(v=msdn.10))

</dd> <dt>

<span id="Windows_Installer_Information"></span><span id="windows_installer_information"></span><span id="WINDOWS_INSTALLER_INFORMATION"></span>Windows Installer Information
</dt> <dd>

[Windows Installer](../msi/windows-installer-portal.md)

</dd> <dt>

<span id="WinQual_Developer_Portal__"></span><span id="winqual_developer_portal__"></span><span id="WINQUAL_DEVELOPER_PORTAL__"></span>WinQual Developer Portal 
</dt> <dd>

[Windows Quality Online Services (Winqual)](/windows-hardware/drivers/dashboard/winqual-submission-tool--winqualexe-)

</dd> <dt>

<span id="DirectX_Developer_Portal"></span><span id="directx_developer_portal"></span><span id="DIRECTX_DEVELOPER_PORTAL"></span>DirectX Developer Portal
</dt> <dd>

[DirectX Developer Center](/previous-versions/windows/apps/hh452744(v=win.10))

</dd> <dt>

<span id="Games_for_Windows_and_DirectX_SDK_Blog"></span><span id="games_for_windows_and_directx_sdk_blog"></span><span id="GAMES_FOR_WINDOWS_AND_DIRECTX_SDK_BLOG"></span>Games for Windows and DirectX SDK Blog
</dt> <dd>

[Games for Windows and the DirectX SDK](https://walbourn.github.io/)

</dd> <dt>

<span id="Additional_DirectX_Articles"></span><span id="additional_directx_articles"></span><span id="ADDITIONAL_DIRECTX_ARTICLES"></span>Additional DirectX Articles
</dt> <dd>

[DirectX Technical Articles](./dx9-technical-articles.md)

</dd> </dl>

 

