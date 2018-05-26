---
title: Using Text Interactions
description: Use text interactions to get text input from the user.
ms.assetid: 3c85e708-a27a-454e-b361-dc1e0ffedb7e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Text Interactions

Use text interactions to get text input from the user. Use the [**DisplayInformation**](package-displayinformation-complextype.md) node to tell the user the type of information that is expected. You can use regular expressions to limit the content that they can enter and extension points to provide additional functionality (for example, adding a Browse button or changing the text window from single-line input to multiline input).

The following shows how to specify text interactions in your manifest. For details on the contents of a text interaction, see the [**TextInteraction**](package-textinteraction-complextype.md) complex type.


```XML
        <TextInteractions>
            <TextInteraction>
                <RegularExpression/>
                <ID>NoInputRestrictions</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>No restrictions on user input</Name>
                    <Description>Does not use a regular expression to limit the contents of the input string.</Description>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint/>
            </TextInteraction>

            <TextInteraction>
                <RegularExpression>^{\d?\d}-{\d?\d}-{\d\d\d\d}$</RegularExpression>
                <ID>InputRestriction</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Restrict user input</Name>
                    <Description>Enter a date in the format MM-DD-YYYY.</Description>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint/>
            </TextInteraction>

            <TextInteraction>
                <RegularExpression/>
                <ID>BrowseComputer</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Browse for a computer</Name>
                    <Description>Testing the Browse(computer) extension point.</Description>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint>
                    <Browse>Computer</Browse>
                </ExtensionPoint>
            </TextInteraction>

            <TextInteraction>
                <RegularExpression/>
                <ID>BrowseFolder</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Browse for a folder</Name>
                    <Description>Testing the Browse(folder) extension point.</Description>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint>
                    <Browse>Folder</Browse>
                </ExtensionPoint>
            </TextInteraction>

            <TextInteraction>
                <RegularExpression/>
                <ID>BrowseFile</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Browse for a file</Name>
                    <Description>Testing the Browse(file) extension point.</Description>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint>
                    <Browse FilterText="Executables" FilterExtension="*.exe">File</Browse>
                </ExtensionPoint>
            </TextInteraction>
 
            <TextInteraction>
                <RegularExpression/>
                <ID>MultipleLineInput</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Test multiple-line input</Name>
                    <Description>Testing use of the EditMode extension point.</Description>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint>
                    <EditMode>Multi</EditMode>
                </ExtensionPoint>
            </TextInteraction>

            <TextInteraction>
                <RegularExpression/>
                <ID>DefaultInputStatic</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Provide a static default string</Name>
                    <Description>Testing the Default extension point.</Description>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint>
                    <Default>Static default string.</Default>
                </ExtensionPoint>
            </TextInteraction>

            <TextInteraction>
                <RegularExpression/>
                <ID>DefaultInputDynamic</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Provide a dynamic default string</Name>
                    <Description>Testing the Default extension point.</Description>
                </DisplayInformation>
                <ContextParameters>
                    <Parameter>
                        <Name>default</Name>
                        <DefaultValue/>
                    </Parameter>
                </ContextParameters>
                <ExtensionPoint>
                    <Default>%default%</Default>
                </ExtensionPoint>
            </TextInteraction>

            <TextInteraction>
                <RegularExpression/>
                <ID>EulaInput</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Test the Eula extension point</Name>
                    <Description>The description node contains the End User License Agreement.</Description>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint>
                    <Eula/>
                </ExtensionPoint>
            </TextInteraction>
        </TextInteractions>
```



The following shows how to invoke the previous interactions in a script.


```PowerShell
$input = Get-DiagInput -Id "NoInputRestrictions"

$date = Get-DiagInput -Id "InputRestriction"

$computer = Get-DiagInput -Id "BrowseComputer"

$folder = Get-DiagInput -Id "BrowseFolder"

$file = Get-DiagInput -Id "BrowseFile"

$input = Get-DiagInput -Id "MultipleLineInput"

$input = Get-DiagInput -Id "DefaultInputStatic"

$input = Get-DiagInput -Id "DefaultInputDynamic" -Parameter @{"default"="dynamic default string"}

$answer = Get-DiagInput -Id "EulaInput"
if ($answer -ieq "accept")
{
    Get-DiagInput -Id "ShowInput" -Parameter @{"default"=$answer}
}  
```



 

 




