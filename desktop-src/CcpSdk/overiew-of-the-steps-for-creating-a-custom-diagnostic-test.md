---
Description: 'To create a custom diagnostic test, you perform the following tasks:If you can use existing command, scripts, or applications in your diagnostic test, you can omit the first two steps above.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '27597a50-7981-4731-a819-c9fc7666a5f2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Overview of the Steps for Creating a Custom Diagnostic Test
---

# Overview of the Steps for Creating a Custom Diagnostic Test

To create a custom diagnostic test, you perform the following tasks:

1.  Create scripts or applications that perform the necessary actions for each of the stages of the test, if needed.
2.  Test the scripts for each stage by running them on the appropriate nodes at the command prompt or by using the **clusrun** command, if needed.
3.  Create an XML file that defines the test and includes the metadata, parameter information, and commands for the test. The XML content of this file follows the schema described in [Diagnostic Test Definition Schema](diagnostic-test-definition-schema.md).
4.  Use the **Add-HpcTest** cmdlet in HPC PowerShell to add the test to the HPC cluster.
5.  Add any files that your test needs to the appropriate folder on all of the nodes in the cluster or to a appropriate share that is accessible from all of the nodes. These files should include any program files or scripts for your test if you created custom program or scripts for the test to run. The location for the files should match the location you specified in the XML file.
6.  Run the test and view the results in HPC Cluster Manager as you would for the built-in tests that Windows HPC Server 2008 R2 provides.

If you can use existing command, scripts, or applications in your diagnostic test, you can omit the first two steps above. Depending on the purpose and complexity of a custom diagnostic test, you also may not need to implement all of the stages of the custom diagnostic test, but can rely on the default behavior for those stages.

This section provides procedures for creating several types of custom diagnostic tests of different levels of complexity.

## In this section

[Steps for Creating a Custom Diagnostic Test that Runs an Existing Command](steps-for-creating-a-custom-diagnostic-test-that-runs-an-existing-command.md)

[Steps for Creating a Custom Diagnostic Test that Checks that a Result is Consistent throughout an HPC Cluster](steps-for-creating-a-custom-diagnostic-test-that-checks-that-a-result-is-consistent-throughout-an-hpc-cluster.md)

[Steps for Creating a Custom Diagnostic Test that Checks that a Result Matches an Expected Value throughout an HPC Cluster](steps-for-creating-a-custom-diagnostic-test-that-checks-that-a-result--matches-an-expected-value-throughout-an-hpc-cluster.md)

[Steps for Creating a Custom Diagnostic Test that Runs a Job](steps-for-creating-a-custom-diagnostic-test-that-runs-a-job.md)

[Steps for Creating a Custom Diagnostic Test that Implements the PreStep and RunStep Stages](steps-for-creating-a-custom-diagnostic-test-that-implements-the-prestep-and-runstep-stages.md)

[Steps for Creating a Custom Diagnostic Test that Implements the RunStep and PostStep Stages](steps-for-creating-a-custom-diagnostic-test-that-implements-the-runstep-and-poststep-stages.md)

## Related topics

<dl> <dt>

[Diagnostics Extensibility in Windows HPC Server 2008 R2 Step-by-Step Guide](diagnostics-extensibility-in-windows-hpc-server-windows-2008-r2-ctp2-step-by-step-guide.md)
</dt> </dl>

 

 



