---
Description: 'Windows&\#160;HPC&\#160;Server&\#160;2008&\#160;R2 provides several features to help you get data to use in custom reports about an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0b912f74-fc96-485b-ba5a-89863e29d059'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Creating Custom Reports for an HPC Cluster
---

# Creating Custom Reports for an HPC Cluster

Windows HPC Server 2008 R2 provides several features to help you get data to use in custom reports about an HPC cluster. For information about these features, see [Reporting Features in Windows HPC Server 2008 R2](reporting-features-in-windows-hpc-server-2008-r2.md). Windows HPC Server 2008 R2 does not provide tools to analyze that data, design layouts for reports that interpret that data, or publish such reports. You can, however, use other Microsoft software products such as Microsoft Office Excel 2007 or SQL Server Reporting Services to perform these tasks.

## Creating a custom report

The general process of creating a custom report for an HPC cluster consists of the following high-level steps:

1.  Transfer the data from the reporting database for the HPC cluster or from an HPC cmdlet to a working location.

    > [!Note]
    >
    > This step is optional, but highly recommended.

     

2.  Use other software to analyze the data and build reports that visually present the data in a meaningful way.

### Transferring data to a working location

Transferring the reporting data to working location is optional, but highly recommended because working with the data in a separate location frees you from the constraints of the design and capabilities of the SQL reporting database, and thus provides you . Working with the data in a separate location thus provides you with the following benefits:

-   Reduces the demand on the resources of the HPC cluster (such as the head node if the reporting database is installed on the head node).

-   Provides you with the flexibility to add items such as cubes to the database for analyzing the data.

-   Enables you to keep data as long you want, subject to the available resources that you dedicate to the computer that hosts your custom reports. The live reporting database for the cluster deletes data according to the configuration of the DataExtensibilityTtl and AllocationHistoryTtl settings.

-   Enables you to control access to the data according to your needs, rather than letting Windows HPC Server 2008 R2 manage access control for the reporting database.

You can use a number of methods to transfer the data from the SQL reporting database or from an HPC cmdlet to a working location.

### Transferring data from the SQL reporting database to a working location

You can transfer reporting data from the SQL reporting database to different kinds of working locations, such as another SQL database or an Excel spreadsheet.

The following table lists methods that you can use to transfer information from the SQL reporting database for the cluster to another SQL database. You will want to use a method that allows you to retrieve data incrementally for a specified date range before the HPC reporting database deletes the data according to the configuration of the DataExtensibilityTtl and AllocationHistoryTtl settings.



| Method                                                                              | Resource                                                                                                                                                             |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SQL Server Import and Export Wizard<br/>                                      | [How to: Run the SQL Server Import and Export Wizard](http://go.microsoft.com/fwlink/p/?linkid=181138) (http://go.microsoft.com/fwlink/p/?linkid=181138)<br/>  |
| Importing and Exporting Bulk Data<br/>                                        | [Importing and Exporting Bulk Data](http://go.microsoft.com/fwlink/p/?linkid=181137) (http://go.microsoft.com/fwlink/p/?linkid=181137)<br/>                    |
| Inserting rows from a remote table by using INSERT and SELECT subqueries<br/> | [Inserting Rows by Using INSERT and SELECT Subqueries](http://go.microsoft.com/fwlink/p/?linkid=181136) (http://go.microsoft.com/fwlink/p/?linkid=181136)<br/> |



 

The following table lists methods that you can use to transfer information from the SQL reporting database for the cluster to Excel.



| Method                                     | Resource                                                                                                                                            |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| External data connection<br/>        | [Connect to (import) SQL Server data](http://go.microsoft.com/fwlink/p/?linkid=181911) (http://go.microsoft.com/fwlink/p/?linkid=181911)<br/> |
| SQL Server Integration Services<br/> | [Exporting SQL Server Data to Excel](http://go.microsoft.com/fwlink/p/?linkid=181140) (http://go.microsoft.com/fwlink/p/?linkid=181140)<br/>  |



 

### Transferring data from an HPC cmdlet to a working location

Windows HPC Server 2008 R2 also provides cmdlets for Windows PowerShell that you can use to get data for custom reports. For information about these cmdlets, see [Reporting Features in Windows HPC Server 2008 R2](reporting-features-in-windows-hpc-server-2008-r2.md).

You can transfer the output of these cmdlets to different types of working locations, such as to an XML file or a SQL database.

### Transferring data from an HPC cmdlet to an XML file

To export the output of an HPC cmdlet to an XML file, redirect the output of the HPC cmdlet to the Windows PowerShell [Export-CliXml](http://go.microsoft.com/fwlink/p/?linkid=113297) cmdlet. The following example exports the output of the Get-HpcMetricValueHistory cmdlet to an XML file.


```PowerShell
Get-HpcMetricValueHistory -StartDate "1/18/2010 12:00:00 AM" -EndDate "1/19/2010 12:00:00 AM" | Export-CliXml -Path C:\HPCReportingFiles\MetricValues_1_18_2010.xml
```



After you export the output of an HPC cmdlet to an XML file, you can access the data in the file within a Windows PowerShell script by using the Windows PowerShell [Import-CliXml](http://go.microsoft.com/fwlink/p/?linkid=113340) cmdlet. This cmdlet reads the data from the XML file and creates an array of objects that correspond to the output of the original HPC cmdlet.

The following example reads an XML file and saves the corresponding array of objects in a variable in a Windows PowerShell script.


```PowerShell
$MetricValueHistory = Import-CliXml -Path C:\HPCReportingFiles\MetricValues_1_18_2010.xml
```



### Transferring data from an HPC cmdlet to a SQL database

You can transfer the output of an HPC cmdlet to a SQL database by using the Windows PowerShell SDK to retrieve the output of the HPC cmdlet and then using ADO.NET to add the data to a SQL database.

The following example is a function that retrieves the output from the Get-HpcMetricValueHistory HPC cmdlet and stores it in a collection of PSObject objects.


```CSharp
        static public Collection<PSObject> getHPCMetricValueHistory(string startDate, string endDate)
        {
            Collection<PSObject> result;
            using (Runspace runspace = RunspaceFactory.CreateRunspace())
            {
                runspace.Open();
                Pipeline pipeline = runspace.CreatePipeline();
                pipeline.Commands.AddScript("Import-Module Microsoft.Hpc");
                pipeline.Commands.AddScript("Get-HpcMetricValueHistory -StartDate \"" + startDate + "\" -EndDate \"" + endDate + "\"");
                result = pipeline.Invoke();
                runspace.Close();
            }

            return result;
        }

```



For information about using the Windows PowerShell SDK to retrieve the output of an HPC cmdlet, see [Writing a Windows PowerShell Host Application]( http://go.microsoft.com/fwlink/p/?linkid=181915) (http://go.microsoft.com/fwlink/p/?linkid=181915).

For information about using ADO.NET to add the data to a SQL database, see [Retrieving and Modifying Data in ADO.NET](http://go.microsoft.com/fwlink/p/?linkid=181914) (http://go.microsoft.com/fwlink/p/?linkid=181914).

### Using other software to analyze the data and create reports

Windows HPC Server 2008 R2 does not provide tools to analyze the HPC reporting data, design layouts for reports that interpret that data, or publish such reports. You can, however, use other Microsoft software products and technologies to perform these tasks, including the following:

-   Excel

-   SQL Server Reporting Services

-   Silverlight

The software or technology that you choose for creating reports depends on your reporting needs and expertise. Because the types of reports and the tools for creating those reports vary, the exact procedure to create a custom report varies as well, and you need to adapt your procedures to your needs and the tools that you use. The following topics provide examples of procedures that you can use the types of reports you can create:

-   [Use Case 1: Creating a Health Report for Daily Jobs in Excel](use-case-1--creating-a-current-health-of-daily-jobs-report-in-microsoft-excel.md)

-   [Use Case 2: Creating Charge Back Reports in Excel](use-case-2--creating-change-back-reports-in-excel.md)

-   [Use Case 3: Creating a Daily Operational Report in SQL Server Reporting Services](use-case-3--creating-a-daily-operational-report-in-sql-server-reporting-services.md)

 

 




