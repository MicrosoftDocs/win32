---
Description: 'Windows&\#160;HPC&\#160;Server&\#160;2008&\#160;R2 provides a way to simplify the creation of a custom diagnostic test that validates whether the result of the test is the same on all of the nodes on which the test ran.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '06fcbe1e-18c9-4607-a918-e6854571700d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Steps for Creating a Custom Diagnostic Test that Checks that a Result is Consistent throughout an HPC Cluster
---

# Steps for Creating a Custom Diagnostic Test that Checks that a Result is Consistent throughout an HPC Cluster

Windows HPC Server 2008 R2 provides a way to simplify the creation of a custom diagnostic test that validates whether the result of the test is the same on all of the nodes on which the test ran. To create this kind of diagnostic test, you include an [**AutoGenerateResult**](autogenerateresult.md) element in the XML file that defines the test, and designate the test type as Consistency.

When you designate a custom diagnostic test as a Consistency test, you do not need to implement a PostStep stage that compares all of results from the different nodes. The diagnostic service handles this comparison for you. The diagnostic service also automatically creates a report that summarizes whether the results were the same for all nodes, and lists the results for all of the nodes.

This example creates a test that checks that the execution policy in Windows PowerShell is the same on all of the nodes on which the user runs the test.

## Step 1: Create an XML file to define the custom test

The XML file in this example contains many of the same elements as the XML file for the example in [Steps for Creating a Custom Diagnostic Test that Runs an Existing Command](steps-for-creating-a-custom-diagnostic-test-that-runs-an-existing-command.md), and you can find information about those elements in that topic. The main changes for the XML in this example consist of the following items:

-   The addition of an [**AutoGenerateResult**](autogenerateresult.md) element to indicate that the test is a Consistency test and that the diagnostic service should automatically generate the report for that type of test.

-   The relocation of the [**Parameters**](parameters--diagnostictest--element.md) element and the [**Parameter**](parameter-element.md) element it contains so that it is the child element of the [**RunStep**](runstep-element.md) element rather than the [**DiagnosticTest**](diagnostictest-element.md) element. This change is specific to the RunStep command that this test uses, and is not a change required for all consistency tests.

    This change makes the parameter specific to the RunStep stage of the test, rather than global for the entire test. The user cannot set the value of a stage-specific parameter when they run the test. The test developer sets the value of this type of parameter in the XML file, and uses it to specify parameters for the command that do not require user input.

**To create an XML file that defines the custom test**

1.  In a text editor such as Notepad, paste the following text to define the metadata for the test.

    ```XML
    <DiagnosticTests>
        <DiagnosticTest
            Name="Check PowerShell Execution Policy Consistency"
            Description="Checks that the value of the PowerShell Execution Policy is consistent on all nodes."
            Company="Contoso, Ltd"
            Suite="PowerShell"
            Alias="ChkPSEPCons">
    
    ```

    

2.  After the text that you inserted in the previous step, paste the following text to designate the diagnostic test as a test that validates whether its result is the same on all of the nodes of the HPC cluster.

    ```XML
                    <AutoGenerateResult TestType="Consistency"/>
    ```

    

3.  After the text that you inserted in the previous step, paste the following text to define the command that the test will run.

    ```XML
            <RunStep Command="powershell.exe">
            <Parameters>
                <Parameter Name="Command" Value="Get-ExecutionPolicy" Format="-{0} {1}"/>
            </Parameters>
            </RunStep>
    ```

    

    This combination of the Command attribute of the RunStep elements and the Parameter element results in the test running the following command for the RunStep stage:

    **powershell.exe -Command Get-ExecutionPolicy**

4.  After the text that you inserted in the previous step, paste the following text to add the necessary closing tags to create a valid XML file.

    ```XML
        </DiagnosticTest>
    </DiagnosticTests>
    ```

    

5.  Save the file as C:\\SampleTests\\PSPolicyConsistency.xml on the head node of the HPC cluster.

## Step 2: Add the test to an HPC Cluster

In Windows HPC Server 2008 R2, you can add diagnostic tests to an HPC cluster by using HPC PowerShell or at the command prompt.

**To add a custom diagnostic test to an HPC cluster by using HPC PowerShell**

1.  On the head node, click **Start**, point to **All Programs**, click **Microsoft HPC Pack 2008 R2**, right-click **HPC PowerShell**, and then click **Run as administrator**.

2.  In **HPC PowerShell**, type the following cmdlet to add the test:

    **Add-HpcTest -File C:\\SampleTests\\PSPolicyConsistency.xml**

    If you need to remove the test from the HPC cluster later, type the **Remove-HpcTest -Alias ChkPSEPCons** cmdlet.

3.  Type the following cmdlet to verify that the test was added to the HPC cluster:

    **Get-HpcTest -Alias ChkPSEPCons**

4.  Type the following cmdlet to verify that the metadata and command for the test were correctly added to the HPC cluster:

    **Get-HpcTestDetail -Alias ChkPSEPCons**

**To add a custom diagnostic test to an HPC cluster at a command prompt**

1.  Open a command prompt window and type the following command to add the test:

    **test Add C:\\SampleTests\\PSPolicyConsistency.xml**

    If you need to remove the test from the HPC cluster later, type the following command:

    **test Remove ChkPSEPCons**

2.  Type the following command to verify that the test was added to the HPC cluster:

    **test ListTests**

3.  Type the following command to verify that the metadata, parameters, and command for the test were correctly added to the HPC cluster:

    **test ViewTest ChkPSEPCons**

## Step 3: Run the test and view the results

After you add a custom diagnostic test to an HPC cluster, you can use HPC Cluster Manager, HPC PowerShell, or the command prompt window to run the test and view the results in the same way that you do for built-in diagnostic tests that Windows HPC Server 2008 R2 provides.

For information about using HPC Cluster Manager, see Overview of HPC Cluster Manager in the [HPC Cluster Manager Help](http://go.microsoft.com/fwlink/p/?linkid=124146) (http://go.microsoft.com/fwlink/p/?linkid=124146).

**To run the custom diagnostic test in HPC Cluster Manager**

1.  In **Diagnostics**, in the **Navigation Pane**, double-click **Tests** to display the list of companies that provided the diagnostic tests that are available on your HPC cluster, if the list is not already visible.

2.  Double-click **Contoso, Ltd** to display the list of suites, then click **PowerShell** to view the list of tests in the **PowerShell** suite.

3.  In the views pane, right-click the **Check PowerShell Execution Policy Consistency** test and click **Run**.

4.  In the **Run Diagnostic Tests** dialog box, select **All nodes** and click **Run**.

5.  If the **Run Test** dialog box appears, click **OK**.

### Additional considerations

To open **HPC Cluster Manager**, click **Start**, point to **All Programs**, click **Microsoft HPC Pack 2008 R2**, and then click **HPC Cluster Manager**. If the **User Account Control** dialog box appears, confirm that the action it displays is what you want, and then click **Continue**.

**To run the custom diagnostic test in HPC PowerShell or at a command prompt**

1.  In **HPC PowerShell**, type the following cmdlet:

    **Invoke-HpcTest -Alias ChkPSEPCons -NodeName** *list\_of\_nodes\_to\_run\_test*

    or

    At a command prompt, type the following command:

    **test run ChkPSEPCons -nodes:***list\_of\_nodes\_to\_run\_test*

2.  Note the run identifier that appears in the output of the cmdlet or at the command prompt so that you can view the results of the test later.

> [!Note]
>
> To specify parameter values for a diagnostic test in HPC PowerShell, use the *Parameters* parameter with a value that has the following format: @{*parameter\_name\_1*="*value1*"\[;*parameter\_name\_2*="*value2*";...\]}
>
> To specify a parameter value for a diagnostic test at the command prompt, include a parameter in the command with the following format: -*parameter\_name*:"*value"*

 

**To view the results of the custom test in HPC Cluster Manager**

1.  In **Diagnostics**, in the **Navigation Pane**, click **Test Results**.

2.  In the views pane, locate the test result for the **Check PowerShell Execution Policy Consistency** test and wait until the **State** for the result changes to **Success** or **Failure**.

3.  Click the test result for the **Check PowerShell Execution Policy Consistency** test.

4.  In the **Detail** pane, click the **Result** tab to view the report on the results for the diagnostic test. The report includes a Summary section that indicates whether the result of the command was the same on all of the nodes, and a section for each node that shows the output of the command on that node.

**To view the results of the custom test in HPC PowerShell**

1.  In HPC PowerShell, type the following cmdlet to verify that the test finished and to see the overall results of the test.

    **Get-HpcTestResultDetail -RunId** *run\_identifier*

2.  Type the following cmdlet to export the report for the test run to a folder:

    **Export-HpcTestResult -RunId** *run\_identifier* **-Path C:\\SampleTests\\PSPolicyConsistency**

3.  In Windows Explorer, navigate to C:\\SampleTests\\PSPolicyConsistency, and then double-click **Report.html**.

**To view the results of the custom test at a command prompt**

1.  Open a command prompt window and type the following command to verify that the test finished and to see the overall results of the test.

    **test ViewRun** *run\_identifier*

2.  Type the following command to view the report for the test run:

    **test ViewResult** *run\_identifier*

 

 



