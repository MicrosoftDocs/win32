---
title: Adding HTML Help Support
description: This feature is introduced in Microsoft Management Console (MMC) 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '87387cf5-ff5f-4816-8c96-97a7ae25df94'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["adding HTML Help support MMC"]
---

# Adding HTML Help Support

This feature is introduced in Microsoft Management Console (MMC) 1.1.

MMC uses HTML Help as its Help system. For each console file (.msc), snap-ins can provide their own compiled HTML Help files (.chm) that MMC combines into a single HTML Help collection file. A collection file is unique to each console file, because different console files usually contain different snap-ins, and therefore require different sets of Help files depending on the snap-ins that have been added.

This means that there is a single table of contents, index, and search engine that contains the HTML Help topics for all snap-ins that have been added to the console file. When a user clicks **Help Topics** on the main console window's **Help** menu, MMC opens the merged HTML Help collection file that includes HTML Help files for all snap-ins in the current console file.

Be aware that for MMC to merge a snap-in's compiled HTML file into a collection file, the snap-in's file must be compiled with a binary table of contents (TOC). If using HTML Help Workshop, set the **Create a binary TOC** option to compile the file with a binary TOC.

MMC provides a number of interfaces and other language constructs for adding HTML Help support to snap-ins. MMC uses a snap-in's implementation of the [**ISnapinHelp2**](isnapinhelp2.md) interface to request the name and location of the snap-in's compiled HTML Help file. The [**GetHelpTopic**](isnapinhelp2-gethelptopic.md) method enables the snap-in to add its compiled HTML Help file to the MMC Help collection file. The [**GetLinkedTopics**](isnapinhelp2-getlinkedtopics.md) method allows the snap-in to specify the names and locations of any HTML Help files that are linked to the snap-in's Help file (specified in the **GetHelpTopic** method).

The [**IDisplayHelp**](idisplayhelp.md) interface enables a snap-in to display a specific HTML Help topic within the collection file. By using the [**ShowTopic**](idisplayhelp-showtopic.md) method (or the [**MMCPropertyHelp**](mmcpropertyhelp.md) function in property pages), a snap-in can open any topic in any HTML Help file within the collection file. The snap-in must specify the compiled HTML Help file name and the topic file name. Be aware that **MMCPropertyHelp** should be used in property pages, which usually execute in a different thread than the snap-in.

The [**MMCN\_CONTEXTHELP**](mmcn-contexthelp.md) notification message is sent when the user requests Help about a selected item by pressing the **F1** key or clicking the **Help** button. A snap-in responds to MMCN\_CONTEXTHELP and displays a Help topic for the particular context by calling the [**IDisplayHelp::ShowTopic**](idisplayhelp-showtopic.md) method, or by calling [**MMCPropertyHelp**](mmcpropertyhelp.md) in the case of property pages.

The user can invoke Help in the following ways:

-   Clicking **Help Topics** on the **Help** menu
-   Pressing **F1** or right-clicking the **Help** button for context-sensitive Help
-   Clicking the **Help** button in a property page owned by the snap-in

When **Help** is invoked, MMC opens the single Help collection file (.col) that it builds and maintains for the current console file. MMC then calls the IComponentData::QueryInterface implementation of the owner of the item that is currently selected in the console (scope or result item) to query for the [**ISnapinHelp2**](isnapinhelp2.md) interface.

[**ISnapinHelp2**](isnapinhelp2.md) is implemented by the snap-in's primary object, which is the object instantiated from the snap-in's CLSID when the snap-in is loaded. For primary snap-ins and namespace extensions, this will be the same object that implements the [**IComponentData**](icomponentdata.md) interface.

When MMC requires the [**ISnapinHelp2**](isnapinhelp2.md) interface, it creates a new instance of the snap-in's primary object and queries it for the interface. This instance of the primary object is only used for **ISnapinHelp2**; MMC releases the instance when it no longer needs the interface.

Snap-in authors should make sure that their snap-in's primary object can function properly in this scenario. For primary snap-ins or namespace extensions, a common error is for the primary object to free resources in its destructor that were acquired in calls to their [**IComponentData::Initialize**](icomponentdata-initialize.md) implementation. Those resources should instead be freed in the [**IComponentData::Destroy**](icomponentdata-destroy.md) method.

If the snap-in (either primary or extension) returns an [**ISnapinHelp2**](isnapinhelp2.md) interface pointer, MMC knows that the snap-in provides the location of its HTML Help file. That is, it implements the [**ISnapinHelp2::GetHelpTopic**](isnapinhelp2-gethelptopic.md) method.

If the query fails for any reason, MMC places a "Help on &lt;your snap-in name&gt;" item on the **Help** menu. If the user clicks this menu item, MMC sends the [**MMCN\_SNAPINHELP**](mmcn-snapinhelp.md) notification to the snap-in's [**IComponent**](icomponent.md) implementation. The snap-in should respond by that displays whatever Help information it has.

MMC's support for the [**MMCN\_SNAPINHELP**](mmcn-snapinhelp.md) notification predates its support for the [**ISnapinHelp**](isnapinhelp2.md) interface. Before **ISnapinHelp**, each snap-in had to provide its own Help system and the **MMCN\_SNAPINHELP** notification told it when to display the Help. Snap-ins are now strongly encouraged to support the **ISnapinHelp** (or **ISnapinHelp2**) interface for that displays Help topics (in HTML Help format).

If a snap-in provides an HTML Help file and MMC hasn't already called the snap-in's [**ISnapinHelp2::GetHelpTopic**](isnapinhelp2-gethelptopic.md) method to request the name and location of the file, it calls the method. It then adds the HTML Help file to the collection file.

MMC caches the name and location of each HTML Help file and stores this information in the collection file. MMC deletes the collection file when the console file is closed and rebuilds it the first time a user requests Help after opening a console file. After the collection file is built MMC continues to use it until the user adds or removes a snap-in, turns an extension on or off, or closes the console file.

When building the collection file, MMC gets HTML Help files from all snap-in types that have been added to the console plus all of their static extensions that have been enabled by the user, and all of their extensions that can only be enabled dynamically.

Be aware that dynamic extensions will always have their HTML Help files added to the collection file, regardless of whether they are instantiated in a console file. Because a snap-in can enable a dynamic extension at any time, MMC does not wait for a dynamic extension to be loaded before including its HTML Help file in the collection file.

To rebuild the collection file, MMC first queries for the [**ISnapinHelp2**](isnapinhelp2.md) interface of each snap-in and extension in the set. It then calls the [**ISnapinHelp2::GetHelpTopic**](isnapinhelp2-gethelptopic.md) method of each snap-in that provides an HTML Help file. Finally, MMC merges all the HTML Help files into the collection file for the console.

## Related topics

<dl> <dt>

[Adding HTML Help Support: Interfaces](adding-html-help-support-interfaces.md)
</dt> <dt>

[Adding HTML Help Support: Implementation Details](adding-html-help-support-implementation-details.md)
</dt> </dl>

 

 




