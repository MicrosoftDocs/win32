---
Description: Displays function instances on a local machine using a graphical user interface.
ms.assetid: 19ddafc6-3f3e-4ce6-a6a9-24ea3a53cf0e
title: Using the Function Discovery Browser (fdbrowser.exe)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Function Discovery Browser (fdbrowser.exe)

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

The Function Discovery Browser (fdbrowser.exe) is a utility that displays function instances on a local machine using a graphical user interface. Developers can use this tool to ensure that the function instances and metadata available on a machine match the expected results.

The Function Discovery Browser was implemented using the Function Discovery API. The source code for this tool is not available. The tool can can be found in the Windows SDK installation location under C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0\\Bin.

## Function Discovery Browser User Interface

The Function Discovery Browser has two panes: the tree view pane and the metadata pane.

The tree view pane shows the [category types](function-discovery-categories.md), [**categories**](category-definitions.md), [**subcategories**](subcategory-definitions.md) (if any), and [function instances](function-objects.md) on the local machine. Click the **+** sign next to an item to display its child categories, subcategories, or function instances. Click a function instance to display its associated metadata.

The contents of the tree view pane are determined by the results of a Function Discovery query. You can change some of the query constraints by following the procedures given below.

The contents of the tree view pane are automatically refreshed from time to time. Contents are refreshed when the function instances are added or removed, or when the query constraints change.

The metadata pane shows the property keys associated with a function instance. The metadata is retrieved from the property store associated with the function instance.

## Displaying Not Present Function Instances in the Function Discovery Browser

A not present function instance is a function instance that is not currently available for use on the system. For example, the function instance associated with a USB device may be marked as not present when the USB device is unplugged.

A not present function instance appears dimmed in the tree view pane. By default, not present function instances do not appear in the Function Discovery Browser.

**To show or hide not present function instances**

-   On the **View** menu, click **Show Not Present Instances**.

When this setting is changed, a new query is executed and the contents of the tree view pane are refreshed.

## Displaying Hidden Function Instances in the Function Discovery Browser

A hidden function instance is a function instance with its PKEY\_FD\_Visibility property key set to FD\_Visibility\_Hidden. The interpretation of this PKEY depends on the provider.

By default, hidden function instances do not appear in the Function Discovery Browser. Either hidden function instances or visible function instances can be displayed in the Function Discovery Browser; you cannot view both types of function instances at the same time.

**To show or hide hidden function instances**

-   On the **View** menu, click **Show Hidden Instances**.

When this setting is changed, a new query is executed and contents of the tree view pane are refreshed.

> [!Note]  
> The PnP provider marks not present function instances as hidden. Before you can view these function instances in the Function Discovery Browser, you must display not present function instances and display hidden function instances.

 

## Including Subcategories in a Query

Some categories have subcategories to provide additional classification information. For example, the Microsoft.Base.Publication, Microsoft.Base.Registration, and Microsoft.PnPX.Association categories all have subcategories.

By default, subcategories are included in the function instance query, which means that function instances associated with a subcategory appear in the tree view pane. When subcategories are not included in the query, a subcategory cannot be expanded to show its associated function instances.

**To include or exclude subcategories from a query**

-   On the **View** menu, click **Include subcategories in query**.

When this setting is changed, a new query is executed and contents of the tree view pane are refreshed.

## Limiting Query Results to a Single Category

You can limit the function instances that appear in the tree view pane to function instances in a single category. This reduces the number of times that the contents of the tree view pane are refreshed. When a query is limited in this way, all categories appear in the tree view pane but only the queried category can be expanded to show its associated function instances.

By default, all categories are queried for function instances.

**To limit query results to a single category**

-   Type the category information into the drop-down box, and then press ENTER.

The category information must be formatted as *category type\\category name*. The category type has two possible values: "Provider" or "Layered". For example, to display only function instances associated with the PnP category, type "Provider\\Microsoft.Base.PnP" into the drop-down box.

If you query a layered category, the returned function instances will be displayed in the tree view pane under the corresponding provider categories. For example, if you query the "Layered\\Microsoft.Networking.Devices" category, you can view the returned function instances by expanding the Microsoft.Networking.Netbios, Microsoft.Networking.SSDP, Microsoft.Networking.WCN, and Microsoft.Networking.WSD categories under the Provider category type.

## Related topics

<dl> <dt>

[Using Function Discovery](using-function-discovery.md)
</dt> </dl>

 

 



