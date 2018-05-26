---
title: Using Launch UI Interactions
description: Use launch UI interactions to launch a UI application.
ms.assetid: 09f6d4c1-7055-4d03-88ca-e1a77680995c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Launch UI Interactions

Use launch UI interactions to launch a UI application. The application should be related to the current task being performed.

The following shows how to specify launch UI interactions in your manifest. For details on the contents of a launch UI interaction, see the [**LaunchUIInteraction**](package-launchuiinteraction-complextype.md) complex type.


```XML
    <Interactions>
        <SingleResponseInteractions/>
        <MultipleResponseInteractions/>
        <TextInteractions/>
        <PauseInteractions/>

        <LaunchUIInteractions>
            <LaunchUIInteraction>
                <Parameters>
                    <Parameter>
                        <Name>arg</Name>
                        <DefaultValue/>
                    </Parameter>
                </Parameters>
                <CommandLine>%windir%\System32\Notepad.exe %arg%</CommandLine>
                <ID>LaunchNotepad</ID>
                <DisplayInformation>
                    <Parameters/>
                    <Name>Launch text editor</Name>
                    <Description/>
                </DisplayInformation>
                <ContextParameters/>
                <ExtensionPoint>
                    <NoCache/>
                </ExtensionPoint>
            </LaunchUIInteraction>
        </LaunchUIInteractions>
    </Interactions>
```



The following shows how to invoke the previous interaction in a script.


```PowerShell
Get-DiagInput -Id "LaunchNotepad" -Parameter @{"arg"="FULLPATHGOESHERE"}
```



 

 




