---
Description: 'In this example, an administrator of an HPC cluster wants to create a daily operational report that shows the average length of a job for different hours of the day and the average length of the time a job takes to start for different job priorities.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5f9bf141-0b0a-412b-b43d-90ff41158861'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'Use Case 3: Creating a Daily Operational Report in SQL Server Reporting Services'
---

# Use Case 3: Creating a Daily Operational Report in SQL Server Reporting Services

In this example, an administrator of an HPC cluster wants to create a daily operational report that shows the average length of a job for different hours of the day and the average length of the time a job takes to start for different job priorities.

This example uses the features of SQL Server Reporting Service to create the report and deploy it on a report server.

This following assumptions are made for this example:

-   The HPCReporting database in this example is either the live HPCReporting database or a database with the same schema and with data that you transferred from the live HPCReporting database. The latter scenario is recommended.

-   You have SQL Server Reporting Services including SQL Server Business Intelligence Development Studio installed on a server that can access the database described in the previous point.

-   You already have configured the report server and a URL for the server.

For more information, see the following resources:

-   [SQL Server Reporting Services](http://go.microsoft.com/fwlink/p/?linkid=181129) (http://go.microsoft.com/fwlink/p/?linkid=181129)

-   [Configuring a Report Server Installation](http://go.microsoft.com/fwlink/p/?linkid=181130) (http://go.microsoft.com/fwlink/p/?linkid=181130)

-   [Introducing Business Intelligence Development Studio]( http://go.microsoft.com/fwlink/p/?linkid=181131) (http://go.microsoft.com/fwlink/p/?linkid=181131)

## Step 1: Create and set up a Report Server Project

To create a report with SQL Server Reporting Services and deploy it on a report server, you can create a report server project that contains the report in SQL Server Business Intelligence Development Studio. SQL Server Business Intelligence Development Studio is Microsoft Visual Studio 2008 with additional project types that are specific to SQL Server business intelligence.

**To create and set up a report server project**

1.  In SQL Server Business Intelligence Development Studio, on the **File** menu, point to **New,** and then click **Project**.

2.  In the **New Project** dialog box, under **Project types**, click **Business Intelligence Projects**, and then under **Templates**, click **Report Server Project**.

3.  Type a name for the project in the **Name** box, and click **OK**.

4.  In **Solution Explorer**, right-click **Shared Data Sources** and then click **Add New Data Source**.

5.  In the **Shared Data Source Properties** dialog box, type a name for the data source in the **Name** box. In the **Type** list, select **Microsoft SQL Server**, and then click **Edit**.

6.  In the **Connection Properties** dialog box, type or select the name of the server instance that contains the HPCReporting database for your cluster or the server instance that contains a copy of that database in the **Server name** box, and type or select **HPCReporting** in the **Select or enter a database name** box.

7.  In the **Connection Properties** dialog box, click **OK**, and then in the **Shared Data Source Properties** dialog box, click **OK**.

## Step 2: Add a new report and add data sets

After you set up the report server project, you can add a new report to the project. To specify the information from the reporting database that you want to use in your report, you add data sets the report.

For information about data sets, see [Creating a Report Dataset](http://go.microsoft.com/fwlink/p/?linkid=181132) (http://go.microsoft.com/fwlink/p/?linkid=181132).

**To add a new report and add data sets for the report**

1.  In the **Solution Explorer** pane, right-click **Reports** and click **Add New Report**.

2.  In the **Report Wizard**, on the **Welcome to the Report Wizard** page, click **Next**, and then on the **Select the Data Source Wizard** page, click **Next**.

3.  On the **Design the Query** page, in the **Query string** box, type the following SQL query, and then click **Next**:.

    ``` syntax
    SELECT CONVERT(varchar, @QueryDate, 112) AS [Date], DATEPART(hour, EventTime) AS [Hour], AVG(CAST(RunTime AS bigint))/1000.0 AS [AvgJobLength (s)] 
    FROM JobHistoryView 
    WHERE EventTime >= @QueryDate AND EventTime < DATEADD(day, 1, @QueryDate) 
    GROUP BY DATEPART(hour, EventTime) 
    ORDER BY DATEPART(hour, EventTime)
    ```

4.  In the **Define Query Parameters** dialog box, click **OK**.

5.  On each of the **Select Report Type**, **Design the Table**, and **Choose the Table Style** pages, click **Next**.

6.  On the **Completing the Wizard** page, type a name for the report in the **Report name** box, and then click **Finish**.

7.  In the **Report Data** pane, right-click the name of the data source that you added to the report, and then click **Add Dataset**.

8.  In the **Dataset Properties** dialog box, click **Query** in the list on the left, type the following SQL query in the **Query** box, and then click **OK**:

    ``` syntax
    SELECT CONVERT(varchar, @QueryDate, 112) AS [Date], AVG(WaitTime) AS [Wait Time], Priority
    FROM JobHistoryView
    WHERE EventTime >= @QueryDate AND EventTime < DATEADD(day, 1, @QueryDate)
    GROUP BY Priority
    ```

9.  In the **Define Query Parameters** dialog box, click **OK**.

## Step 3: Design the report layout

To help the users of your report understand the information in the report, you will want to organize the information visually in a report layout that contains items such as text, tables, and charts. You can use features in SQL Server Business Intelligence Development Studio to design the layout of your report and add these items.

For information about designing the layout of a report, see [Designing the Report Layout](http://go.microsoft.com/fwlink/p/?linkid=181133) (http://go.microsoft.com/fwlink/p/?linkid=181133).

**To design the report layout**

1.  On the **Design** tab for your report, click a cell in the default table. In the set of rectangles that appear above the columns and to the left of the rows in the table, click the corner rectangle, and then press DELETE.

2.  Right-click anywhere in the body of the report under the name of the report, point to **Insert**, and then click **Text Box**.

3.  Right-click the new text box, and then click **Expression**.

4.  In the **Expression** dialog box, in the **Category** list, click **Parameters**. In the **Values** list, double-click **QueryDate**, and then click **OK** to add the query date to the text box.

5.  Drag the text box that contains the query date so that the top of that text box aligns with the bottom of the text box that contains the name of the report, and resize the text box so that it extends the width of the report.

6.  Right-click anywhere in the body of the report under the text box that you just resized, point to **Insert**, and then click **Chart**.

7.  In the **Select Chart Type** dialog box, under **Line**, click the leftmost chart type, and then click **OK**.

8.  On the **Design** tab, click the new chart. In the **Report Data** pane, click **Hour** under **DataSet1** and drag it to the **Drop category fields here** box on the **Design** tab. In the **Report Data** pane, click **AvgJobLength\_s\_** under **DataSet1** and drag it to the **Drop data fields here** box on the **Design** tab.

9.  On the **Design** tab, double-click the chart title and change the text as follows:

    ``` syntax
    Average Job Length
    ```

10. Double-click the label for the vertical axis and change the text as follows:

    ``` syntax
    Average Job Length (s)
    ```

11. Double-click the label for the horizontal axis and change the text as follows:

    ``` syntax
    Hour of the Day
    ```

12. Drag the chart so that the top of this chart aligns with the bottom of the text box that contains the query date and the left side of the chart aligns with the left side of the report. Resize the chart so that it extends half the width of the body of the report.

13. Right-click the report to the right of the first chart and below the text box with the query date, point to **Insert**, and then click **Chart**.

14. In the **Select Chart Type** dialog box, under **Column**, click the top left chart type, and then click **OK**.

15. On the **Design** tab, click the new chart. In the **Report Data** pane, click **Priority** under **DataSet2** and drag it to the **Drop category fields here** box on the **Design** tab. Then, in the **Report Data** pane, click **Wait\_Time** under **DataSet2** and drag it to the **Drop data fields here** box on the **Design** tab.

16. On the **Design** tab, double-click the chart title, and change the text as follows:

    **Avg. Job Wait Time by Priority**

17. Double-click the label for the vertical axis, and change the text as follows:

    **Avg. Job Wait Time (ms)**

18. Double-click the label for the horizontal axis, and change the text as follows:

    **Priority**

19. Drag this second chart so that the top of this chart aligns with the bottom of the text box that contains the query date and the left side of the chart aligns with the right side of the first chart. Resize the chart so that it extends half the width of the body of the report.

    You may need to adjust the sizes and positions of the text boxes, the charts, and the body of the report so that the charts are large enough to show all of the data and all of the items on the report fit together neatly. You can also adjust the format of the items in the report, such as the text color, background color, and font. For information about making these types of adjustments to the report layout, see [Designing the Report Layout](http://go.microsoft.com/fwlink/p/?linkid=181133) (http://go.microsoft.com/fwlink/p/?linkid=181133).

## Step 4: Preview, build, and deploy the report

After you have queried for the information for your report from the database, and you have specified a report layout to provide that information to the user in a meaningful way, you are ready to preview, build, and deploy the report.

For information about previewing and deploying reports, see [Publishing Data Sources and Reports](http://go.microsoft.com/fwlink/p/?linkid=181134) (http://go.microsoft.com/fwlink/p/?linkid=181134x).

**To preview, build, and deploy the report**

1.  Click the **Preview** tab. In the **Query Date** box, type a date for which you have data about the jobs that ran on your cluster, and then click **View Report**.

2.  Verify that the report appears as desired.

3.  On the **Standard** toolbar, in the **Solution Configuration** list, click **Release**.

4.  On the **Build** menu, click **Build Solution,** and then examine the messages in the **Output** pane to verify that the solution built successfully.

5.  On the **Project** menu, click *Project\_Name***Properties**.

6.  In the *Project\_Name***Property Pages** dialog box, in the **TargetServerURL** box, type the URL for the report server to which you want to deploy the report, and then click **OK**.

7.  On the **Build** menu, click **Deploy***Project\_Name*.

8.  In the **Output** pane, monitor the messages that appear to verify that the deployment succeeds. Click the URL for the report server, and verify that your report appears on the server.

 

 



