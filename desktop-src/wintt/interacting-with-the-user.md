---
title: Interacting with the User
ms.assetid: 'f5b92d8c-b0ed-4430-8d1a-7854a7be82b9'
description: 
---

# Interacting with the User

If you need to request information from the user, prompt the user to take action, or inform the user about a change that was made, you can use the following interactions:

-   [Single-response interactions](using-single-response-interactions.md) let the user select a single choice from a list of choices
-   [Multiple-response interactions](using-multiple-response-interactions.md) let the user select multiple choices from a list of choices
-   [Text interactions](using-text-interactions.md) let the user provide text input
-   [Pause interactions](using-pause-interactions.md) let you provide instructions to the user
-   [Launch UI interactions](using-launchui-interactions.md) let the user launch a UI application

You must define the interactions in the troubleshooting manifest. To invoke the interactions, specify the interaction's ID when you call the [Get-DiagInput](get-diaginput-cmdlet.md) cmdlet from your troubleshooter, resolver, or verifier scripts. The **RequiresInteractivity** node of the [**Script**](package-script-complextype.md) definition must be set to true.

## Customizing Interactions

Each interaction contains an **ExtensionPoint** element. You can use the **ExtensionPoint** element to customize the interaction. For example, you can add additional information to the interaction or set the default value or selections for the interaction. See each interaction for the extension points that they support.

The extension points are used only by the WTP wizard (MSDT.exe); the extension points are not supported by the command-line client using the [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlet.

 

 




