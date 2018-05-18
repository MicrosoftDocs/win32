---
Description: 'The simplest kind of custom diagnostic test that you can create is a test that runs an existing command- line command or script that produces a small amount of output.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3189413b-fbf3-46b3-b06f-40b60d9170cb'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Steps for Creating a Custom Diagnostic Test that Runs an Existing Command
---

# Steps for Creating a Custom Diagnostic Test that Runs an Existing Command

The simplest kind of custom diagnostic test that you can create is a test that runs an existing command- line command or script that produces a small amount of output. If you are using existing commands and scripts, you do not need to implement and test your own scripts or applications for each of the test stages.

Also, when you want to create a test that runs an existing command, you can often customize just the RunStep stage of the test. You do not need to customize the PreStep stage if you do not need to perform any validation before the test runs, nor do you need to customize the PostStep stage if the output of the command is simple.

The example in this section creates a custom diagnostic test that runs an existing command to determine the amount of free disk space available for a specified drive on each of the nodes of the cluster. The output of the **fsutil volume diskfree** command that the test runs is fairly short and simple, so the test can reasonably display the default result, which concatenates the output of the command from all of the nodes just as the HPC **clusrun** command does.

## Step 1: Create an XML file to define the custom test

To define a custom diagnostic test, you create an XML file that contains the metadata and commands for the test. For this example, the XML file contains the following elements:



| Element                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiagnosticTests**](diagnostictests-element.md)<br/>        | Serves as the root element of the file, and contains the definitions of all of the tests in the file.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**DiagnosticTest**](diagnostictest-element.md)<br/>          | Defines an individual diagnostic test, and specifies the metadata for the test through the values of its attributes.<br/> The metadata includes the name, description, company, suite, alias, version, and exclusivity of the test.<br/>                                                                                                                                                                                                                                                                                                                                                                               |
| [**Parameters**](parameters--diagnostictest--element.md)<br/> | Contains a set of one or more parameters for the diagnostic test or a stage in the diagnostic test.<br/> If the [**Parameters**](parameters--diagnostictest--element.md) element is a child of the [**DiagnosticTest**](diagnostictest-element.md) element, as in this example, the parameters are global and apply to the entire diagnostic test. If the **Parameters** element is a child of the [**PreStep**](prestep-element.md), [**RunStep**](runstep-element.md), or [**PostStep**](poststep-element.md) element, the parameters apply only to the stage of the test that corresponds to the element.<br/> |
| [**Parameter**](parameter-element.md)<br/>                    | Defines a parameter for a diagnostic test or a stage in a diagnostic test.<br/> If the parameter is global and has a **Visibility** attribute with a value of True, as in this example, the user can set the value of the parameter when the user runs the test.<br/> Other attributes of this parameter define the name, switch name, data type, default value, allowed values, minimum value, and maximum value for the parameter, as well as the format to use to include the parameter in the commands for the PreStep, RunStep, and PostStep stages of the test.<br/>                                       |
| [**RunStep**](runstep-element.md)<br/>                        | Specifies the command to run for the RunStep stage of the diagnostic test. This command runs on all of the nodes that the user specified when starting the test, unless the PreStep stage of the test changes the list of nodes for the test.<br/>                                                                                                                                                                                                                                                                                                                                                                           |



 

**To create an XML file that defines the custom test**

1.  In a text editor such as Notepad, paste the following text to define the metadata for the test.

    ```XML
    <DiagnosticTests>
        <DiagnosticTest
            Name="Free Disk Space"
            Description="Checks the amount of disk space free on the specified drive."
            Company="Contoso, Ltd"
            Suite="Sample"
            Alias="diskspace">
    
    ```

    

2.  After the text that you inserted in the previous step, paste the following text to define a parameter for the test.

    ```XML
            <Parameters>
                <Parameter Name="Drive" SwitchName="Drive" Type="String" Visibility="True" 
                    Description="The letter name of the drive for which you want to check the amount of free disk space, without a colon (:) or backslash (). The default is C." 
                    DefaultValue="C" Format="{1}:"/>
            </Parameters>
    ```

    

    The Drive parameter in this example specifies the drive on which the test should check the amount of free disk space. This parameter is a positional parameter rather than a named parameter in the command, so the **Format** attribute does not include the *{0}* placeholder that represents the switch name. The *{1}* placeholder represents the value for the parameter.

    You can also set the values of environment variables for a diagnostic test by including the [**EnvironmentVariables**](environmentvariables--diagnostictest--element.md) and [**Variable**](variable-element.md) elements in the XML file that defines the diagnostic test.

3.  After the text that you inserted in the previous step, paste the following text to define the command that the test will run.

    ```XML
            <RunStep Command="fsutil volume diskfree"/>
    ```

    

    This combination of the Command attribute of the RunStep element and the Parameter element that you added earlier in this procedure results in the test running the following command by default for the RunStep stage:

    **fsutil volume diskfree C:**

    The value of the **Command** attribute can be any command that you can run from a command prompt without additional prompting for input, including command-line commands, command scripts and batch files, applications, and Windows PowerShell cmdlets and scripts run with the PowerShell.exe command. For an example command that runs a Windows PowerShell cmdlet, see [Steps for Creating a Custom Diagnostic Test that Checks that a Result is Consistent Throughout an HPC Cluster](steps-for-creating-a-custom-diagnostic-test-that-checks-that-a-result-is-consistent-throughout-an-hpc-cluster.md).

4.  After the text that you inserted in the previous step, paste the following text to add the necessary closing tags to create a valid XML file.

    ```XML
        </DiagnosticTest>
    </DiagnosticTests>
    ```

    

5.  Save the file as C:\\SampleTests\\DiskSpaceTest.xml on the head node of the HPC cluster.

## Step 2: Add the test to an HPC Cluster

In Windows HPC Server 2008 R2, you can add diagnostic tests to an HPC cluster by using HPC PowerShell or at the command prompt.

**To add a custom diagnostic test to an HPC cluster by using HPC PowerShell**

1.  On the head node, click **Start**, point to **All Programs**, click **Microsoft HPC Pack 2008 R2**, right-click **HPC PowerShell**, then click **Run as administrator**.

2.  In **HPC PowerShell**, type the following cmdlet to add the test:

    **Add-HpcTest -File C:\\SampleTests\\DiskSpaceTest.xml**

    If you need to remove the test from the HPC cluster later, type the **Remove-HpcTest -Alias diskspace** cmdlet.

3.  Type the following cmdlet to verify that the test was added to the HPC cluster:

    **Get-HpcTest -Alias diskspace**

4.  Type the following command to verify that the metadata, parameters, and command for the test were correctly added to the HPC cluster:

    **Get-HpcTestDetail -Alias diskspace**

**To add a custom diagnostic test to an HPC cluster at a command prompt**

1.  Open a command prompt window and type the following command to add the test:

    **test Add C:\\SampleTests\\DiskSpaceTest.xml**

    If you need to remove the test from the HPC cluster later, type the following command:

    **test Remove diskspace**

2.  Type the following command to verify that the test was added to the HPC cluster:

    **test ListTests**

3.  Type the following command to verify that the metadata, parameters, and command for the test were correctly added to the HPC cluster:

    **test ViewTest diskspace**

## Step 3: Run the test and view the results

After you add a custom diagnostic test to an HPC cluster, you can use HPC Cluster Manager, HPC PowerShell, or the command prompt to run the test and view the results in the same way that you do for built-in diagnostic tests that Windows HPC Server 2008 R2 provides.

For information about using HPC Cluster Manager, see Overview of HPC Cluster Manager in the [HPC Cluster Manager Help](http://go.microsoft.com/fwlink/p/?linkid=124146) (http://go.microsoft.com/fwlink/p/?linkid=124146).

**To run the custom diagnostic test in HPC Cluster Manager**

1.  In **Diagnostics**, in the **Navigation Pane**, double-click **Tests** to display the list of companies that provided the diagnostic tests that are available on your HPC cluster, if the list is not already visible.

2.  Double-click **Contoso, Ltd** to display the list of suites, then click **Sample** to view the list of tests in the **Sample** suite.

3.  In the views pane, right-click the **Free Disk Space** test and click **Run**.

4.  In the **Run Diagnostic Tests** dialog box, select **All nodes** and click **Run**.

    You can specify values for the parameters of test by clicking **Configure Test Parameters** in the **Run Diagnostic Tests** dialog box before you click **Run**, but you should just accept the default value for this example. If you specify a drive that does not exist on all of the nodes in the HPC cluster for this test, the test fails.

5.  If the **Run Test** dialog box appears, click **OK**.

### Additional considerations

To open **HPC Cluster Manager**, click **Start**, point to **All Programs**, click **Microsoft HPC Pack 2008 R2**, and then click **HPC Cluster Manager**. If the **User Account Control** dialog box appears, confirm that the action it displays is what you want, and then click **Continue**.

**To run the custom diagnostic test in HPC PowerShell or at a command prompt**

1.  In **HPC PowerShell**, type the following cmdlet:

    **Invoke-HpcTest -Alias diskspace -NodeName** *ListOfNodesToRunTest*

    or

    At a command prompt, type the following command:

    **test run diskspace -nodes:***ListOfNodesToRunTest*

2.  Note the run identifier that appears in the output of the cmdlet or at the command prompt so that you can view the results of the test later.

> [!Note]
>
> To specify parameter values for a diagnostic test in HPC PowerShell, use the *Parameters* parameter with a value that has the following format: @{*ParameterName1*="*Value1*"\[;*ParameterName2*="*vValue2*";...\]}
>
> To specify a parameter value for a diagnostic test at the command prompt, include a parameter in the command with the following format: -*ParameterName*:"*Value"*

 

**To view the results of the custom test in HPC Cluster Manager**

1.  In **Diagnostics**, in the **Navigation Pane**, click **Test Results**.

2.  In the views pane, locate the test result for the **Free Disk Space** test and wait until the **State** for the result changes to **Complete**.

3.  Click the test result for the **Free Disk Space** test.

4.  In the **Detail** pane, click the **Result** tab to view the output of the command on each of the nodes in the cluster.

**To view the results of the custom test in HPC PowerShell**

1.  In HPC PowerShell, type the following cmdlet to verify that the test finished and to see the overall results of the test.

    **Get-HpcTestResultDetail -RunId** *RunIdentifier*

2.  Type the following cmdlet to export the report for the test run to a folder:

    **Export-HpcTestResult -RunId** *RunIdentifier* **-Path C:\\SampleTests\\DiskSpaceResult**

3.  In Windows Explorer, navigate to C:\\SampleTests\\DiskSpaceResult and then double-click **Report.html**.

**To view the results of the custom test at a command prompt**

1.  Open a command prompt window and type the following command to verify that the test finished and to see the overall results of the test.

    **test ViewRun** *RunIdentifier*

2.  Type the following command to view the report for the test run:

    **test ViewResult** *RunIdentifier*

The report for the test should appear similar to the following.

``` syntax
## COMPUTENODE1 --> Finished

Total # of free bytes        : 33324670976
Total # of bytes             : 41940938752
Total # of avail free bytes  : 33324670976
## 

## COMPUTENODE2 --> Finished

Total # of free bytes        : 33496813568
Total # of bytes             : 41940938752
Total # of avail free bytes  : 33496813568
## 

## HEADNODE --> Finished

Total # of free bytes        : 23128948736
Total # of bytes             : 41940938752
Total # of avail free bytes  : 23128948736
## 

```

## Related topics

<dl> <dt>

[Overview of the Steps for Creating a Custom Diagnostic Test](overiew-of-the-steps-for-creating-a-custom-diagnostic-test.md)
</dt> </dl>

 

 




