---
description: The executable program that interprets packages and installs products is Msiexec.exe.Note  Msiexec also sets an error level on return that corresponds to System Error Codes. The following table identifies the standard command-line options for this program. Command-line options are case insensitive.Windows Installer 2.0:  The command-line options that are identified in this topic are available beginning with Windows Installer 3.0. The Windows Installer Command-Line Options are available with Windows Installer&\#160;3.0 and earlier versions.
ms.assetid: b1707c88-1cca-45ab-bb23-6002bfd5204e
title: Standard Installer Command-Line Options
ms.topic: article
ms.date: 05/31/2018
---

# Standard Installer Command-Line Options

The executable program that interprets packages and installs products is Msiexec.exe.

> [!Note]  
> Msiexec also sets an error level on return that corresponds to [System Error Codes](../debug/system-error-codes.md).

 

The following table identifies the standard command-line options for this program. Command-line options are case insensitive.

**Windows Installer 2.0:** The command-line options that are identified in this topic are available beginning with Windows Installer 3.0. The Windows Installer [Command-Line Options](command-line-options.md) are available with Windows Installer 3.0 and earlier versions.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Option</th>
<th>Parameters</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>/help</strong></td>
<td> </td>
<td>Help and quick reference option. Displays the correct usage of the setup command including a list of all switches and behavior. The description of usage can be displayed in the user interface. Incorrect use of any option invokes this help option.<br/> Example: <strong>msiexec /help</strong><br/>
<blockquote>
[!Note]<br />
The equivalent Windows Installer <a href="command-line-options.md">Command-Line Option</a> is <strong>/?</strong>.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><strong>/quiet</strong></td>
<td> </td>
<td>Quiet display option. The installer runs an installation without displaying a user interface. No prompts, messages, or dialog boxes are displayed to the user. The user cannot cancel the installation. Use the <strong>/norestart</strong> or <strong>/forcerestart</strong> standard command-line options to control reboots. If no reboot options are specified, the installer restarts the computer whenever necessary without displaying any prompt or warning to the user.<br/> Examples: <br/> <strong>msiexec /package Application.msi /quiet</strong><br/> <strong>Msiexec /uninstall Application.msi /quiet</strong><br/> <strong>Msiexec /update msipatch.msp /quiet</strong><br/> <strong>Msiexec /uninstall msipatch.msp /package Application.msi / quiet</strong><br/>
<blockquote>
[!Note]<br />
The equivalent Windows Installer <a href="command-line-options.md">Command-Line Option</a> is <strong>/qn</strong>.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><strong>/passive</strong></td>
<td> </td>
<td>Passive display option. The installer displays a progress bar to the user that indicates that an installation is in progress but no prompts or error messages are displayed to the user. The user cannot cancel the installation. Use the <strong>/norestart</strong> or <strong>/forcerestart</strong> standard command-line options to control reboots. If no reboot option is specified, the installer restarts the computer whenever necessary without displaying any prompt or warning to the user. <br/> Example: <strong>msiexec /package Application.msi /passive</strong> <br/>
<blockquote>
[!Note]<br />
The equivalent Windows Installer <a href="command-line-options.md">Command-Line Option</a> is <strong>/qb!-</strong> with <a href="rebootprompt.md"><strong>REBOOTPROMPT</strong></a>=S set on the command line.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><strong>/norestart</strong></td>
<td> </td>
<td>Never restart option. The installer never restarts the computer after the installation.<br/> Example: msiexec /package Application.msi <strong>/norestart</strong><br/>
<blockquote>
[!Note]<br />
The equivalent Windows Installer command line has <a href="reboot.md"><strong>REBOOT</strong></a>=ReallySuppress set on the command line.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><strong>/forcerestart</strong></td>
<td> </td>
<td>Always restart option. The installer always restarts the computer after every installation.<br/> Example: msiexec /package Application.msi <strong>/forcerestart</strong><br/>
<blockquote>
[!Note]<br />
The equivalent Windows Installer command line has <a href="reboot.md"><strong>REBOOT</strong></a>=Force set on the command line.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><strong>/promptrestart</strong></td>
<td> </td>
<td>Prompt before restarting option. Displays a message that a restart is required to complete the installation and asks the user whether to restart the system now. This option cannot be used together with the <strong>/quiet</strong> option.<br/>
<blockquote>
[!Note]<br />
The equivalent Windows Installer command line has <a href="rebootprompt.md"><strong>REBOOTPROMPT</strong></a> = &quot;&quot; set on the command line.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><strong>/uninstall</strong></td>
<td><em><Package.msi|ProductCode></em></td>
<td>Uninstall product option. Uninstalls a product.<br/>
<blockquote>
[!Note]<br />
The equivalent Windows Installer <a href="command-line-options.md">Command-Line Option</a> is <strong>/x</strong>.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><strong>/uninstall</strong></td>
<td><em>/package <Package.msi | ProductCode> /uninstall <Update1.msp | PatchGUID1>[;Update2.msp | PatchGUID2]</em></td>
<td>Uninstall update option. Uninstalls an update patch.<br/>
<blockquote>
[!Note]<br />
The equivalent Windows Installer <a href="command-line-options.md">Command-Line Option</a> is <strong>/I</strong> with <a href="msipatchremove.md"><strong>MSIPATCHREMOVE</strong></a>=Update1.msp | PatchGUID1[;Update2.msp | PatchGUID2] set on the command line.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><strong>/log</strong></td>
<td><em><logfile></em></td>
<td>Log option. Writes logging information into a log file at the specified existing path. The path to the log file location must already exist. The installer does not create the directory structure for the logfile.<br/> The following information is entered into the log:<br/>
<ul>
<li>Status messages</li>
<li>Nonfatal warnings</li>
<li>All error messages</li>
<li>Start up of actions</li>
<li>Action-specific records</li>
<li>User requests</li>
<li>Initial UI parameters</li>
<li>Out-of-memory or fatal exit information</li>
<li>Out-of-disk-space messages</li>
<li>Terminal properties</li>
</ul>
<blockquote>
[!Note]<br />
The equivalent Windows Installer <a href="command-line-options.md">Command-Line Option</a> is <strong>/L*</strong>.
</blockquote>
<br/>
<blockquote>
[!Note]<br />
For more information about all the methods that are available for setting the logging mode, see <a href="normal-logging.md">Normal Logging</a> in the <a href="windows-installer-logging.md">Windows Installer Logging</a> section.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><strong>/package</strong></td>
<td><em><Package.msi|ProductCode></em></td>
<td>Install product option. Installs or configures a product.<br/>
<blockquote>
[!Note]<br />
The equivalent Windows Installer <a href="command-line-options.md">Command-Line Option</a> is <strong>/I</strong>.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><strong>/update</strong></td>
<td><em><Update1.msp>[;Update2.msp]</em></td>
<td>Install patches option. Installs one or multiple patches. <br/>
<blockquote>
[!Note]<br />
The equivalent Windows Installer command line has <a href="patch.md"><strong>PATCH</strong></a> = [msipatch.msp]<;PatchGuid2> set on the command line.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 
