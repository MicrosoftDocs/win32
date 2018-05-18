---
title: Using Multiple-Response Interactions
description: Use multiple-response interactions to present a list of choices to the user from which they may select more than one choice.
ms.assetid: 'd8f49246-93cf-4b02-a09b-e7295eabdd2a'
---

# Using Multiple-Response Interactions

Use multiple-response interactions to present a list of choices to the user from which they may select more than one choice. In the manifest, you can specify the static choices. You can also specify choices at run time using the -Choice parameter of [Get-DiagInput](get-diaginput-cmdlet.md). The list of choices changes from using check boxes to a list when the number of choices is more than four.

The following shows how to specify multiple-response interactions in your manifest. For details on the contents of a multiple-response interaction, see the [**MultipleResponseInteraction**](package-multipleresponseinteraction-complextype.md) complex type.


```XML
    <Interactions>
        <SingleResponseInteractions/>

        <MultipleResponseInteractions>
            <MultipleResponseInteraction>
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
                            <Default/>
                            <Icon>@resource.dll,-101</Icon>
                        </ExtensionPoint>
                    </Choice>
                    <Choice>
                        <DisplayInformation>
                            <Parameters/>
                            <Name>Green</Name>
                            <Description>Description of Choice 2.</Description>
                        </DisplayInformation>
                        <Value>2</Value>
                        <ExtensionPoint>
                            <Icon>@resource.dll,-102</Icon>
                        </ExtensionPoint>
                    </Choice>
                    <Choice>
                        <DisplayInformation>
                            <Parameters/>
                            <Name>Blue</Name>
                            <Description>Description of Choice 3.</Description>
                        </DisplayInformation>
                        <Value>3</Value>
                        <ExtensionPoint>
                            <Default/>
                            <Icon>@resource.dll,-103</Icon>
                        </ExtensionPoint>
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
            </MultipleResponseInteraction>
        </MultipleResponseInteractions>
        <TextInteractions/>
        <PauseInteractions/>
        <LaunchUIInteractions/>
    </Interactions>
```



The following shows how to invoke the previous interaction in a script.


```PowerShell
$color = Get-DiagInput -Id "ColorSelection"
  
$colors = @{"Name"="Yellow"; "Value"="4"; "Description"="Description of choice 4"; "ExtensionPoint"="<Default/><Icon>@resource.dll,-104</Icon>"}, @{"Name"="Purple"; "Value"="5"; "Description"="Description of choice 5"; "ExtensionPoint"="<Icon>@resource.dll,-105</Icon>"}
$color = Get-DiagInput -Id "ColorSelection" -Choice $colors

#$color = Get-DiagInput -Id "ColorSelection" -Choice @{"Name"="Yellow"; "Value"="4"; "Description"="Description of choice 4"; "ExtensionPoint"="<Default/><Icon>@resource.dll,-104</Icon>"}, @{"Name"="Purple"; "Value"="5"; "Description"="Description of choice 5"; "ExtensionPoint"="<Icon>@resource.dll,-105</Icon>"}
```



 

 




