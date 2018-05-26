---
title: Get-TroubleshootingPack Cmdlet
description: Gets information about a troubleshooting pack and can be used to generate an answer file.
ms.assetid: d8b273d0-e679-46b0-adca-4492f29907a6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Get-TroubleshootingPack Cmdlet

Gets information about a troubleshooting pack and can be used to generate an answer file.

## Syntax


```PowerShell
Get-TroubleshootingPack [-Path] <String> [[-AnswerFile] <String>]
```



## Detailed Description

Typically, use this cmdlet to:

-   Discover information about a troubleshooting pack.
-   Generate an answer file.
-   Get a DiagPack object that you pass to Invoke-TroubleshootingPack.

If you do not know the purpose of a troubleshooting pack, call this cmdlet to discover information about the troubleshooting pack. For example, you can discover the root causes that it can find, the resolvers used to resolve the root causes, and any questions that require a response from the user during the troubleshooting, resolution, or verification phases. You can also discover who the publisher is before you decide to run it.

If the troubleshooting pack asks for user input and if you plan to run the pack in unattended mode, you will need to provide an answer file. You use this cmdlet to generate the answer file that you then pass to the [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlet.

To run a troubleshooting pack, you must call this cmdlet to get the DiagPack object that you then pass to the [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlet.

## Parameters

### -Path *String*

The path to the folder that contains the troubleshooting pack to get. The path may be an absolute, relative, or UNC path.

You can specify this parameter or you can pipe the path to Get-TroubleshootingPack.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | true  |
| Position?                   | 0     |
| Default value               | None  |
| Accept pipeline input?      | true  |
| Accept wildcard characters? | false |
| Alias                       | p     |



 

### -AnswerFile *String*

The name of the answer file. For each text, single-response and multiple-response interaction contained in the troubleshooting pack, the cmdlet will display the interaction to the user and write the user's response to the answer file. Note that the cmdlet skips single-response and multiple-response interactions that have the **AllowDynamicResponses** node set to true. For more information, see the Notes section.

If the file exists, the cmdlet overwrites the file. If you specify a path, the path may be an absolute, relative, or UNC path, and it must exist. If you do not specify a path, the cmdlet writes the answer file to the current working directory of the Windows PowerShell process.



| Attribute                   | Value |
|-----------------------------|-------|
| Required?                   | false |
| Position?                   | named |
| Default value               | None  |
| Accept pipeline input?      | false |
| Accept wildcard characters? | false |
| Alias                       | af    |



 

## Input and Return Types

The input type is the type of the objects that you can pipe to the cmdlet. The return type is the type of the objects that the cmdlet emits.

| Type        | Description                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Input type  | StringThe path to the folder that contains the troubleshooting pack. See the Path parameter.<br/>                                 |
| Return type | Microsoft.Windows.Diagnosis.DiagPackContains information about the troubleshooting pack. For details, see the Notes section.<br/> |



 

## Notes

To pass the DiagPack object that this cmdlet returns to the Invoke-TroubleshootingPack cmdlet, you can either:

-   Assign the object to a variable and set the -DiagPack parameter of the Invoke-TroubleshootingPack cmdlet to the variable
-   Pipe the object to the Invoke-TroubleshootingPack cmdlet

If you display the output from the cmdlet in a Windows PowerShell window, the output contains the following information about the pack:

-   Pack identifier
-   Publisher name
-   Pack version
-   Pack name

To discover all of the properties and methods of the DiagPack object, use the Get-Member cmdlet. Use the Select-Object and formatting cmdlets (for example, Format-Table and Format-List) to customize the output.

Typically, to discover information about the troubleshooting pack, you will use the RootCauses and Interactions properties of the DiagPack object. To discover the root causes defined by the DiagPack object, access the RootCauses property of the DiagPack object. The RootCauses property is an array of RootCause objects. To access a RootCause object in the array, use a zero-based index (for example, $\_.RootCauses\[0\]).

To discover the resolvers for a root cause, use the Resolutions property of the RootCause object. The Resolutions property is an array of Resolution objects. To access a Resolution object in the array, use a zero-based index (for example, $\_.RootCauses\[0\].Resolutions\[0\]).

To discover the interactions (questions) defined by the DiagPack object, access the Interactions property of the DiagPack object. The Interactions property is an array of Interaction objects. To access an Interaction object in the array, use a zero-based index (for example, $\_.Interactions\[0\]). There are five interaction types. The text, single response, and multiple response interactions require user input; the pause and launch user interface interactions do not. The Interaction.Properties property contains information that is unique to each interaction. For example, for launch UI interactions, Properties contains the commandline key; for single-response and multiple-response interactions, Properties contains the ADR key, which indicates if the list contains dynamic choices; and for text interactions, Properties contains the Regex key for the regular expression that is used to limit the input.

The following XSD shows the elements and types that you can use to write an answer file; however, you should use the -AnswerFile parameter instead to create the answer file.

``` syntax
<xsd:schema xmlns:dcmAF="http://www.microsoft.com/schemas/dcm/resultreport/2008" 
            xmlns:xsd='http://www.w3.org/2001/XMLSchema' 
            targetNamespace="http://www.microsoft.com/schemas/dcm/resultreport/2008" 
            elementFormDefault="unqualified">

 <xsd:complexType name='Interaction'>
  <xsd:sequence>
   <xsd:element name='Value' type='xsd:string' minOccurs='0' maxOccurs='unbounded'/>
  </xsd:sequence>
  <xsd:attribute name='ID' type='xsd:string' use='required'/>
 </xsd:complexType>

 <xsd:complexType name='AnswerFile'>
  <xsd:sequence>
   <xsd:element name='Interaction' type='dcmAF:Interaction' minOccurs='0' maxOccurs='unbounded'/>
  </xsd:sequence>
 </xsd:complexType>

 <xsd:element name='Answers' type='dcmAF:AnswerFile'/>

</xsd:schema>
```

An answer file can contain responses for text interactions and single-response and multiple-response interactions. For text and single-response interactions, the **Interaction** node will contain a single **Value** node. For multiple-response interactions, the **Interaction** node can contain multiple **Value** nodes. Note that for dynamic single-response and multiple-response interactions, you can manually add answers to the answer file. The following example shows an answer file that contains the answers for a troubleshooting pack that contains a multiple-response interaction and a text interaction.

``` syntax
<Answers>
  <Interaction ID="interaction1">
    <Value>Value for choice 1 goes here</Value>
    <Value>Value for choice 3 goes here</Value>
  </Interaction>
  <Interaction ID="interaction2">
    <Value>Value for text input goes here</Value>
  </Interaction>
</Answers>
```

## Examples

The following examples show how to use the cmdlet.

### Example 1

The following example shows how to get the Aero DiagPack object.

**$aero = Get-TroubleshootingPack -Path C:\\Windows\\Diagnostics\\System\\Aero**

### Example 2

The following example shows how to discover the root causes for the Aero troubleshooting pack.

**PS:&gt;$aero = Get-TroubleshootingPack -Path C:\\Windows\\Diagnostics\\System\\Aero $aero.Rootcauses\[2\]**

### Example 3

The following example shows how to discover the resolvers for a root cause.

**PS:&gt;$aero = Get-TroubleshootingPack C:\\Windows\\Diagnostics\\System\\Aero $aero.RootCauses\[2\].Resolutions\[0\]**

### Example 4

The following example shows how to use Get-TroubleshootingPack to generate an answer file for a troubleshooting pack.

**PS:&gt;$aero = Get-TroubleshootingPack C:\\Windows\\Diagnostics\\System\\Aero -Answer AeroAnswerFile.xml**

 

 





