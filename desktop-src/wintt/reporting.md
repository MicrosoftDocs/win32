---
title: Reporting
description: WTP generates two XML report files when it runs the troubleshooting pack ResultsReport.xml and DebugReport.xml.
ms.assetid: 929bcc24-8381-4718-9bb5-c82271f21ed3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reporting

WTP generates two XML report files when it runs the troubleshooting pack: ResultsReport.xml and DebugReport.xml. The results report contains the following information:

-   The troubleshooters that were run and whether the root causes were detected and fixed.
-   The resolvers that were run successfully, failed, or were not run.
-   Information about the computer on which the package ran.

The following procedure describes how to access the results report.

**To access the results report**

1.  Open **Control Panel** and click **All Control Panel Items**, **Troubleshooting**
2.  On the left side, click **View History**
3.  At the bottom of the **History** window, click **Include troubleshooters run as administrator**
4.  Select an instance of the troubleshooter based on **Name** and **Date**
5.  Right-click the instance and select **Open file location**
6.  Open the results report

WTP uses an XSL style sheet that is based on the [Report](report-schema.md) schema to render the ResultReport.xml file. You can use the report schema to write transforms for consuming the contents of a results report.

To update the status of the root cause in the reports, you must use the [Update-DiagRootcause](update-diagrootcause-cmdlet.md) cmdlet in your troubleshooter and verifier scripts. In the troubleshooter script, the -Detected parameter will set the root cause status in the report to Not Detected (false) or Detected (true). In the verifier script, the -Detected parameter will set the root cause status in the report to Fixed (true) or Not Fixed (false). If you do not use Update-DiagRootcause in the troubleshooter script, the root cause status is Not Checked.

The debug report contains a list of methods called on your package and a list of scripts run for your package. Each method has its return code, the arguments it was called with, and how long it took to run. Each script invocation has information on whether it succeeded or failed, the arguments it was called with, how long it took to run, and any specific exceptions raised by the script. The information is useful for improving the performance of your package or determining why something is failing. For details on using the debug report, see [Debugging Troubleshooting Packs](debugging-troubleshooting-packs.md).

The contents of the reports are localized to the locale of the user who initiated the troubleshooting pack.

If you use the [Invoke-TroubleshootingPack](invoke-troubleshootingpack-cmdlet.md) cmdlet to run the pack from the command line, all result files, including the reports, are deleted when the pack completes. To persist the reports, use the -Result parameter to save the files to a specified folder.

## Custom Reporting

You can use the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet to add additional information to the report that can be useful for understanding the state of the computer or the execution of the script. The information is added to the result report unless the -Verbosity parameter is set to Debug, in which case the information is added to the debug report.

The location in the report to which the details are added depends on the phase from which you are calling the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet. For example, if you are calling Update-DiagReport from a troubleshooter, the details are added to the Detection Details section of the report unless you include the -RootcauseId parameter, in which case the details are added to the Issues Found section of the report. If you are calling Update-DiagReport from a resolver, the details are added to the Issues Found section of the report for that resolution. If you are calling Update-DiagReport from a verifier, the call is ignored unless the -Verbosity parameter is set to Debug, in which case the details are added to the DebugReport.

If you include the -RootcauseId parameter, you must call at some point the [Update-DiagRootcause](update-diagrootcause-cmdlet.md) cmdlet for that root cause to provide status (you cannot use -RootcauseId for a "Not Checked" root cause).

You can add the information directly in the report using an XML object or you can add a link in the report that points to a file that contains the information. If you specify an XML object, the XML must be well formed. To ensure that the XML is well formed, use the ConvertTo-Xml cmdlet to encode the object as an XML document. You would then pipe the result to Update-DiagReport (for example, $obj \| ConvertTo-Xml \| Update-DiagReport). For details, see the Notes section of [Update-DiagReport](update-diagreport-cmdlet.md).

For debug reports, you should add tracing statements, error codes, exceptions, and other useful information for determining why the script is not working as expected. The following example shows how to add a stack trace to the debug report.


```PowerShell
try {
...
}
catch {
$_.Exception.StackTrace | ConvertTo-Xml | Update-DiagReport -Id Exception -Name Exception -Verbosity Debug
throw
}
```



 

 




