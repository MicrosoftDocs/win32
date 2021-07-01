---
description: You can launch a rooted view of a junction point through a shortcut file to that junction point.
title: How to Open a Rooted View of a Junction Point Through a Shortcut File
ms.topic: article
ms.date: 05/31/2018
---

# How to Open a Rooted View of a Junction Point Through a Shortcut File

You can launch a rooted view of a junction point through a [shortcut file](./links.md) to that junction point.

## Instructions


Set the shortcut file's Target line to Explorer.exe with a /root flag. The exact form of the command depends on the location of the junction point:

-   If the junction point is a subfolder of the Desktop, use:

    ``` syntax
    Explorer.exe /e,/root,::{Extension CLSID}
    ```

-   If the junction point is a file system folder, use:

    ``` syntax
    Explorer.exe /e,/root,[Fully qualified path to the folder]
    ```

-   If the junction point is a subfolder of a system virtual folder, use:

    ``` syntax
    Explorer.exe /e,/root,::{Folder CLSID}\::{Extension CLSID}
    ```

    The system virtual folders that can contain junction points have the following class identifiers (CLSIDs):

    

    | System Folder     | Class Identifier                       |
    |-------------------|----------------------------------------|
    | My Computer       | {20D04FE0-3AEA-1069-A2D8-08002B30309D} |
    | My Network Places | {208D2C60-3AEA-1069-A2D7-08002B30309D} |
    | Control Panel     | {21EC2020-3AEA-1069-A2DD-08002B30309D} |
    | Internet Explorer | {871C5380-42A0-1069-A2EA-08002B30309D} |

    

     

## Related topics

<dl> <dt>

[Specifying a Namespace Extension's Location](nse-junction.md)
</dt> <dt>

[How to Open a Rooted View of a Junction Point Through the Registry](how-to-use-a-junction-point-to-open-a-rooted-view.md)
</dt> </dl>

 

 
