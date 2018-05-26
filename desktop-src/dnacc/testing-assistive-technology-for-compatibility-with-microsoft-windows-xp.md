---
Description: Microsoft Accessible Technology Group
ms.assetid: 3fe69954-e2a2-4ac1-85d6-50bcc3a204db
title: Testing Assistive Technology for Compatibility with Microsoft Windows XP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Testing Assistive Technology for Compatibility with Microsoft Windows XP

Microsoft Accessible Technology Group

April 2002

**Summary:** This article prioritizes areas of the Microsoft Windows XP interface that can be tested to ensure compatibility between assistive technologies and Windows XP. (7 printed pages)

-   [How to Test](#how-to-test)
    -   [Tools that Aid Testing](#tools-that-aid-testing)
-   [What to Test](#what-to-test)
    -   [Testing Control Panel](#testing-control-panel)
    -   [Testing the Programs in Accessories](#testing-the-programs-in-accessories)
    -   [Testing Other User Interface Areas Besides Control Panel and Accessories](#testing-other-user-interface-areas-besides-control-panel-and-accessories)
    -   [Testing Internet Explorer](#testing-internet-explorer)

## How to Test

To ensure compatibility between your assistive technology and Microsoft Windows XP, you need to confirm that assistive technology can work with the Windows XP user interface. To make such testing easier, the Microsoft Accessible Technology Group has prioritized the most important user interface features, as shown in the following table.



| Feature                                                                                                                                                                                                                                                                            | Priority |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| Features that are new or have a new user interface in Windows XP<br/> - and -<br/> Features that contain known software bugs in Microsoft Windows 2000.<br/> - and -<br/> Features that work fully in Windows 2000 but might not in Windows XP.<br/> | P1       |
| Features that both work fully in Windows 2000 and are accessed frequently by users of assistive technology.                                                                                                                                                                        | P2       |
| Features that work fully in Windows 2000 but are accessed infrequently by users of assistive technology.                                                                                                                                                                           | P3       |



 

At a minimum, test the user interface of each feature at its first and second levels. For example, in Control Panel, test all buttons and tabs in the **Display Properties** dialog box, and also test any dialog boxes that appear when you click a button in the **Display Properties** dialog box. You can test any dialog box that appears when you click the second level of buttons.

### Tools that Aid Testing

Use the following tools to test your assistive technology:

-   Accessibility Event Watcher (AccEvent) to monitor how your assistive technology supports WinEvents.
-   Inspect Object (Inspect) to monitor how your assistive technology supports Microsoft Active Accessibility (MSAA) objects.
-   Narrator to compare the functionality of your screen reader to that of Narrator, which comes with Windows XP.
-   Magnifier to compare the functionality of your screen magnifier to that of Magnifier, which comes with Windows XP.

You can get AccEvent and Inspect from the [Microsoft Windows SDK Update for Windows 7 and .NET Framework 4](http://go.microsoft.com/fwlink/p/?linkid=208210). To download just the tools, select only **Tools** from the **Installation Options** page of the Windows SDK setup wizard.

## What to Test

The most important areas of the Windows XP user interface to be tested include:

-   [Control Panel](#testing-control-panel).
-   [Accessories](#testing-the-programs-in-accessories).
-   [Other](#testing-other-user-interface-areas-besides-control-panel-and-accessories) user interface areas besides Control Panel and Accessories.
-   [Microsoft Internet Explorer](#testing-internet-explorer).

The following sections prioritize items within these test areas.

### Testing Control Panel



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Control Panel Category</th>
<th>User Interface Task</th>
<th>Priority</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Appearance and Themes</td>
<td><ul>
<li>Change the computer theme.</li>
<li>Change the screen resolution.</li>
<li>View <strong>Taskbar and Start Menu</strong> dialog box. Change to <strong>Classic Start</strong> menu. Add folders and files.</li>
<li>Show most recently used documents.</li>
<li>View <strong>Folder Options</strong> dialog box.</li>
<li>View <strong>Display</strong> dialog box.</li>
</ul></td>
<td>P1</td>
</tr>
<tr class="even">
<td>Network and Internet Connections</td>
<td>Set up a network and Internet connection using your assistive technology.</td>
<td>P2</td>
</tr>
<tr class="odd">
<td>Sounds, Speech and Audio Devices</td>
<td>Change voice speed.</td>
<td>P2</td>
</tr>
<tr class="even">
<td>Accessibility Options</td>
<td>Select <strong>High Contrast</strong>.</td>
<td>P1</td>
</tr>
<tr class="odd">
<td>Add or Remove Programs</td>
<td><ul>
<li>Add a program from <strong>Add New Programs</strong>.</li>
<li>Add a Windows component.</li>
<li>Remove a program.</li>
</ul></td>
<td>P1</td>
</tr>
<tr class="even">
<td>Printers and Other Hardware</td>
<td>Add a printer.</td>
<td>P2</td>
</tr>
<tr class="odd">
<td>Performance and Maintenance</td>
<td><ul>
<li>In the <strong>Administrative Tools</strong> folder, view <strong>Computer Management</strong>.</li>
<li>In the <strong>System</strong> folder, turn off automatic updating.</li>
</ul></td>
<td>P1</td>
</tr>
<tr class="even">
<td>User Accounts</td>
<td>Test the user interface at its first and second levels.</td>
<td>P1</td>
</tr>
<tr class="odd">
<td>Date, Time, Language, and Regional Options</td>
<td>Test the user interface at its first and second levels.</td>
<td>P3</td>
</tr>
<tr class="even">
<td>Other Control Panel Options</td>
<td>Test the user interface at its first and second levels.</td>
<td>P3</td>
</tr>
</tbody>
</table>



 

### Testing the Programs in Accessories

Confirm that your assistive technology works with the programs in the **Accessories** folder. The following table lists the programs to test.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Accessories Program</th>
<th>Priority</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Accessibility
<ul>
<li>Accessibility Wizard</li>
<li>Utility Manager</li>
<li>Magnifier</li>
<li>Narrator</li>
</ul></td>
<td>P1<br/> P1<br/> P1<br/> P1<br/></td>
</tr>
<tr class="even">
<td>Communications
<ul>
<li>Microsoft NetMeeting</li>
</ul></td>
<td>P2<br/></td>
</tr>
<tr class="odd">
<td>Entertainment
<ul>
<li>CD Player</li>
<li>Volume Control</li>
<li>Microsoft Windows Media Player</li>
</ul></td>
<td>P2<br/> P2<br/> P2<br/></td>
</tr>
<tr class="even">
<td>System Tools
<ul>
<li>Disk Defragmenter</li>
<li>Disk Cleanup</li>
<li>Getting Started</li>
<li>System Information</li>
<li>System Restore</li>
</ul></td>
<td>P2<br/> P2<br/> P2<br/> P2<br/> P1<br/></td>
</tr>
<tr class="odd">
<td>Calculator</td>
<td>P1</td>
</tr>
<tr class="even">
<td>Command Prompt Console</td>
<td>P1</td>
</tr>
<tr class="odd">
<td>Notepad</td>
<td>P2</td>
</tr>
<tr class="even">
<td>Synchronize</td>
<td>P2</td>
</tr>
<tr class="odd">
<td>WordPad (tooltip functionality only)</td>
<td>P1</td>
</tr>
</tbody>
</table>



 

### Testing Other User Interface Areas Besides Control Panel and Accessories

The following table lists areas of the user interface other than Control Panel and Accessories. Perform the user interface tasks to confirm that your assistive technology works with Windows XP.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>User Interface Area</th>
<th>User Interface Task</th>
<th>Priority</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Start Menu and Submenus</td>
<td><ul>
<li>Use Windows Classic Start Menu.</li>
<li>Use Windows XP Start Menu.</li>
</ul></td>
<td>P1</td>
</tr>
<tr class="even">
<td>Turn Off Computer</td>
<td>Turn off computer.</td>
<td>P1</td>
</tr>
<tr class="odd">
<td>Log Off Dialog Box</td>
<td><ul>
<li>Change user.</li>
<li>Clear Fast-User Switching check box.</li>
</ul></td>
<td>P1</td>
</tr>
<tr class="even">
<td>Explorer</td>
<td><ul>
<li>Change views (Thumbnails, Tiles, Icons, List, Details).</li>
<li>Use Film Strip view (in My Picture).</li>
<li>View My Computer.</li>
<li>View Recycle Bin.</li>
<li>View My Documents.</li>
</ul></td>
<td>P1<br/> P1<br/> P2<br/> P2<br/> P2<br/></td>
</tr>
<tr class="odd">
<td>My Network Place</td>
<td>Test the user interface at its first and second levels.</td>
<td>P2</td>
</tr>
<tr class="even">
<td>Help and Support Center</td>
<td>Test the user interface at its first and second levels.</td>
<td>P1</td>
</tr>
<tr class="odd">
<td>Run in Compatibility Mode</td>
<td>Test all features.</td>
<td>P1</td>
</tr>
<tr class="even">
<td>Desktop</td>
<td>Create shortcut on desktop.</td>
<td>P2</td>
</tr>
<tr class="odd">
<td>Quick Launch, Applications Tray, and System Tray</td>
<td><ul>
<li>Tab from <strong>Start</strong> menu for two cycles. Notice tab order.</li>
<li>Add application icons to Quick Launch until the <strong>More</strong> button appears. Use the keyboard to test the <strong>More</strong> button.</li>
<li>Make the <strong>More</strong> button appear in the System Tray. (In the <strong>Taskbar and Start Menu Properties</strong> dialog box, click <strong>Hide Inactive Icons</strong>.) Use the keyboard to browse items in the System Tray.</li>
</ul></td>
<td>P1</td>
</tr>
<tr class="even">
<td>Search</td>
<td><ul>
<li>Search a file.</li>
<li>Search a computer.</li>
<li>Search a website.</li>
</ul></td>
<td>P2<br/> P3<br/> P2<br/></td>
</tr>
<tr class="odd">
<td>Run</td>
<td><ul>
<li>Choose from the list box.</li>
<li>Launch an application, and test whether it is properly exposed.</li>
<li>Run Regedit.</li>
<li>Run Winver.</li>
<li>Run MMC.</li>
<li>Access a network share.</li>
</ul></td>
<td>P1<br/> P2<br/> P3<br/> P3<br/> P1<br/> P2<br/></td>
</tr>
<tr class="even">
<td>Startup</td>
<td>Make sure all applications are accessible within the folder.</td>
<td>P3</td>
</tr>
</tbody>
</table>



 

### Testing Internet Explorer

The following table lists features related to Internet Explorer. Perform the user interface tasks to confirm that your assistive technology works with Windows XP.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Internet Explorer Feature</th>
<th>User Interface Task</th>
<th>Priority</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Microsoft Internet Connection Wizard</td>
<td><ul>
<li>Establish a dial-up connection.</li>
<li>Establish a LAN connection.</li>
</ul></td>
<td>P1</td>
</tr>
<tr class="even">
<td>Microsoft Internet Explorer Browser</td>
<td><ul>
<li>Make sure that links work.</li>
<li>Add to favorites, and organize favorites.</li>
<li>Save a webpage.</li>
<li>Tab quickly through all the links on a page.</li>
<li>Start Explorer from Quick Launch toolbar.</li>
<li>Access a URL using the <strong>Run</strong> command.</li>
<li>Make sure DHTML does not break MSAA objects.</li>
<li>Access embedded objects.</li>
<li>Access the Tree Control.</li>
<li>Access the Menu band.</li>
<li>Make sure that image maps work. (An <em>image map</em> consists of links behind different parts of an image.)</li>
</ul></td>
<td>P1</td>
</tr>
<tr class="odd">
<td>Internet Options</td>
<td>From the <strong>Accessibility</strong> tab, test the user interface at its first and second levels.</td>
<td>P1</td>
</tr>
<tr class="even">
<td>Microsoft Outlook Express</td>
<td>Test the user interface at its first and second levels.</td>
<td>P2</td>
</tr>
<tr class="odd">
<td>Windows Updates</td>
<td>Test the user interface at its first and second levels.</td>
<td>P3</td>
</tr>
<tr class="even">
<td>Microsoft MSN Explorer</td>
<td>Test the user interface at its first and second levels.</td>
<td>P1</td>
</tr>
<tr class="odd">
<td>Address Book</td>
<td>Test the user interface at its first and second levels.</td>
<td>P2</td>
</tr>
<tr class="even">
<td>MSN Messenger Service</td>
<td>Test the user interface at its first and second levels.</td>
<td>P1</td>
</tr>
<tr class="odd">
<td>MSN Search</td>
<td>Test the user interface at its first and second levels.</td>
<td>P2</td>
</tr>
</tbody>
</table>



 

 

 




