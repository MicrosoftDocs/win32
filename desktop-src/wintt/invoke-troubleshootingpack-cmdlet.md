---
title: Invoke-TroubleshootingPack Cmdlet
description: Runs a troubleshooting pack from a Windows Powershell window in interactive or unattended mode.
ms.assetid: 07707830-67d2-4ff0-a70e-e9e16dc74c12
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Invoke-TroubleshootingPack Cmdlet

Runs a troubleshooting pack from a Windows Powershell window in interactive or unattended mode.

## Syntax

``` syntax
Invoke-TroubleshootingPack [-Pack] <TroubleshootingPack> 
[[-AnswerFile] <String>] [[-Unattended]] [[-Result] <String>]
```

## Detailed Description

A troubleshooting pack determines the root cause of issues found with the computer, resolves the issues, and verifies that the issues were resolved. You can request that the cmdlet save reports that detail the issues that were found and their resolutions.

In interactive mode, the user can select the resolvers to run. In unattended mode, the resolvers that run are determined at run time. If the pack includes interactions that ask questions, the user will need to provide answers to the questions, or you will need to specify an answer file that contains the answers to the questions. For details on how to generate an answer file for a troubleshooting pack, see the [Get-TroubleshootingPack](get-troubleshootingpack-cmdlet.md) cmdlet.

You can save the result report, debug report, XSL, and any linked files that you specify to a specified folder. Both reports contain the issues that were found and their resolutions; however, the debug report contains additional information that can be useful in debugging issues with the troubleshooting pack.

## Parameters

### -DiagPack *Pack*

The troubleshooting pack to run. To get the DiagPack object, call the [Get-TroubleshootingPack](get-troubleshootingpack-cmdlet.md) cmdlet.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | true  |
| Position?                   | 0     |
| Default value               | None  |
| Accept pipeline input?      | true  |
| Accept wildcard characters? | false |
| Alias                       | p     |



 

### -AnswerFile *String*

The name of the answer file that you created using the [Get-TroubleshootingPack](get-troubleshootingpack-cmdlet.md) cmdlet. The answer file provides answers to the questions that the troubleshooting pack may ask. For details on creating an answer file, see the Get-TroubleshootingPack cmdlet.

If you run the troubleshooting pack in unattended mode and the pack asks questions that require answers, you should specify an answer file. If the answer file does not contain the answer to a question, Invoke-TroubleshootingPack will return an error to the script; the script can continue to execute or it can stop.

Typically, you do not use an answer file in interactive mode but sometimes it is useful for administrators to provide answers and just have the users pick the resolvers.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | named |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | ad    |



 

### -Unattended

Directs the Invoke-TroubleshootingPack cmdlet to run the troubleshooting pack in unattended mode. By default, the troubleshooting pack runs interactively. If the troubleshooting pack asks questions that require a response, you should also specify an answer file (see the *AnswerFile* parameter).

In unattended mode, the resolvers run in the order they occur in the manifest. The resolver runs only if it does not run manually, does not require elevated privileges (or requires elevated privileges and you are running as an administrator), and the status of the root cause is not Fixed or Detected.

To determine whether the root cause runs manually, access the RootCause.Manual property (for example, $pack.RootCauses\[0\].Manual). To determine whether the resolution requires elevated privileges, access the Resolution.RequiresElevation property (for example, $pack.RootCauses\[0\].Resolutions\[0\].RequiresElevation). To determine whether the root cause is fixed, access the RootCause.Status property (for example, $pack.RootCauses\[0\].Status).



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | named |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | u     |



 

### -Result *String*

The path to where the results are written. The results include the following files:

-   ResultsReport.xml
-   DebugReport.xml
-   Results.xsl
-   Any linked files that you include using the Update-DiagReport cmdlet

The path may be an absolute, relative, or UNC path. The cmdlet creates the path if it does not exist. If the folder contains the files, the cmdlet overwrites the files. If you do not specify this parameter, the Invoke-TroubleshootingPack cmdlet does not save the results.

If a failure occurs, the results and debug reports contain the results up to the point of the failure.

The Results.xsl applies only to the ResultsReport.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | named |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | r     |



 

## Input and Return Types

The input type is the type of the objects that you can pipe to the cmdlet. The return type is the type of the objects that the cmdlet emits.

| Type        | Description                                                                                                                                          |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input type  | Microsoft.Windows.Diagnosis.DiagPackThe troubleshooting pack to run. To get the DiagPack object, call the Get-TroubleshootingPack cmdlet.<br/> |
| Return type | None                                                                                                                                                 |



 

## Examples

The following examples show how to use the cmdlet.

### Example 1

The following example shows how to run the specified pack in interactive mode. The example uses the Get-TroubleshootingPack cmdlet to get the DiagPack object and pipes it to the Invoke-TroubleshootingPack cmdlet. The troubleshooting pack runs interactively and does not save the result files.

**PS:&gt;Get-TroubleshootingPack -Path C:\\Windows\\Diagnostics\\System\\Aero \| Invoke-TroubleshootingPack**

### Example 2

The following example shows how to run the specified pack in interactive mode and save the results to the specified folder. The example uses the Get-TroubleshootingPack cmdlet to get the DiagPack object and assign it to a variable. The variable is then used with the Pack parameter to specify the troubleshooting pack to run. The troubleshooting pack runs interactively and saves the result files to the specified folder.

**PS:&gt;$aero = Get-TroubleshootingPack C:\\Windows\\Diagnostics\\System\\Aero**

**PS:&gt;Invoke-TroubleshootingPack -Pack $aero -Result C:\\DiagResult**

### Example 3

The following example shows how to run the specified pack in unattended mode using an answer file. The example uses the Get-TroubleshootingPack cmdlet to get the DiagPack object and assign it to a variable. The variable is then used with the Pack parameter to specify the troubleshooting pack to run. The troubleshooting pack runs in attended mode and does not save the result files.

**PS:&gt;$aero = Get-TroubleshootingPack C:\\Windows\\Diagnostics\\System\\Aero -Answer AeroAnswerFile.xml**

**PS:&gt;Invoke-TroubleshootingPack -Pack $aero -Answer AeroAnswerFile.xml -Unattended**

 

 





