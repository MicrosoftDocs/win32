---
title: Using Single-Response Interactions
description: Use single-response interactions to present a list of choices to the user from which they may select a single choice.
ms.assetid: 9b713b03-0951-4193-9c2b-0d87a4897790
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Single-Response Interactions

Use single-response interactions to present a list of choices to the user from which they may select a single choice. In the manifest, you can specify the static choices. You can also specify choices at run time using the -Choice parameter of [Get-DiagInput](get-diaginput-cmdlet.md). You can also use single-response interactions to show CommandLinks.

The following shows how to specify single-response interactions in your manifest. For details on the contents of a single-response interaction, see the [**SingleResponseInteraction**](package-singleresponseinteraction-complextype.md) complex type.

You can remove the &lt;Default&gt; extension point from the comment when using the first ColorSelection usage example; however, the &lt;Default&gt; extension point needs to be commented out or removed for the second ColorSelection usage example to work because the Orange dynamic value specifies the &lt;Default&gt; extension point (only one value can specify the &lt;Default&gt; extension point).


```XML
    <Interactions>
        <SingleResponseInteractions>
            <SingleResponseInteraction>
                <AllowDynamicResponses>true</AllowDynamicResponses>
                <Choices>
                    <Choice>
                        <DisplayInformation>
                            <Parameters/>
                            <Name>Red</Name>
                            <Description>Description of Choice 1.</Description>
                        </DisplayInformation>
                        <Value>1</Value>
                        <ExtensionPoint>
<!--                            <Default/> -->
                        </ExtensionPoint>
                    </Choice>
                    <Choice>
                        <DisplayInformation>
                            <Parameters/>
                            <Name>Green</Name>
                            <Description>Description of Choice 2.</Description>
                        </DisplayInformation>
                        <Value>2</Value>
                        <ExtensionPoint/>
                    </Choice>
                    <Choice>
                        <DisplayInformation>
                            <Parameters/>
                            <Name>Blue</Name>
                            <Description>Description of Choice 3.</Description>
                        </DisplayInformation>
                        <Value>3</Value>
                        <ExtensionPoint/>
                    </Choice>
                </Choices>
                <ID>ColorSelection</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Select a color</Name>
                    <Description/>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint/>
            </SingleResponseInteraction>

            <SingleResponseInteraction>
                <AllowDynamicResponses>false</AllowDynamicResponses>
                <Choices>
                    <Choice>
                        <DisplayInformation>
                            <Parameters/>
                            <Name>Command 1</Name>
                            <Description>Description of Command 1.</Description>
                        </DisplayInformation>
                        <Value>1</Value>
                        <ExtensionPoint/>
                    </Choice>
                    <Choice>
                        <DisplayInformation>
                            <Parameters/>
                            <Name>Command 2</Name>
                            <Description>Description of Command 2.</Description>
                        </DisplayInformation>
                        <Value>2</Value>
                        <ExtensionPoint/>
                    </Choice>
                </Choices>
                <ID>CommandSelection</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Pick a command</Name>
                    <Description/>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint>
                    <CommandLinks/>
                </ExtensionPoint>
            </SingleResponseInteraction>
        </SingleResponseInteractions>

        <MultipleResponseInteractions/>
        <TextInteractions/>
        <PauseInteractions/>
        <LaunchUIInteractions/>
    </Interactions>
```



The following shows how to invoke the previous interactions in a script.


```PowerShell
$color = Get-DiagInput -Id "ColorSelection"

$command = Get-DiagInput -Id "CommandSelection"

$colors = @{"Name"="Orange"; "Value"="4"; "Description"="Description of choice 4"; "ExtensionPoint"="<Default/>"}, @{"Name"="Yellow"; "Value"="5"; "Description"="Description of choice 5"; "ExtensionPoint"=""}

$color = Get-DiagInput -Id "ColorSelection" -Choice $colors

#$color = Get-DiagInput -Id "ColorSelection" -Choice @{"Name"="Orange"; "Value"="4"; "Description"="Description of choice 4"; "ExtensionPoint"="<Default/>"}, @{"Name"="Yellow"; "Value"="5"; "Description"="Description of choice 5"; "ExtensionPoint"=""}
```



 

 




