---
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ffc085ca-90bc-40a7-9606-9eda0a93e487'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'Use Case 2: Creating Charge Back Reports in Excel'
---

# Use Case 2: Creating Charge Back Reports in Excel

In this example, an administrator of an HPC cluster wants to determine how much to charge users for running jobs on the cluster. Different organizations can use different methods to determine the charge for using a cluster. Some possible methods for determining the charge for using a cluster include:

-   Charging a fixed rate for the total duration of all of the jobs that the user runs.

-   Charging different rates for different jobs depending on the node groups to which the nodes that run the jobs belong.

    This case assumes that the cluster administrator has set up a set of node groups in advance for the purpose of calculating the charges for using the cluster. This set of node groups as a whole should have the following characteristics:

    -   It should be mutually exclusive, which means that the set includes a given node in only one of the node groups in the set.

    -   It should be collectively exhaustive, which means that the set contains all of the nodes in the cluster.

-   Charging different rates for different jobs depending on the type of the processors that are included on the nodes that ran the jobs.

This example shows how to calculate the total charges for users in all three of these cases. The example consists of creating a stored procedure to query the relevant databases in the HPCReporting database for the necessary data, creating a command script to run the stored procedure periodically and export the results to a comma-separated value (.csv) file, and opening the .csv file in Excel to add additional calculations and create the report.

The following assumptions are made for this example:

-   The HPCReporting database in this example is either the live HPCReporting database or a database with the same schema and with data that you transferred from the live HPCReporting database. The latter scenario is recommended.

-   Excel is installed on a computer that has access to the HPCReporting database described in the previous point.

## Step 1: Creating and running the stored procedure to obtain the necessary data for the charge calculations

Before you can create the report in Excel, you need to create the following items:

-   A stored procedure that queries the HPCReporting database to get the relevant data

-   A command file that runs the stored procedure and saves the result to a .csv file

You can then run the command file periodically to get the data for different time periods.

**To create and run the stored procedure**

1.  Choose one of the following options depending on how you want to charge your users:

    -   If you want to charge users a fixed rate for the total duration of all of the jobs that the users run, type the following Transact-SQL statements in a text editor such as Notepad.

        ``` syntax
        SET ANSI_NULLS ON
        GO

        SET QUOTED_IDENTIFIER ON
        GO

        CREATE PROCEDURE [dbo].ChargeBackJobUsageBased
            @StartQueryTime datetime, 
            @EndQueryTime datetime
        AS
        BEGIN
            SET NOCOUNT ON;
            SELECT [Owner], SUM(CAST(J.RunTime as bigint)) AS RunTime
               FROM HPCReporting.dbo.JobHistoryView AS J
               WHERE J.EventTime >= @StartQueryTime AND J.EventTime < @EndQueryTime
               GROUP BY [Owner]

        END

        GO
        ```

    -   If you want to charge different rates for different jobs depending on the node groups to which the nodes that run the jobs belong, type the following Transact-SQL statements in a text editor such as Notepad. In the list of values after the IN operator in the WHERE clause, use the list of mutually exclusive and collectively exhaustive node groups that you set up to associate node groups with rates.

        ``` syntax
        SET ANSI_NULLS ON
        GO

        SET QUOTED_IDENTIFIER ON
        GO

        CREATE PROCEDURE [dbo].ChargeBackGroupBased
            @StartQueryTime datetime, 
            @EndQueryTime datetime
        AS
        BEGIN
            SET NOCOUNT ON;
            SELECT GroupName, [Owner], SUM(DATEDIFF(ms, A.StartTime, A.EndTime)) AS RunTime
            FROM HPCReporting.dbo.JobHistoryView AS J JOIN HPCReporting.dbo.AllocationHistoryView AS A ON J.JobID=A.JobID AND J.RequeueID=A.RequeueID
            JOIN HPCReporting.dbo.NodeGroupMembershipView AS G ON A.NodeName=G.NodeName
            WHERE J.EventTime >= @StartQueryTime AND J.EventTime < @EndQueryTime AND G.GroupName IN ('NodeGroup1', 'NodeGroup2',..., 'NodeGroupN')
            GROUP BY GroupName, [Owner]

        END

        GO
        ```

    -   If you want to charge different rates for different jobs depending on the type of the processors included on the nodes that run the jobs, type the following Transact-SQL statements in a text editor such as Notepad.

        ``` syntax
        SET ANSI_NULLS ON
        GO

        SET QUOTED_IDENTIFIER ON
        GO

        CREATE PROCEDURE [dbo].ChargeBackProcessorBased
            @StartQueryTime datetime, 
            @EndQueryTime datetime
        AS
        BEGIN
            SET NOCOUNT ON;
            SELECT REPLACE(REPLACE(Processor, ',', ';'), '"', ') AS Processor, [Owner], SUM(DATEDIFF(ms, A.StartTime, A.EndTime)) AS RunTime
            FROM HPCReporting.dbo.JobHistoryView AS J JOIN HPCReporting.dbo.AllocationHistoryView AS A ON J.JobID=A.JobID AND J.RequeueID=A.RequeueID
            JOIN HPCReporting.dbo.NodeView AS N ON A.NodeName=N.NodeName
            WHERE J.EventTime >= @StartQueryTime AND J.EventTime < @EndQueryTime
            GROUP BY REPLACE(REPLACE(Processor, ',', ';'), '"', '), [Owner]


        END

        GO
        ```

        The REPLACE functions in this example replace the commas (,) that occur in the processor names with semicolons (;) so that the processor names are not split among multiple columns when you open the .csv files later in Excel. They remove the quotation marks (") in those processor names so that they can serve as valid values in some Excel functions that are used later.

    > [!Note]
    >
    > The schema name of dbo in these examples is not mandatory, but is a default value that makes later steps simpler.

     

2.  Save the text file as *drive*:\\Reporting\\CreateReportingProcedure.sql.

3.  Open a Command Prompt window, and run the following command to run the Transact-SQL statements and create the stored procedure:

    **osql -s localhost\\COMPUTECLUSTER -E -d HPCReporting -i** *drive***:\\Reporting\\CreateReportingProcedure.sql**

    If needed, replace localhost with the name of the computer that hosts the database you are using, replace COMPUTECLUSTER with the name of the server instance for that database, and replace HPCReporting with the name of that database.

4.  In a text editor such as Notepad, enter the following text and remove the two colons (:) and the space at the beginning of the line that corresponds to the name of the stored procedure that you created earlier in this procedure.

    ``` syntax
    set StartQueryTime='%1'
    set EndQueryTime='%2'

    :: Remove the two colons and space character from the start of the line that corresponds to the stored procedure that you want to run.
    :: bcp "EXEC HPCReporting.dbo.ChargeBackJobUsageBased %StartQueryTime%, %EndQueryTime%" queryout "JobUsageBased_%2.csv" -c -t , -T -S localhost\COMPUTECLUSTER
    :: bcp "EXEC HPCReporting.dbo.ChargeBackGroupBased %StartQueryTime%, %EndQueryTime%" queryout "GroupBased_%2.csv" -c -t , -T -S localhost \COMPUTECLUSTER
    :: bcp "EXEC HPCReporting.dbo.ChargeBackProcessorBased %StartQueryTime%, %EndQueryTime%" queryout "ProcessorBased_%2.csv" -c -t , -T -S localhost\COMPUTECLUSTER
    ```

    If needed, replace localhost with the name of the computer that hosts the database you are using, replace COMPUTECLUSTER with the name of the server instance for that database, and replace HPCReporting with the name of that database.

5.  Save the file as *drive*:\\Reporting\\ExportChargeBackFile.cmd.

6.  Open a Command Prompt window, and run the following command change to the *drive*:\\Reporting directory.

    **cd** *drive***:\\Reporting**

7.  Run the ExportChargeBackFile command with the start date and end date of the time period for which you want to calculate the charges for using the cluster as parameters, for example:

    **ExportChargeBackFile 2009-12-1 2009-12-15**

    This command creates a .csv file with the data you need in the *drive*:\\Reporting directory.

After you create the stored procedure and command file, you can run the ExportChargeBackFile command regularly for new time periods to get the information that you need to calculate the charges to users for running jobs on the cluster. To avoid charging users multiple times for running the same job, specify a time period for the ExportChargeBackFile command that does not overlap the time periods you specified when you ran the command previously. For example, if you previously ran the **ExportChargeBackFile 2009-12-1 2009-12-15** command, next time run the **ExportChargeBackFile 2009-12-16 2009-12-31** command.

**Frequency for exporting data to calculate chargeback** The examples that charge different rates depending on the node group or processor that the job ran on use information from the [**AllocationHistoryView**](allocationhistoryview.md). The HPCReporting database typically stores the data for this view for only a short amount of time—five days by default. The length of time that the database stores this data is specified by the AllocationHistoryTtl configuration parameter. So for these examples, you need to run the ExportChargeBackFile command as often or more often than the value specified by this configuration parameter.

The database stores the data for the [JobHistoryView](jobhistoryview.md) that is used in the example that charges a single rate for total job usage for a longer period of timeâ€”365 days by default. The length of time that the database stores this data is specified by the DataExtensibilityTtl configuration parameter. In this case, you need to run the ExportChargeBackFile command as often or more often than the value specified by the DataExtensibilityTtl configuration parameter.

For more information about these configuration parameters that control how long the database stores data, see [Reporting Features in Windows HPC Server 2008 R2](reporting-features-in-windows-hpc-server-2008-r2.md).

## Step 2: Adding charge calculations and creating the report in Excel

After you export the data for a given time period to a .csv file, you can open that file in Excel, add calculations to determine the charge for each user, and create a report of those charges.

Creating a report in the case where you charge a single rate for total job duration is slightly easier than in the other cases.

**To add charge calculations and create the report in Excel when charging a single rate for total job usage**

1.  In Windows Explorer, browse to the *drive*:\\Reporting folder, and then double-click **JobUsageBased\_***EndDate***.csv**.

2.  Verify that the spreadsheet contains user names in the first column and numbers in the second column.

3.  Right-click the row number for the first row, and click **Insert** to insert a new row before the first row.

4.  Add the following heading text to the first three columns of the first row.

    

    |                     |                                       |                             |
    |---------------------|---------------------------------------|-----------------------------|
    | **User**<br/> | **Total Job Runtime (ms)**<br/> | **Total Charge**<br/> |

    

     

5.  In the cell directly under the **Total Charge** heading, enter the following formula:

    **=B2\****rate\_per\_hour***/3600000**

6.  Click the cell to which you added the formula and drag the mouse down the column to the last row that contains data, and then type CTRL+D to apply the formula to each row.

7.  On the **Home** tab, in the **Cells** group, click **Format**, then click **Format Cells**.

8.  On the **Number** tab of the **Format Cells** dialog box, under **Category**, click **Currency**, select the dollar sign (**$**) from the **Symbol** list, type **2** in the **Decimal places** box, and then click **OK**.

9.  Click the Office button, and click **Save** to save the file.

Creating a report in the cases where you charge a different rates for different node groups or different processors is somewhat more complex.

**To add charge calculations and create the report in Excel when charging different rates for different node groups**

1.  In Windows Explorer, browse to the *drive*:\\Reporting folder, and then double-click **GroupBased\_***EndDate***.csv** or **ProcessorBased\_***EndDate***.csv**.

2.  Verify that the spreadsheet contains node group names or processor information in the first column, user names in the second column, and numbers in the third column.

3.  Click the column **B** label to select the second column.

4.  On the **Home** tab, in the **Clipboard** group, click **Copy**.

5.  On the **Home** tab, in the **Cells** group, click **Insert**, and then click **Insert Sheet**. The new worksheet becomes the active worksheet.

6.  On the **Home** tab, in the **Clipboard** group, click **Paste**. The values from the second column of the original worksheet are pasted into the first column of the new worksheet.

7.  Click the **Data** tab, and in the **Data Tools** group, click **Remove Duplicates**.

8.  In the **Remove Duplicates** dialog box, click **OK**.

9.  In the **Microsoft Office Excel** dialog box, click **OK**.

10. Right-click the row number for the first row, and click **Insert** to insert a new row before the first row.

11. Add the following heading text to the first two columns of the first row.

    

    |                     |                             |
    |---------------------|-----------------------------|
    | **User**<br/> | **Total Charge**<br/> |

    

     

12. Choose one of the following option depending on how you want to charge your users:

    -   If you charge different rates for using different node groups, enter the following formula in the cells directly under the **Total Charge** heading. Include terms for each node group and substitute the names and rates for each of the node groups as appropriate.

        **=SUMIFS('GroupBased\_***EndDate***'!C:C,'GroupBased\_***EndDate***'!A:A, "=***NodeGroup1*"**, 'GroupBased\_***EndDate***'!B:B, Sheet1!A2)\****Hourly\_Rate\_For\_NodeGroup1***/3600000+SUMIFS('GroupBased\_***EndDate***'!C:C,'GroupBased\_***EndDate*'**!A:A, "=***NodeGroup2***", 'GroupBased\_***EndDate*'**!B:B, Sheet1!A2)\****Hourly\_Rate\_For\_NodeGroup2***/3600000+***...***+SUMIFS('GroupBased\_***EndDate***'!C:C,'GroupBased\_***EndDate***'!A:A, "=***NodeGroupN***", 'GroupBased\_***EndDate*'**!B:B, Sheet1!A2)\****Hourly\_Rate\_For\_NodeGroupN***/3600000**

    -   If you charge different rates for using different types of processors, enter the following formula in the cell directly under the **Total Charge** heading. Include terms for each processor and substitute the names (using the format on the original worksheet) and rates for each of the processors as appropriate.

        **=SUMIFS('ProcessorBased\_***EndDate***'!C:C,'ProcessorBased\_***EndDate***'!A:A, "=***Processor1*"**, 'ProcessorBased\_***EndDate***'!B:B, Sheet1!A2)\****Hourly\_Rate\_For\_Processor1***/3600000+SUMIFS('ProcessorBased\_***EndDate***'!C:C,'ProcessorBased\_***EndDate*'**!A:A, "=***Processor2***", 'ProcessorBased\_***EndDate*'**!B:B, Sheet1!A2)\****Hourly\_Rate\_For\_Processor2***/3600000+***...***+SUMIFS('ProcessorBased\_***EndDate***'!C:C,'ProcessorBased\_***EndDate***'!A:A, "=***ProcessorN***", 'ProcessorBased\_***EndDate*'**!B:B, Sheet1!A2)\****Hourly\_Rate\_For\_ProcessorN***/3600000**

13. Click the cell directly under the **Total Charge** heading and drag the mouse down the column to the last row that contains data, and then type CTRL+D to apply the formula to each row.

14. On the **Home** tab, in the **Cells** group, click **Format**, and then click **Format Cells**.

15. On the **Number** tab of the **Format Cells** dialog box, under **Category**, click **Currency**, select the dollar sign (**$**) from the **Symbol** list, type **2** in the **Decimal places** box, and then click **OK**.

16. Click the Office button and click **Save** to save the file.

 

 




