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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Wizard and Wizard97 Pages

\[Support for Failover Cluster Administrator extension DLLs was removed in Windows Server 2008.\]

[Failover Cluster Administrator](cluster-administrator.md) calls your implementation of [**IWEExtendWizard::CreateWizardPages**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iweextendwizard-createwizardpages) when an administrator runs the Cluster Resource Wizard for a [resource type](resource-types.md) that you are extending. Failover Cluster Administrator calls your implementations of **IWEExtendWizard::CreateWizardPages** and [**IWEExtendWizard97::CreateWizard97Pages**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iweextendwizard97-createwizard97pages) when an administrator runs the Failover Cluster Application Wizard for a resource type that you are extending. Your implementations of these two methods should:

1.  Create the wizard pages to be added to the wizard.
2.  Call the Failover Cluster Administrator information interfaces as needed. See [Using the Information Interfaces](using-the-information-interfaces.md).
3.  For each page to be added:

    -   Call [**IWCWizardCallback::AddWizardPage**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iwcwizardcallback-addwizardpage) or [**IWCWizard97Callback::AddWizard97Page**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iwcwizard97callback-addwizard97page) to add the page.
    -   Call [**IWCWizardCallback::EnableNext**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iwcwizardcallback-enablenext) or [**IWCWizard97Callback::EnableNext**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iwcwizard97callback-enablenext) to specify whether another page follows the current page.

 

 




