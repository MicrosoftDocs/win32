---
description: As mentioned in Ink Analysis Overview, the ink analysis technology internally maintains a tree-based document model to contain analysis results and relationships.
ms.assetid: 33ba9292-3bc7-41ba-a602-e2fc94cd3a57
title: Data Proxy with Ink Analysis
ms.topic: article
ms.date: 05/31/2018
---

# Data Proxy with Ink Analysis

As mentioned in [Ink Analysis Overview](ink-analysis-overview.md), the ink analysis technology internally maintains a tree-based document model to contain analysis results and relationships. If your application already has an established document store that is different, you will need to make use of the ink analysis features designed to proxy data between disparate document models.

## Types of Data Proxy

The data proxy features enable your application to:

-   Integrate analysis results data back into an existing document model.
-   Communicate previous results (or state) back into the [**InkAnalyzer**](inkanalyzer.md).
-   Communicate non-ink state into the [**InkAnalyzer**](inkanalyzer.md).
-   Communicate only the minimum set of data (both previous and non-ink state) needed to complete the analysis operation.
-   Easily update the internal application document model with analysis results.

There are two basic approaches to ink analysis data proxy. The differences lay in the details of when and how the synchronization between the document models occurs. The first approach, synchronous update, requires the modification of the ink analysis document model as changes occur in the application document. The second approach, on-demand update, requires only the data affected by changes to the application document model to be passed to the [**InkAnalyzer**](inkanalyzer.md). That is, only the data for the parts of the Ink Analysis document model that are in the same area as modifications to the application document need be passed to the **InkAnalyzer** as it needs them.

### Synchronous Update

The synchronous update approach requires the modification (creation and deletion) of nodes in the [**InkAnalyzer**](inkanalyzer.md) object's collection of [**ContextNode**](icontextnode.md) objects as they occur in the application document. For example, each time a text word is added to the application, a corresponding **TextWord** styled **ContextNode** is created in the **InkAnalyzer**. If the location of the text word on the page changes, then the location of the corresponding **ContextNode** is updated at the same time. This method is less efficient in terms of computing resources than the on-demand method because every document change involves an update to the **InkAnalyzer**, even if the change does not affect the ink being analyzed.

The following example is meant to show how synchronous update works. Imagine an application that has an existing document model. When the end-user makes a change to the document, such as adding new text, the change is processed as follows:

1.  The end user creates the new data.
2.  The application determines how to process the data, stores it, and renders it.
3.  For practical purposes, the following steps take place simultaneously.
    1.  The application places the data into its document model.
    2.  The application creates an [**InkAnalyzer**](inkanalyzer.md) and updates it. Doing this simultaneously assures that the **InkAnalyzer** always has the most recent information.
    3.  The application calls [**BackgroundAnalyze**](iinkanalyzer-backgroundanalyze.md) on the [**InkAnalyzer**](inkanalyzer.md) to begin analysis.
4.  A series of events is fired if the change involves ink and the [**InkAnalyzer**](inkanalyzer.md) determines new results. One event is fired for each change made to the collection of [**ContextNode**](icontextnode.md) objects in the **InkAnalyzer**. These events include [**ContextNodeCreated**](-ianalysisproxyevents-contextnodecreated.md), [**ContextNodeDeleting**](-ianalysisproxyevents-contextnodedeleting.md), [**ContextNodeMovingToPosition**](-ianalysisproxyevents-contextnodemovingtoposition.md), [**ContextNodePropertiesUpdated**](-ianalysisproxyevents-contextnodepropertiesupdated.md), [**ContextNodeLinkAdding**](-ianalysisproxyevents-contextnodelinkadding.md), [**ContextNodeLinkDeleting**](-ianalysisproxyevents-contextnodelinkdeleting.md), and [**ContextNodeReparenting**](-ianalysisproxyevents-contextnodereparenting.md). The application handles these events to proxy the results of the analysis operation back into the document model as appropriate.
5.  The application updates the layout of the document, pulling the new data from the document model.
6.  The new data is rendered back to the end user.

### On-Demand Update

The on-demand approach only requires the data to be passed for those [**ContextNode**](icontextnode.md) objects that are in the areas that are being analyzed. The needed **ContextNode** objects are extracted from the application's document model just after the analysis operation is invoked, and again just prior to reconciling the results. While more complicated to implement than synchronous updates, this approach yields better performance results.

## Related topics

<dl> <dt>

[Ink Analysis Overview](ink-analysis-overview.md)
</dt> <dt>

[**InkAnalyzer Class (C++)**](inkanalyzer.md)
</dt> <dt>

[**Microsoft.Ink.InkAnalyzer**](/previous-versions/ms583671(v=vs.100))
</dt> <dt>

[**Microsoft.Ink.ContextNode**](/previous-versions/ms551996(v=vs.100))
</dt> </dl>

 

 
