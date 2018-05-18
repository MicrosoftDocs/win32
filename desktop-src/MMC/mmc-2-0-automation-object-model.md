---
title: MMC 2.0 Automation Object Model
description: Microsoft Management Console (MMC) 2.0 includes the first release of the MMC automation object model architecture for snap-in and extension developers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'eb7c92e7-d834-4736-bff4-74940c9bb194'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMC 2.0 automation object model", "automation object model"]
---

# MMC 2.0 Automation Object Model

Microsoft Management Console (MMC) 2.0 includes the first release of the MMC automation object model architecture for snap-in and extension developers. The MMC 2.0 automation object model may also be used by developers who do not want to write snap-ins or extensions, but who would like to write programs that interact with MMC.

MMC 2.0 contains the following new objects.



| Object                                                                   | Description                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AppEventsDHTMLConnector Object**](appeventsdhtmlconnector-object.md) | Object that provides a means for automation clients to receive events from MMC; this object is used by scripts running on DHTML pages created by view extensions. For more information about view extensions, see [Extending Views](extending-views.md). |
| [**Application Object**](application-object.md)                         | The MMC 2.0 application object, which can be used to access other MMC 2.0 automation objects.                                                                                                                                                             |
| [**Column Object**](column-object.md)                                   | Result pane column object.                                                                                                                                                                                                                                |
| [**Columns Collection**](columns-collection.md)                         | Collection of [**Column**](column-object.md) objects.                                                                                                                                                                                                    |
| [**ContextMenu Object**](contextmenu-object.md)                         | MMC context menu object.                                                                                                                                                                                                                                  |
| [**Document Object**](document-object.md)                               | MMC console document object.                                                                                                                                                                                                                              |
| [**Extension Object**](extension-object.md)                             | MMC snap-in extension.                                                                                                                                                                                                                                    |
| [**Extensions Collection**](extensions-collection.md)                   | Collection of [**Extension**](extension-object.md) objects.                                                                                                                                                                                              |
| [**Frame Object**](frame-object.md)                                     | MMC console frame object; this object encapsulates the MMC main window.                                                                                                                                                                                   |
| [**MenuItem Object**](menuitem-object.md)                               | MMC menu item object.                                                                                                                                                                                                                                     |
| [**Node Object**](node-object.md)                                       | MMC node object.                                                                                                                                                                                                                                          |
| [**Nodes Collection**](nodes-collection.md)                             | Collection of [**Node**](node-object.md) objects.                                                                                                                                                                                                        |
| [**Properties Collection**](properties-collection.md)                   | Collection of [**Property**](property-object.md) objects.                                                                                                                                                                                                |
| [**Property Object**](property-object.md)                               | MMC property object.                                                                                                                                                                                                                                      |
| [**ScopeNamespace Object**](scopenamespace-object.md)                   | MMC namespace object.                                                                                                                                                                                                                                     |
| [**SnapIn Object**](snapin-object.md)                                   | MMC snap-in object.                                                                                                                                                                                                                                       |
| [**SnapIns Collection**](snapins-collection.md)                         | Collection of [**SnapIn**](snapin-object.md) objects.                                                                                                                                                                                                    |
| [**View Object**](view-object.md)                                       | MMC view object. This object serves as the external object when an MMC snap-in hosts Microsoft Internet Explorer components.                                                                                                                              |
| [**Views Collection**](views-collection.md)                             | Collection of [**View**](views-collection.md) objects.                                                                                                                                                                                                   |



 

## Handling Object Model Error Conditions in Scripts

When a script is executed, a call to an MMC object model interface may generate a run-time error that halts execution of the script. As a good coding practice, you should use the error handling mechanism of your script language to handle these errors. For example, VBScript provides the "on error resume next" statement for handling errors inline.

When adapting VBScript example code for use in your own working environment, inserting an "on error resume next" statement in each procedure helps trap errors that may otherwise halt script execution. An error code "err" can then be inspected immediately after a script statement that causes a run-time error. To clear the value in "err", use the VBScript "err.clear" command. For more information about using "on error" statements in VBScript, see the VBScript User's Guide.

For example, use the following code to trap an execution error caused by a non-existent snap-in:


```VB
on error resume next
objMMC.Document.SnapIns.Add("Folder1") `if a Snap-in does not exist MMC throws an error
if err then
`Trap the error just after the statement where an error/exception can occur and handle it elegantly
            msgbox("Snap-in Not found")  
            err.clear
end if
```



To trap an exception caused when a node child is not found for a scope node, use the following code:


```VB
Function ScopeNodeHasChild(ScopeNamespace, SampleNode) 
    on error resume next
    ScopeNamespace.Expand(SampleNode)
    set NodeFound = ScopeNamespace.GetChild(SampleNode)
    if err then 
              ScopeNodeHasChild = false
        exit function 
        `Return False when there are no child nodes for the scope node.
    end if
              ScopeNodeHasChild = true 
              `Return True when a child node is found.
End Function
```



## Related topics

<dl> <dt>

[Getting Started with the Automation Object Model](getting-started-with-the-automation-object-model.md)
</dt> <dt>

[Using the Extended View Extension - Implementation Details](using-the-extended-view-extension-implementation-details.md)
</dt> </dl>

 

 




