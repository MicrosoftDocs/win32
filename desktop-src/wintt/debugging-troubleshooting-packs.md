---
title: Debugging a Troubleshooting Pack
description: A troubleshooting pack can fail during initialization or during the troubleshooting, resolution, or verification phase.
ms.assetid: '5a99a6e5-14dc-4326-9c4d-952767825573'
---

# Debugging a Troubleshooting Pack

A troubleshooting pack can fail during initialization or during the troubleshooting, resolution, or verification phase. Typically, an initialization failure is the result of the pack not being signed or signed correctly, the pack being modified after it was signed, or the pack containing a bad file. Initialization can also fail if the XML is malformed or not valid.

If the error occurred during one of the troubleshooting, resolution, or verification phases, you probably did not catch an exception from WTP or other Windows PowerShell code. To determine the cause of the error, view the debug report that WTP generates when the pack runs. To access the debug report, follow these steps:

1.  Open **Control Panel** and click **All Control Panel Items**, **Troubleshooting**
2.  On the left side, click **View History**
3.  At the bottom of the **History** window, click **Include troubleshooters run as administrator**
4.  Select an instance of the troubleshooter based on **Name** and **Date**
5.  Right-click the instance and select **Open file location**
6.  Open the debug reports (the debug report files end with \*.Debugreport.xml)

Look through the report and find the phase that failed, the script that failed, exception details, or the stack trace.

To help determine why the script is failing, you can use test mode. To test your scripts (without having to comment out your WTP cmdlet calls), configure your development computer to enable TSP Script Test Mode. Test mode lets you test each script in isolation. To enable TSP Script Test Mode:

1.  Open an Elevated PowerShell Window.
2.  Enable execution of unsigned scripts by running `Set-ExecutionPolicy RemoteSigned`.
3.  Run the TestModeSetup.ps1 script included with the TSPDesigner binaries in the Windows SDK.

You can use test mode to find syntax and logic issues in the script; however, you cannot use test mode to find ID mismatches or bad parameters, or to test extensions or user interactions.

If the manifest defines parameters, you must pass the parameters to the script as shown in the following example:

`.\myscript.ps1 paramName=paramValue`

If test mode does not show the error, one of the WTP cmdlets may have thrown an exception. Typically, this is because your script passed bad arguments to the WTP cmdlet.

You can also add debug statements to your debug report using the -Verbosity parameter of the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet. For details, see [Reporting](reporting.md).

## Common errors

The following are common errors that can occur:

-   A script references files that are not included in the pack folder.
-   The interaction or root cause IDs specified in the script do not match those in the troubleshooting manifest. Make sure that the root cause IDs passed to [Update-DiagRootcause](update-diagrootcause-cmdlet.md) match those specified in the manifest.

 

 




