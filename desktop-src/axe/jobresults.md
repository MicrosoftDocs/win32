---
title: JobResults class
description: This interface provides access to JobResults objects.
ms.assetid: 'DBB2BAE8-55D0-4A08-B835-C68D049230DA'
keywords: ["JobResults class Access Execution Engine", "JobResults class Access Execution Engine , described"]
topic_type:
- apiref
api_name:
- JobResults
api_type:
- COM
---

# JobResults class

This interface provides access to **JobResults** objects.

**JobResults** has these types of members:

-   [Methods](#methods)

### Methods

The **JobResults** class has these methods.



| Method                                                            | Description                                                                                            |
|:------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| [**~JobResults**](jobresults--jobresults.md)                     | Destructor method.<br/>                                                                          |
| [**AddAssessment**](jobresults-addassessment.md)                 | Adds an [**Assessment**](assessment-inf.md) to this **JobResults** object.<br/>                 |
| [**AddAssessmentsFromJob**](jobresults-addassessmentsfromjob.md) | Adds [**Assessment**](assessment-inf.md) objects to this **JobResults** object.<br/>            |
| [**GetAssessmentResults**](jobresults-getassessmentresults.md)   | Returns the [**AssessmentResultsCollection**](assessmentresultscollection.md) for the job.<br/> |
| [**GetCanBeAnalyzed**](jobresults-getcanbeanalyzed.md)           | Returns an indicator of whether the job results can be analyzed.<br/>                            |
| [**GetJobExecuted**](jobresults-getjobexecuted.md)               | Returns the [**Job**](job-if.md) that produced this **JobResults** object.<br/>                 |
| [**GetToBeAnalyzedCount**](jobresults-gettobeanalyzedcount.md)   | Returns the count of assessment results to be analyzed for the job.<br/>                         |
| [**MarkAllToBeAnalyzed**](jobresults-markalltobeanalyzed.md)     | Sets the to be analyzed indicators for all assessment results for the job.<br/>                  |



 

 

 





