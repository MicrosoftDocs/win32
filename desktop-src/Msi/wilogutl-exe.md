---
description: Wilogutl.exe assists the analysis of log files from a Windows Installer installation, and it displays suggested solutions to errors that are found in a log file.
ms.assetid: 09aa03ba-992f-47ab-999b-ebdfe85c1ea7
title: Wilogutl.exe
ms.topic: article
ms.date: 05/31/2018
---

# Wilogutl.exe

Wilogutl.exe assists the analysis of log files from a Windows Installer installation, and it displays suggested solutions to errors that are found in a log file.

Non-critical errors are not displayed. Wilogutl.exe can be run in quiet mode or with a user interface (UI). The tool generates reports as text files in both the UI and quiet modes. It works best with verbose Windows Installer log files, but also works with non-verbose logs. For more information, see [Logging](logging.md).

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Syntax

**wilogutl.exe** *\[<options>\]\[<source file>\]\[<options>\]\[<report file directory>\]*

You can use the following command lines to run in quiet mode.

**wilogutl /q /l** *c:\\mymsilog.log* **/o** *c\\outputdir\\*

**wilogutl /q /l** *c:\\mymsilog.log*

## Command-Line Options

Wilogutl.exe uses the following case insensitive command-line options. A dash delimiter can be used in place of a slash.



| Option | Description                                                                                                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| none   | Runs in UI mode—without command-line options.                                                                                                                                                   |
| /q     | Specifies the quiet mode. Wilogutl.exe generates report files and does not display a user interface.                                                                                            |
| /l     | Specifies the name of the log file to be analyzed. This option is required when using the quiet mode.                                                                                           |
| /o     | Specifies the output directory for report files. This output path is used only when running in quiet mode. If the option is not present, the reports are put in the C:\\WiLogResults directory. |



 

When run in UI mode, Wilogutl.exe displays the following dialog boxes.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Windows Installer Verbose Log Analyzer</td>
<td>The Windows Installer Verbose Log Analyzer dialog box enables users to select a log file for analysis:
<ul>
<li>The <strong>Open</strong> button opens the file in Notepad. The preview area can be used to verify that the correct log file has been selected.</li>
<li>The <strong>Analyze</strong> button begins log file analysis and displays the Detailed Log File View dialog box.</li>
</ul></td>
</tr>
<tr class="even">
<td>Detailed Log File View</td>
<td>The Detailed Log File View dialog box displays logged error information. Use the <strong>Back</strong> and <strong>Next</strong> buttons to navigate through multiple errors. To display non-critical errors select the <strong>Show Ignored Debug Errors</strong> check box. The installer version on the computer used to run the logged installation is displayed. If the logged installation was run with elevated permissions, the <strong>Elevated install</strong> check box is selected and information is provided in the <strong>Client Side Privilege Details</strong> and <strong>Server Side Privilege Details</strong> text boxes. The Detailed Log File View dialog box contains the following buttons:<br/>
<ul>
<li><strong>States</strong> - Show the Feature and Component States dialog box.</li>
<li><strong>Properties</strong> - Show the Properties dialog box.</li>
<li><strong>Policies</strong> - Show the Policies dialog box.</li>
<li><strong>HTML Annotated Log</strong> - Show log as annotated HTML file.</li>
<li><strong>Save Results</strong> - Save report files to specified directory.</li>
<li><strong>Error Message Help</strong> - Show installer error message help.</li>
<li><strong>Help</strong> - Show help for Windows Installer Setup Log Analyzer.</li>
<li><strong>How to Read a Log File</strong> - Show the log file help document.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Feature and Component States</td>
<td>The <strong>Feature and Component States</strong> dialog box displays the states of features and components:
<ul>
<li>The <strong>Feature</strong> column shows the name for the feature in the installation package.</li>
<li>The <strong>Component</strong> column shows the name of the component in the installation package.</li>
<li>The <strong>Installed</strong> column shows the feature or component's state at the end of the installation.</li>
<li>The <strong>Request</strong> column shows the user's selection during the installation for the feature or component's state.</li>
<li>The <strong>Action</strong> column shows the action taken by the installer for the feature or component.</li>
</ul>
For more information, see <a href="/windows/desktop/api/Msiquery/nf-msiquery-msigetcomponentstatea"><strong>MsiGetComponentState</strong></a> and <a href="/windows/desktop/api/Msiquery/nf-msiquery-msigetfeaturestatea"><strong>MsiGetFeatureState</strong></a>.<br/></td>
</tr>
<tr class="even">
<td>Properties</td>
<td>The Properties dialog box shows Windows Installer <a href="properties.md">Properties</a> and their values at the end of the installation. You can sort the properties by name or by value:
<ul>
<li>The <strong>Client</strong> tab shows properties and values during the client side portion of the installation.</li>
<li>The <strong>Server</strong> tab shows properties and values during the server portion of the installation.</li>
<li>The <strong>Nested</strong> tab shows the properties and values of any <a href="concurrent-installations.md">Concurrent Installations</a>.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Policies</td>
<td>The Policies dialog box displays the <a href="system-policy.md">System Policy</a> set after the installation:
<ul>
<li>A value of 0 (zero) set for the policy means the policy is not enabled.</li>
<li>A value of 1 (one) means the policy is enabled.</li>
<li>A value of ? (question mark) means the policy value is not recorded in the log.</li>
</ul>
If you need a policy value that is not in the log, try using Regedit.exe to check the registry keys on the computer failing the installation.<br/></td>
</tr>
</tbody>
</table>



 

## Report Files

When performing a quiet mode analysis or clicking the **Save Results** button on the **Detailed Log File View** dialog, the Windows Installer Setup Analyzer tool generates three text files and an HTML annotated log file.

The following table identifies the names and contents in the report files.



| Name                      | Description                                                                                                                    |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| logfilename\_summary.txt  | Summarizes the log file. Lists the information displayed by the Detailed Log File View dialog box and the first error.         |
| logfilename\_errors.txt   | Identifies the number of errors, the errors, and recommended solutions. This file lists both critical and non-critical errors. |
| logfilename\_policies.txt | Identifies the policy names and values set at the end of the installation as in the Policies dialog box.                       |
| details\_logfilename.htm  | An HTML annotated log with a legend for the color coding.                                                                      |



 

## Return Values

If invalid command-line arguments are passed for quiet mode operations, Wilogutl.exe does nothing, and the process returns one of the values in the following table.



| Value | Meaning                                                                 |
|-------|-------------------------------------------------------------------------|
| 1     | Bad output directory is specified.                                      |
| 2     | Bad log file name is specified.                                         |
| 3     | Passed /q, but is missing the required switch /l for the log file name. |
| 4     | Passed /l, but is missing the required switch /q for quiet mode.        |



 

## Related topics

<dl> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> </dl>

 

 




