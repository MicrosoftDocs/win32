---
title: Adding Wizard and Wizard97 Pages
description: Failover Cluster Administrator calls your implementation of IWEExtendWizard CreateWizardPages when an administrator runs the Cluster Resource Wizard for a resource type that you are extending.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '623cb58b-10d8-4ae9-9da1-1f94877435dd'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["wizard pages Failover Cluster", "wizard pages Failover Cluster , adding"]
---

# Adding Wizard and Wizard97 Pages

\[Support for Failover Cluster Administrator extension DLLs was removed in Windows Server 2008.\]

[Failover Cluster Administrator](cluster-administrator.md) calls your implementation of [**IWEExtendWizard::CreateWizardPages**](iweextendwizard-createwizardpages.md) when an administrator runs the Cluster Resource Wizard for a [resource type](resource-types.md) that you are extending. Failover Cluster Administrator calls your implementations of **IWEExtendWizard::CreateWizardPages** and [**IWEExtendWizard97::CreateWizard97Pages**](iweextendwizard97-createwizard97pages.md) when an administrator runs the Failover Cluster Application Wizard for a resource type that you are extending. Your implementations of these two methods should:

1.  Create the wizard pages to be added to the wizard.
2.  Call the Failover Cluster Administrator information interfaces as needed. See [Using the Information Interfaces](using-the-information-interfaces.md).
3.  For each page to be added:

    -   Call [**IWCWizardCallback::AddWizardPage**](iwcwizardcallback-addwizardpage.md) or [**IWCWizard97Callback::AddWizard97Page**](iwcwizard97callback-addwizard97page.md) to add the page.
    -   Call [**IWCWizardCallback::EnableNext**](iwcwizardcallback-enablenext.md) or [**IWCWizard97Callback::EnableNext**](iwcwizard97callback-enablenext.md) to specify whether another page follows the current page.

 

 




