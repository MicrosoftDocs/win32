---
Description: 'The administration console snap-in for the fax service exposes a set of extensible node types.'
ms.assetid: '13c836f5-4a76-43b6-9059-d09ff8e0ee4b'
title: 'MMC Snap-in Node Types'
---

# MMC Snap-in Node Types

The administration console snap-in for the fax service exposes a set of extensible node types. For each of these node types, the snap-in provides a set of information that the extension can retrieve by using the methods of the [IDataObject](http://msdn.microsoft.com/en-us/library/ms688421.aspx) interface and the clipboard format associated with the information.

The following topics contain a description of each node type, its GUID, and the format of the information the methods of the [IDataObject](http://msdn.microsoft.com/en-us/library/ms688421.aspx) interface can provide to the extension.

-   [Fax Device Node](-mfax-fax-device-node.md). This node type allows you to add device-specific behavior or properties to individual fax devices you expose.
-   [Fax Device Provider Node](-mfax-fax-device-provider-node.md). This node type allows you to qualify behavior that is related to an fax service provider (FSP) at a global level. It also allows you to add properties that apply to all the fax devices that an FSP exposes.
-   [Inbound Routing Method Node](-mfax-inbound-routing-method-node.md). This node type allows an administrator to configure the behavior of a fax routing method exposed by a fax routing extension. It also allows you to configure a method listed in the fax routing methods catalog. The node covers both device-specific settings and global settings.

## Routing Methods Catalog

The *routing methods catalog* is a list of all the inbound fax routing methods on the system. The catalog enables an administrator to configure system-wide parameters for individual fax routing methods.

 

 



