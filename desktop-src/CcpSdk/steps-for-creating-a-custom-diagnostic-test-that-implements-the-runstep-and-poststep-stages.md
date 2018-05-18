---
Description: 'The previous examples in this guide used the AutoGenerateResult element to automatically generate a report for a specific type of diagnostic test, or used a default report that consisted of the output from each of the nodes in the test concatenated into one result. If the results of your test are complex or require additional processing, or if you want to have more control over how the report appears and what information it contains, you can create your own report.NodeName.out in the %ProgramFiles%\\Microsoft HPC Pack 2008 R2\\Data\\Diagnostics\\TestRunID folder on the head node, and you can then use these files in the PostStep stage.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3b48b768-c41a-4cc6-8fea-438f50e37139'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Steps for Creating a Custom Diagnostic Test that Implements the RunStep and PostStep Stages
---

# Steps for Creating a Custom Diagnostic Test that Implements the RunStep and PostStep Stages

The previous examples in this guide used the [**AutoGenerateResult**](autogenerateresult.md) element to automatically generate a report for a specific type of diagnostic test, or used a default report that consisted of the output from each of the nodes in the test concatenated into one result. If the results of your test are complex or require additional processing, or if you want to have more control over how the report appears and what information it contains, you can create your own report.

You create your own report by implementing a PostStep stage that creates a Report.html file. To make the data from your test easier to access while creating the report, you can also create StepResult XML to provide the data in a structured manner for each of the nodes in the RunStep stage. You can also create StepResult XML that summarizes the result for all of the nodes in the PostStep stage.

You can use the Diagnostic Helper API to create the StepResult XML. To provide the StepResult XML for a node for the RunStep stage so that the PostStep stage can use it, write the XML to standard output. The diagnostics service saves the standard output of the RunStep stage on each node in a file named *NodeName*.out in the %ProgramFiles%\\Microsoft HPC Pack 2008 R2\\Data\\Diagnostics\\*TestRunID* folder on the head node, and you can then use these files in the PostStep stage.

You can save the summary StepResult XML to the PostStepResult.xml file. If this file contains a list of failed nodes, HPC Cluster Manager provide a way of pivoting from viewing information about test result to viewing information about a failed node.

The example in this section implements the RunStep and PostStep stages so that they produce this StepResult XML in the manner just described and produce a Report.html file. The example checks the operating system culture, user interface culture, Windows PowerShell culture, and Windows PowerShell user interface culture on the nodes specified for the test, and checks whether those values are consistent both within each individual node and across all of the nodes in the test.

## Step 1: Create the script for the RunStep stage

This example implements the RunStep stage as a Windows PowerShell script. The script uses Windows PowerShell cmdlets to get the culture information and the Diagnostic Helper API to create StepResult XML that provides the results of the test for each node.

**To create the RunStep script**

1.  On the head node of your HPC cluster, create a shared folder named **DiagShare** and grant everyone read permissions.

2.  In a text editor such as Notepad, paste the following lines of Windows PowerShell script, which load the DLL for the Diagnostic Helper API so that you can create StepResult XML for the results of the test on each node. You can later use this XML in the PostStep stage to build a report for the test results.

    ```PowerShell
    # Installing HPC Pack 2008 R2 SDK on the head node installs the DLL for the Diagnostic Helper API at 
    # %CCP_SDK%\bin\Microsoft.Hpc.Diagnostics.Helpers.dll on the head node.
    $ccpHome = "\\" + $env:CCP_SCHEDULER + "\c$\Program Files\Microsoft HPC Pack 2008 R2 SDK\";
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

    $diagsHelper = "Microsoft.Hpc.Diagnostics.Helpers";
    
    ```

    

    This code calls the System.Reflection.Assembly.LoadFile method to load the DLL for the Diagnostic Helper API.

3.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which get the operating system culture, user interface culture, Windows PowerShell culture, and Windows PowerShell user interface culture and stores these values in variables.

    ```PowerShell
    $OSCulture = (Get-Culture).Name;
    $UICulture = (Get-UICulture).Name;
    $PS_Culture = (Get-Variable PSCulture).Value;
    $PSUI_Culture = (Get-Variable PSUICulture).Value;
    
    ```

    

    This code uses the Get-Culture cmdlet to get the operating system culture and the Get-UICulture cmdlet to get the user interface culture. The code then uses the Get-Variable cmdlet to get the values of the PSCulture and PSUICulture variables, which contain the Windows PowerShell culture and Windows PowerShell user interface culture.

4.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which create a new StepResult object in which to store the results of the diagnostic test for the node, and set the NodeName property of the StepResult object to the name of the node on which the script is running.

    ```PowerShell
    $stepResult = New-Object "$diagsHelper.StepResult";
    $stepResult.NodeName = $env:COMPUTERNAME;
    ```

    

    This code uses the New-Object cmdlet and the constructor for the StepResult class to create a new StepResult object, then sets the StepResult.NodeName property.

5.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which create a table to hold the data that the diagnostic test produced on the node and add four columns to the table, one column for each of the culture values that you retrieved in step 3.

    ```PowerShell
    $table = New-Object "$diagsHelper.StepResult+Table"("Culture Information");

    $table.Columns.Add( (New-Object "$diagsHelper.StepResult+Column"(" Culture")) );
    $table.Columns.Add( (New-Object "$diagsHelper.StepResult+Column"("UI Culture")) );
    $table.Columns.Add( (New-Object "$diagsHelper.StepResult+Column"("PowerShell Culture")) );
    $table.Columns.Add( (New-Object "$diagsHelper.StepResult+Column"("PowerShell UI Culture")) );
    
    ```

    

    This code uses the New-Object cmdlet and the constructor for the StepResult.Table class to create a new Table object.

    The code then uses the New-Object cmdlet and the constructor for the StepResult.Column class to create new columns. The parameter in the constructor for the StepResult.Column class specifies the text to use as the heading for the column.

    The code uses the System.Collections.Generic.List.Add method to add the Column objects to the Columns property of the Table object.

6.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which create a new row in the table and add four new items to the row that contain the culture values that you retrieved in step 3.

    ```PowerShell
    $row = New-Object "$diagsHelper.StepResult+Row";

    $row.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"($OSCulture)) );
    $row.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"($UICulture)) );
    $row.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"($PS_Culture)) );
    $row.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"($PSUI_Culture)) );
    ```

    

    This code uses the New-Object cmdlet and the constructor for the StepResult.Row class to create a new Row object.

    The code then uses the New-Object cmdlet and the constructor for the StepResult.RowItem class to create new table cells in the row. The parameter in the constructor for the StepResult.RowItem class specifies the value to use for the entry in the cell. In this example, these values are the culture values that you retrieved in step 3.

    The code uses the System.Collections.Generic.List.Add method to add the RowItem objects to the Items property of the Row object.

7.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which add the row to the table and then add the table to the StepResult object.

    ```PowerShell
    $table.Rows.Add($row);

    $stepResult.Tables.Add($table);
    ```

    

    This code uses the System.Collections.Generic.List.Add method to add the Row object to the Rows property of the Table object, and then to add the Table object to the Tables property for the StepResult object.

8.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which test whether the culture values are all the same and add the appropriate result code and bulleted list item to the StepResult object.

    ```PowerShell
    if (($OSCulture -eq $UICulture) -and ($UICulture -eq $PS_Culture) -and ($PS_Culture -eq $PSUI_Culture))
    {

        $stepResult.Result = [Microsoft.Hpc.Diagnostics.Helpers.StepResult+ResultCode]::Success;
        $stepResult.BulletPoints.Add( (New-Object "$diagsHelper.StepResult+Information"([Microsoft.Hpc.Diagnostics.Helpers.StepResult+InformationType]::Information, 
                                       "The Operating System Culture, UI Culture, PowerShell Culture, and PowerShell UI Culture are all consistent on this node.")));
    }

    else
    {
        $stepResult.Result = [Microsoft.Hpc.Diagnostics.Helpers.StepResult+ResultCode]::Warning;
        $stepResult.BulletPoints.Add( (New-Object "$diagsHelper.StepResult+Information"([Microsoft.Hpc.Diagnostics.Helpers.StepResult+InformationType]::Warning, 
                                       "The Operating System Culture, UI Culture, PowerShell Culture, and PowerShell UI Culture are not all consistent on this node.")));
    }
    
    ```

    

    This code sets the Result property of the StepResult object to the appropriate value from the StepResult.ResultCode enumeration.

    The code then uses the New-Object cmdlet and the constructor for the StepResult.Information class to create a new Information object with a appropriate value from the StepResult.InformationType enumeration and a message describing whether the culture values are consistent within the node.

    The code uses the System.Collections.Generic.List.Add method to add the Information object to the BulletPoints property of the StepResult object.

9.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script, which trap any errors that occur in the script and serializes the StepResult object as XML that is sent to standard output. If an error occurs, the script adds a result code of failure and the exception message for the script are added to the StepResult object before serializing the StepResult object and exiting.

    ```PowerShell
    Trap 

    {    

        $stepResult.Result = [Microsoft.Hpc.Diagnostics.Helpers.StepResult+ResultCode]::Failure;
        $stepResult.ExceptionMessage  = $_.Exception.Message;
        $stepResult.XmlSerializeToStandardOut();
        break;

    }

    $stepResult.XmlSerializeToStandardOut();
    ```

    

    If an error occurs, the code sets the ExceptionMessage property of the StepResult object to the exception message for the script.

    Regardless of whether an error occurred, the code calls the StepResult.XmlSerializeToStandardOut method to serialize the StepResult object as XML and send the XML to standard output. In the context of the RunStep stage of a diagnostic test, the diagnostic service saves the standard output and standard error streams for the RunStep command to a file named *NodeName*.out in the %ProgramFiles%\\Microsoft HPC Pack 2008 R2\\Data\\Diagnostics\\*TestRunID* folder on the head node of the HPC cluster so that the PostStep stage can process and display the results from all of the nodes.

10. Save this script with a name of CultureTest2\_RunStep.ps1 in the shared folder that you created in the first step of this procedure.

## Step 2: Test the script for the RunStep stage

To test your RunStep script, you should run the script from the command prompt before incorporating it into a diagnostic test.

For a RunStep script, test the script on compute nodes rather than just on the head node, because the RunStep stage of a diagnostic test can run on any nodes that the user specifies.

For this example, you will want to save the XML output you get when testing this script from several nodes, so you can use that output to test the PostStep stage later.

**To test the RunTest script**

1.  On the **Start** menu on a node in the HPC cluster on which you might want to run the test, click **Run**.
2.  In the **Run** dialog box, type **\\\\%CCP\_SCHEDULER%\\DiagShare** and click **OK** to verify that you can access the DiagShare shared folder on the head node.
3.  At a command prompt, type the following command to get the operating system culture and note the result.

    **powershell.exe -Command (Get-Culture).Name**

4.  Type the following command to get the user interface culture and note the result.

    **powershell.exe -Command (Get-UICulture).Name**

5.  Type the following command to get the Windows PowerShell culture and note the result.

    **powershell.exe -Command (Get-Variable PSCulture).Value**

6.  Type the following command to get the Windows PowerShell user interface culture and note the result.

    **powershell.exe -Command (Get-Variable PSUICulture).Value**

7.  Type the script for the RunStep stage by typing the following command:

    **powershell.exe -ExecutionPolicy Bypass -Command "& {\\\\%CCP\_SCHEDULER%\\DiagShare\\CultureTest2\_RunStep.ps1}"**

    Output similar to the following example should appear.

    ``` syntax
    <?xml version="1.0"?>
    <StepResult xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" NodeName="COMPUTENODE1">
      <Result>Success</Result>
      <Message/>
      <ExceptionMessage/>
      <Nodes xsi:nil="true"/>
      <FailedNodes/>
      <Environment/>
      <Parameters/>
      <Tables>
        <Table Description="Culture Information" Name="" Tags="">
          <Columns>
            <Column>Operating System Culture</Column>
            <Column>UI Culture</Column>
            <Column>PowerShell Culture</Column>
            <Column>PowerShell UI Culture</Column>
          </Columns>
          <Rows>
            <Row>
              <Items>
                <RowItem>en-US</RowItem>
                <RowItem>en-US</RowItem>
                <RowItem>en-US</RowItem>
                <RowItem>en-US</RowItem>
              </Items>
            </Row>
          </Rows>
        </Table>
      </Tables>
      <BulletPoints>
        <Information>
          <Type>Information</Type>
          <Message>The Operating System Culture, UI Culture, PowerShell Culture, and PowerShell UI
     Culture are all consistent on this node.</Message>
        </Information>
      </BulletPoints>
    </StepResult>
    ```

8.  Verify that the four culture values you obtained in steps 3 through 6 match the contents of the four RowItem elements in the XML output.

9.  Save the output that appeared in the previous file as a text file named *NodeName*.out in the C:\\SampleTest\\PostStepTest folder on the head node.

    You will need the *NodeName*.out file to test the PostStep script later in this scenario.

10. Repeat this "To test the RunTest script" procedure on several nodes in the HPC cluster.

## Step 3: Create the script for the PostStep stage

This example implements the PostStep stage as a Windows PowerShell script. The example uses the Diagnostics Helper API to get the StepResult XML for the individual nodes from the RunStep stage and processes those results further. The example then creates a Report.html file that provides formatted report of the results of the test, and uses the Diagnostics Helper API to create a PostStepResult.xml file that contains a summary of the test result in the StepResult XML format.

**To create a script for the PostStep stage**

1.  In a text editor such as Notepad, paste the following lines of Windows PowerShell script, which load the DLL for the Diagnostic Helper API so that you can process the StepResult XML files that contain the results for each node and create a PostStepResult XML file that contains a summary of all of the results for the test.

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

    #----------------------------------------------------------------------
    # Global variable declarations
    #----------------------------------------------------------------------
    $diagsHelper = "Microsoft.Hpc.Diagnostics.Helpers";

    #
    # Array for storing information from the nodes in the test
    #
    $arrNodes = @();
    
    ```

    

    This code calls the System.Reflection.Assembly.LoadFile method to load the DLL for the Diagnostic Helper API. The code also creates some global variable for use throughout the script.

2.  After the text that you pasted in the previous step, paste the following lines of Windows PowerShell script.

    ```PowerShell
    # The CollectResults function takes a list of StepResult objects for all of the nodes
    # and collects the data in those objects in a form that is easier to process.
    function CollectResults 
    {
       param ($nResults)

       # Process the StepResult object for each node in the test by looping 
       # through the list of all of the StepResult objects.
       foreach ($nResult in $nResults)

       {

           # Create a new System.Object object for storing key information for each node.
           $objNode = New-Object System.Object;

           # Add the NodeName and Result properties of the StepResult object as properties of 
           # the System.Object object.
           $objNode | Add-Member -type NoteProperty -name NodeName -Value $nResult.NodeName;
           $objNode | Add-Member -type NoteProperty -name Result -Value $nResult.Result;

           # Check the StepResult object has the expected single table,
           # and that the table has the expected single row.
           if ($nResult.Tables.Count -eq 1)
           {

               if ($nResult.Tables[0].Rows.Count -eq 1)

               {
               
                   # Get the row.
                   $nRow = $nResult.Tables[0].Rows[0];

                   # The cells in the table row contain the culture values for the node. Get these values
                   # and add them as properties of the System.Object object.
                   $objNode | Add-Member -type NoteProperty -name OSCulture -Value $nrow.Items[0].Value;
                   $objNode | Add-Member -type NoteProperty -name UICulture -Value $nrow.Items[1].Value;
                   $objNode | Add-Member -type NoteProperty -name PSCulture -Value $nrow.Items[2].Value;
                   $objNode | Add-Member -type NoteProperty -name PSUICulture -Value $nrow.Items[3].Value;

               }
          
           }

        # Add the System.Object object to the global array.   
        $script:arrNodes += $objNode

        }

    }
    
    ```

    

    This code defines a function that takes a list of StepResult objects for all of the nodes in the test and copies the data in those objects into another set of objects that the code can later use to compare results from different nodes more easily.

    The code uses the New-Object cmdlet and the constructor for the .NET Framework System.Object class to create the new objects, and the Add-Member cmdlet to add properties to those objects.

    The code uses the StepResult.NodeName, StepResult.Tables, StepResult.Rows, and StepResult.Row.Items properties that you already used in the RunStep script to get information from the StepResult objects. The last three of those StepResult properties are lists, and the code uses the properties and index for the System.Collections.Generic.List class to get information in those lists.

    The culture values that this diagnostic test examines are stored in table cells in the StepResult objects. Table cells are StepResult.RowItem objects, and the code uses the StepResult.RowItem.Value property to get those culture values.

    Finally the code stores all of the System.Object objects in global array you created earlier in the script.

3.  After the text that you pasted in the previous step, paste the following lines of PowerShell script.

    ```PowerShell
    # The GenerateSummary function creates and returns a StepResult object that summarizes 
    # the diagnostic test data for all of the nodes. The function uses the properties of the System.Object objects created in the CollectResults
    # function to make comparisons across nodes and generate summary results about the consistency of culture values within and across nodes.
    function GenerateSummary
    {

        # Set up some boolean variables to track the overall result for the
        # test and the consistency of values within and across nodes.
        [bool]$bWarning = $false;
        [bool]$bFailure = $false;
        [bool]$bWithin = $false;
        [bool]$bAcross = $true;

        # Create a new StepResult object to hold a summary of the data for all of
        # the nodes in the test, and set the NodeName property of that object to Summary.
        $summResult = New-Object "$diagsHelper.StepResult";
        $summResult.NodeName = "Summary";

        # Create a table for the summary data.
        $summaryTable = New-Object "$diagsHelper.StepResult+Table"("Culture Summary Table");

        # Create the columns for the table.
        $summaryTable.Columns.Add( (New-Object "$diagsHelper.StepResult+Column"("Operating System Culture")) );
        $summaryTable.Columns.Add( (New-Object "$diagsHelper.StepResult+Column"("UI Culture")) );
        $summaryTable.Columns.Add( (New-Object "$diagsHelper.StepResult+Column"("PowerShell Culture")) );
        $summaryTable.Columns.Add( (New-Object "$diagsHelper.StepResult+Column"("PowerShell UI Culture")) );

        # Create the row for the table.
        $summaryRow = New-Object "$diagsHelper.StepResult+Row";

        # Check if any node had a result of Warning. If the result for any node is Warning, the overall 
        # result should be Warning at best.
        foreach($node in $arrNodes)

        {

            if ($node.Result -eq [Microsoft.Hpc.Diagnostics.Helpers.StepResult+ResultCode]::Warning)
            {

                $bWarning = $true;
                break;

            }

        }

        # Check if any node had a result of Failed. If the result for any node is Failed, the overall 
        # result should be Failed, and the failed node should be added to the list of failed nodes.
        foreach($node in $arrNodes)

        {

            if ($node.Result -eq [Microsoft.Hpc.Diagnostics.Helpers.StepResult+ResultCode]::Failure)

            {

                $bFailure = $true;

                # Add the node to the list of failed nodes.
                $summResult.FailedNodes.Add( (New-Object "$diagsHelper.StepResult+Node"($node.NodeName)) );

            }

        }

        # Check if the operating system culture was the same for all of the nodes, and add a row item that
        # shows whether the operating system culture was consistent. If the result is not consistent, then
        # the result should be a Warning, and the set of culture values will not be consistent across nodes.
        foreach($node in $arrNodes)

        {

            if ($node.OSCulture -ne $arrNodes[0].OSCulture)

            {

                $summaryRow.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"("Not Consistent")) );
                $bWarning = $true;
                $bAcross = $false;   
                break;

            }

            if($node.NodeName -eq $arrNodes[$arrNodes.length-1].NodeName)

            {

                $summaryRow.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"("Consistent")) );
      
            }

        }

        # Check if the user interface culture was the same for all of the nodes, and add a row item that
        # shows whether the user interface culture was consistent. If the result is not consistent, then
        # the result should be a Warning, and the set of culture values will not be consistent across nodes.
        foreach($node in $arrNodes)

        {

            if ($node.UICulture -ne $arrNodes[0].UICulture)

            {

                $summaryRow.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"("Not Consistent")) );
                $bWarning = $true;
                $bAcross = $false;   
                break;

            }


            if($node.NodeName -eq $arrNodes[$arrNodes.length-1].NodeName)

            {

                $summaryRow.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"("Consistent")) );
      
            }

        }

        # Check if the PowerShell culture was the same for all of the nodes, and add a row item that
        # shows whether the PowerShell culture was consistent. If the result is not consistent, then
        # the result should be a Warning, and the set of culture values will not be consistent across nodes.
        foreach($node in $arrNodes)

        {

            if ($node.PSCulture -ne $arrNodes[0].PSCulture)

            {

                $summaryRow.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"("Not Consistent")) );
                $bWarning = $true;
                $bAcross = $false;   
                break;

            }


            if($node.NodeName -eq $arrNodes[$arrNodes.length-1].NodeName)

            {

                $summaryRow.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"("Consistent")) );

            }
      
        }

        # Check if the PowerShell user interface culture was the same for all of the nodes, and add a row item that
        # shows whether the PowerShell user interface culture was consistent. If the result is not consistent, then
        # the result should be a Warning, and the set of culture values will not be consistent across nodes.
        foreach($node in $arrNodes)

        {

            if ($node.PSUICulture -ne $arrNodes[0].PSUICulture)

            {

                $summaryRow.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"("Not Consistent")) );
                $bWarning = $true;
                $bAcross = $false;   
                break;

            }


            if($node.NodeName -eq $arrNodes[$arrNodes.length-1].NodeName)

            {

                $summaryRow.Items.Add( (New-Object "$diagsHelper.StepResult+RowItem"("Consistent")) );

            }
      
        }

        # Check if the result for all of the nodes was Success. If the result for all nodes is Success,
        # then for each node, the four culture values were consistent within the node. If the Result for any
        # node is not Success, then the four culture values were inconsistent with each other on at least one 
        # node. Add a bullet point to the summary for either case.
        foreach($node in $arrNodes)

        {

            if ($node.Result -ne [Microsoft.Hpc.Diagnostics.Helpers.StepResult+ResultCode]::Success)

            {

                $summResult.BulletPoints.Add( (New-Object "$diagsHelper.StepResult+Information"([Microsoft.Hpc.Diagnostics.Helpers.StepResult+InformationType]::Warning, "The operating system culture, UI culture, PowerShell culture, and PowerShell UI culture are not consistent with each other on at least one node.")) );
                break;

            }


            if($node.NodeName -eq $arrNodes[$arrNodes.length-1].NodeName)

            {


                $summResult.BulletPoints.Add( (New-Object "$diagsHelper.StepResult+Information"([Microsoft.Hpc.Diagnostics.Helpers.StepResult+InformationType]::Information, "The operating system culture, UI culture, PowerShell culture, and PowerShell UI culture are consistent with each other on each node.")) );
                $bWithin = $true;

            }
      
        }

        # If for each of the four culture values, the culture value was consistent across all of the nodes, then the set of four values
        # is also consistent across all of the nodes (the four culture values may be inconsistent with each other within a single node, but
        # all of the nodes have the same inconsistency). If $bAcross is still true, then the set of values is consistent across all of the nodes.
        # Add the appropriate bullet item for either case.
        if($bAcross -eq $true)
        {

            $summResult.BulletPoints.Add( (New-Object "$diagsHelper.StepResult+Information"([Microsoft.Hpc.Diagnostics.Helpers.StepResult+InformationType]::Information, "The set of values for the operating system culture, UI culture, PowerShell culture, and PowerShell UI culture are the same for each node.")) );

        }

        else 

        {

           $summResult.BulletPoints.Add( (New-Object "$diagsHelper.StepResult+Information"([Microsoft.Hpc.Diagnostics.Helpers.StepResult+InformationType]::Warning, "The set of values for the operating system culture, UI culture, PowerShell culture, and PowerShell UI culture are different on different nodes.")) );
      
        }


        # If the set of four culture values is consistent across all of the nodes, and for each node, the four culture values are consistent with
        # each other, then the cultures are consistent both within and across nodes. All of culture values on all of the nodes are the same value.
        # Add the appropriate bullet point to the summary for either case.
        if(($bAcross -eq $true) -and ($bWithin -eq $true))
        {

            $summResult.BulletPoints.Add( (New-Object "$diagsHelper.StepResult+Information"([Microsoft.Hpc.Diagnostics.Helpers.StepResult+InformationType]::Information, "The operating system culture, UI culture, PowerShell culture, and PowerShell UI culture are consistent both within each node and across all of the nodes.")) );

        }

        else 

        {

            $summResult.BulletPoints.Add( (New-Object "$diagsHelper.StepResult+Information"([Microsoft.Hpc.Diagnostics.Helpers.StepResult+InformationType]::Warning, "The operating system culture, UI culture, PowerShell culture, and PowerShell UI culture are not consistent either within each node or across all of the nodes.")) );
      
        }

        # Add the row to the table and the table to the StepResult object.
        $summaryTable.Rows.Add($summaryRow);
        $summResult.Tables.Add($summaryTable);

        # If any node had a result of Failure, set the overall result to Failure.
        # If any node had a result of Warning, or if any of the four culture values 
        # was not consistent across the nodes, set the overall result to Warning.
        # Otherwise, set the overall result to Success.
        if($bFailure -eq $true)
        {
        $summResult.Result = [Microsoft.Hpc.Diagnostics.Helpers.StepResult+ResultCode]::Failure;
        }
        elseif ($bWarning -eq $true)
        {
        $summResult.Result = [Microsoft.Hpc.Diagnostics.Helpers.StepResult+ResultCode]::Warning;
        }
        else
        {
        $summResult.Result = [Microsoft.Hpc.Diagnostics.Helpers.StepResult+ResultCode]::Success;
        }

        # Return the summary StepResult object so that it can be added to the others.
        return $summResult;

    }
    
    ```

    

    This code creates a StepResult object that contains a summary of the data for all of the nodes. The code is quite similar to the code in the RunStep script that created the StepResult object for the nodes.

    The only new item from the Diagnostic Helper API that this code uses is the FailedNodes property of the StepResult object, which is a list of the nodes for which the test failed. The other items from the Diagnostic Helper API in this code were all also used in the RunStep script.

4.  After the text that you pasted in the previous step, paste the following lines of PowerShell script.

    ```PowerShell
    # The BuildReport function takes a TestResult object that contains all of the StepResult objects
    # for the test, including the summary StepResult object, and generates an HTML report for the results.
    function BuildReport
    {
        param 
        (
            [Microsoft.Hpc.Diagnostics.Helpers.TestResult] $resultContainer
        )

        # The diagnostic service expects the report to have a name of Report.html, so use that
        # name. The diagnostic service expects to find the file in the %ProgramFiles%\Microsoft HPC Pack 2008 R2\Data\Diagnostics\<test_run_id>
        # folder on the head node, which is the working directory the diagnostic service uses when it runs the PostStep script,
        # so you can just save the file to the current working directory.
        $reportName = "Report.html";

        # Add header tags to the file.
        Set-Content -Path $reportName -Value "<html xmlns=""http://www.w3.org/1999/xhtml"">";
        Add-Content -Path $reportName -Value "<head>";

        # Use the value of the TestResult.Name property in the title of the HTML.
        Add-Content -Path $reportName -Value ("<title>HPC Diagnostic Test - " + $resultContainer.Name + "</title>");

        # Run functions to insert a cascading style sheet (CSS) and support 
        # for expanding and collapsing the sections of the report that correspond to each 
        # StepResult object.
        InsertStyleSheet($reportName);
        InsertToggle($reportName);

        Add-Content -Path $reportName -Value "</head>";

        # Add the body of the HTML file.
        Add-Content -Path $reportName -Value "<body>";

        # Add a heading with name of the TestResult object.
        Add-Content -Path $reportName -Value "<p class=""SuiteHeader"">";
        Add-Content -Path $reportName -Value $resultContainer.Name;
        Add-Content -Path $reportName -Value "</p>";

        # Generate the content for each of the individual StepResult objects
        # in the TestResult object.
        $resultContainer.StepResults | Foreach-Object {
            RenderStepResult $_ $resultContainer.Name $reportName;
        }

        # Add the closing tags.
        Add-Content -Path $reportName -Value "</body>";
        Add-Content -Path $reportName -Value "</html>";
    }
       

    # The InsertStyleSheet function takes the name of the HTML file for the report that the test
    # is generating, and adds a CSS file to that HTML file.
    function InsertStyleSheet
    {
        param ( [string] $reportName )
        
        # The CSS file that Windows HPC Server uses for built-in reports is at
        # %ProgramFiles%\Microsoft HPC Pack 2008 R2\bin\styles.css.
        $cssPath = $ccpHome + "Bin\styles.css";
        if (Test-Path $cssPath)
        {
            $cssContents = Get-Content -Path $cssPath;
        }
        else
        {
            Write-Warning "Could not find styles.css.";
        }
        
        Add-Content -Path $reportName -Value $cssContents;
    }


    # The InsertToggle function takes the name of the HTML file for the report that the test
    # is generating, and adds support for expanding and collapsing sections of the file that 
    # correspond to each of the StepResult objects for the test.
    function InsertToggle
    {
        param ( [string] $reportName )
        
        # Adds code that expands and collapses sections. The images used in the built-in reports
        # are in the %ProgramFiles%\Microsoft HPC Pack 2008 R2\bin folder.
        Add-Content -Path $reportName -Value "<script type=""text/jscript"" language=""jscript"">";
        Add-Content -Path $reportName -Value "function toggleCollapse(id, imgId)";
        Add-Content -Path $reportName -Value "{";
        Add-Content -Path $reportName -Value "var toggle = document.getElementById(id);";
        Add-Content -Path $reportName -Value "var toggleImage = document.getElementById(imgId);";
        Add-Content -Path $reportName -Value "if( toggle.style.display == ""none"" )";
        Add-Content -Path $reportName -Value "{";
        Add-Content -Path $reportName -Value "toggle.style.display = """";";
        Add-Content -Path $reportName -Value ("toggleImage.src = """ + $ccpHome.Replace("\","\\") + `
            "Bin\\SM072_ChevronCollapsed.png"";");
        Add-Content -Path $reportName -Value "}";
        Add-Content -Path $reportName -Value "else";
        Add-Content -Path $reportName -Value "{";
        Add-Content -Path $reportName -Value "toggle.style.display = ""none"";";
        Add-Content -Path $reportName -Value ("toggleImage.src = """ + $ccpHome.Replace("\","\\") + `
            "Bin\\SM071_ChevronExpanded.png"";");
        Add-Content -Path $reportName -Value "}";
        Add-Content -Path $reportName -Value "}";
        Add-Content -Path $reportName -Value "</script>";
    }
    ```

    

    This code includes several functions that together create a HTML file named Report.html that contains a report of the results for the diagnostic test. This report appears on the **Result** tab for the test result in **HPC Cluster Manager**.

    The code mainly uses the Set-Content and Add-Content cmdlets to add HTML content to the file. Most of the code is not specific to diagnostic tests, and a detailed explanation of all the code is beyond the scope of this document.

    The items in the code that are specific to diagnostic tests are:

    -   The parameter for the BuildReport function is a TestResult object that contains all of the StepResult objects for the test run.

    -   The title of the HTML file and a heading in the file use the Name property of the TestResult object.

    -   Each of the StepResult objects in the TestResult object is passed to the RenderStepResult function, which adds a section to the report for the StepResult object.

5.  After the text that you pasted in the previous step, paste the following lines of PowerShell script.

    ```PowerShell
    # The RenderStepResult function takes a StepResult object, the name of the diagnostic test, and the file name
    # of the HTML report for the diagnostic test run, and adds a section for the StepResult object to the HTML report.
    function RenderStepResult
    {
        param 
        (
            [Microsoft.Hpc.Diagnostics.Helpers.StepResult] $renResult,
            [string] $tstName,
            [string] $reportName
        )
        
        # Add items to support expanding and collapsing the section, and 
        # display the name of the node for this section of the report.
        Add-Content -Path $reportName -Value "<div class=""SuiteBody"">";
        Add-Content -Path $reportName -Value "<table class=""CollapseHeader"" width=""640px"">";
        Add-Content -Path $reportName -Value ("<tr onclick=""toggleCollapse('" + $tstName + $renResult.NodeName + `
            "', '" + $tstName + $renResult.NodeName + "ToggleImage');"" style=""cursor:pointer;"">");
        Add-Content -Path $reportName -Value ("<td>" + $renResult.NodeName + "</td>");
        $resultFont = "success";

        # Add the result for the StepResult object to the report.
        switch ($renResult.Result)
        {
            "Failure" {$resultFont = "failure";break;}
            "Warning" {$resultFont = "warning";break;}
            "Success" {$resultFont = "success";break;}
        }
        Add-Content -Path $reportName -Value ("<td class=""Summary"" align=""right""><font class=""" + `
            $resultFont + """>" + $renResult.Result + "</font></td>");

        if (Test-Path ($ccpHome + "Bin\SM071_ChevronExpanded.png"))
        {
            Add-Content -Path $reportName -Value ("<td width=""40px"" align=""center""><img id=""" + `
                $tstName + $renResult.NodeName + "ToggleImage"" alt=""Expand/Collapse"" src=""" + `
                $ccpHome + "Bin\SM071_ChevronExpanded.png""/></td>");
        }
        Add-Content -Path $reportName -Value "</tr>";
        Add-Content -Path $reportName -Value "</table>";
        Add-Content -Path $reportName -Value ("<div id=""" + $tstName + $renResult.NodeName + `
            """ style=""display:none"">");

        # Add the bullet points from the StepResult object to the report.
        RenderBulletPoints $renResult $reportName;

        # Add the tables for the StepResult object to the report.
        $renResult.Tables | %{
            RenderTable $_ $reportName;
        }
        Add-Content -Path $reportName -Value "</div>";
        Add-Content -Path $reportName -Value "</div>";
    }
    
    ```

    

    This code adds a section for a StepResult object for the test to the Report.html file.

    The code mainly uses the Add-Content cmdlet to add HTML content to the file. Most of the code is not specific to diagnostic tests, and a detailed explanation of all the code is beyond the scope of this document.

    The items in the code that are specific to diagnostic tests are:

    -   The parameters are the StepResult object for which information is to be added to the report, the Name property of the TestResult object, and the file name of the report file.

    -   The NodeName and Result properties of the StepResult object are used as part of the heading for the expandable section of the report.

    -   The StepResult object is passed to the RenderBullets function in order to add the bullet points for the object to the section.

        The Tables property of the StepResult object is passed to the RenderTables function in order to add the tables for the object to the section.

6.  After the text that you pasted in the previous step, paste the following lines of PowerShell script.

    ```PowerShell
    # The RenderBulletPoints function takes a StepResult object for a diagnostic test run and
    # the name of the HTML report file for the test run, and adds the bullet points for the StepResult object to the report.
    function RenderBulletPoints
    {
        param 
        (
            [Microsoft.Hpc.Diagnostics.Helpers.StepResult] $renResult,
            [string] $reportName
        )
     
        # Check if the StepResult object has any bullet points.   
        if (($renResult.BulletPoints -ne $null) -and ($renResult.BulletPoints.Count -gt 0))
        {
            # Create an unordered list.
            Add-Content -Path $reportName -Value "<UL>";
            
            # For each bullet point, add a list item to the list.  
            $renResult.BulletPoints | %{
                [string] $style = "";
                if ($_.Type -eq "Failure")
                {
                    $style = "style=""color:#FF0000""";
                }
                elseif ($_.Type -eq "Warning")
                {
                    $style = "style=""color:#FF8800""";
                }
                Add-Content -Path $reportName -Value ("<LI " + $style +">");
                Add-Content -Path $reportName -Value $_.Message;
                Add-Content -Path $reportName -Value "</LI>";
            }
            
            Add-Content -Path $reportName -Value "</UL>";
        }
    }


    # The RenderTable function takes a StepResult.Table object and the file name of the report for the
    # diagnostic test run and adds the table to the report.
    function RenderTable
    {
        param 
        (
            [Microsoft.Hpc.Diagnostics.Helpers.StepResult+Table] $renResultTable,
            [string] $reportName
        )
        
        # Add the name and description of the table to the report.
        Add-Content -Path $reportName -Value "<p class=""TableTitle"">";
        Add-Content -Path $reportName -Value $renResultTable.Name;
        Add-Content -Path $reportName -Value "</p>";
        
        Add-Content -Path $reportName -Value "<p class=""Description"">";
        Add-Content -Path $reportName -Value $renResultTable.Description;
        Add-Content -Path $reportName -Value "</p>";
        
        # Add the table itself to the report.
        Add-Content -Path $reportName -Value "<table class=""DisplayTable"" CellSpacing=""0"">";
        Add-Content -Path $reportName -Value "<tr>";
        
        # Add the column headings to the table.
        $renResultTable.Columns | %{
            Add-Content -Path $reportName -Value ("<td class=""HeaderCell"">" + $_.Name + "</td>");
        }
        Add-Content -Path $reportName -Value "</tr>";
     
        # Add the rows to the table.
        $renResultTable.Rows | %{
            Add-Content -Path $reportName -Value "<tr>";
            $_.Items | %{
                Add-Content -Path $reportName -Value ("<td class=""TableCell"">" + $_.Value + "</td>");
            }
            Add-Content -Path $reportName -Value "</tr>";
        }

        Add-Content -Path $reportName -Value "</table>";
    }
    
    ```

    

    This code adds the bullet points and tables for a StepResult object for the test to the Report.html file.

    The code mainly uses the Add-Content cmdlet to add HTML content to the file. Most of the code is not specific to diagnostic tests, and a detailed explanation of all the code is beyond the scope of this document.

    The RenderBulletPoints function uses the StepResult.BulletPoints, StepResult.Information.Type, and StepResult.Information.Message properties.

    The RenderTable function uses StepResult.Table.Name, StepResult.Table.Description, StepResult.Table.Columns, StepResult.Column.Name, StepResult.Table.Rows, StepResult.Row.Items, and StepResult.RowItem.Value properties.

7.  After the text that you pasted in the previous step, paste the following lines of PowerShell script.

    ```PowerShell
    # Main
    $currentPath = [Environment]::CurrentDirectory;

    # Get the StepResult XML from all the nodes for the RunStep stage and store them as a list of
    # StepResult objects.
    $nodeResults = [Microsoft.Hpc.Diagnostics.Helpers.StepResult]::GetResultsFromDirectory($currentPath);

    # Create a new TestResult object for all of the StepResult objects and give it a name.
    $result = New-Object "$diagsHelper.TestResult";

    $result.Name = "Culture Consistency Within and Across Nodes";

    # Get information from the StepResult objects for the nodes and store it for easier access within the 
    # rest of the script.
    collectResults($nodeResults);

    # Add the StepResult objects for each node to the TestResult object.
    foreach ($nodeResult in $nodeResults)
    {

       $result.StepResults.Add($nodeResult);

    }

    # Create a StepResult object that summarizes the result for all of the
    # nodes.
    $summaryResult = GenerateSummary;

    # Add the summary StepResult object as the first one in the TestResult object.
    $result.StepResults.Insert(0, $summaryResult);

    # Create an HTML report from TestResult object
    BuildReport($result);

    # Serialize the summary StepResult object as XML and save the XML in the
    # PostStepResult.xml file.
    $summaryResult.XmlSerializeToFile("PostStepResult.xml");
    ```

    

    This code represents the main portion of the script. The code performs the following actions:

    -   Calls the StepResult.GetResultsFromDirectory method to get the StepResult XML for each node from the *NodeName*.out files that the RunStep stage created, and saves that information as a list of StepResult objects, one for each node.

    -   Uses the New-Object cmdlet and the constructor to the TestResult class to create a new TestResult object, and sets the Name property of that object.

    -   Calls the CollectResults function in this script to get information from the StepResult objects for the nodes and save the information in a way that the code can access more easily for processsing.

    -   Uses the System.Collections.Generic.List.Add method to add the StepResult objects to the TestResult object.

    -   Calls the GenerateSummary function of this script to create a StepResult object that summarizes the results for all of the nodes in the test.

    -   Uses the System.Collections.Generic.List.Insert method to add the summary StepResult object to the TestResult object as the first object in the list.

    -   Calls the BuildReport function in this script to create a Report.html file from all of the information the TestResult object.
    -   Calls the StepResult.XmlSerializeToFile method to serialize the summary StepResult object as XML as save it to the PostStepResult.xml file.

8.  Save the script file as C:\\SampleTests\\CultureTest2\_PostStep.ps1 on the head node of your HPC cluster.

## Step 4: Test the script for the PostStep stage

To test your PostStep script, you should run the script from the command prompt before incorporating it into a diagnostic test. You only need to test the PostStep script on the head node, because the PostStep stage only runs on the head node during a diagnostic test.

To test this PostStep script, you will need the *NodeName*.out files that you created when you tested the RunStep script. These files will provide results for the PostStep script to work with. In the context of a diagnostic test, the diagnostic service saves the *NodeName*.out files in the correct location for use by the PostStep stage automatically.

**To test the PostStep script**

1.  At a command prompt on the head node, use the **cd** command to change to the C:\\SampleTest\\PostStepTest folder in which you saved the *NodeName*.out files when you tested the RunStep script. For example.

    **cd C:\\SampleTest\\PostStepTest**

2.  Type the following command to test the PostStep script:

    **powershell.exe -Command "& {C:\\SampleTest\\CultureTest2\_PostStep.ps1}"**

3.  Type the **dir** command to verify that the script created the Report.html and PostStepResult.xml files.

4.  Open the PostStepResult.xml file in a text editor such as Notepad. The contents of the file should be similar to the following example:

    ```XML
    <?xml version="1.0"?>
    <StepResult xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" NodeName="Summary">
      <Result>Success</Result>
      <Message/>
      <ExceptionMessage/>
      <Nodes xsi:nil="true"/>
      <FailedNodes/>
      <Environment/>
      <Parameters/>
      <Tables>
        <Table Description="Culture Summary Table" Name="" Tags="">
          <Columns>
            <Column>Operating System Culture</Column>
            <Column>UI Culture</Column>
            <Column>PowerShell Culture</Column>
            <Column>PowerShell UI Culture</Column>
          </Columns>
          <Rows>
            <Row>
              <Items>
                <RowItem>Consistent</RowItem>
                <RowItem>Consistent</RowItem>
                <RowItem>Consistent</RowItem>
                <RowItem>Consistent</RowItem>
              </Items>
            </Row>
          </Rows>
        </Table>
      </Tables>
      <BulletPoints>
        <Information>
          <Type>Information</Type>
          <Message>The operating system culture, UI culture, PowerShell culture, and PowerShell UI culture are consistent with each other on each node.</Message>
        </Information>
        <Information>
          <Type>Information</Type>
          <Message>The set of values for the operating system culture, UI culture, PowerShell culture, and PowerShell UI culture are the same for each node.</Message>
        </Information>
        <Information>
          <Type>Information</Type>
          <Message>The operating system culture, UI culture, PowerShell culture, and PowerShell UI culture are consistent both within each node and across all of the nodes.</Message>
        </Information>
      </BulletPoints>
    </StepResult>
    ```

    

5.  Open the Report.html file in a web browser.

6.  Verify that the report has a Summary section and a section for each of the nodes for which you created a *NodeName*.out file.
7.  Verify that the information in each section matches the expected result.

## Step 5: Create an XML file to define the custom test

The XML file in this example is similar to the ones in the examples in earlier in this guide. See those examples for additional description of the XML elements that you use to define a custom test.

The one important difference in the XML for this test is that the XML contains a [**PostStep**](poststep-element.md) element that specifies the script for the PostStep stage.

**To create an XML file that defines the custom test**

1.  In a text editor such as Notepad, paste the following text to define the metadata for the test.

    ```XML
    <DiagnosticTests>
        <DiagnosticTest
            Name="Culture Consistency Within and Across Nodes"
            Description="Checks culture consistency within and across nodes."
            Company="Contoso, Ltd"
            Suite="Test"
            Alias="CultureTest2">
    
    ```

    

2.  After the text that you inserted in the previous step, paste the following text to define the command that you want to run for the RunStep stage of the diagnostic test.

    ```XML
            <RunStep Command="powershell.exe">
                <Parameters>
                    <Parameter Name="ExecutionPolicy" Value="Bypass" Format="-{0} {1}"/>
                    <Parameter Name="Command" Value="&amp;amp; {\\%CCP_SCHEDULER%\DiagShare\CultureTest2_RunStep.ps1}" Format="-{0} {1}"/>
                </Parameters>
            </RunStep>
    ```

    

    This example uses RunStep-specific parameters to specify some parameters to the **powershell.exe** command that do not require user input. The following command is the RunStep command that this combination of XML elements represents:

    **powershell.exe -ExecutionPolicy Bypass -Command "& {\\\\%CCP\_SCHEDULER%\\DiagShare\\CultureTest2\_RunStep.ps1}"**

3.  After the text that you inserted in the previous step, paste the following text to specify the command that you want to run for the PostStep stage of the test.

    ```XML
            <PostStep Command="powershell.exe">
                <Parameters>
                    <Parameter Name="Command" Value="&amp;amp; {C:\DiagsTest\CultureTest2_PostStep.ps1}" Format="-{0} {1}"/>
                </Parameters>
            </PostStep>
    ```

    

    This example uses PostStep-specific parameters to specify some parameters to the **powershell.exe** command that do not require user input. The following command is the PostStep command that this combination of XML elements represents:

    **powershell.exe -Command "& {C:\\SampleTests\\CultureTest2\_PostStep.ps1}"**

4.  After the text that you inserted in the previous step, paste the following text to add the necessary closing tags to create a valid XML file.

    ```XML
        </DiagnosticTest>
    </DiagnosticTests>
    ```

    

5.  Save the file as C:\\SampleTests\\CultureTest2.xml on the head node.

## Step 6: Add the test to an HPC cluster

In Windows HPC Server 2008 R2, you can add diagnostic tests to an HPC cluster by using HPC PowerShell or at the command prompt.

**To add a custom diagnostic test to an HPC cluster by using HPC PowerShell**

1.  On the head node, click **Start**, point to **All Programs**, click **Microsoft HPC Pack 2008 R2**, right-click **HPC PowerShell**, and then click **Run as administrator**.

2.  In **HPC PowerShell**, type the following cmdlet to add the test:

    **Add-HpcTest -File C:\\SampleTests\\CultureTest2.xml**

    If you need to remove the test from the HPC cluster later, type the **Remove-HpcTest -Alias CultureTest2** cmdlet.

3.  Type the following cmdlet to verify that the test was added to the HPC cluster:

    **Get-HpcTest -Alias CultureTest2**

4.  Type the following command to verify that the metadata and command for the test were correctly added to the HPC cluster:

    **Get-HpcTestDetail -Alias CultureTest2**

**To add a custom diagnostic test to an HPC cluster at a command prompt**

1.  Open a command prompt window and type the following command to add the test:

    **test Add C:\\SampleTests\\CultureTest2.xml**

    If you need to remove the test from the HPC cluster later, type the following command:

    **test Remove CultureTest2**

2.  Type the following command to verify that the test was added to the HPC cluster:

    **test ListTests**

3.  Type the following command to verify that the metadata, parameters, and command for the test were correctly added to the HPC cluster:

    **test ViewTest CultureTest2**

## Step 7: Run the test and view the results

After you add a custom diagnostic test to an HPC cluster, you can use HPC Cluster Manager, HPC PowerShell, or the command prompt window to run the test and view the results in the same way that you do for built-in diagnostic tests that Windows HPC Server 2008 R2 provides.

For information about using HPC Cluster Manager, see Overview of HPC Cluster Manager in the [HPC Cluster Manager Help](http://go.microsoft.com/fwlink/p/?linkid=124146) (http://go.microsoft.com/fwlink/p/?linkid=124146).

**To run the custom diagnostic test in HPC Cluster Manager**

1.  In **Diagnostics**, in the **Navigation Pane**, double-click **Tests** to display the list of companies that provided the diagnostic tests that are available on your HPC cluster, if the list is not already visible.

2.  Double-click **Contoso, Ltd** to display the list of suites, then click **Test** to view the list of tests in the **Test** suite.

3.  In the views pane, right-click the **Culture Consistency Within and Across Nodes** test and click **Run**.

4.  In the **Run Diagnostic Tests** dialog box, select **All nodes** and click **Run**.

5.  If the **Run Test** dialog box appears, click **OK**.

### Additional considerations

To open **HPC Cluster Manager**, click **Start**, point to **All Programs**, click **Microsoft HPC Pack 2008 R2**, and then click **HPC Cluster Manager**. If the **User Account Control** dialog box appears, confirm that the action it displays is what you want, and then click **Continue**.

**To run the custom diagnostic test in HPC PowerShell or at a command prompt**

1.  In **HPC PowerShell**, type the following cmdlet:

    **Invoke-HpcTest -Alias CultureTest2 -NodeName** *ListOfNodesToRunTest*

    or

    At a command prompt, type the following command:

    **test run CultureTest2 -nodes:***ListOfNodesToRunTest*

2.  Note the run identifier that appears in the output of the cmdlet or at the command prompt so that you can view the results of the test later.

> [!Note]
>
> To specify parameter values for a diagnostic test in HPC PowerShell, use the *Parameters* parameter with a value that has the following format: @{*ParameterName1*="*Value1*"\[;*ParameterName2*="*vValue2*";...\]}
>
> To specify a parameter value for a diagnostic test at the command prompt, include a parameter in the command with the following format: -*ParameterName*:"*Value"*

 

**To view the results of the custom test in HPC Cluster Manager**

1.  In **Diagnostics**, in the **Navigation Pane**, click **Test Results**.

2.  In the views pane, locate the test result for the **Culture Consistency Within and Across Nodes** test and wait until the **State** for the result changes to **Success** or **Failure**.

3.  Click the test result for the **Culture Consistency Within and Across Nodes** test.

4.  In the **Detail** pane, click the **Result** tab to view the report on the results for the diagnostic test.

**To view the results of the custom test in HPC PowerShell**

1.  In HPC PowerShell, type the following cmdlet to verify that the test finished and to see the overall results of the test.

    **Get-HpcTestResultDetail -RunId** *RunIdentifier*

2.  Type the following cmdlet to export the report for the test run to a folder:

    **Export-HpcTestResult -RunId** *RunIdentifier* **-Path C:\\SampleTests\\CultureTest2**

3.  In Windows Explorer, navigate to C:\\SampleTests\\CultureTest2 and then double-click **Report.html**.

**To view the results of the custom test at a command prompt**

1.  Open a command prompt window and type the following command to verify that the test finished and to see the overall results of the test.

    **test ViewRun** *RunIdentifier*

2.  Type the following command to view the report for the test run:

    **test ViewResult** *RunIdentifier*

 

 



