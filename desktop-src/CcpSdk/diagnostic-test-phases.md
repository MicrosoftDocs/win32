---
Description: 'A diagnostic test consists of three distinct stages that differ in purpose and the location in the cluster where they run. The following table summarizes these stages.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e88c08e4-0e62-4850-849d-64a7634ddd84'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Diagnostic Test Stages
---

# Diagnostic Test Stages

A diagnostic test consists of three distinct stages that differ in purpose and the location in the cluster where they run. The following table summarizes these stages.



| Stage               | Nodes                                                                                                                               | Definition Required                                                                  | Description                                                                                                                                                                                                                                                         |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PreStep<br/>  | Head node<br/>                                                                                                                | Only for tests that run jobs<br/>                                              | Performs tasks to setup and validate the test, including changing the list on nodes on which the test should run. For tests that run jobs, this stage adds the tasks that you want to run in the RunStep job to that job.<br/>                                |
| RunStep<br/>  | All nodes that the user specified for the test, subject to any modifications to that list that the PreStep command makes<br/> | Only for tests that run commands, and not allowed for tests that run jobs<br/> | Performs the actual work of the diagnostic test.<br/>                                                                                                                                                                                                         |
| PostStep<br/> | Head node<br/>                                                                                                                | No<br/>                                                                        | Performs additional processing of the results of the test and creates a report of the results to display in **HPC Cluster Manager**, and can perform administrative operations such as changing the state of a node to offline based on the test result.<br/> |



 

The following diagram shows the relationship between the diagnostic test stages and the flow of data between them for a test that runs a command.

![diagnostic test stages and data flow](images/diagnosticsworkflow.png)

This topic describes these stages, the requirements for tests that implement these stages, and the input and output for these stages.

## PreStep Stage

The PreStep stage of a diagnostic test can perform validation and setup tasks for the diagnostic test. These tasks can include:

-   Changing the list of nodes that the user requested for the test, so that the test runs only on nodes with specific properties, such as having a node state of online.

-   Setting the values of parameters and environment variables for the test programmatically.

For tests that run jobs, this stage adds the tasks that you want to run in the RunStep job to that job. For these type of tests, you must implement the PreStep stage and specify it in the XML file that defines the diagnostic test.

For tests that run command, specifying a PreStep stage is optional.

The PreStep stage runs only on the head node of the HPC cluster.

### Input for the PreStep stage

The input for the PreStep stage consists on a list of nodes that the user specified for the test, the identifier of the job for the RunStep stage, and the values of parameters for the test.

The diagnostic service provides the list of nodes that the user specified for the test in the DIAG\_NODELIST environment variable. If the list of nodes is longer than 32,767 characters, the list will be too long to store in a single environment variable. In this case, the diagnostic services divides the list up among multiple environment variables named DIAG\_NODELIST, DIAG\_NODELIST1, DIAG\_NODELIST2, DIAG\_NODELIST3, and so on as needed. The restriction on the length of the DIAG\_NODELIST element is consistent with restriction on the length of the node list that HPC Job Scheduler Service uses.

The diagnostic service automatically creates a job for the RunStep stage of the test before the PreStep stage, and provides the job identifier of this job in the DIAG\_RUNSTEP\_JOBID environment variable. Diagnostic tests that run jobs can use this job identifier to add tasks to the RunStep job during the PreStep stage.

The diagnostic service provides the values of the parameters for the diagnostic test to the PreStep stage through the command line.

### Output of the PreStep stage

The output of the PreStep stage can include a processed list of nodes on which the RunStage should run, parameter and environment variable values for the RunStep stage, and the standard output and standard error for the PreStep stage command.

The PreStep stage can provide output in the form of a PreStepResult.xml file. The diagnostic service saves this file to the current working directory on the head node, which the DIAG\_DATA environment variable specifies as \\\\%CCP\_SCHEDULER%\\Diagnostics\\%DIAG\_RUNID% in the context of a diagnostic test. You should not save the file to a different location. This file contains StepResult XML that conforms to the schema described in [Diagnostic Test Step Result Schema](diagnostic-test-step-result-schema.md). You can use the Diagnostic Helper API to generate this XML programmatically. For information about the Diagnostic Helper API, see [Microsoft.Hpc.Diagnostics.Helpers](https://msdn.microsoft.com/library/microsoft.hpc.diagnostics.helpers.aspx).

If the value of the **ResultXML** attribute of the [**PreStep**](prestep-element.md) element in the XML file that defines the diagnostic test is **True**, then PreStepResult.xml must contain information about the nodes on which the RunStep stage should run. If the value of the ResultXML attribute is **false**, the diagnostic service ignores the results in the PreStepResult.xml file.

The diagnostic service interleaves the standard output and standard error streams for the PreStep stage and saves the result in the prestep.result file in the head node working directory. If the value of the **ResultXML** attribute of the [**PreStep**](prestep-element.md) element in the XML file that defines the diagnostic test is false and the PreStep stage does not create a PreStepResult.xml file, the prestep.result file can specify the nodes on which the RunStep stage should run by including a line in the following format:

``` syntax
Nodes: node1,node2,node3,...
```

If the diagnostic test does not implement the PreStep stage, or if the test does not create a PreStepResult.xml file or any standard output when the value of the **ResultXML** attribute of the [**PreStep**](prestep-element.md) element for the diagnostic test is false, the diagnostic service passes to the RunStep stage the same list of nodes that it passed to the PreStep stage.

If the PreStep command fails, **HPC Cluster Manager** displays the contents of the prestep.result file on the **Results** tab for the test run. The PreStep command fails if it returns a nonzero exit code.

## RunStep Stage

The RunStep stage performs the actual work of the diagnostic test. This stage must be specified in the XML file that defines the test for tests that run a command, in order to specify the command that the test should run.

For tests that run a job, the job takes the place of a RunStep command. Because you configure and add tasks to the job in the PreStep stage, you do not need to specify a RunStep stage for this type of test and an error will occur if you do specify this stage.

This stage runs once on each of the nodes in the node list that the PreStep stage produces. The diagnostic service calls the command that you specify for the RunStep stage with the parameter values and environment variable settings that the PreStep stage produces or the values that the XML file that defines the diagnostic test specifies.

Windows HPC Server 2008 R2 does not enforce any requirements for the output of the RunStep stage. The output of the RunStep stage typically includes the information that the PostStep stage needs to display the results of the test in the report for the test. The RunStep stage can provide this information in the StepResult XML format in order to provide the test data in a structured form that the PostStep stage can access more easily.

The standard output and standard error streams on each node for the RunStep stage are piped to a file named *NodeName*.out in the %DIAG\_DATA% directory. If the RunStep stage produces StepResult XML to describe the results of the test, the RunStep command should write the XML to standard output so that the XML is included in the *NodeName*.out files. The PostStep stage can then process these files to obtain the RunStep results for each node.

> [!Note]
>
> If the output of your RunStep stage includes a file in addition to standard output and standard error, the file is saved to the %TEMP% directory on the compute node rather than to the %DIAG\_DATA% file share on the head node. If you create a file during the RunStep stage, such as when you call the [**StepResult.XmlSerializeToFile**](frlrfMicrosoftHpcDiagnosticsHelpersStepResultClassXmlSerializeToFileTopic) method, save or copy the file to a file share that is accessible from the head node so that the PostStep stage can use the file. The diagnostics service and other Windows HPC Server 2008 R2 services use the %DIAG\_DATA% file share, so saving many files or large files on that file share could affect the performance of the head node.

 

## PostStep Stage

The PostStep stage processes the raw results of the RunStep stage as needed and creates a report to display the results. This stage can also perform administrative operations such as changing the state of a node to offline based on the test result.

Specifying the PostStep stage is optional for both tests that run a command and tests that run a job. Implementing the PostStep stage is recommended if your test produces complex data or a large volume of data, if you need to perform additional processing of the results from the individual nodes to obtain a result for the test, or if you want to have more control over the appearance and content of the report for the diagnostic test.

Windows HPC Server 2008 R2 defines two types of tests for which the diagnostic service can automatically process the results and generate a report for the results of the test. These types of tests are consistency tests and comparison tests. If you designate a test as one of these types, you do not need to implement a PostStep stage, and cannot specify a PostStep command. For more information about consistency and comparison tests, see [Types of Diagnostic Tests](types-of-diagnostic-tests.md).

The PostStep stage runs only on the head node of the HPC cluster.

### Input for the PostStep stage

The input for the PostStep stage typically consists of the directory in which the *NodeName*.out files that the RunStep stage produced reside. These files contain the raw results that the PostStep stage needs to process.

> [!Note]
>
> If a node is unreachable in the RunStep stage, the diagnostic test produces no standard output, standard error, or *NodeName*.out file for that node. If you implement a PostStep stage, the diagnostics service does not automatically set the result for that node to **Failure**. The code for the PostStep stage should compare the number of output files with number of nodes in the DIAG\_NODELIST environment variable to ensure that all the nodes ran the test before the PostStep stage sets the overall test result to **Complete** or **Success**.

 

### Output of the PostStep stage

The PostStep stage can produce two files that include information about the results of the test, Report.html and PostStepResult.xml. The diagnostic service saves these files to the %DIAG\_DATA% working directory on the head node.

Diagnostic tests that implement the PostStep stage must create a Report.html file. **HPC Cluster Manager** displays the content of this Report.html file on the **Result** tab for the test run. The report typically contains a section summarizing the result for all of the nodes in the test and sections that present the results of the test for individual nodes.

The PostStepResult.xml file contains StepResult XML and is optional. The file usually contains summary results for all on the nodes in the cluster. If this file includes a list of failed nodes, a command to pivot to a failed node from the test result is available in **HPC Cluster Manager**. The file can also contain other StepResult XML data that might be useful for the administrator. As with all StepResult XML content, you can use the Diagnostic Helper API to generate the XML programmatically.

The diagnostic service interleaves the standard output and standard error stream for the PostStep stage and saves them in the poststep.result file in the working directory on the head node.

If a diagnostic test does not implement a PostStep stage and is not designated as consistency or comparison test, the diagnostic service concatenates the RunStep output from all of nodes and saves it in the poststep.result file, then displays this file on the **Result** tab for the test result in **HPC Cluster Manager**.

If the PostStep command fails, **HPC Cluster Manager** displays the contents of the poststep.result file on the **Result** tab for the test run. The PostStep command fails if it returns a nonzero exit code.

## Related topics

<dl> <dt>

[Diagnostics Extensibility in Windows HPC Server 2008 R2 Step-by-Step Guide](diagnostics-extensibility-in-windows-hpc-server-windows-2008-r2-ctp2-step-by-step-guide.md)
</dt> <dt>

[Types of Diagnostic Tests](types-of-diagnostic-tests.md)
</dt> </dl>

 

 




