---
title: Write-DiagProgress Cmdlet
description: Writes a progress string to the troubleshooting client.
ms.assetid: a674d2b4-9d67-46cd-9136-3e6e8bb2f7dd
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Write-DiagProgress Cmdlet

Writes a progress string to the troubleshooting client.

## Syntax

``` syntax
Write-DiagProgress [-Activity] <String> [[-Status] <String>]
```

## Detailed Description

The progress strings are in the form of an activity string that describes the activity being performed and an optional status string that describes the status of that activity (for example, if the activity is copying files, the status might be the current file being copied).

Typically, you should use this cmdlet if the activity takes more than one second to complete.

## Parameters

### -Activity *String*

A localized string that describes the activity that the script is performing (for example, Initializing or Copying files). Activity strings should describe long-running operations.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | true  |
| Position?                   | 0     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | a     |



 

### -Status *String*

A localized string that describes the current status of the activity defined by the Activity parameter (for example, if the activity is copying files, the status could be the name of the file being copied). Status strings should be used to update the status of a long running activity.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | 1     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | s     |



 

## Input and Return Types

The input type is the type of the objects that you can pipe to the cmdlet. The return type is the type of the objects that the cmdlet emits.

| Type        | Description |
|-------------|-------------|
| Input type  | None        |
| Return type | None        |



 

## Examples

The following examples show how to use the cmdlet.

### Example 1

The following example shows how to specify the current activity being performed by the script.

**PS:&gt;Write-DiagProgress -Activity "Checking network connectivity"**

### Example 2

The following example shows how to specify the status of the current activity being performed by the script.

**PS:&gt;Write-DiagProgress -Activity "Checking network connectivity" -Status "Contacting Microsoft.com"**

 

 




