---
description: Your snap-in extension must display the current configuration and analysis information to the users.
ms.assetid: 503bc283-c1cd-4258-a27e-4046553882fa
title: Displaying Configuration and Analysis Information
ms.topic: article
ms.date: 05/31/2018
---

# Displaying Configuration and Analysis Information

Your snap-in extension must display the current configuration and analysis information to the users.

To display information, the attachment snap-in extension node must extend the Security Configuration snap-ins using the Services node. The Services node is the MMC snap-in that administers services installed on the system.

The node types that can be extended are as follows:

-   Configuration Services NodeType={24a7f717-1f0c-11d1-affb-00c04fb984f9}
-   Inspection Services NodeType={678050c7-1ff8-11d1-affb-00c04fb984f9}

When the Services node is expanded, the MMC notifies all registered snap-in extensions. Each attachment snap-in should insert itself under the Services node, and perform the following tasks:

-   Call **QueryInterface** to get a pointer to the [**ISceSvcAttachmentData**](/windows/desktop/api/Scesvc/nn-scesvc-iscesvcattachmentdata) interface exposed by the Security Configuration snap-ins.
-   Call [**ISceSvcAttachmentData::Initialize**](/windows/desktop/api/Scesvc/nf-scesvc-iscesvcattachmentdata-initialize) to inform the Security Configuration snap-ins that the snap-in extension is loaded and to establish a context for communications.
-   Call [**ISceSvcAttachmentData::GetData**](/windows/desktop/api/Scesvc/nf-scesvc-iscesvcattachmentdata-getdata) to retrieve configuration information from the database. This step can be performed either when the snap-in extension initializes itself or when the user opens its node.

For more information, see [Adding an Attachment Snap-in Extension Node](adding-an-attachment-snap-in-extension-node.md).

 

 



