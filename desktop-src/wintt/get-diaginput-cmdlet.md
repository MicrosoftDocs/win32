---
title: Get-DiagInput Cmdlet
description: Displays interactions that get information from or provide information to the user.
ms.assetid: ef4f25ca-9cce-4159-9359-a0b7d338bec0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get-DiagInput Cmdlet

Displays interactions that get information from or provide information to the user.

## Syntax

``` syntax
Get-DiagInput [-Id] <String> [[-Parameter] <Collections.Hashtable>] [[-Choice] <Collections.Hashtable[]>]
```

## Detailed Description

Specify an interaction from the manifest to display to the user. If the interaction requires parameter values or dynamic values, specify those values, too. You use this cmdlet only if the RequiresInteractivity node in the manifest is set to true.

An interaction can be of the following types:

-   Single-response interaction that displays a list of choices from which the user can select one choice.
-   Multiple-response interaction that displays a list of choices from which the user can select many choices.
-   Text input interaction that displays a single-line or multiline text box into which the user enters text.
-   Pause interaction that displays information or instructions to the user. The interaction then waits for the user to respond before returning.
-   Launch UI interaction that displays a related application to launch.

## Parameters

### -Id *String*

An identifier that identifies the interaction in the troubleshooting pack's manifest to display. The identifier is case insensitive.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | true  |
| Position?                   | 0     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | None  |



 

### -Parameter *Collections.Hashtable*

A hash table of key/value pairs that define the parameters used by the interaction. Each key in the hash table must be unique and must match a parameter declared by the Parameters or ContextParameters nodes of the interaction. The key name is case insensitive. You must include parameters that do not specify a default parameter value in the interaction; parameters that include a default value are optional.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | 1     |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | p     |



 

### -Choice *Collections.Hashtable\[\]*

An array of hash tables that specify the dynamic values for a single-response or multiple-response interaction that are added to static values that were defined in the manifest.

Each hash table in the array specifies a single choice. The hash table must contain the following key/value pairs:

-   Name The value for this key is the display name for the choice. The name should be localized.
-   Value The value for this key is the value to return if the user selects this choice.
-   Description The value for this key is a description of the choice. The description is shown as a tooltip in MSDT when the user hovers over the choice.
-   ExtensionPoint An XML string that contains one or more extension points that the client supports.

You must specify a value for the Name and Value key/value pairs; however, the value for the Description and ExtensionPoint key/value pairs are optional. The key names are case insensitive.

Specify this parameter only if the single-response or multiple-response interaction sets the AllowDynamicResponses node to true.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | 2     |
| Default value               | None  |
| Accept pipeline input?      | true  |
| Accept wildcard characters? | false |
| Alias                       | c     |



 

## Input and Return Types

The input type is the type of the objects that you can pipe to the cmdlet. The return type is the type of the objects that the cmdlet emits.

| Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input type  | Collections.Hashtable\[\]For single-response and multiple-response interactions, you can pipe an array of hash tables that contain the dynamic choices to add to the list of static choices defined by the interaction. See the Choice parameter.<br/>                                                                                                                                                                                                                              |
| Return type | String\[\]A array of strings. For single-response interactions, the array contains a single item that contains the selected choice. For multiple-response interactions, the array can contain multiple items that contain the selected choices. For text interactions, the array contains a single item that contains the input text. For launch UI interactions, the array contains a single item that contains "Run" or "NotRun". There is no output for pause interactions.<br/> |



 

## Examples

The following examples show how to use the cmdlet.

### Example 1

The following example shows how to display the NetworkDown interaction to the user.

**PS:&gt;Get-DiagInput -Id "NetworkDown"**

### Example 2

The following example shows how to pass a parameter value to the NetworkDown interaction.

**PS:&gt;Get-DiagInput -Id "NetworkDown" -Parameter @{"param"="value"}**

### Example 3

The following example shows how to pass a list of choices to the MultipleResponse interaction and receive the response.

**$input = Get-DiagInput -Id "MultipleResponse" -Choice @{"Name"="Choice1"; "Value"="Value that Choice1 returns"}**

 

 





