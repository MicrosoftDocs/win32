---
title: How to Generate an MI Provider from a MOF File
description: Once you have configured the MI development environment and created a Microsoft Visual Studio project for your MI provider, the next step is to generate the MI provider source code files from your MOF file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8FA62DD9-EEA8-4B63-B4BD-E4388D5942B5
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How to: Generate an MI Provider from a MOF File

Once you have [configured the MI development environment](how-to--configure-the-mi-development-environment.md) and [created a Microsoft Visual Studio project for your MI provider](how-to-create-a-visual-studio-project-for-an-mi-provider.md), the next step is to generate the MI provider source code files from your MOF file. This topic presents step-by-step instructions on performing that task using the Convert-MofToProvider tool.

> [!Note]  
> If you're new to MI provider development and/or just want to learn how to develop an MI provider and don't have a MOF file, the following steps provide a simple MOF file example.

 

1.  Open a command prompt.
2.  Change directories to the source directory of the Visual Studio created in [How to: Create a Visual Studio Project for an MI Provider](how-to-create-a-visual-studio-project-for-an-mi-provider.md). If you are in the correct directory, you will see two files: *projectName*.vcxproj and *projectName*.vcxproj.filters.
3.  Copy your MOF file to the location located in the previous step. If you don't have a MOF file, the following MOF will suffice for a simple test. If that's the case, copy and paste the following contents into a file called process.mof and save it to the project's source code directory.

    ```mof
    #pragma include ("cim_schema_2.26.0.mof")
    #pragma include ("MSFT_Qualifiers.mof")

    // MSFT_WindowsProcess class derives from CIM_Process class,
    // which defines the schema for the processes running on windows OS.
    [ClassVersion("1.0.0")]
    class MSFT_WindowsProcess : CIM_Process
    {
     string CommandLine;

     [Description("This instance method demonstrates modifying the "
      "priority of a given process."
      "The method returns an integer value of 0 if the "
      "operation was successfully completed,"
      "and any other number to indicate an win32 error code.")]
     uint32 SetPriority([In] uint32 Priority);

     [static,
     Description("This static method demonstrates creating a process "
      "by supplying commandline to start a new process."
      "It will output the reference to the newly created process."
      "The method returns an integer value of 0 if the process "
      "was successfully created, and any other number to "
      "indicate an win32 error code.")]
     uint32 Create([In] string CommandLine, [Out] CIM_Process ref Process);
    };
    ```

    

4.  Run the Convert-MofToProvider tool to generate the source code files for your provider. In the following example, the tool is being called using values - such as for the **MofFile** and **ClassList** parameters - that represent the sample MOF file introduced in the previous step. If you're not using the sample MOF file, you'll need to adjust these values to represent the MOF file and its defined classes that you are using.

    > [!Note]  
    > The following call to the Convert-MofToProvider tool is split across multiple lines for display purposes. You should enter this as a single line.

     

    ``` syntax
    convert-moftoprovider -MofFile process.mof -ClassList MSFT_WindowsProcess 
    -IncludePath %CIM2260DIR% %MIINCLUDEDIR% -ExtraClass Cim_Error -SkipLocalize
    ```

    The following tables lists the files generated and their purpose.

    

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>File(s)</th>
    <th>Purpose</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td>CIM_ManagedElement.h<br/> CIM_ManagedSystemElement.h<br/> CIM_LogicalElement.h<br/> CIM_Job.h<br/> CIM_Error.h<br/> CIM_ConcreteJob.h<br/> CIM_EnabledLogicalElement.h<br/> CIM_Process.h<br/> MSFT_WindowsProcess.h<br/></td>
    <td>The header (.h) files define class types and helper functions to manipulate instances of the class - such as set/clear the property value, construct, clone and destruct.<br/></td>
    </tr>
    <tr class="even">
    <td>module.c<br/></td>
    <td>Facilitates the following tasks:<br/>
    <ul>
    <li>Implements the MI provider entry function - <strong>MI_Main</strong>.</li>
    <li>Implements the <strong>Load</strong> function that is called when the provider is being loaded.</li>
    <li>Implements the <strong>UnLoad</strong> function that is called once the provider is being unloaded.</li>
    </ul></td>
    </tr>
    <tr class="odd">
    <td>MSFT_WindowsProcess.c<br/></td>
    <td>Implements the intrinsic and extrinsic methods of the <strong>MSFT_WindowsProcess</strong> class that are defined in the MOF file.<br/> Intrinsic methods include <strong>Enumerate</strong>, <strong>Get</strong>, <strong>Delete</strong>, <strong>Modify</strong>, and <strong>Create</strong>.<br/> Extrinsic methods include <strong>SetPriority</strong>, <strong>Create</strong>, and <strong>RequestStateChange</strong>.<br/>
    <blockquote>
    [!Note]<br />
    The <strong>RequestStateChange</strong> method is defined only in the parent class - <strong>CIM_EnabledLogicalElement</strong> - but not in the <strong>MSFT_WindowsProcess</strong> schema. Therefore, it is treated as not implemented. If the developer wants to implement this method within the <strong>MSFT_WindowsProcess</strong>, the <strong>RequestStateChange</strong> method must be redefined in the <strong>MSFT_WindowsProcess</strong> schema. To see an example of this, download the [MI API Samples](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306594) and look at how the <strong>MSFT_WindowsService::StopService</strong> method is implemented.
    </blockquote>
    <br/></td>
    </tr>
    <tr class="even">
    <td>schema.c<br/></td>
    <td>Includes the full schema of all related classes. This file should never be modified. To change the schema, modify the original MOF and re-generate the code.<br/></td>
    </tr>
    <tr class="odd">
    <td>WMIAdapter.c<br/></td>
    <td>Contains the DLL entry point - <strong>DllMain</strong> - as well as other standard DLL functions.<br/></td>
    </tr>
    <tr class="even">
    <td>provider.def<br/></td>
    <td>Defines list of exported APIs from MI provider DLL.<br/></td>
    </tr>
    <tr class="odd">
    <td>strings.rc<br/></td>
    <td>This resource file is generated only when you run the Convert-MofToProvider tool without specifying the <strong>SkipLocalize</strong> parameter and contains the localized strings for MI status and error messages. You should never modify this file directly as it is overwritten each time the <strong>Convert-MofToProvider</strong> tool is run without the -<strong>-SkipLocalize</strong> parameter. If you need to define additional resources, create a second resource file and use the <strong>#include</strong> directive to merge the contents of the strings.rc files into the new file. For more information about resource files and using the <strong>#include</strong> directive, see the [About Resource Files](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308943) topic (Http://Go.Microsoft.Com/FWLink/p/?LinkID=308943).<br/></td>
    </tr>
    </tbody>
    </table>

    

     

5.  Once you've generated the MI provider from your MOF file, the next step is to [build an MI provider using Visual Studio](how-to-build-an-mi-provider-using-visual-studio.md).

 

 





