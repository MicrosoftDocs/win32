---
title: Using Pause Interactions
description: A pause interaction lets you provide instructions to the user (for example, asking the user to connect the network cable to the computer).
ms.assetid: '4ddc7fb3-b58c-4005-bfd3-9933134c89b9'
---

# Using Pause Interactions

A pause interaction lets you provide instructions to the user (for example, asking the user to connect the network cable to the computer). Use the **Name** node of [**DisplayInformation**](package-displayinformation-complextype.md) to provide the instruction and the **Description** node to provide additional information if necessary. You can use extension points to provide additional functionality (for example, adding links to the page).

The following shows how to specify pause interactions in your manifest. For details on the contents of a pause interaction, see the [**PauseInteraction**](package-pauseinteraction-complextype.md) complex type.


```XML
    <Interactions>
        <SingleResponseInteractions/>
        <MultipleResponseInteractions/>
        <TextInteractions/>

        <PauseInteractions>
            <PauseInteraction>
                <ID>ConnectNetworkCable</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Please connect the network cable to the computer</Name>
                    <Description/>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint/>
            </PauseInteraction>

            <PauseInteraction>
                <ID>PauseWithLink</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Test the Link extension point</Name>
                    <Description>Please see the link below for additional information.</Description>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint>
                    <Link>URLGOESHERE</Link>
                    <LinkText>DISPLAYTEXTFORLINKGOESHERE</LinkText>
                </ExtensionPoint>
            </PauseInteraction>
        </PauseInteractions>
        <LaunchUIInteractions/>
    </Interactions>
```



The following shows how to invoke the previous interactions in a script.


```PowerShell
Get-DiagInput -Id ConnectNetworkCable

Get-DiagInput -Id "PauseWithLinks"
```



 

 




