---
title: AXE Schema Reference
description: AXE uses XML to describe assessments, jobs, assessment results and job results.
ms.assetid: 880399FA-D595-43A7-AC01-D1EF8AFBD55F
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AXE Schema Reference

AXE uses XML to describe assessments, jobs, assessment results and job results. This section provides the XSD schema for the XML, and it also provides a subsection that describes the XML elements.

An AXE assessment manifest is an XML file the describes an AXE assessment. An AXE job manifest is an XML file that describes an AXE job, which is a set of AXE assessments. A job may run multiple instances of an assessment. The job manifest includes the parameters that are specific for each assessment instance, and the parameters that apply to the entire job.

The XML element that represents an assessment manifest is [**AxeAssessmentManifest**](axeassessmentmanifest.md). The element that represents a job manifest is [**AxeJobManifest**](axejobmanifest.md). To create a job manifest, AXE marshals the assessment manifests to [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288) elements, one assessment per element. It then collects these under the [**AssessmentManifests**](assessmentmanifests.md) element of the **AxeJobManifest** element.

An [**AssessmentRun**](assessmentrun.md) element contains information for a particular instance of an assessment and these are collected in [**AssessmentRuns**](assessmentruns.md) of the **AxeJobManifest** element.

When an assessment runs it creates one or more result files containing the assessment results. AXE combines the assessment result files into a job results file. The job results file contains the entire job used to generate the results, so reporting tools never need to use others sources for essential information.

The XML element that represents an assessment result is [**AssessmentResult**](assessmentresult.md). The element that represents job results is [**AxeJobResults**](axejobresults.md).

Assessments can create multiple result files as long as each uses **AssessmentResult** as the root node. Assessments should not write the [**ResultsLocation**](resultslocation.md), [**Guid**](guid.md) and [**ExitCode**](exitcode.md) children of **AssessmentResult** because these nodes are created by AXE.

[AXE XSD Schema](axe-xsd-schema.md)

[AXE XML Elements](axe-xml-elements.md)

## Related topics

<dl> <dt>

Assessment Execution Engine
</dt> </dl>

 

 




