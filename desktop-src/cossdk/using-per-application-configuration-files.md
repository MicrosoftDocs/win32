---
description: Using Per-Application Configuration Files
ms.assetid: a600e5a4-b2bb-45a6-8b86-5ea3caf7aa78
title: Using Per-Application Configuration Files
ms.topic: article
ms.date: 05/31/2018
---

# Using Per-Application Configuration Files

Using COM+ per-application configuration files requires the following basic steps:

-   Configure an application root directory for a COM+ application.
-   Create application.manifest and application.config files in the COM+ application root directory.

> [!Note]  
> Per-application configuration files are only available starting with Windows XP with Service Pack 2 (SP2) and Windows Server 2003.

 

**To use a per-application configuration file**

1.  Create a .NET class library, with a reference to the System.EnterpriseServices assembly.

2.  The class library should contain the following code:

    ```CSharp
    using System;
    using System.Configuration;
    using System.EnterpriseServices;

    public class Class1 : ServicedComponent
    {
        public string GetConfigData()
        {
            return System.Configuration.ConfigurationSettings.AppSettings
                 ["ConfigData1"];
        }
    }
    ```

    

    Note that "ConfigData1" is a sample setting name. You can replace this with the setting name of your choice.

3.  Create an empty COM+ application. For instructions on how to do this, see [Creating a New COM+ Application](creating-a-new-com--application.md).
4.  Install the class library you created into the COM+ application. For instructions on how to do this, see [Installing New Components](installing-new-components.md).
5.  In the Component Services administrative tool, right-click the COM+ application you created and select **Properties**.
6.  In the **Properties** dialog box, select the **Activation** tab.
7.  Make sure the **Activation type** is set to **Server application**.
8.  In the **Application Root Directory** text box, enter the path or browse to the directory where you want to store your application configuration files for this application.
9.  Click **OK**.

    Note that you can also specify the COM+ application root directory through the ApplicationDirectory property of the [**COMAdminCatalogObject**](comadmincatalogobject.md) class. For more information, see [**Applications**](applications.md).

10. In the directory you chose to store your application configuration files, create a file named *application*.manifest. With a text editor, add the following text to this file:

    ``` syntax
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" />
    ```

11. In the same directory, create a file named *application*.config. With a text editor, add the following text to this file:

    ``` syntax
    <?xml version="1.0"?>
    <configuration>
        <appSettings>
            <add key="ConfigData1" value="Configuration Data Number 1"/>
        </appSettings>
    </configuration>
    ```

    Note that this configuration file is just an example. You can create multiple keys with different names and values. Note, however, that "ConfigData1" matches the setting name used in the class library created earlier.

12. Create a .NET console application, with a reference to the .NET class library you created earlier, and a reference to the System.EnterpriseServices assembly.
13. The console application should contain the following code:
    ```CSharp
    using System;
    using System.IO;

    class Client
    {
    [STAThread]
        static void Main(string[] args)
        {
            Class1 server = new Class1();
            Console.WriteLine(server.GetConfigData());
            Console.ReadLine();
        }
    }
    ```

    

Run the console application. The output should be:

``` syntax
Configuration Data Number 1
```

 

 



