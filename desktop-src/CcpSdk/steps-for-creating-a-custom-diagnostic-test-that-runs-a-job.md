---
Description: 'In Windows&\#160;HPC&\#160;Server&\#160;2008&\#160;R2, you can create diagnostic tests that run a command or that run a job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd9df1f03-84d8-46fb-b11c-f720529218a6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Steps for Creating a Custom Diagnostic Test that Runs a Job
---

# Steps for Creating a Custom Diagnostic Test that Runs a Job

In Windows HPC Server 2008 R2, you can create diagnostic tests that run a command or that run a job. You can create a test that runs a job when you want your test to perform operations that a command run using the HPC **clusrun** command cannot perform, such as running Message Passing Interface (MPI) applications or parametric sweep tasks.

This example creates a job that runs the **hostname.exe** command on all of the nodes specified for the test.

## Step 1: Create the command for the PreStep stage

To create a test that runs a job, you need to add the tasks that you want the job to run to the job that the diagnostic service automatically creates to run in the RunStep stage. You need to add these tasks in the PreStep stage, so you need a custom implementation of the PreStep stage.

This custom implementation of the PreStep stage that add tasks to the RunStep job can be a command-line script that uses HPC command-line commands, an HPC PowerShell script that uses HPC PowerShell cmdlets, or a script or application that uses the HPC managed or unmanaged API. Your choice of which option to use for your custom PreStep implementation depends on the other operations your script may also need to perform, and whether those operations are possible in the given interface or language.

This example provides two alterative implementations of the PreStep stage. One implementation is a batch file that uses the HPC [job add](http://go.microsoft.com/fwlink/p/?linkid=165379) command (http://go.microsoft.com/fwlink/p/?linkid=165379), and the other is a console application written in C# that uses the HPC managed API.

**To create the command for the PreStep stage as a batch file**

1.  In a text editor such as Notepad, paste the following lines.

    ```XML
    @echo off
    for %%a in (%DIAG_NODELIST%) do (job add %DIAG_RUNSTEP_JOBID% /requirednodes:%%a hostname.exe)
    exit /b 0
    ```

    

    This batch file uses the **job add** command to add a task to the job that the diagnostic service automatically creates for the RunStep job. The diagnostic service stores the job identifier for this job in the DIAG\_RUNSTEP\_JOBID environment variable, and the list of nodes that the user specified for the test in the DIAG\_NODELIST environment variable.

2.  Save the file as C:\\SampleTests\\JobTest.bat on the head node of your HPC cluster.

If you need to perform other tasks in the PreStep stage for your command, you may want to use a different interface for modifying jobs that is more suited for your tasks. This next example uses the HPC managed API in C#.

**To create the command for the PreStep stage as a console application in C#**

1.  On the **File** menu in Visual Studio® 2008, point to **New** and click **Project**.

2.  In the **New Project** dialog box, click **Visual C#** under **Project Types**, click **Console Application** under **Templates**, and type **AddTask** in the **Name** box, then click **OK**.

3.  On the **Project** menu, click **Add Reference**.

4.  On the **Browse** tab of the **Add Reference** dialog box, navigate to the folder in which you have the HPC Pack 2008 R2 SDK installed, double-click **Bin** and click **Microsoft.Hpc.Scheduler.dll**, then click **OK**.

5.  After the four **using** statements in the code stub file on the **Program.cs** tab, add the following line of code.

    ```CSharp
    using Microsoft.Hpc.Scheduler;
    ```

    

6.  Inside the Main function in the code, add the following line of code to get the identifier of the job that the diagnostic service automatically created for the RunStep stage, which the diagnostic service stores in the DIAG\_RUNSTEP\_JOBID environment variable and which will be supplied as the first argument for the PreStep command.

    ```CSharp
    int jobid = Int32.Parse(args[0]);       //RunStep job identifier
    ```

    

7.  After the code that you added in the previous step, but before the end of the Main function, add the following lines of code.

    ```CSharp
    IScheduler scheduler = new Scheduler();
    scheduler.Connect(args[2]);
    ```

    

    This code creates a new Scheduler object and uses the [IScheduler.Connect](http://go.microsoft.com/fwlink/p/?linkid=165380) method (http://go.microsoft.com/fwlink/p/?linkid=165380) to connect to the scheduler on the head node specified in the third argument of PreStep command.

8.  After the code that you added in the previous step, but still before the end of the Main function, add the following lines of code.

    ```CSharp
    ISchedulerJob job = scheduler.OpenJob(jobid);
    job.AutoCalculateMax = false;
    job.AutoCalculateMin = false;
    ```

    

    This code uses the [IScheduler.OpenJob](http://go.microsoft.com/fwlink/p/?linkid=165381) method (http://go.microsoft.com/fwlink/p/?linkid=165381) to open the job that the diagnostic service automatically created for the RunStep stage, and sets the [AutoCalculateMax](http://go.microsoft.com/fwlink/p/?linkid=165382) property (http://go.microsoft.com/fwlink/p/?linkid=165382) and [AutoCalculateMin](http://go.microsoft.com/fwlink/p/?linkid=165383) property (http://go.microsoft.com/fwlink/p/?linkid=165383) of the job to **false**.

9.  After the code that you added in the previous step, but still before the end of the Main function, add the following lines of code.

    ```CSharp
    string nodelist = args[3];

    int nodecount = 0;

    foreach (string node in nodelist.Split(','))
    {

        ISchedulerTask task = job.CreateTask();
        task.CommandLine = args[1];             //Sample command line


        IStringCollection nodes = scheduler.CreateStringCollection();
     
        nodes.Add(node);
        task.RequiredNodes = nodes;

        task.MinimumNumberOfCores = 1;
        task.MaximumNumberOfCores = 1;

        job.AddTask(task);
       
        nodecount++;
    }
    ```

    

    This code gets the list of nodes that the user specified through the test, which the diagnostic service stores in the DIAG\_NODELIST environment variable and which is supplied as the fourth argument for the PreStep command.

    The code splits the list into individual nodes, and uses the [ISchedulerJob.CreateTask](http://go.microsoft.com/fwlink/p/?linkid=165458) method (http://go.microsoft.com/fwlink/p/?linkid=165458) to create a task for each node. For that task, the code sets the value of the [CommandLine](http://go.microsoft.com/fwlink/p/?linkid=165459) property (http://go.microsoft.com/fwlink/p/?linkid=165459) to the value of the second argument, the [RequiredNodes](http://go.microsoft.com/fwlink/p/?linkid=165461) property (http://go.microsoft.com/fwlink/p/?linkid=165461) to the name of the node for which the task was created, and the [MinimumNumberOfCores](http://go.microsoft.com/fwlink/p/?linkid=165460) property (http://go.microsoft.com/fwlink/p/?linkid=165460) and [MaximumNumberOfCores](http://go.microsoft.com/fwlink/p/?linkid=165462) property (http://go.microsoft.com/fwlink/p/?linkid=165462) of the task to 1. The code then uses the [ISchedulerJob.AddTask](http://go.microsoft.com/fwlink/p/?linkid=165463) method (http://go.microsoft.com/fwlink/p/?linkid=165463) to add the task to RunStep job.

10. After the code that you added in the previous step, but still before the end of the Main function, add the following lines of code.

    ```CSharp
    job.MinimumNumberOfCores = nodecount;
    job.MaximumNumberOfCores = nodecount;

    job.Commit();
    ```

    

    This code sets the **MinimumNumberOfCores** and **MaximumNumberOfCores** properties of the RunStep job to the total number of nodes that the user specified for the diagnostic test, then uses the **ISchedulerJob.Commit** method to save the changes to the job.

11. On the **File** menu, click **Save Program.cs**.

12. In the **Solution Configurations** box on the **Standard** toolbar, click **Release**.

13. On the **Build** menu, click **Build Solution**.

14. In Windows Explorer or at a command prompt, confirm that the AddTask.exe file was created in the %USERPROFILE%\\Documents\\Visual Studio 2008\\Projects\\AddTask\\AddTask\\bin\\Release folder.

## Step 2: Create an XML file to define the custom test

The XML file in this example contains many of the same elements as the XML file for the example in [Steps for Creating a Custom Diagnostic Test that Runs an Existing Command](steps-for-creating-a-custom-diagnostic-test-that-runs-an-existing-command.md), and you can find information about those elements in that topic.

The one addition to the XML in this example is the [**PreStep**](prestep-element.md) element, which includes a **Command** attribute that specifies the command for the script of application that you want to run in the PreStep stage.

This example also does not include a [**RunStep**](runstep-element.md) element. You do not specify a command to run in the RunStep stage, because you already provided an implementation of the RunStep stage by adding tasks to the RunStep job in the PreStep stage.

**To create an XML file that defines the custom test**

1.  In a text editor such as Notepad, paste the following text to define the metadata for the test.

    ```XML
    <DiagnosticTests>
        <DiagnosticTest
            Name="Sample Job Test"
            Description="Submits a job that runs the hostname.exe command."
            Company="Contoso, Ltd"
            Suite="Sample"
            Alias="jobtest">
    ```

    

2.  After the text that you inserted in the previous step, paste the following text to define the command that you want to run for the PreStep stage of the diagnostic test, if you used the batch file example for the PreStep command.

    ```XML
            <PreStep Command="c:\SampleTests\JobTest.bat"/>
    ```

    

    or

    After the text that you inserted in the previous step, paste the following text to define the command that you want to run for the PreStep stage of the diagnostic test, if you used the C# example for the PreStep command.

    ```XML
            <PreStep Command="&amp;quot;%USERPROFILE%\Documents\Visual Studio 2008\Projects\AddTask\AddTask\bin\Release\AddTask.exe&amp;quot; %DIAG_RUNSTEP_JOBID% hostname.exe %CCP_SCHEDULER% %DIAG_NODELIST%"/>
    ```

    

    The path for the addtask.exe program in this example must be surrounded by quotation marks (") because the path includes spaces. Quotation marks are special characters in XML, so you need the specify the `&quot;` character entity to specify them. For information on character entities, see [Character and Entity References](http://go.microsoft.com/fwlink/p/?linkid=165386) (http://go.microsoft.com/fwlink/p/?linkid=165386).

3.  After the text that you inserted in the previous step, paste the following text to add the necessary closing tags to create a valid XML file.

    ```XML
        </DiagnosticTest>
    </DiagnosticTests>
    ```

    

4.  Save the file as C:\\SampleTests\\JobTest.xml.

## Step 3: Add the test to an HPC Cluster

In Windows HPC Server 2008 R2, you can add diagnostic tests to an HPC cluster by using HPC PowerShell or at the command prompt.

**To add a custom diagnostic test to an HPC cluster by using HPC PowerShell**

1.  On the head node, click **Start**, point to **All Programs**, click **Microsoft HPC Pack 2008 R2**, right-click **HPC PowerShell**, and then click **Run as administrator**.

2.  In **HPC PowerShell**, type the following cmdlet to add the test:

    **Add-HpcTest -File C:\\SampleTests\\JobTest.xml**

    If you need to remove the test from the HPC cluster later, type the **Remove-HpcTest -Alias jobtest** cmdlet.

3.  Type the following cmdlet to verify that the test was added to the HPC cluster:

    **Get-HpcTest -Alias jobtest**

4.  Type the following cmdlet to verify that the metadata and command for the test were correctly added to the HPC cluster:

    **Get-HpcTestDetail -Alias jobtest**

**To add a custom diagnostic test to an HPC cluster at a command prompt**

1.  Open a command prompt window and type the following command to add the test:

    **test Add C:\\SampleTests\\JobTest.xml**

    If you need to remove the test from the HPC cluster later, type the following command:

    **test Remove jobtest**

2.  Type the following command to verify that the test was added to the HPC cluster:

    **test ListTests**

3.  Type the following command to verify that the metadata, parameters, and command for the test were correctly added to the HPC cluster:

    **test ViewTest jobtest**

## Step 4: Run the test and view the results

After you add a custom diagnostic test to an HPC cluster, you can use HPC Cluster Manager, HPC PowerShell, or command-line commands to run the test and view the results in the same way that you do for built-in diagnostic tests that Windows HPC Server 2008 R2 provides.

For information about using HPC Cluster Manager, see Overview of HPC Cluster Manager in the [HPC Cluster Manager Help](http://go.microsoft.com/fwlink/p/?linkid=124146) (http://go.microsoft.com/fwlink/p/?linkid=124146).

**To run the custom diagnostic test in HPC Cluster Manager**

1.  In **Diagnostics**, in the **Navigation Pane**, double-click **Tests** to display the list of companies that provided the diagnostic tests that are available on your HPC cluster, if the list is not already visible.

2.  Double-click **Contoso, Ltd** to display the list of suites, then click **Sample** to view the list of tests in the **Sample** suite.

3.  In the views pane, right-click the **Sample Job Test** test and click **Run**.

4.  In the **Run Diagnostic Tests** dialog box, select **All nodes** and click **Run**.

5.  If the **Run Test** dialog box appears, click **OK**.

### Additional considerations

To open **HPC Cluster Manager**, click **Start**, point to **All Programs**, click **Microsoft HPC Pack 2008 R2**, and then click **HPC Cluster Manager**. If the **User Account Control** dialog box appears, confirm that the action it displays is what you want, and then click **Continue**.

**To run the custom diagnostic test in HPC PowerShell or at a command prompt**

1.  In **HPC PowerShell**, type the following cmdlet:

    **Invoke-HpcTest -Alias jobtest -NodeName** *ListOfNodesToRunTest*

    or

    At a command prompt, type the following command:

    **test run jobtest -nodes:***ListOfNodesToRunTest*

2.  Note the run identifier that appears in the output of the cmdlet or at the command prompt so that you can view the results of the test later.

> [!Note]
>
> To specify parameter values for a diagnostic test in HPC PowerShell, use the *Parameters* parameter with a value that has the following format: @{*ParameterName1*="*Value1*"\[;*ParameterName2*="*vValue2*";...\]}
>
> To specify a parameter value for a diagnostic test at the command prompt, include a parameter in the command with the following format: -*ParameterName*:"*Value"*

 

**To view the results of the custom test in HPC Cluster Manager**

1.  In **Diagnostics**, in the **Navigation Pane**, click **Test Results**.

2.  In the views pane, locate the test result for the **Sample Job Test** test and wait until the **State** for the result changes to **Complete**.

3.  Click the test result for the **Sample Job Test** test.

4.  In the **Detail** pane, click the **Result** tab to view the report on the results for the diagnostic test.

**To view the results of the custom test in HPC PowerShell**

1.  In HPC PowerShell, type the following cmdlet to verify that the test finished and to see the overall results of the test.

    **Get-HpcTestResultDetail -RunId** *RunIdentifier*

2.  Type the following cmdlet to export the report for the test run to a folder:

    **Export-HpcTestResult -RunId** *RunIdentifier* **-Path C:\\SampleTests\\JobTest**

3.  In Windows Explorer, navigate to C:\\SampleTests\\JobTest and then double-click **Report.html**.

**To view the results of the custom test at a command prompt**

1.  Open a command prompt window and type the following command to verify that the test finished and to see the overall results of the test.

    **test ViewRun** *RunIdentifier*

2.  Type the following command to view the report for the test run:

    **test ViewResult** *RunIdentifier*

The report for the test should appear similar to the following.

``` syntax
## COMPUTENODE1 --> Finished

ComputeNode1
## 

## COMPUTENODE2 --> Finished

ComputeNode2
## 

## HEADNODE --> Finished

HeadNode
## 

```

 

 



