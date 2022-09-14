---
title: Using WinSAT
description: You can use the Windows System Assessment Tool (WinSAT) API to initiate formal and ad hoc assessments of the computer's hardware configuration, retrieve the base score for the computer and scores for each subcomponent of the assessment, and retrieve details of the assessment, such as the details of the processor that was assessed.
ms.assetid: b0860c4a-cec3-440c-b31a-7e7ad1b393d2
ms.topic: article
ms.date: 05/31/2018
---

# Using WinSAT

\[WinSAT may be altered or unavailable for releases after Windows 8.1.\]

You can use the Windows System Assessment Tool (WinSAT) API to [initiate formal and ad hoc assessments](#initiating-an-assessment) of the computer's hardware configuration, [retrieve the base score for the computer](#retrieving-the-scores-of-the-assessment) and scores for each subcomponent of the assessment, and [retrieve details of the assessment](#retrieving-details-of-the-assessment), such as the details of the processor that was assessed.

## Initiating an assessment

After Windows 8.1 you can initiate formal and ad hoc assessments of the computer. A formal assessment assesses the following subcomponents of the computer:

-   CPU
-   Memory
-   Primary disk
-   Video card

To initiate a formal assessment, call the [**IInitiateWinSATAssessment::InitiateFormalAssessment**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iinitiatewinsatassessment-initiateformalassessment) method. The results of formal assessments are saved in the assessment store and can be retrieved at a later date.

Typically, you use ad hoc assessments to assess only one subcomponent of the computer, for example, the CPU or the memory. However, you can use the **formal** switch to assess all subcomponents. To initiate an ad hoc assessment, call the [**IInitiateWinSATAssessment::InitiateAssessment**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iinitiatewinsatassessment-initiateassessment) method. Note that the results of ad hoc assessments are not saved in the assessment store.

To retrieve notification when progress is made or when the assessment completes, implement the [**IWinSATInitiateEvents**](/windows/desktop/api/Winsatcominterfacei/nn-winsatcominterfacei-iwinsatinitiateevents) interface.

You cannot run formal assessments remotely or on a computer that is running on batteries. You also cannot remotely run an ad hoc assessment on the graphics subcomponent.

## Retrieving the scores of the assessment

You can retrieve the base score of the computer and the score for each subcomponent of the assessment. You can use the API to retrieve the scores for only formal assessments. To retrieve the scores for ad hoc assessments, you must include the **-xml** argument in the command line to save the assessment results to an XML file and then parse the file for the subcomponent's score.

The base score is a general measurement of the computer's hardware configuration. A higher base score generally means that the computer will perform better and faster than a computer with a lower base score, especially when performing more advanced and resource-intensive tasks.

Each hardware component receives an individual subscore. Your computer's base score is determined by the lowest subscore. For example, if the lowest subscore of an individual hardware component is 2.6, then the base score is 2.6. The base score is not an average of the combined subscores.

A user can use the base score to confidently buy programs and other software that are matched to their computer's base score. For example, if the computer has a base score of 3.3, then the user can confidently purchase any software designed for this version of Windows that requires a computer with a base score of 3 or lower.

To retrieve the base score, first call the [**IQueryRecentWinSATAssessment::get\_Info**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iqueryrecentwinsatassessment-get_info) method to get the [**IProvideWinSATResultsInfo**](/windows/desktop/api/Winsatcominterfacei/nn-winsatcominterfacei-iprovidewinsatresultsinfo) interface. Then, call the [**IProvideWinSATResultsInfo::get\_SystemRating**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iprovidewinsatresultsinfo-get_systemrating) method to get the base score.

A user can use subcomponent scores to determine whether a subcomponent of the computer can support a specific type of application. For example, a user that spends more time reading or writing documents may require a higher score for the disk than a user who runs scientific applications, and a user who runs scientific applications would probably want a higher CPU subcomponent score and may not be concerned with a lower disk score.

To retrieve the score for each subcomponent, first call the [**IQueryRecentWinSATAssessment::get\_Info**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iqueryrecentwinsatassessment-get_info) method to get the [**IProvideWinSATResultsInfo**](/windows/desktop/api/Winsatcominterfacei/nn-winsatcominterfacei-iprovidewinsatresultsinfo) interface. Then call the [**IProvideWinSATResultsInfo::GetAssessmentInfo**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iprovidewinsatresultsinfo-getassessmentinfo) method to get the [**IProvideWinSATAssessmentInfo**](/windows/desktop/api/Winsatcominterfacei/nn-winsatcominterfacei-iprovidewinsatassessmentinfo) interface. For each subcomponent whose score you want to retrieve, call the [**IProvideWinSATAssessmentInfo::get\_Score**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iprovidewinsatassessmentinfo-get_score) method.

## Retrieving details of the assessment

The WinSAT API provides the overall base score and scores for each subcomponent. To get details of the assessment (for example, the metrics used to compute the score and details of the processor that was assessed), you must retrieve the data from the XML assessment document. To retrieve details of the most recent formal assessment, call the [**IQueryRecentWinSATAssessment::get\_XML**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iqueryrecentwinsatassessment-get_xml) method. To retrieve the details from each assessment in the WinSAT data store, call the [**IQueryAllWinSATAssessments::get\_AllXML**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iqueryallwinsatassessments-get_allxml) method.

For information on the XML schema and the details that you can retrieve, see [WinSAT Schema](winsat-schema.md).

 

 




