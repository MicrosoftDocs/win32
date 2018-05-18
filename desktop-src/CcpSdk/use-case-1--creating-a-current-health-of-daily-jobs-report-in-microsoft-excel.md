---
Description: 'In this example, a cluster administrator runs a fixed set of jobs every day and wants to have a convenient way to view the health of those jobs for the current day.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a9458622-1ba2-42af-a2c0-e5273171b962'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'Use Case 1: Creating a Health Report for Daily Jobs in Excel'
---

# Use Case 1: Creating a Health Report for Daily Jobs in Excel

In this example, a cluster administrator runs a fixed set of jobs every day and wants to have a convenient way to view the health of those jobs for the current day. Not only does the administrator want to check whether the jobs succeeded or failed, but whether the jobs took the expected amount of time. The administrator has estimates of how long each of the jobs should take to run and does not expect the duration of the jobs to vary from the estimates by more than three percent.

This example uses features of Microsoft Office Excel 2007 to get the job history data from the HPCReporting database and to analyze the data and summarize the results. To indicate the health of the job, the example uses the values in the following table.



| Health value      | Description                                                                                                              |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Red<br/>    | The job failed or was canceled.<br/>                                                                               |
| Yellow<br/> | The job finished, but the duration of the job differed from the expected duration by more than three percent.<br/> |
| Green<br/>  | The job finished, and the duration of the job differed from the expected duration by less than three percent.<br/> |



 

The following assumptions are made for this example:

-   A set of jobs is created and submitted to the HPC cluster on a daily basis through a mechanism such as a scheduled task that runs a script or program to create the jobs in an automated fashion.

-   Each job in this set of jobs has a name, and that name remains the same every day. The name for a job in the set of daily jobs should not be the same as the name of any other job in the set or any job for the HPC cluster that is not part of this daily set of jobs.

-   The administrator already has estimates for the amount of time that the jobs should take to run.

-   The HPCReporting database in this example is either the live HPCReporting database or a database with the same schema and with data that you transferred from the live HPCReporting database. The latter scenario is recommended.

-   Excel is installed on a computer that has access to the HPCReporting database described in the previous point.

> [!Note]  
> You need to refresh the report each day to get the current data for the report. After the report is refreshed, the data in the report applies only to the most recent submission of the jobs that the report tracks, and the report does not track the state or performance of the jobs over multiple days. You need to save the report data daily or modify the report to track the history of the job state and performance.

 

## Step 1: Create a connection to the SQL database to get job history data

To create this report, you first need to get the relevant data from the JobHistoryView in the HPCReporting database for the cluster, or a copy of that database.

**To create a connection to the SQL database to get job history data**

1.  In Excel, click the **Data** tab. In the **Get External Data** group, click **From Other Sources** and then click **From SQL Server**.

2.  In the **Server name** box on the **Connect to Database Server** page of the **Data Connection Wizard**, type the name of the computer and SQL Server instance that hosts the HPCReporting database for your HPC cluster or a database that contains a copy of the data from that database.

    The name that you type should have a format of *ServerName*\[\\*InstanceName*\]. You can omit the instance name if you transferred the reporting data to the unnamed default SQL instance on another server.

3.  Click **Use Windows Authentication** and then click **Next**.

    or

    Click **Use the following User Name and Password** if you want to connect to the database with a different account or do not want to use Windows authentication to connect to the database, then type a user name and password for an account that can access the database in the **User Name** and **Password** boxes and click **Next**.

4.  On the **Select Database and Table** page, select **HPCReporting** from the **Select the database that contains the data you want** list, select the **Connect to a specific table** check box, click **JobHistoryView**, and then click **Next**.

5.  On the **Save Data Connection File and Finish** page, type a description for the connection in the **Description** box, and then click **Finish**.

6.  In the **Import Data** dialog box, click **Properties**.

7.  On the **Usage** tab of the **Connection Properties** dialog box, select the **Refresh every 60 minutes** and **Refresh data when opening the file** check boxes, and then click **OK**.

8.  In the **Import Data** dialog box, click **OK**.

9.  Double-click the tab on the worksheet that populates with the job history data, and change the name to **Job History Details**.

10. Leave the Excel file open for the next section.

## Step 2: Create the report

After you have set up the Excel file so that it has the relevant job history data, you can set up a worksheet for the report.

To create the report, you need to add column headings, and then fill in the names of the jobs that you want to track and the amount of time you expect each job to take. Then you add a **Refresh** button to the form and create VBScript code for a macro that you assign to the button. When the user clicks **Refresh**, the script will calculate and fill in the information for the rest of the report.

**To create the report**

1.  In the Excel file that you created by following the previous procedure in this topic, double-click the tab for an empty worksheet and change the name of the worksheet to **Summary**.

2.  In the first row of the **Summary** tab, add the following values to the first five cells to create headings for the report:

    

    |                         |                                           |                          |                                         |                       |
    |-------------------------|-------------------------------------------|--------------------------|-----------------------------------------|-----------------------|
    | **Job Name**<br/> | **Expected Job Duration (ms)**<br/> | **Job State**<br/> | **Actual Job Duration (ms)**<br/> | **Health**<br/> |

    

     

3.  In the **Job Name** column, add the names of the jobs for which you want to track the job health. Add each name only once.

4.  In the **Expected Job Duration (ms)** column, add the amount of time in milliseconds that you expect the corresponding jobs in the **Job Name** column to take.

5.  If the **Developer** tab is not visible, perform the following actions to make it visible:

    -   Click the Office button and then click **Excel Options**.
    -   In the **Excel Options** dialog box, click **Popular**, select the **Show Developer tab in the Ribbon** check box, and then click **OK**.

6.  On the **Developer** tab, click **Insert**, then click the button control in the top left under **Form Controls**.

7.  Near the top of the sixth column of the sheet, drag the cursor to create a button of the size that you want.

8.  In the **Assign Macro** dialog box, click **New**.

9.  In the **Microsoft Visual Basic** editor, in the **Book1 - Module1 (Code)** window, replace the existing code with the following code:

    ```VB
    Option Explicit
    Option Compare Text

    Function GetColorFromString(colorString As String) As Long

        If colorString = "Red" Then
            GetColorFromString = RGB(255, 0, 0)
        ElseIf colorString = "Green" Then
            GetColorFromString = RGB(0, 255, 0)
        ElseIf colorString = "Yellow" Then
            GetColorFromString = RGB(255, 200, 0)
        Else
            GetColorFromString = RGB(0, 0, 255)
        End If
                                                        
    End Function
                                                        
    Sub Button1_Click()
                                                            
        Dim jobList As New Collection
        Dim expectTimeList As New Collection
        Dim jobTimeList As New Collection
        Dim populateStartIndex As Long
        Dim i As Long
        Dim j As Long
        populateStartIndex = 4
        With Worksheets("Summary")
            For i = 2 To 5000
                If (IsEmpty(.Cells(i, 1))) Then
                    populateStartIndex = i
                    i = 5000
                    ' Break.
                Else
                    jobList.Add (.Cells(i, 1))
                    expectTimeList.Add (.Cells(i, 2))
                    Dim minDate As Date
                    minDate = "1900-01-01"
                    jobTimeList.Add (minDate)
                    ' Clear the last three columns.
                    Worksheets("Summary").Cells(i, 3).ClearContents
                    Worksheets("Summary").Cells(i, 4).ClearContents
                    Worksheets("Summary").Cells(i, 5).ClearContents
                End If
            Next i
            ' Clear the rows after the first row without a job name.
            For i = populateStartIndex + 1 To 2000000000
                If (IsEmpty(.Cells(i, 1))) Then
                    i = 2000000000
                    ' Break.
                Else
                    .Cells(i, 1).EntireRow.ClearContents
                End If
            Next i
        End With
                                                                                                                                                                                                                                                                   
        With Worksheets("Job History Details")
            For i = 2 To 2000000000
                If (IsEmpty(.Cells(i, 1))) Then
                    i = 2000000000
                    ' Break.
                Else
                    ' Get the actual run time and event for the job.
                    Dim evt As String
                    Dim light As String
                    Dim jobName As String
                    Dim runTime As Long
                    Dim expectedTime As Long
                    Dim evtTime As Date
                                                                                                                                                                                                                                                                   
                    jobName = .Cells(i, 4)
                    evt = .Cells(i, 5)
                    evtTime = .Cells(i, 6)
                    runTime = .Cells(i, 19)
                    ' In case the job is not found.
                    light = "Black"
                    expectedTime = -1
                                                                                                                                                                                                                                                                   
                    ' Test if the job is in the list of jobs to track.
                    For j = 1 To jobList.Count
                        If jobList.Item(j) = jobName Then
                            If (Not evt = "Finished") Then
                                light = "Red"
                            Else
                                expectedTime = expectTimeList.Item(j)
                                If (runTime) >= expectedTime * 1.03 Or runTime <= expectedTime * 0.97 Then
                                    light = "Yellow"
                                Else
                                    light = "Green"
                                End If
                            End If
                                                                                                                                                                                                                                                                   
                           ' Update the job later.
                            If jobTimeList.Item(j) < evtTime Then
                                jobTimeList.Remove (j)
                                If jobTimeList.Count = 0 Then
                                    jobTimeList.Add (evtTime)
                                ElseIf j > 1 Then
                                    jobTimeList.Add evtTime, , , j - 1
                                Else
                                    jobTimeList.Add evtTime, , j
                                End If
                                                                                                                                                                                                                                                                   
                            Worksheets("Summary").Cells(j + 1, 3) = evt
                            Worksheets("Summary").Cells(j + 1, 4) = runTime
                            Worksheets("Summary").Cells(j + 1, 5).Hyperlinks.Delete
                            Worksheets("Summary").Cells(j + 1, 5).Hyperlinks.Add Anchor:=Worksheets("Summary").Cells(j + 1, 5), Address:="", _
                                SubAddress:=("'Job History Details'!A" + Trim(Str(i)) + ""), ScreenTip:="click to go to detailed row", TextToDisplay:=light
                            Worksheets("Summary").Cells(j + 1, 5).Font.Color = GetColorFromString(light)
                            End If                                                                                                                                                                                                                                 

                        End If
                    Next j
                End If
            Next i
        End With
    End Sub
    
    ```

    

10. On the **File** menu, click **Close and Return to Microsoft Excel**.

11. Right-click the button that you created, click **Edit Text**, and then change the text to **Refresh**.

12. Click the **Refresh** button. The macro fills in the third, fourth, and fifth columns to complete the report.

13. Save the file.

You can now open this Excel file on future days, click **Refresh** on the **Summary** tab, and get the current status of the jobs for that day. If some jobs failed, you can investigate the failures and rerun the failed jobs. If the actual duration of some jobs differed too much from the expected duration, you can investigate the causes.

 

 




