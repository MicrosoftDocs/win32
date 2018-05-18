---
title: Update-DiagRootCause Cmdlet
description: Reports the status of a root cause.
ms.assetid: '04b6b5bd-c6fd-41f1-baff-59402f0e58ec'
---

# Update-DiagRootCause Cmdlet

Reports the status of a root cause.

## Syntax

``` syntax
Update-DiagRootcause [-Id] <String> [-InstanceId] <String> [-Detected] <Boolean> [-Parameter] <Collections.Hashtable>]
```

## Detailed Description

The Update-DiagRootCause cmdlet reports the status of a root cause (indicates whether a root cause exists on a computer).

You can call this cmdlet from a troubleshooting script and verification script but not from a resolution script.

## Parameters

### -Id *String*

The identifier of the root cause whose status you want to update. The identifier is case-sensitive and must match the ID of a root cause declared in the troubleshooting manifest.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | true  |
| Position?                   | 0     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | id    |



 

### -InstanceId *String*

A unique string identifier that identifies a specific instance of the root cause.

You would use an instance identifier to identify instances of a generic root cause. For example, if the root cause discovers issues with devices, one instance may identify issues with a printer device and the second instance may identify issues with a scanner device. If the text for the root cause was: "Your %device% device is broken.", you could then call this cmdlet as follows:

-   **Update-DiagRootCause -Id "Device" -InstanceId "Printer" -Parameter @{"device"="Printer"}**
-   **Update-DiagRootCause -Id "Device" -InstanceId "Scanner" -Parameter @{"device"="Scanner"}**



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | 1     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | id    |



 

### -Detected *Boolean*

Determines whether the root cause exists on the computer. Set to $true, if the root cause exists on the computer; otherwise, $false.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | true  |
| Position?                   | 2     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | None  |



 

### -Parameter *Collections.Hashtable*

A hash table of key/value pairs that define the parameters used by the root cause or its children nodes. Each key in the hash table must be unique and must match a parameter declared by nodes of the root cause. The key name is case-sensitive. You must include parameters that do not specify a default parameter value in the root cause; parameters that include a default value are optional.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | 3     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | p     |



 

## Input and Return Types

The input type is the type of the objects that you can pipe to the cmdlet. The return type is the type of the objects that the cmdlet emits.

| Type        | Description |
|-------------|-------------|
| Input type  | None        |
| Return type | None        |



 

## Examples

The following examples show how to use the cmdlet.

### Example 1

The following example shows how to update the status of the MyRootCause root cause. The affect that the Detected parameter has on the status depends on the current value of its status. For example, if the current status is Not Checked, setting Detected to true changes the status to Detected.

**PS:&gt;Update-DiagRootCause -Id "MyRootCause" -Detected $true**

### Example 2

The following example shows how to pass parameter values to the root cause.

**PS:&gt;Update-DiagRootCause -Id "MyRootCause" -Detected $false -Parameter @{"Param1"="ParamValue"}**

 

 




