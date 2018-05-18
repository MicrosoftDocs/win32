---
Description: 'As an alternative to running existing commands for a diagnostic test, you can create your own scripts or console applications to run in each of the stages of a diagnostic test.TestRunID\\NodeName.out on the head node, and combines these output files as the Poststep.result file in the same location. If you do not implement a custom PostStep stage or specify the diagnostic test as a consistency or comparison test, HPC Cluster Manager displays the contents of the Poststep.result file on the Result tab for the test result.Steps for Creating a Custom Diagnostic Test that Implements the RunStep and PostStep Stages. For an example of a consistency test, see Steps for Creating a Custom Diagnostic Test that Checks that a Result is Consistent throughout an HPC Cluster. For an example of a comparison test, see Steps for Creating a Custom Diagnostic Test that Checks that a Result Matches an Expected Value throughout an HPC Cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4a51387a-2da9-4102-8a2b-75116147c6a8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Steps for Creating a Custom Diagnostic Test that Implements the PreStep and RunStep Stages
---

# Steps for Creating a Custom Diagnostic Test that Implements the PreStep and RunStep Stages

As an alternative to running existing commands for a diagnostic test, you can create your own scripts or console applications to run in each of the stages of a diagnostic test.

For the PreStep stage, a custom script can perform tasks to setup and validate the test. This PreStep script runs only on the head node. The PreStep script can change the list of nodes on which the RunStep stage should run and change the values of parameters and environment variables. To provide this updated information to the RunStep stage, the PreStep script can create a PreStepResult.xml file. The Diagnostic Helper API provides a programmatic way to create this XML file.

A RunStep script performs the actual work of the diagnostic test, and runs on all of the nodes that the user specified for the test, unless the PreStep script changed the node list. If the PreStep script changed the node list, the RunStep script runs on those nodes instead.

The diagnostic service saves the standard output and standard error streams of the RunStep script for each node in a file named %ProgramFiles%\\Microsoft HPC Pack 2008 R2\\Data\\Diagnostics\\*TestRunID*\\*NodeName*.out on the head node, and combines these output files as the Poststep.result file in the same location. If you do not implement a custom PostStep stage or specify the diagnostic test as a consistency or comparison test, **HPC Cluster Manager** displays the contents of the Poststep.result file on the **Result** tab for the test result.

The example in this section checks whether the operating system culture on the nodes in the test match the operating system culture on the head node for the HPC cluster. This example provides a custom implementation of the PreStep stage to get the value of the operating system culture on the head node and to filter out nodes that are not online or that do not have a node health of OK from the node list. This example also provides a custom implementation of the RunStep stage that gets the operating system culture of each node in the test and compares it to the operating system culture of the head node.

You can provide a custom implementation for the PostStep stage as well as the PreStep and RunStep stages of a diagnostic test, although the example in this section only provides custom implementations of the PreStep and RunStep stages.

For an example of a custom implementation of the PostStep stage, see [Steps for Creating a Custom Diagnostic Test that Implements the RunStep and PostStep Stages](steps-for-creating-a-custom-diagnostic-test-that-implements-the-runstep-and-poststep-stages.md). For an example of a consistency test, see [Steps for Creating a Custom Diagnostic Test that Checks that a Result is Consistent throughout an HPC Cluster](steps-for-creating-a-custom-diagnostic-test-that-checks-that-a-result-is-consistent-throughout-an-hpc-cluster.md). For an example of a comparison test, see [Steps for Creating a Custom Diagnostic Test that Checks that a Result Matches an Expected Value throughout an HPC Cluster](steps-for-creating-a-custom-diagnostic-test-that-checks-that-a-result--matches-an-expected-value-throughout-an-hpc-cluster.md).

## Step 1: Create the script for the PreStep stage

The PreStep stage of a diagnostic test can perform validation and setup tasks for the diagnostic test. These tasks can include:

-   Filtering the list of nodes that the user requested for the test, so that the test runs only on nodes with specific properties, such as having a node state of online.

-   Setting the values of parameters and environment variables for the test programmatically.

This example PreStep script is a Windows PowerShell script that filters the node list so that the test runs only on nodes that have a node state of online and a node health of OK. The script also checks the operating system culture of the head node by running the Get-Culture Windows PowerShell cmdlet.

This PreStep script stores this information in a Microsoft.Hpc.Diagnostics.Helpers.StepResult object, and then uses the XmlSerializeToFile method of that object to create an XML file that contains the information. The RunStep stage can then use the information in this file to get the processed node list and parameter value.

**To create the script for the PreStep stage**

1.  In a text editor such as Notepad, paste the following lines of Windows PowerShell script, which call the System.Reflection.Assembly.LoadFile method to load the DLL for the Diagnostic Helper API for the Windows PowerShell script so that you can create a StepResult.xml file for the PreStep stage.

    ```PowerShell
    # Installing HPC Pack 2008 R2 SDK installs the DLL for the Diagnostic Helper API at 
    # %CCP_SDK%\bin\Microsoft.Hpc.Diagnostics.Helpers.dll.
    $ccpHome = $env:CCP_SDK
    $diagsHelperPath = $ccpHome + "Bin\Microsoft.Hpc.Diagnostics.Helpers.dll";

    if (Test-Path $diagsHelperPath)
    {
        [Reflection.Assembly]::LoadFile($diagsHelperPath) | Out-Null;
    }

    else
    {
        Write-Warning "Could not find Microsoft.Hpc.Diagnostics.Helpers.dll.";
        return -1;
    }
    ```

    

2.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which use the New-Object cmdlet and the constructor for the StepResult class to create a new StepResult object that will contain the objects that represent the information that you want to include in the StepResult.xml file.

    ```PowerShell
    # Create an object as Microsoft.Hpc.Diagnostics.Helpers.StepResult.
    $stepResult = New-Object Microsoft.Hpc.Diagnostics.Helpers.StepResult;
    ```

    

3.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which check that the nodes on which the user chose to run the test are all online and have a node health of OK, and adds the nodes with those properties to the StepResult object.

    ```PowerShell
    # The diagnostic service automatically sets the DIAG_NODELIST environment 
    # variable so that it contains a comma-separated list of the nodes that the 
    # user specified for the test. 
    $nodeList = $Env:DIAG_NODELIST;

    # Counter for nodes that are online and OK. If the there are no nodes that are online and OK, the test 
    # should not run.
    $nodeOutputCount = 0;
    $hpcNodes = @();  
      
        if($nodeList -ne $null)
        {
         
            # Process each node in the list of nodes.
            foreach ($node in $nodeList.Split(','))
            {

                # Check that the node is online and has a node health of OK.
                if(((Get-HpcNode -Name $node).NodeState -eq "Online") -and ((Get-HpcNode -Name $node).NodeHealth -eq "OK"))           

                {

                    # Create a Node object for the node and add it to the StepResult object.
                    $hpcNodes += New-Object Microsoft.Hpc.Diagnostics.Helpers.StepResult+Node($node);
                    $nodeOutputCount++;

                }

                else

                {

                   # Write a warning to the Prestep.result file to provide diagnostic 
                   # information about why the test did not run on one of the nodes 
                   # that the user selected. 
                   $warning = -join ("The following node was either not online or did not have a node health`nof OK, so the test was not run on the node: ", $node)
                   Write-Warning $warning

                }

            }

            $stepResult.Nodes = $hpcNodes;
    ```

    

    The diagnostic service saves the list of the nodes that the user selected for the test in the DIAG\_NODELIST environment variable. This code separates that comma-delimited list into separate node names, then runs the HPC PowerShell Get-HpcNode cmdlet to get NodeState and NodeHealth properties of the HPC PowerShell HPCNode object for each node.

    If the node is online and OK, the code uses the New-Object cmdlet and the constructor for the Microsoft.Hpc.Diagnostics.Helpers.StepResult.Node class to create a Node object for the node, and adds the Node object to the Nodes property of the StepResult object for the PreStep stage so that the RunStep stage will run on the node.

    If the node is not online or not OK, the code does node create a Node object to add to the Nodes property of the StepResult object, but prints a warning instead. If the node in not included in the StepResult object, the RunStep stage will not run on that node.

4.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which get the operating system culture for the head node and add a Parameter object for that operating system culture to the collection of parameters for the StepResult object, so that the test can pass the parameter to the RunStep command.

    ```PowerShell
            $HeadNodeCulture = (Get-Culture).Name      
     
            $Parameter1 = New-Object Microsoft.Hpc.Diagnostics.Helpers.StepResult+Parameter("HeadNodeCulture", $HeadNodeCulture, "-{0} {1}");
            $stepResult.Parameters.Add($Parameter1);     

        }
    ```

    

    This code gets the operating system culture for the head node by calling the Get-Culture Windows PowerShell cmdlet. The code then uses the New-Object Windows PowerShell cmdlet and the constructor for the Microsoft.Hpc.Diagnostics.Helpers.StepResult.Parameter class to create a Parameter object for this value of the operating system culture, and uses the System.Collections.Generic.List.Add to add this Parameter object to the Parameters property of the StepResult object for the PreStep stage so that PreStep stage can provide the value of this parameter to the RunStep stage.

5.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which serialize the content of the StepResult object as the PreStepResult.xml file.

    ```PowerShell
        if($nodeOutputCount -eq 0)
        {

        Write-Warning "None of the nodes for the test are online and have a node health of`nOK, so the test was not run. Check that the nodes on which you want to run the `ntest are online and have a node health of OK, then rerun the test.";
        return -1;

        }

        else 
        {

        $stepResult.XmlSerializeToFile(".\PreStepResult.xml");
        
        }
    ```

    

    This code checks if there were any nodes that were online and OK, and calls the Microsoft.Hpc.Diagnostics.Helpers.StepResult.XmlSerializeToFile method to serialize the contents of the StepResult object to the PreStepResult.xml file if there are nodes that remain on which to run the test. When this script runs in the context of a diagnostic test, the diagnostic service automatically saves the PreStepResult.xml file in the %ProgramFiles%\\Microsoft HPC Pack 2008 R2\\Data\\Diagnostics\\*TestRunID* folder. The diagnostic service checks for the PreStepResult.xml file in this location to provide information for the RunStep stage, so you should not change the location of the file by specifying a different path.

6.  Save the file as C:\\SampleTests\\CultureTestPreStep.ps1 on the head node of your HPC cluster.

## Step 2: Test the script for the PreStep stage

To test your PreStep script, you should run the script from the command prompt on the head node of your HPC cluster before incorporating it into a diagnostic test.

You do not need to run the script on nodes other than the head node, because the PreStep stage of a diagnostic test runs only on the head node.

**To test the script for the PreStep stage**

1.  At a command prompt on the head node of your HPC cluster, type the **set** command to set the DIAG\_NODELIST environment value to a comma-separated list of the nodes in the cluster on which you might want to run the test. For example:

    **set DIAG\_NODELIST=HeadNode,ComputeNode1,ComputeNode2**

    In the context of a diagnostic test, the diagnostic service automatically sets the DIAG\_NODELIST environment variable. To test the script outside of that context, you need to set this environment variable manually.

2.  Type the following command to verify that the Windows PowerShell execution policy allows you to run your Windows PowerShell script:

    **powershell.exe -Command Get-ExecutionPolicy**

    For information about PowerShell execution policies, see [about\_Execution\_Policies](http://go.microsoft.com/fwlink/p/?linkid=165384) (http://go.microsoft.com/fwlink/p/?linkid=165384).

3.  Type the following command to check the node state and node health values for the nodes you added to the DIAG\_NODELIST environment variable:

    **powershell.exe -Command "& {Add-PsSnapin Microsoft.HPC; Get-HpcNode %DIAG\_NODELIST%}"**

4.  Type the following command to check the operating system culture for the head node:

    **powershell.exe -Command Get-Culture**

5.  Type the script for the PreStep stage by specifying it in the Command parameter of the powershell.exe command:

    **powershell.exe -Command "& {Add-PsSnapin Microsoft.HPC; C:\\SampleTests\\CultureTestPreStep.ps1}"**

6.  Verify that the working directory for your command prompt contains a file named PreStepResult.xml.

    The XML in that file should list all of the nodes that you used in the DIAG\_NODELIST environment variable and that are online and have a node health of OK, and should also contain an entry for a parameter with a value for the operating system culture. The following example shows typical contents of the PreStepResult.xml file for this script.

    ```XML
    <?xml version="1.0"?>
    <StepResult xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" NodeName="HEADNODE">
      <Result>NoResult</Result>
      <Message/>
      <ExceptionMessage/>
      <Nodes>
        <Node>COMPUTENODE2<Parameters/></Node>
        <Node>HEADNODE<Parameters/></Node>
      </Nodes>
      <FailedNodes/>
      <Environment/>
      <Parameters>
        <Parameter Name="HeadNodeCulture" Value="en-US" Format="-{0} {1}"/>
      </Parameters>
      <Tables/>
      <BulletPoints/>
    </StepResult>
    ```

    

## Step 3: Create the script for the RunStep stage

As an alternative to running commands for a diagnostic test, you can create your own scripts and console applications to run in the RunStep stage. The RunStep stage runs on all of the nodes in the test, subject to any processing of that node list in the PreStep stage, so your scripts or application files must be accessible from all of the nodes in the HPC cluster.

This example RunStep script is a Windows PowerShell script. The script has one mandatory parameter that specifies the operating system culture of the head node. The script for the PreScript stage described earlier in this section determines this value, and provides it to the RunStep stage by way of the PreStepResult.xml file that the PreStep script created. The diagnostic service automatically gets the parameter values from this file and provides them to the RunStep script.

The RunStep script uses the Get-Culture to get the operating system culture of the node on which it is running. The script that compares this to the operating system culture for the head node, and constructs a message that indicates whether the values match. Finally, the script writes that message to standard output, which is saved to the %ProgramFiles%\\Microsoft HPC Pack 2008 R2\\Data\\Diagnostics\\*TestRunID*\\*NodeName*.out file when the script runs in the context of a diagnostic test.

**To create the script for the RunStep stage**

1.  On the head node of your HPC cluster, create a shared folder named **DiagShare** and grant everyone has read permissions.

2.  In a text editor such as Notepad, paste the following lines of Windows PowerShell script, which declare that the Windows PowerShell script requires a mandatory HeadNodeCulture parameter.

    ```PowerShell
    Param(
    [Parameter(Mandatory=$true)]
    [string] $HeadNodeCulture
    )
    
    ```

    

3.  After the code that you pasted in the previous step, paste the following line of Windows PowerShell script, which uses the Windows PowerShell Get-Culture command to the get operating system culture of the node on which the RunStep stage is running.

    ```PowerShell
    $NodeCulture = (Get-Culture).Name
    
    ```

    

4.  After the code that you pasted in the previous step, paste the following lines of Windows PowerShell script, which compare the operating system culture for the head node to the operating system for the current node and create a message that indicates whether the values matched.

    ```PowerShell
    if ($NodeCulture -eq $HeadNodeCulture)

        {

        $result = -join ("The operating system culture on this node is ",$NodeCulture,", which matches the operating`nsystem culture on the head node.")

        }

    else

        {

        $result = -join ("The operating system culture on this node is ",$NodeCulture,", which does not match the`noperating system culture of ",$HeadNodeCulture," on the head node.")

        }
    ```

    

5.  After the code that you pasted in the previous step, paste the following line of Windows PowerShell script, which writes the message created in the previous step to the output for the script.

    ```PowerShell
    Write-Output $result
    ```

    

6.  Save this script with a name of CultureTestRunStep.ps1 in the shared folder that you created in the first step of this procedure.

When you specify a command for the RunStep stage in the XML file that defines the diagnostic test, you must specify the command in the same way to you would run the command from a command prompt. For Windows PowerShell scripts, you need to run the script using the **powershell.exe** command, and specify the script in the Command parameter.

If a Windows PowerShell script that you want to run for the RunStep stage has parameters of its own, complications arise because the diagnostic service adds the parameters and values to the end of the RunStep command. The **powershell.exe** command interprets these parameters as parameters for the **powershell.exe** command, rather than as parameters for the script, because they do not get incorporated in the value of the Command parameter.

To work around this issue, you can create a command file for the RunStep stage that includes the call to the Windows PowerShell command. This command file can process the parameters that the diagnostic service passes to the RunStep stage and incorporate them into the Command parameter for the **powershell.exe** command in the correct location.

**To create a command to run the script for the RunStep stage**

1.  In a new file in a text editor such as Notepad, type the following text, which checks that the command file was run with the correct syntax.

    ``` syntax
    @echo off
    if NOT %1 == -HeadNodeCulture goto :InvalidSyntax
    if "%2" == "" goto :InvalidSyntax
    ```

2.  After the text that you pasted in the previous step, paste the following text, which runs the Windows PowerShell script you created earlier in this procedure.

    ``` syntax
    powershell.exe -ExecutionPolicy Bypass -Command "& {\\%CCP_SCHEDULER%\DiagShare\CultureTestRunStep.ps1 %1 %2}"
    goto :eof
    ```

    This command sets the execution policy to Bypass because the Windows PowerShell script that the command calls is located on a shared folder. If you copy the Windows PowerShell script to the same location on all of the nodes in the HPC cluster and specify the local copy of the script in this command, you then do not need to set the execution policy to Bypass.

3.  After the text that you pasted in the previous step, paste the following text, which prints an error message if the command was run with an incorrect syntax.

    ``` syntax
    :InvalidSyntax
    echo Invalid Syntax. The expected syntax is: 
    echo CultureTestRunStep -HeadNodeCulture ^<culture^>.

    :eof
    ```

4.  Save this script with a name of CultureTestRunStep.cmd in the shared folder that you created earlier in this section.

## Step 4: Test the script for the RunStep stage

To test your RunStep script, you should run the script from the command prompt before incorporating it into a diagnostic test.

For a RunStep script, test the script on compute nodes rather than just on the head node, because the RunStep stage of a diagnostic test can run on any nodes that the user specifies.

**To test the RunStep script**

1.  On the **Start** menu on the nodes in the HPC cluster on which you might want to run the test, click **Run**.
2.  In the **Run** dialog box, type **\\\\%CCP\_SCHEDULER%\\DiagShare** and click **OK** to verify that you can access the DiagShare shared folder on the head node.
3.  At a command prompt on the nodes in the HPC cluster on which you might want to run the test, run the script for the RunStep stage by typing the following command:

    **\\\\%CCP\_SCHEDULER%\\DiagShare\\CultureTestRunStep.cmd -HeadNodeCulture en-US**

    In the context of a diagnostic test, the diagnostic service specifies the *HeadNodeCulture* parameter for the RunStep script using the entry for the parameter in the PreStepResult.xml file. To run the RunStep script outside the context of a diagnostic test, you need to supply a value for the *HeadNodeCulture* parameter as part of the command.

## Step 5: Create an XML file to define the custom test

The XML file in this example is similar to the ones in the examples in earlier in this guide. See those examples for additional description of the XML elements that you use to define a custom test.

The one important difference in the XML elements for this test is that the [**PreStep**](prestep-element.md) element specifies a value of **True** for the **ResultXML** attribute. This value indicates that the PreStepResult.xml file that the PreStep stage creates contains a Nodes element that specifies the nodes on which the diagnostic service should run the RunStep stage.

**To create an XML file that defines the custom test**

1.  In a text editor such as Notepad, paste the following text to define the metadata for the test.

    ```XML
    <DiagnosticTests>
        <DiagnosticTest
            Name="Operating System Culture Test"
            Description="Tests if the operating system culture on each node matches the operating system culture on the head node."
            Company="Contoso, Ltd"
            Suite="Sample"
            Alias="CultureTest">
    
    ```

    

2.  After the text that you inserted in the previous step, paste the following text to define the command that you want to run for the PreStep stage of the diagnostic test.

    ```XML
            <PreStep Command="powershell.exe" ResultXml="True">
                <Parameters>
                    <Parameter Name="Command" Value="&amp;amp; {Add-PsSnapin Microsoft.HPC; C:\SampleTests\CultureTestPreStep.ps1}" Format="-{0} {1}"/>
                </Parameters>
            </PreStep>
    ```

    

    This example uses PreStep-specific parameters to specify some parameters to the **powershell.exe** command that do not require user input. The following command is the PreStep command that this combination of XML elements represents:

    **powershell.exe -Command "& {Add-PSSnapin Microsoft.HPC; C:\\SampleTests\\CultureTestPreStep.ps1}"**

3.  After the text that you inserted in the previous step, paste the following text to specify the command that you want to run for the RunStep stage of the test.

    ```XML
                    <RunStep Command="\\%CCP_SCHEDULER%\DiagShare\CultureTestRunStep.cmd"/>
    ```

    

4.  After the text that you inserted in the previous step, paste the following text to add the necessary closing tags to create a valid XML file.

    ```XML
        </DiagnosticTest>
    </DiagnosticTests>
    ```

    

5.  Save the file as C:\\SampleTests\\CultureTest.xml.

## Step 6: Add the test to an HPC Cluster

In Windows HPC Server 2008 R2, you can add diagnostic tests to an HPC cluster by using HPC PowerShell or at the command prompt.

**To add a custom diagnostic test to an HPC cluster by using HPC PowerShell**

1.  On the head node, click **Start**, point to **All Programs**, click **Microsoft HPC Pack 2008 R2**, right-click **HPC PowerShell**, and then click **Run as administrator**.

2.  In **HPC PowerShell**, type the following cmdlet to add the test:

    **Add-HpcTest -File C:\\SampleTests\\CultureTest.xml**

    If you need to remove the test from the HPC cluster later, type the **Remove-HpcTest -Alias CultureTest** cmdlet.

3.  Type the following cmdlet to verify that the test was added to the HPC cluster:

    **Get-HpcTest -Alias CultureTest**

4.  Type the following cmdlet to verify that the metadata and command for the test were correctly added to the HPC cluster:

    **Get-HpcTestDetail -Alias CultureTest**

**To add a custom diagnostic test to an HPC cluster at a command prompt**

1.  At a command prompt, type the following command to add the test:

    **test Add C:\\SampleTests\\CultureTest.xml**

    If you need to remove the test from the HPC cluster later, type the following command:

    **test Remove CultureTest**

2.  Type the following command to verify that the test was added to the HPC cluster:

    **test ListTests**

3.  Type the following command to verify that the metadata, parameters, and command for the test were correctly added to the HPC cluster:

    **test ViewTest CultureTest**

## Step 7: Run the test and view the results

After you add a custom diagnostic test to an HPC cluster, you can use HPC Cluster Manager, HPC PowerShell, or the command prompt window to run the test and view the results in the same way that you do for built-in diagnostic tests that Windows HPC Server 2008 R2 provides.

For information about using HPC Cluster Manager, see Overview of HPC Cluster Manager in the [HPC Cluster Manager Help](http://go.microsoft.com/fwlink/p/?linkid=124146) (http://go.microsoft.com/fwlink/p/?linkid=124146).

**To run the custom diagnostic test in HPC Cluster Manager**

1.  In **Diagnostics**, in the **Navigation Pane**, double-click **Tests** to display the list of companies that provided the diagnostic tests that are available on your HPC cluster, if the list is not already visible.

2.  Double-click **Contoso, Ltd** to display the list of suites, then click **Sample** to view the list of tests in the **Sample** suite.

3.  In the views pane, right-click **Operating System Culture Test** and click **Run**.

4.  In the **Run Diagnostic Tests** dialog box, select **All nodes** and click **Run**.

5.  If the **Run Test** dialog box appears, click **OK**.

### Additional considerations

To open **HPC Cluster Manager**, click **Start**, point to **All Programs**, click **Microsoft HPC Pack 2008 R2**, and then click **HPC Cluster Manager**. If the **User Account Control** dialog box appears, confirm that the action it displays is what you want, and then click **Continue**.

**To run the custom diagnostic test in HPC PowerShell or at a command prompt**

1.  In **HPC PowerShell**, type the following cmdlet:

    **Invoke-HpcTest -Alias CultureTest -NodeName** *ListOfNodesToRunTest*

    or

    At a command prompt, type the following command:

    **test run CultureTest -nodes:***ListOfNodesToRunTest*

2.  Note the run identifier that appears in the output of the cmdlet or at the command prompt so that you can view the results of the test later.

> [!Note]
>
> To specify parameter values for a diagnostic test in HPC PowerShell, use the *Parameters* parameter with a value that has the following format: @{*ParameterName1*="*Value1*"\[;*ParameterName2*="*Value2*";...\]}
>
> To specify a parameter value for a diagnostic test at the command prompt, include a parameter in the command with the following format: -*ParameterName*:"*Value"*

 

**To view the results of the custom test in HPC Cluster Manager**

1.  In **Diagnostics**, in the **Navigation Pane**, click **Test Results**.

2.  In the views pane, locate the test result for the **Operating System Culture Test** and wait until the **State** for the result changes to **Complete**.

3.  Click the test result for the **Operating System Culture Test** .

4.  In the **Detail** pane, click the **Result** tab to view the report on the results for the diagnostic test.

**To view the results of the custom test in HPC PowerShell**

1.  In HPC PowerShell, type the following cmdlet to verify that the test finished and to see the overall results of the test.

    **Get-HpcTestResultDetail -RunId** *RunIdentifier*

2.  Type the following cmdlet to export the report for the test run to a folder:

    **Export-HpcTestResult -RunId** *RunIdentifier* **-Path C:\\SampleTests\\CultureTest**

3.  In Windows Explorer, navigate to C:\\SampleTests\\CultureTest and then double-click **Report.html**.

**To view the results of the custom test at a command prompt**

1.  At a command prompt, type the following command to verify that the test finished and to see the overall results of the test.

    **test ViewRun** *RunIdentifier*

2.  Type the following command to view the report for the test run:

    **test ViewResult** *RunIdentifier*

The report for the test should appear similar to the following.

``` syntax
## COMPUTENODE2 --> Finished

The operating system culture on this node is en-US, which matches the operating
system culture on the head node.
## 

## HEADNODE --> Finished

The operating system culture on this node is en-US, which matches the operating
system culture on the head node.
## 

```

When the diagnostic test was run to generate this output, the ComputeNode1 node was offline, so the RunStep stage did not run on ComputeNode1, and no results appear for that node.

 

 



