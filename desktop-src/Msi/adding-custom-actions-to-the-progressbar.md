---
description: Custom Actions can add time and progress information to a ProgressBar control. For more information about creating an action display dialog box having a ProgressBar, see Authoring a ProgressBar Control.
ms.assetid: 101e6b59-3791-450c-9dc6-8930bd665a93
title: Adding Custom Actions to the ProgressBar
ms.topic: article
ms.date: 05/31/2018
---

# Adding Custom Actions to the ProgressBar

[Custom Actions](custom-actions.md) can add time and progress information to a [ProgressBar](progressbar-control.md) control. For more information about creating an action display dialog box having a ProgressBar, see [Authoring a ProgressBar Control](authoring-a-progressbar-control.md).

Note that two custom actions must be added to the Windows Installer package to accurately report time and progress information to the ProgressBar. One custom action must be a deferred custom action. This custom action should complete your custom installation and send the amounts of individual increments to the [ProgressBar](progressbar-control.md) control when the installer runs the installation script. The second custom action must be an immediate execution custom action that informs the ProgressBar how many ticks to add to the total count during the acquisition and script generation phase of the installation.

**To add a custom action to the ProgressBar**

1.  Decide how the custom action will describe its progress. For example, a custom action that installs registry keys could display a progress message and update the [ProgressBar](progressbar-control.md) each time the installer writes one registry key.
2.  Each update by the custom action changes the length of the [ProgressBar](progressbar-control.md) by a constant increment. Specify or calculate the number of ticks in each increment. Typically a change in ProgressBar length of one tick corresponds to the installation of one byte. For example, if the installer installs approximately 10000 bytes when it writes one registry key, you can specify that there are 10000 ticks in an increment.
3.  Specify or calculate the total number of ticks the custom action adds to the length of the [ProgressBar](progressbar-control.md). The number of ticks added by the custom action is usually calculated as: (tick increment) x (number of items). For example, if the custom action writes 10 registry keys, the installer installs approximately 100000 bytes and the installer therefore must increase the estimate of the final total length of the ProgressBar by 100000 ticks.
    > [!Note]  
    > To calculate this dynamically, the custom action must contain a section that is immediately executed during script generation. The amount of ticks reported by your deferred execution custom action must be equal to the number of ticks added to the total tick count by the immediate execution action. If this is not the case, the time remaining as reported by the TimeRemaining text control will be inaccurate.

     

4.  Separate your custom action into two sections of code: a section that runs during the script generation phase and a section that runs during the execution phase of the installation. You can do this using two files or you can use one file by conditioning on the run mode of the installer. The following sample uses one file and checks the installation state. Sections of the sample are conditioned to run depending on whether the installer is in the execution or script generation phase of the installation.
5.  The section that runs during script generation should increase the estimate of the final total length of the [ProgressBar](progressbar-control.md) by the total number of ticks in the custom action. This is done by sending a **ProgressAddition** progress message.
6.  The section that runs during the execution phase of installation should set up message text and templates to inform the user about what the custom action is doing and to direct the installer on updating the [ProgressBar](progressbar-control.md) control. For example, inform the installer to move the ProgressBar forward one increment and send an explicit progress message with each update. There is usually a loop in this section if the custom action is installing something. With each pass through this loop, the installer can install one reference item such as a registry key and update the ProgressBar control
7.  Add an immediate execution custom action to your Windows Installer package. This custom action informs the [ProgressBar](progressbar-control.md) how much to advance during the aquisition and script generation phases of the installation. For the following sample, the source is the DLL created by compiling the sample code and the target is the entry point, CAProgress.
8.  Add a deferred execution custom action to your Windows Installer package. This custom action completes the steps of the actual installation and informs the [ProgressBar](progressbar-control.md) how much to advance the bar at the time when the installer runs the installation script. For the following sample, the source is the DLL created by compiling the sample code and the target is the entry point, CAProgress.
9.  Schedule both custom actions between [InstallInitialize](installinitialize-action.md) and [InstallFinalize](installfinalize-action.md) in the [InstallExecuteSequence](installexecutesequence-table.md) table. The deferred custom action should be scheduled immediately after the immediate execution custom action. The installer will not run the deferred custom action until the script is executed.

The following sample shows how a custom action can be added to the [ProgressBar](progressbar-control.md). The source of both custom actions is the DLL created by compiling the sample code and the target of both custom actions is the entry point, CAProgress. This sample does not make any actual changes to the system, but operates the ProgressBar as if installing 10 reference items that are each approximately 10,000 bytes in size. The installer updates the message and ProgressBar each time it installs a reference item.


```C++
#include <windows.h>
#include <msiquery.h>
#pragma comment(lib, "msi.lib")

// Specify or calculate the number of ticks in an increment
// to the ProgressBar
const UINT iTickIncrement = 10000;
 
// Specify or calculate the total number of ticks the custom 
// action adds to the length of the ProgressBar
const UINT iNumberItems = 10;
const UINT iTotalTicks = iTickIncrement * iNumberItems;
 
UINT __stdcall CAProgress(MSIHANDLE hInstall)
{
    // Tell the installer to check the installation state and execute
    // the code needed during the rollback, acquisition, or
    // execution phases of the installation.
  
    if (MsiGetMode(hInstall,MSIRUNMODE_SCHEDULED) == TRUE)
    {
        PMSIHANDLE hActionRec = MsiCreateRecord(3);
        PMSIHANDLE hProgressRec = MsiCreateRecord(3);

        // Installer is executing the installation script. Set up a
        // record specifying appropriate templates and text for
        // messages that will inform the user about what the custom
        // action is doing. Tell the installer to use this template and 
        // text in progress messages.
 
        MsiRecordSetString(hActionRec, 1, TEXT("MyCustomAction"));
        MsiRecordSetString(hActionRec, 2, TEXT("Incrementing the Progress Bar..."));
        MsiRecordSetString(hActionRec, 3, TEXT("Incrementing tick [1] of [2]"));
        UINT iResult = MsiProcessMessage(hInstall, INSTALLMESSAGE_ACTIONSTART, hActionRec);
        if ((iResult == IDCANCEL))
            return ERROR_INSTALL_USEREXIT;
              
        // Tell the installer to use explicit progress messages.
        MsiRecordSetInteger(hProgressRec, 1, 1);
        MsiRecordSetInteger(hProgressRec, 2, 1);
        MsiRecordSetInteger(hProgressRec, 3, 0);
        iResult = MsiProcessMessage(hInstall, INSTALLMESSAGE_PROGRESS, hProgressRec);
        if ((iResult == IDCANCEL))
            return ERROR_INSTALL_USEREXIT;
              
        //Specify that an update of the progress bar's position in
        //this case means to move it forward by one increment.
        MsiRecordSetInteger(hProgressRec, 1, 2);
        MsiRecordSetInteger(hProgressRec, 2, iTickIncrement);
        MsiRecordSetInteger(hProgressRec, 3, 0);
 
        // The following loop sets up the record needed by the action
        // messages and tells the installer to send a message to update
        // the progress bar.

        MsiRecordSetInteger(hActionRec, 2, iTotalTicks);
       
        for( int i = 0; i < iTotalTicks; i+=iTickIncrement)
        {
            MsiRecordSetInteger(hActionRec, 1, i);

            iResult = MsiProcessMessage(hInstall, INSTALLMESSAGE_ACTIONDATA, hActionRec);
            if ((iResult == IDCANCEL))
                return ERROR_INSTALL_USEREXIT;
          
            iResult = MsiProcessMessage(hInstall, INSTALLMESSAGE_PROGRESS, hProgressRec);
            if ((iResult == IDCANCEL))
                return ERROR_INSTALL_USEREXIT;
   
            //A real custom action would have code here that does a part
            //of the installation. For this sample, code that installs
            //10 registry keys.
            Sleep(1000);
                    
        }
        return ERROR_SUCCESS;
    }
    else
    {
        // Installer is generating the installation script of the
        // custom action.
  
        // Tell the installer to increase the value of the final total
        // length of the progress bar by the total number of ticks in
        // the custom action.
        PMSIHANDLE hProgressRec = MsiCreateRecord(2);

         MsiRecordSetInteger(hProgressRec, 1, 3);
            MsiRecordSetInteger(hProgressRec, 2, iTotalTicks);
        UINT iResult = MsiProcessMessage(hInstall, INSTALLMESSAGE_PROGRESS, hProgressRec);
           if ((iResult == IDCANCEL))
            return ERROR_INSTALL_USEREXIT;     
        return ERROR_SUCCESS;
     }
}
```



 

 



