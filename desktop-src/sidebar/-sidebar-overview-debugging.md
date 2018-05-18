---
title: Gadgets for Windows Sidebar Debugging
description: This overview describes the various methods and techniques that can be used to debug gadgets.
ms.assetid: '215f84ea-9db7-4c50-b788-b81074706f71'
keywords: ["Windows Sidebar,debugging", "Sidebar,debugging", "gadgets,debugging", "debugging gadgets", "Gadget Picker,debugging", "Windows Sidebar,script debuggers", "Sidebar,script debuggers", "gadgets,script debuggers", "script debuggers", "Windows Sidebar,encoding", "Sidebar,encoding", "gadgets,encoding", "Windows Sidebar,fonts", "Sidebar,fonts", "gadgets,fonts", "Windows Sidebar,UTF-8 character encoding", "Sidebar,UTF-8 character encoding", "gadgets,UTF-8 character encoding", "UTF-8 character encoding"]
---

# Gadgets for Windows Sidebar Debugging

\[ The Windows Gadget Platform/Sidebar is available for use in the following versions of Windows: Windows 7, Windows Vista, and Windows Server 2008. It may be altered or unavailable in subsequent versions. \]

This overview describes the various methods and techniques that can be used to debug gadgets.

-   [Debugging a Missing Gadget](#debugging-a-missing-gadget)
-   [Debugging Code](#debugging-code)
-   [Debuggers](#debuggers)
-   [Tips](#tips)
    -   [Character Encoding](#character-encoding)
    -   [Fonts](#fonts)

## Debugging a Missing Gadget

If a gadget fails to appear in the **Gadget picker**, the likely culprit is an invalid or malformed gadget.xml manifest file. Open the manifest file with Windows Internet Explorer or other XML editor to check.

If a gadget appears in the **Gadget picker** but is displayed with the Sidebar's generic gadget image, ensure that the desired image exists in the gadget file structure and that the path to the image file in the manifest is correct.


```
<hosts>
    <host name="sidebar">
        <base type="HTML" apiVersion="1.0.0" src="sample.html" />
        <permissions>Full</permissions>
        <platform minPlatformVersion="1.0" />
        <defaultImage src="icon.png" />
    </host>
</hosts>
```



This procedure may require repeating if either the gadget drag-and-drop image or the developer's logo is missing or broken.


```
<author name="Microsoft">
    <info url="msdn.microsoft.com" />
    <logo src="logo.png" />
</author>
...
<icons>
<icon height="48" width="48" src="icon.png" />
</icons>
```



## Debugging Code

Depending on the complexity of the gadget code, debugging can consist simply of dumping information to the gadget UI (similar to simple Web applications) at specific code points or by catching exceptions with a `try...catch` block. Microsoft JScript alerts are often used for quick and dirty debugging, but these are not implemented in the Sidebar. If necessary, this limitation can be worked around by using the equivalent Microsoft Visual Basic Scripting Edition (VBScript) MsgBox function.

If the complexity of your gadget code requires a more robust debugging solution then a number of script debuggers are available.

## Debuggers

Any script debugger can be used to debug a gadget, including Microsoft Script Debugger, Microsoft Script Editor, and Microsoft Visual Studio. Enabling gadget debugging requires a minor tweak to the Internet Explorer settings:

From the menu, click **Tools** and select **Internet Options**.

![internet options in windows internet explorer](images/reference/internetoptions.png)

Click the **Advanced** tab and verify that both **Disable script debugging** check boxes are not selected.

![ie tools\|options\|advanced\|disable script debugging](images/reference/iedisablescriptdebugging.png)

If using Visual Studio for debugging, click **Tools**, select **Options**, and ensure that **Just-In-Time** debugging is enabled for Script:

![just-in-time debugging for script in visual studio](images/reference/vsjitdebugging.png)

To dump specific output to the debugger console, the [**outputString**](system-debug-outputstring.md) method can be used:


```
// --------------------------------------------------------------------
// Attempt to save the file and throw an error if the file name does 
// not include a file name extension.
// --------------------------------------------------------------------
function SaveFile()
{
    var fso = new ActiveXObject( "Scripting.FileSystemObject" );
    // Throw an arbitrary error to demonstrate the outputString method.
    try
    {
        if (sFilename.indexOf(".") == -1)
        {            
            throw "'File name' does not specify a file name extension.";
        }
        var file = 
            fso.OpenTextFile(sFilePath + sFilename, 
            FOR_WRITING, CREATE_NEW);
        file.Write(sContent);
        file.Close();
        fso = file = null;
    }
    catch(e)
    {
        System.Debug.outputString(e);
    }
}
```



To break into the gadget runtime at a particular execution point and step through the code, you can place this line of code where necessary:


```
debugger;
```



When the `debugger` statement is executed the Visual Studio Just-In-Time Debugger dialog will prompt you to open a registered debugger:

![the visual studio just-in-time debugger dialog](images/reference/vsjitdebuggingdialog.png)

Once a debugger is selected, the code will be displayed in the debugger with the break point highlighted. From this point you can step through the code and get runtime information for any gadget element:

![stepping through the code in the debugger](images/reference/vsdebuggingstepping.png)

## Tips

### Character Encoding

It is highly recommended that all gadget HTML and script files be saved with UTF-8 character encoding.

The following steps can be taken to ensure the encoding of these files:

1.  Open the file in Notepad.
2.  On the **File** menu, click **Save as...**
3.  In the **Save as** dialog box, confirm that the value in the **Encoding** drop-down is **UTF-8**.

If the value in the **Encoding** drop-down is not UTF-8:

1.  In the **Encoding** drop-down, select **UTF-8**.
2.  Click **Save** to overwrite the existing file.

Repeat this process for all gadget HTML and script files.

### Fonts

If font information is specified for the gadget UI in HTML or Cascading Style Sheets (CSS), the font size must be included and it must be an absolute measure in pixels.

 

 




