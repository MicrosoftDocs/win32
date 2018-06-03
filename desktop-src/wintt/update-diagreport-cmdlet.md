---
title: Update-DiagReport Cmdlet
description: Adds a custom section to the troubleshooting report.
ms.assetid: ec10b88c-cfb1-460a-aa84-df1ec6d88fb2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Update-DiagReport Cmdlet

Adds a custom section to the troubleshooting report.

## Syntax

``` syntax
Update-DiagReport [-Xml] <XmlDocument> [-Id] <String> [-Name] <String> 
[[-Description] <String>] [[-Verbosity] <String>] [[RootcauseId] <String> [RootcauseInstanceId] <String>]

Update-DiagReport [-File] <String> [-Id] <String> [-Name] <String> 
[[-Description] <String>] [[-Verbosity] <String>] [[RootcauseId] <String> [RootcauseInstanceId] <String>]
```

## Detailed Description

The Update-DiagReport cmdlet adds a custom section to the troubleshooting report that support professionals or administrators can use to further troubleshoot a problem.

## Parameters

### -Xml *XmlDocument*

An XmlDocument object that contains the information to add to the custom section of the report. To ensure that the XML is valid, use ConvertTo-Xml to encode the object as an XML document.

Note that this parameter and the File parameter are mutually exclusive.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | true  |
| Position?                   | 0     |
| Default value               | None  |
| Accept pipeline input?      | true  |
| Accept wildcard characters? | false |
| Alias                       | x     |



 

### -File *String*

The name of the file that contains the additional information for this section of the report. The report will contain a link to the file. Specify an absolute, relative, or UNC path to the file. The path is relative to the working directory of the Windows PowerShell runspace. The user must have read permissions to the file.

The file is copied to the result folder if you also specify the Result parameter.

Note that this parameter and the Xml parameter are mutually exclusive.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | true  |
| Position?                   | 0     |
| Default value               | None  |
| Accept pipeline input?      | true  |
| Accept wildcard characters? | false |
| Alias                       | f     |



 

### -Id *String*

A string identifier used to identify this custom section of the report. The identifier is not localized. The identifier is used as a secondary sort after Verbosity for ordering content in the report.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | true  |
| Position?                   | 1     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | None  |



 

### -Name *String*

The localized name to use as the title for the section of the report that you are adding.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | true  |
| Position?                   | 2     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | n     |



 

### -Description *String*

A localized description that describes this section of the report. The description is shown in the report after the contents of the Name parameter.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | 3     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | d     |



 

### -Verbosity *String*

Determines the level of detail to include in the report when an error occurs. The possible values are:

-   Informational
-   Warning
-   Error
-   Debug

The default is Informational (most verbose). For Informational, Warning, and Error, the information is displayed in the client and written to the ResultReport.xml file. For Debug, the information is written to the DebugReport.xml file.

This parameter also determines the icon to associate with the custom section that you adding and the order in which the section is displayed relative to any other custom sections. The sort order is Error, Warning, and Informational. If you add multiple custom sections with the same verbosity value (for example, Error), the Id parameter value is used as a secondary sort to sort the custom sections.



| Attribute                   | Value         |
|-----------------------------|---------------|
| Required?                   | false         |
| Position?                   | 4             |
| Default value               | Informational |
| Accept pipeline input?      | false         |
| Accept wildcard characters? | false         |
| Alias                       | v             |



 

### -RootcauseId *String*

The identifier of the root cause to which you want to add the information; the information is included with the root cause in the Issues Found section of the report. If you do not specify an identifier, the information is included in the Detection Details section of the report.

If you use root cause instances, use the RootcauseInstanceId parameter to specify the instance to which you want to add the additional information.

You can use this parameter only in the troubleshooting phase. If you use the same script for troubleshooting and verification, the call is ignored in the verification phase. You cannot use this parameter if Verbosity is set to Debug.

Use this parameter only if status has been or will be reported using the [Update-DiagRootCause](update-diagrootcause-cmdlet.md) cmdlet; you cannot use this parameter for root causes that do not have a status.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | named |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | rid   |



 

### -RootcauseInstanceId *String*

The identifier of an instance of the root cause to which you want to add the information; the information is included with the root cause instance in the Issues Found section of the report. If you do not specify an identifier, the information is included in the Detection Details section of the report.

Use this parameter only if you specify the RootcauseId parameter.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | named |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | riid  |



 

## Input and Return Types

The input type is the type of the objects that you can pipe to the cmdlet. The return type is the type of the objects that the cmdlet emits.

| Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input type  | System.Xml.XmlDocument or System.StringThe input type depends on whether you are using the Xml parameter or the File parameter. If you are using the Xml parameter, specify an XmlDocument object that contains the information to add to the report. If you are using the File parameter, specify a String object that contains the path to the file that contains the additional information.<br/> |
| Return type | None                                                                                                                                                                                                                                                                                                                                                                                                       |



 

## Notes

Each time a troubleshooting pack is executed, information generated by the troubleshooting, resolution, and verification phases is collected and compiled into a report; the report also contains information about the computer. This information can be useful to an advanced user who is trying to understand what is happening in the system and what troubleshooting steps to try next.

By default, the report contains the following information:

-   The name, description, and version of the troubleshooting pack
-   The publisher of the pack
-   The root causes that the pack looks for and whether they were found or not found
-   The resolvers that are used to fix the root causes, and whether they were run or did not run
-   Information about the computer

You can use this cmdlet to add additional information to the report that may help the user resolve the issue.

The section of the report to which the details are added depends on the troubleshooting phase from which you are calling the Update-DiagReport cmdlet. For example, if you are calling this cmdlet from the troubleshooting phase, the details are added to the Detection Details section of the report unless you include the -RootcauseId parameter, in which case the details are included with the root cause in the Issues Found section of the report. If you are calling this cmdlet from the resolver phase, the details are included with the resolution in the Issues Found section of the report. The information from the verification phase is added only if the Verbosity parameter is set to Debug (and is added only to the DebugReport).

Information that you add to the troubleshooting section typically provides additional information about why you think there is or is not a problem. Information that you add to the resolution section typically describes the changes that were made to fix the problem.

You can include the additional information directly in the report or you can include a link in the report that points the user to a file that contains the additional information. To include the information directly in the report, use the Xml parameter. To specify a link to a file that contains the additional information, use the File parameter. The Xml and File parameters are mutually exclusive. As an option to specifying them as parameters, you can pipe them to this cmdlet.

If you specify an XML object, the XML must be wellformed. To ensure that the XML is wellformed, use the ConvertTo-Xml cmdlet to encode the object as an XML document. You would then pipe the result to Update-DiagReport (for example, $obj \| ConvertTo-Xml \| Update-DiagReport). However, the report does not render all XML objects. To ensure that your XML renders, use the following mechanisms:

-   `Get-Event | ConvertTo-Xml | Update-DiagReport`
-   `<string> | ConvertTo-Xml | Update-DiagReport`
-   `$obj | Select-Object -Property @{Name=<localizedpropertyname>;Expression={$_.OldPropertyName}} | ConvertTo-Xml | Update-DiagReport`

## Examples

The following examples show how to use the cmdlet.

### Example 1

The following example shows how to add additional information to the report using the pipeline. In this case, an array of file name strings are added to the report. The example pipes an array of file name strings to ConvertTo-Xml to encode the strings as a valid XmlDocument object. The XmlDocument object is then piped to the Update-DiagReport cmdlet (instead of using the Xml parameter).

**PS:&gt;$deletedFiles \| ConvertTo-Xml \| Update-DiagReport -Id "Deleted\_Files" -Name "Deleted Files"**

### Example 2

The following example shows how to add to the report a link to a file that contains the additional information.

**PS:&gt;Update-DiagReport -File "SampleFile.ext"  Id "Sample\_File" -Name "Sample File"**

### Example 3

The following example shows how to add additional information to the report using the pipeline. In this case, an array of file name strings are added to the report. This example shows how to add additional information to the report using the Xml parameter. In this case, the Xml parameter is set to a variable that contains a valid XmlDocument object.

**PS:&gt;Update-DiagReport -Xml $events  Id "Application\_Events" -Name "Application Event Log" -Description "All application events with ID 100."**

 

 





