---
title: Adding Wizard and Wizard97 Pages
description: Failover Cluster Administrator calls your implementation of IWEExtendWizard CreateWizardPages when an administrator runs the Cluster Resource Wizard for a resource type that you are extending.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 623cb58b-10d8-4ae9-9da1-1f94877435dd
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- wizard pages Failover Cluster
- wizard pages Failover Cluster , adding
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Adding Wizard and Wizard97 Pages

\[Support for Failover Cluster Administrator extension DLLs was removed in Windows Server 2008.\]

[Failover Cluster Administrator](cluster-administrator.md) calls your implementation of [**IWEExtendWizard::CreateWizardPages**](/windows/previous-versions/cluadmex/nf-cluadmex-iweextendwizard-createwizardpages?branch=master) when an administrator runs the Cluster Resource Wizard for a [resource type](resource-types.md) that you are extending. Failover Cluster Administrator calls your implementations of **IWEExtendWizard::CreateWizardPages** and [**IWEExtendWizard97::CreateWizard97Pages**](/windows/previous-versions/cluadmex/nf-cluadmex-iweextendwizard97-createwizard97pages?branch=master) when an administrator runs the Failover Cluster Application Wizard for a resource type that you are extending. Your implementations of these two methods should:

1.  Create the wizard pages to be added to the wizard.
2.  Call the Failover Cluster Administrator information interfaces as needed. See [Using the Information Interfaces](using-the-information-interfaces.md).
3.  For each page to be added:

    -   Call [**IWCWizardCallback::AddWizardPage**](/windows/previous-versions/cluadmex/nf-cluadmex-iwcwizardcallback-addwizardpage?branch=master) or [**IWCWizard97Callback::AddWizard97Page**](/windows/previous-versions/cluadmex/nf-cluadmex-iwcwizard97callback-addwizard97page?branch=master) to add the page.
    -   Call [**IWCWizardCallback::EnableNext**](/windows/previous-versions/cluadmex/nf-cluadmex-iwcwizardcallback-enablenext?branch=master) or [**IWCWizard97Callback::EnableNext**](/windows/previous-versions/cluadmex/nf-cluadmex-iwcwizard97callback-enablenext?branch=master) to specify whether another page follows the current page.

 

 




