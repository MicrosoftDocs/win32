---
description: You can use the WMI scripting type library to call WMI Scripting API methods from Microsoft Visual Studio and in Windows Script Host WSF files.
ms.assetid: 6ef4e210-0733-4f2a-89c1-1a7aca5a19d9
ms.tgt_platform: multiple
title: Using the WMI Scripting Type Library
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Using the WMI Scripting Type Library

You can use the WMI scripting type library to call WMI Scripting API methods from Microsoft Visual Studio and in Windows Script Host WSF files.

## Using the WMI Scripting Type Library with Microsoft Visual Studio

> [!Note]  
> Visual InterDev 6.0 features have been integrated into [Microsoft Visual Studio .NET](https://msdn.microsoft.com/vstudio/default.aspx).

 

The following procedure describes how to enable the integrated development environment (IDE) to be aware of the WbemScripting type library.

**To add the WMI Scripting type library to the project references**

1.  Select **Add References** from the **Project** menu.
2.  In the COM tab of the **Add Reference** box, select Microsoft WMI Scripting V1.2 Library.
3.  If no suitable option appears in the References list, add it by using **Browse** in the **References** box. The **Browse** opens an **Add Reference** box that enables you to locate the WbemScripting type library.

    The WbemScripting type library resides in the file Wbemdisp.tlb in the %windir%\\System32\\Wbem directory.

4.  Select the file and click **Open**. Microsoft WMI Scripting V1.2 Library appears on the references list. Ensure that you select the box next to this item in the list.

## Using the WMI Scripting Type Library with Windows Script Host 2.0

You can include the reference to the **WbemScripting.SWbemLocator** in a Windows Script Host WSF file, unlike a script written in Visual Basic, Scripting Edition or other scripting languages. This enables you to use constant names instead of values. For example, use **WbemAuthenticationLevelPktPrivacy** rather than the value 6 when setting authentication.

Scripts can connect with the Scripting API for WMI type library using the following methods:

-   Specifying the WbemScripting GUID in the VBScript methods [CreateObject](/previous-versions//xzysf6hc(v=vs.85)) and [**GetObject**](https://msdn.microsoft.com/library/e9waz863(v=VS.71).aspx).

    This alerts Windows Script Host to connect to the WMI object set.

    The following VBScript code example creates a new [**SWbemDateTime**](swbemdatetime.md) object.

    ```VB
    Set dateTime = CreateObject("WbemScripting.SWbemDateTime")
    ```

    

-   Using the [Moniker string](constructing-a-moniker-string.md) "winmgmts:" when obtaining a new or existing object.

    The following VBScript code example uses the "winmgmts:" moniker to get the instance of [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) with a **Handle** property of 0 (zero). **Handle** is the key property for this class.

    ```VB
    Set Process = GetObject("winmgmts:Win32_Process.Handle=0")
    ```

    

-   Referencing the WMI type library using the &lt;reference&gt; tag of the WSH 2.0 XML file format. If you use the &lt;reference&gt; tag, the tag must have either a **uuid** attribute whose value is the **GUID** of the WMI type library, or (recommended) an object attribute whose value is the **PROGID** of any of the WMI scripting objects you can create.

    The following VBScript code example uses the PROGID of "WbemScripting" . To run the script, save the text in a file with a .wsf extension.

    ```VB
    <?xml version="1.0" encoding="US-ASCII"?>
    <job>
    <reference object="WbemScripting.SWbemLocator"/>
    <script language="VBScript">
        set service = GetObject("winmgmts:")
        ' Following line uses a symbolic 
        ' constant from the WMI type library
        service.Security_.impersonationLevel = _
            wbemImpersonationLevelDelegate
    </script>
    </job>
    ```

    

-   Using an <**object**> tag to create a WMI scripting object. You can specify the **id** attribute with the value of a name that references the WMI scripting object you want to create, and the **progid** attribute equal to the PROID of the WMI scripting object.

    The following WSH script displays the hostname and the number of processors on the local computer. To run the script, save the text in a file with a .wsf extension.

    ```XML
    <?xml version="1.0" encoding="US-ASCII"?>
    <job>
     <object id="objSWbemLocator" progid="WbemScripting.SWbemLocator"/>
     <script language="VBScript">

      strComputer = "."
      Set objSWbemServices = objSWbemLocator.ConnectServer(strComputer, "root\cimv2")
      Set colSettings = objSWbemServices.ExecQuery("Select * From Win32_ComputerSystem")
      For Each objComputer in colSettings
       Wscript.Echo "System Name: " & objComputer.Name
       Wscript.Echo "Number of Processors: " & objComputer.NumberOfProcessors
      Next

     </script>
    </job>
    ```

    

## Related topics

<dl> <dt>

[Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script)
</dt> <dt>

[Scripting API for WMI](scripting-api-for-wmi.md)
</dt> </dl>

 

 
